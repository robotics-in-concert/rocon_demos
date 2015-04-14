#!/usr/bin/env python
import roslib; roslib.load_manifest('world_canvas_client_py')
import rospy
from concert_software_farmer import SoftwareFarmClient, FailedToStartSoftwareException

import world_canvas_client

def publish_map(world, namespace):
    map_name = rospy.get_param('map_name')
    map_topic = rospy.get_param('map_topic')

    # Get the 2D map for the given world
    map_ac = world_canvas_client.AnnotationCollection(world=world, types=['nav_msgs/OccupancyGrid'], srv_namespace=namespace, names=[map_name])
    map_ac.load_data()

    # Publish the map on server side; topic type is get from the annotation info
    map_ac.publish(map_topic, None, False, False)   # i.e. by_server=True, as_list=False
    
    return map_ac

def publish_location(world, namespace):
    table_topic = rospy.get_param('table_topic')
    viz_table_topic = rospy.get_param('viz_table_topic')

    table_ac = world_canvas_client.AnnotationCollection(world=world, types=['yocs_msgs/Waypoint'], srv_namespace=namespace)
    table_ac.load_data()
    table_ac.publish(table_topic, 'yocs_msgs/WaypointList', by_server=False, as_list=True)
    table_ac.publish_markers(viz_table_topic)
    return table_ac


def publish_ar_marker(world, namespace):
    ar_topic = rospy.get_param('ar_topic')
    viz_ar_topic = rospy.get_param('viz_ar_topic')

    ar_ac = world_canvas_client.AnnotationCollection(world=world, types=['ar_track_alvar_msgs/AlvarMarker'], srv_namespace=namespace)
    ar_ac.load_data()
    ar_ac.publish(ar_topic, 'ar_track_alvar_msgs/AlvarMarkers', by_server=False, as_list=True, list_attribute='markers')
    ar_ac.publish_markers(viz_ar_topic)
    return ar_ac

if __name__ == '__main__':
    rospy.init_node('world_canvas_client')
    world = rospy.get_param('world')
    #namespace = rospy.get_param('wc_namespace')

    try:
        sfc = SoftwareFarmClient()
        success, namespace, _unused_parameters = sfc.allocate("concert_software_common/world_canvas_server")

        if not success:
            raise FailedToStartSoftwareException("Failed to allocate software")

        rospy.loginfo("Publish World : world canvas namespace : %s"%namespace)
        map_ac = publish_map(world, namespace)
        table_ac = publish_location(world, namespace)
        ar_ac = publish_ar_marker(world, namespace)
        rospy.loginfo("Done")
        rospy.spin()

    except (FailedToStartSoftwareException, SoftwareReleaseTimeoutException) as e:
        rospy.logerr("Publish World : %s"%str(e))
