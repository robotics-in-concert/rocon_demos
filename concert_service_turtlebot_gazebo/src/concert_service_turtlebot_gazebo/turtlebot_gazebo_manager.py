#!/usr/bin/env python

import os
import rocon_python_utils
import rospkg
import rospy
import subprocess
import tempfile

from concert_service_gazebo import RobotManager 
from gateway_msgs.msg import Rule, ConnectionType
from gazebo_msgs.srv import DeleteModel, DeleteModelRequest

def reformat_position_vector(position_vector):
    """
    Reformats position vector so that it can be used with the turtlebot launch script
    """
    if len(position_vector) == 2:
        return [position_vector[0],
                position_vector[1],
                0.0, 0.0, 0.0, 0.0]
    if len(position_vector) == 3:
        return [position_vector[0],
                position_vector[1],
                0.0, 0.0, 0.0, 
                position_vector[2]]
    return [position_vector[x] if x < len(position_vector) else 0.0 for x in range(6)]

def generate_spawn_robot_launch_script(name, gazebo_name, location, 
                                       use_full_gazebo_model=False,
                                       configuration_file=None):
    """
    Generates the roslaunch script for a single robot, wrapping the appropriate
    launch file in turtlebot_gazebo
    """
    launch_text = '<launch>\n'
    launch_text += '  <group ns="%s">\n' % name
    launch_text += '    <include file="$(find turtlebot_gazebo)/launch/amcl_demo.launch">'
    launch_text += '      <arg name="world" value="%s"/>\n' % gazebo_name
    launch_text += '      <arg name="robotid" value="%s"/>\n' % name
    launch_text += '      <arg name="tf_prefix" value="/%s"/>\n' % name
    launch_text += '      <arg name="x" value="%s"/>\n' % location[0]
    launch_text += '      <arg name="y" value="%s"/>\n' % location[1]
    launch_text += '      <arg name="z" value="%s"/>\n' % location[2]
    launch_text += '      <arg name="roll" value="%s"/>\n' % location[3]
    launch_text += '      <arg name="pitch" value="%s"/>\n' % location[4]
    launch_text += '      <arg name="yaw" value="%s"/>\n' % location[5]
    if use_full_gazebo_model:
        launch_text += '      <arg name="use_full_gazebo_model" value="true"/>\n'
    else:
        launch_text += '      <arg name="use_full_gazebo_model" value="false"/>\n'
    if configuration_file:
        launch_text += '      <arg name="configuration_file" value="%s"/>\n' % configuration_file
    launch_text += '    </include>\n'
    launch_text += '  </group>\n'
    launch_text += '</launch>\n'
    return launch_text

def start_roslaunch_process(launch_script):
    """
    Robots are spawned using roslaunch instead of gazebo/spawn_model so that
    a few other scripts such as robot_state_publisher can also be launched.
    This convenience function helps launch a roslaunch script
    """
    temp = tempfile.NamedTemporaryFile(mode='w+t', delete=False)
    temp.write(launch_script)
    temp.close()
    command_args = ['roslaunch', temp.name]
    command_args.append('--screen')
    roslaunch_env = os.environ.copy()
    try:
        # ROS_NAMESPACE gets set since we are inside a node here
        # got to get rid of this otherwise it pushes things down
        del roslaunch_env['ROS_NAMESPACE']
    except KeyError:
        pass
    process = subprocess.Popen(command_args, env=roslaunch_env)
    return process

class TurtlebotManager(RobotManager):

    def __init__(self, namespace = '/'):
        rospy.wait_for_service(namespace + 'gazebo/delete_model')
        self.delete_model = rospy.ServiceProxy(namespace + 'gazebo/delete_model', DeleteModel)
        self.namespace = namespace
        self.use_full_gazebo_model = rospy.get_param('use_full_gazebo_model', False)
        self.configuration_file = rospy.get_param('configuration_file', None)
        if self.configuration_file != None:
            try:
                self.configuration_file = rocon_python_utils.ros.find_resource_from_string(self.configuration_file)
            except rospkg.ResourceNotFound:
                raise rospkg.ResourceNotFound("could not resolve configuration file [%s]" % self.configuration_file)
        self.processes = {}

    def spawn_robot(self, name, position_vector):
        reformatted_position_vector = reformat_position_vector(position_vector)
        launch_script = generate_spawn_robot_launch_script(name, self.namespace + '/gazebo', 
                                                           reformatted_position_vector,
                                                           self.use_full_gazebo_model,
                                                           self.configuration_file)
        self.processes[name] = start_roslaunch_process(launch_script)

    def delete_robot(self, name):
        delete_service_req = DeleteModelRequest(name)
        try:
            self.processes[name].terminate()
            self.delete_model(delete_service_req)
        except rospy.ServiceException:  # communication failed
            rospy.logerr("GazeboTurtlebotManager : unable to delete model %s" % name)

    def prepare_rocon_launch_text(self, robots):
        port = 11
        launch_text = '<concert>\n'
        for name in robots:
            launch_text += '  <launch title="%s:114%s" package="concert_service_gazebo" name="robot.launch" port="114%s">\n' % (name, str(port), str(port))
            launch_text += '    <arg name="robot_name" value="%s"/>\n' % name
            launch_text += '    <arg name="robot_concert_whitelist" value="Gazebo Concert;Concert Tutorial"/>\n'
            launch_text += '    <arg name="robot_rapp_whitelist" value="[rocon_apps, turtlebot_rapps, turtlebot_gazebo_concert]"/>\n'
            launch_text += '  </launch>\n'
            port = port + 1
        launch_text += '</concert>\n'
        return launch_text

    def get_flip_rule_list(self, name):
        return [Rule(ConnectionType.SUBSCRIBER, '/' + name + '/cmd_vel', None),
                Rule(ConnectionType.PUBLISHER, '/' + name + '/odom', None),
                Rule(ConnectionType.PUBLISHER, '/' + name + '/scan_filtered', None),
                Rule(ConnectionType.SERVICE, '/static_map', None), #TODO: Shouldn't be hardcoded
                Rule(ConnectionType.PUBLISHER, '/map', None), #TODO: Shouldn't be hardcoded
                Rule(ConnectionType.PUBLISHER, '/tf', None), 
                Rule(ConnectionType.PUBLISHER, '/tf_static', None),
                Rule(ConnectionType.PUBLISHER, '/clock', None)]
