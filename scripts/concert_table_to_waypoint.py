#!/usr/bin/env python

import rospy
import world_canvas_client

import yocs_msgs.msg as yocs_msgs

def convert_table_to_waypoint(table):

    w = yocs_msgs.Waypoint() 
    
    w.name = table.name
    w.pose = table.pose.pose.pose
    w.header = table.pose.header

    return w


if __name__ == '__main__':
    rospy.init_node('convert_data')
    world = 'yujin_rnd'
    namespace = '/software/world_canvas'

    ac = world_canvas_client.AnnotationCollection(world=world, types=['yocs_msgs/Table'], srv_namespace=namespace)
    ac.load_data()

    annots = ac.get_annotations()

    for a in annots:
        table = ac.get_data(a)
        w = convert_table_to_waypoint(table)
        ac.remove(a.id)
        a.type = 'yocs_msgs/Waypoint'
        ac.add(a, w)
        print(str('%s has been converted'%a.name))

    ac.save()
