#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import actionlib
import rospy
import vending_machine_control.msg as vending_machine_msgs
import std_msgs.msg as std_msgs
import utils

class VendingMachineManager(object):
    """
        Vending machine manager
    """
    def __init__(self):
        '''
            Arduino communication
        '''
        self.pub_drink_order = rospy.Publisher('arduino/drink_order', std_msgs.Int8, latch=True)
        self.sub_order_result = rospy.Subscriber('arduino/order_result', std_msgs.Int8, self._arduinoOrderResultCB)
        # indicates if the last sent order has been processed
        self._order_processed = False
        # list of processed orders
        self.processed_orders = []
        # stores the currently processed drink type

        '''
            Action interface
        '''
        self.server = actionlib.SimpleActionServer('~drink_ordering',
                                                   vending_machine_msgs.DrinkOrderAction,
                                                   self._execute,
                                                   False)
        self.server.start()

        ''' configure available drinks '''
        self.drink1 = rospy.get_param("~drink1", vending_machine_msgs.DrinkType.COKE)
        self.drink2 = rospy.get_param("~drink2", vending_machine_msgs.DrinkType.MAX)

    def _arduinoOrderResultCB(self, data):
        rospy.loginfo("Result received: " + str(data))
        processed_order = int()
        if data.data == 1:
            processed_order = self.drink1
            self.processed_orders.append(processed_order)
            self._order_processed = True
        elif data.data == 2:
            processed_order = self.drink2
            self.processed_orders.append(processed_order)
            self._order_processed = True
        else:
            rospy.logerr("Vending machine did not process the order correctly! Error code: " + str(data.data))

    def _execute(self, goal):
        '''
            Parse action goal and send order to Arduino
        '''
        feedback = vending_machine_msgs.DrinkOrderFeedback()
        feedback.order_status.data = "Vending machine manager: Processing drink orders ..."
        self.server.publish_feedback(feedback)
        rospy.loginfo(str(feedback.order_status.data))

        orders = []
        for type in goal.drink_types:
            if utils.verifyDrinkType(type.drink_type, self.drink1, self.drink2):
                drink_amount = goal.drink_amounts[goal.drink_types.index(type)]
                for x in range (0, drink_amount):
                    orders.append(type.drink_type)
        orders.reverse()

        all_orders_processed = False
        self._order_processed = True # set to true to start order process

        while not all_orders_processed and not rospy.is_shutdown():
            if self._order_processed:
                self._order_processed = False
                if len(orders) > 0:
                    # publish next order
                    current_order = orders.pop()
                    feedback.order_status.data = "Vending machine manager: Processing drink order: "\
                                                 + utils.getDrinkName(current_order)
                    self.server.publish_feedback(feedback)
                    rospy.loginfo(str(feedback.order_status.data))
                    new_order = std_msgs.Int8()
                    if current_order == self.drink1:
                        new_order.data = 1
                    else:
                        new_order.data = 2
                    self.pub_drink_order.publish(new_order)
                else:
                    all_orders_processed = True
            else:
                rospy.sleep(0.5)

        result = vending_machine_msgs.DrinkOrderResult()
        for drink in self.processed_orders:
            if drink not in result.delivered_drink_types:
                new_drink_type = vending_machine_msgs.DrinkType()
                new_drink_type.drink_type = drink
                result.delivered_drink_types.append(new_drink_type)
                result.delivered_drink_amounts.append(1)
            else:
                result.delivered_drink_amounts[result.delivered_drink_types.index(drink)] = \
                    result.delivered_drink_amounts[result.delivered_drink_types.index(drink)] + 1
        rospy.loginfo("Vending machine manager: Order processed.")
        self.server.set_succeeded(result)

    def spin(self):
        while not rospy.is_shutdown():
            rospy.sleep(1.0)
