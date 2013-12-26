#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import actionlib
import rospy
import vending_machine_control.msg as vending_machine_msgs
import std_msgs.msg as std_msgs

class VendingMachineManager(object):
    """
        Vending machine manager
    """
    def __init__(self):
        '''
            Arduino communication
        '''
        self.pub_drink_order = rospy.Publisher('arduino/drink_order', std_msgs.Int8)
        self.sub_order_result = rospy.Subscriber('arduino/order_result', std_msgs.Int8, self._arduinoOrderResultCB)
        ''' indicates if the last sent order has been processed '''
        self.order_processed = True
        ''' list of processed orders '''
        self.processed_orders = []
        ''' stores the currently processed drink type '''
        self.current_order = 0

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
        processed_order = int()
        if data.data == 1:
            processed_order = self.drink1
            self.processed_orders.append(processed_order)
            self.order_processed = True
        elif data.data == 2:
            processed_order = self.drink2
            self.processed_orders.append(processed_order)
            self.order_processed = True
        else:
            rospy.logerr("Vending machine did not process the order correctly! Error code: " + str(data.data))

    def _execute(self, goal):
        feedback = vending_machine_msgs.DrinkOrderFeedback()
        feedback.order_status.data = "Processing orders ..."
        self.server.publish_feedback(feedback)
        rospy.loginfo(str(feedback.order_status.data))
        ''' parse goal and send order to Arduino '''
        all_orders_processed = False
        orders = []
        for type in goal.drink_types:
            if self.verifyDrinkType(type.drink_type):
                drink_amount = goal.drink_amounts[goal.drink_types.index(type)]
                for x in range (0, drink_amount):
                    orders.append(type.drink_type)
        orders.reverse()

        while not all_orders_processed and not rospy.is_shutdown():
            if len(orders) > 0:
                if self.order_processed:
                    ''' publish next order '''
                    self.current_order = orders.pop()
                    feedback.order_status.data = "Processing order: " + self.getDrinkName(self.current_order)
                    self.server.publish_feedback(feedback)
                    rospy.loginfo(str(feedback.order_status.data))
                    new_order = std_msgs.Int8()
                    if self.current_order == self.drink1:
                        new_order.data = 1
                    else:
                        new_order.data = 2
                    self.pub_drink_order.publish(new_order)
                    self.order_processed = False
                rospy.sleep(0.5)
            else:
                all_orders_processed = True

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
        self.server.set_succeeded(result)

    def spin(self):
        while not rospy.is_shutdown():
            rospy.sleep(1.0)

##############################################################################
# Utils
##############################################################################
    '''
        Checks, if drink number matches the knows drinks
    '''
    def verifyDrinkType(self, drink):
        if drink == vending_machine_msgs.DrinkType.COKE or \
            drink == vending_machine_msgs.DrinkType.CIDER or \
            drink == vending_machine_msgs.DrinkType.MAX:
            if drink == self.drink1 or drink == self.drink2:
                return True
            else:
                rospy.logwarn("Drink type '" + self.getDrinkName(drink) + "' currently not available.")
                return False
        else:
            rospy.logerr("Unknown drink type '" + str(drink) + "'")
            return False

    '''
        Returns the name of the drink type
    '''
    def getDrinkName(self, drink):
        if drink == vending_machine_msgs.DrinkType.COKE:
            return "Coke"
        elif drink == vending_machine_msgs.DrinkType.CIDER:
            return "Cider"
        elif drink == vending_machine_msgs.DrinkType.MAX:
            return "Max"
        else:
            rospy.logerr("Unknown drink type '" + str(drink) + "'")
            return ""
