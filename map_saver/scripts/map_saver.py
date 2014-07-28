#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy 
import subprocess
import map_store.srv as map_store_srvs

def process_save_map(req):
    filename = rospy.get_param('filename', req.map_name) 
    tmp_name = filename + '_tmp'

    tmp_output = subprocess.check_output(['rosrun','map_server','map_saver','-f',tmp_name])
    rospy.sleep(2.0)
    tmp_name = tmp_name + '.yaml'
    crop_output = subprocess.check_output(['rosrun','map_server','crop_map',tmp_name,filename])
    rospy.loginfo('Map Saved into %s'%str(filename))

    return map_store_srvs.SaveMapResponse()
    

if __name__ == '__main__':
    rospy.init_node('map_saver')

    srv_saver = rospy.Service('save_map', map_store_srvs.SaveMap, process_save_map)
    rospy.spin()
