#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import vending_machine_control.msg as vending_machine_msgs

def verifyDrinkType(new_drink, drink1, drink2):
    '''
        Checks, if drink number matches the knows drinks
    '''
    if new_drink == vending_machine_msgs.DrinkType.COKE or \
        new_drink == vending_machine_msgs.DrinkType.CIDER or \
        new_drink == vending_machine_msgs.DrinkType.MAX:
        if new_drink == drink1 or new_drink == drink2:
            return True
        else:
            rospy.logwarn("Drink type '" + getDrinkName(new_drink) + "' currently not available.")
            return False
    else:
        rospy.logerr("Unknown drink type '" + str(new_drink) + "'")
        return False

def getDrinkName(drink):
    '''
        Returns the name of the drink type
    '''
    if drink == vending_machine_msgs.DrinkType.COKE:
        return "Coke"
    elif drink == vending_machine_msgs.DrinkType.CIDER:
        return "Cider"
    elif drink == vending_machine_msgs.DrinkType.MAX:
        return "Max"
    else:
        rospy.logerr("Unknown drink type '" + str(drink) + "'")
        return ""
