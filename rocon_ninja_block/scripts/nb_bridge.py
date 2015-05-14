#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_devices/license/LICENSE
#
#################################################################################

# ros
import rospy
from rocon_ninja_block import NinjaBlockBridge

if __name__ == '__main__':
    rospy.init_node('nb_bridge')

    if rospy.has_param('~nb_bridge_server_host'):
        server_host = rospy.get_param('~nb_bridge_server_host')
    else:
        print "You need nb_bridge_server_host"
        exit(1)

    if rospy.has_param('~nb_bridge_server_port'):
        server_port = rospy.get_param('~nb_bridge_server_port')
    else:
        print "You need nb_bridge_server_port"
        exit(1)

    if rospy.has_param('~nb_bridge_public_key'):
        public_key = rospy.get_param('~nb_bridge_public_key')
    else:
        print "You need nb_bridge_public_key"
        exit(1)

    if rospy.has_param('~nb_bridge_callback_host'):
        callback_url_host = rospy.get_param('~nb_bridge_callback_host')
    else:
        print "You need nb_bridge_callback_host"
        exit(1)

    if rospy.has_param('~nb_bridge_callback_port'):
        callback_url_port = rospy.get_param('~nb_bridge_callback_port')
    else:
        print "You need nb_bridge_callback_port"
        exit(1)
    
    nb_bridge = NinjaBlockBridge(host=server_host,
                                 port=server_port,
                                 public_key=public_key,
                                 callback_url_host=callback_url_host,
                                 callback_url_port=callback_url_port)
    nb_bridge.start()
    
    print "Bye Bye"
