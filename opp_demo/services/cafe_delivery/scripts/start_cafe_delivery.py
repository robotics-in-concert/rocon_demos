#!/usr/bin/env python
import rospy
import yaml
import concert_service_roslaunch
import map_store.srv
import annotations_store.srv

from concert_msgs.srv import *
from concert_msgs.msg import *


if __name__ == '__main__':
    rospy.init_node('start_cafe_delivery', anonymous=True)

    name = rospy.get_param("name")
    uuid = rospy.get_param("uuid")
    description = rospy.get_param("description")
    filename = rospy.get_param('~filename')

    name, impl = concert_service_roslaunch.load_linkgraph_from_file(filename)
    sgsh =  concert_service_roslaunch.StaticLinkGraphHandler(name, uuid, description, impl)

    sgsh.request_resources(True)

        
    ### Loading a proper map for the cafe
    map_id = rospy.get_param('~map_id',None)

    rospy.rostime.wallsleep(5)

    if map_id:
        rospy.loginfo("Loading map : " + str(map_id))
        rospy.wait_for_service('/database/publish_map')
        map_load = rospy.ServiceProxy('/database/publish_map',map_store.srv.PublishMap)
        rospy.wait_for_service('/database/publish_annotations')
        anno_load = rospy.ServiceProxy('/database/publish_annotations',annotations_store.srv.PublishAnnotations)
        map_load(map_id)
        anno_load(map_id)
    else:
        rospy.logerr("No map ID")
    rospy.spin()
