#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import cafe_msgs.msg as cafe_msgs
import random

###################
# Utils
###################
def generate_menus():
    MENU_POOL = ["Cafe Latte", 
                 "Capuccino", 
                 "DDal Ba", 
                 "Coke", 
                 "Americano", 
                 "Koreano", 
                 "Kobukino", 
                 "Sul tang mool"]
    menus = []
    
    for i in range(1,4):
        m = cafe_msgs.Menu()
        m.name = random.choice(MENU_POOL)
        m.size = random.randint(1,3)
        m.qty = random.randint(1,5)
        menus.append(m)
    
    return menus


def create_order():
    name_pool = ['Gamza King', 'Whoola woop', 'Ganzang Gonzang']

    order = cafe_msgs.RemoteOrder()
    order.name = random.choice(name_pool) 
    order.time = 'Monday 2014'
    order.status = cafe_msgs.RemoteOrderStatus.ORDER_SENT  
    order.estimated_arrival = random.randint(5,10)

    order.menus = generate_menus()

    return order


##################
#    Main
##################

def process_order_status(msg):
    global order
    global order_status_updated
    order.status = msg.status
    order_status_updated = order_status_updated + 1

if __name__ == '__main__':
    global order_status_updated
    global order

    rospy.init_node('dummy_order')

    order_status_updated = 0
    order = create_order() 

    order_pub = rospy.Publisher('/cafe/remote_order', cafe_msgs.RemoteOrder)
    order_update_pub = rospy.Publisher('/cafe/remote_order_update', cafe_msgs.RemoteOrderUpdate)
    status_usb = rospy.Subscriber('/cafe/remote_order_status', cafe_msgs.RemoteOrderStatus, process_order_status)

    rospy.sleep(1)
    order_pub.publish(order)
    rospy.loginfo('Dummy Order : Order for %s Sent'%order.name)
    rospy.sleep(1)

    while not rospy.is_shutdown():
        if order_status_updated == 1:
            rospy.loginfo('Dummy Order : [%s] status [%s]'%(order.name,order.status)) 
            rospy.loginfo('Dummy Order : Sending arrival time update')
            update = cafe_msgs.RemoteOrderUpdate() 
            update.name = order.name
            update.estimated_arrival = random.randint(1,4)
            update.status = cafe_msgs.RemoteOrderStatus.ORDER_PICKED_UP
            order_update_pub.publish(update)

        if order_status_updated == 2:
             rospy.loginfo('Dummy Order : Order has been cleared')
             break

        rospy.sleep(1)
    rospy.loginfo('Bye Bye')
