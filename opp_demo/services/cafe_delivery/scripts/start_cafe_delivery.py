#!/usr/bin/env python
import rospy
import yaml
import concert_service_roslaunch
import map_store.srv
import annotations_store.srv

from concert_msgs.srv import *
from concert_msgs.msg import *

def load_linkgraph_from_file(filename):
    lg = LinkGraph() 
    name = "None"

    with open(filename) as f:
        impl = yaml.load(f)
        name = impl['name'] 
        
        for node in impl['nodes']:
            node['min'] = node['min'] if 'min' in node else 1
            node['max'] = node['max'] if 'max' in node else 1
            node['force_name_matching'] = node['force_name_matching'] if 'force_name_matching' in node else False

            lg.nodes.append(LinkNode(node['id'], node['tuple'], node['min'], node['max'], node['force_name_matching']))
        for topic in impl['topics']:
            lg.topics.append(LinkConnection(topic['id'], topic['type']))

        if 'service' in impl:
            for service in impl['services']:
                lg.services.append(LinkConnection(service['id'], service['type']))
        for action in impl['actions']:
            lg.actions.append(LinkConnection(action['id'], action['type']))
        for edge in impl['edges']:
            lg.edges.append(LinkEdge(edge['start'], edge['finish'], edge['remap_from'], edge['remap_to']))

    return name, lg

if __name__ == '__main__':
    rospy.init_node('start_cafe_delivery', anonymous=True)
    filename = rospy.get_param('~filename')
    name, impl = load_linkgraph_from_file(filename)
    name = rospy.get_param("name")
    uuid = rospy.get_param("uuid")
    description = rospy.get_param("description")
    sgsh =  concert_service_roslaunch.StaticLinkGraphHandler(name, uuid, description, impl)

    rospy.rostime.wallsleep(3.0)  # human time
    sgsh.request_resources(True)

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
    rospy.spin()
