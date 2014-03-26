#!/usr/bin/env python
import rospy
import yaml
import concert_service_roslaunch
import concert_service_utilities
import map_store.srv
import annotations_store.srv

from concert_msgs.srv import *
from concert_msgs.msg import *

if __name__ == '__main__':
    rospy.init_node('start_cafe_delivery', anonymous=True)
    (name, description, uuid) = concert_service_utilities.get_service_info()
    filename = rospy.get_param('~filename')
    impl_name, impl = concert_service_roslaunch.load_linkgraph_from_file(filename)

    if not name:
        name = impl_name        

    sgsh =  concert_service_roslaunch.StaticLinkGraphHandler(name, description, uuid, impl)

    rospy.rostime.wallsleep(3.0)  # human time
#sgsh._request_resources(True)

    map_id = rospy.get_param('~map_id',None)

    #  It is hack to wait until the map database is up.
    #  The proper way to do is wait until the service obtained the all resources and request to load a map
    rospy.rostime.wallsleep(5.0)  # human time
    if map_id:
        rospy.loginfo("Loading map : " + str(map_id))
        rospy.wait_for_service('/database/publish_map')
        map_load = rospy.ServiceProxy('/database/publish_map',map_store.srv.PublishMap)
        rospy.wait_for_service('/database/publish_annotations')
        anno_load = rospy.ServiceProxy('/database/publish_annotations',annotations_store.srv.PublishAnnotations)
        map_load(map_id)
        anno_load(map_id)
    else:
        rospy.loginfo("No map ID")
    sgsh.spin()
