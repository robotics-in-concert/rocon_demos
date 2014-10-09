#!/usr/bin/env python
import roslib; roslib.load_manifest('world_canvas_client_py')
import rospy

import world_canvas_client

def publish_map(world, namespace):
    map_name = rospy.get_param('map_name')
    map_topic = rospy.get_param('map_topic')

    # Get the 2D map for the given world
    map_ac = world_canvas_client.AnnotationCollection(world=world, types=['nav_msgs/OccupancyGrid'], srv_namespace=namespace)
    map_ac.loadData()

    # Publish the map on server side; topic type is get from the annotation info
    map_ac.publish(map_topic, None, True, False)   # i.e. by_server=True, as_list=False

def publish_location(world, namespace):
    #TODO
    pass

def publish_ar_marker(world):
    #TODO
    pass

if __name__ == '__main__':
    rospy.init_node('world_canvas_client')
    world = rospy.get_param('world')
    namespace = rospy.get_param('wc_namespace')

    publish_map(world, namespace)

    #publish_location(world, namespace)
    #publish_ar_marker(world, namespace)
    rospy.loginfo("Done")
    rospy.spin()
