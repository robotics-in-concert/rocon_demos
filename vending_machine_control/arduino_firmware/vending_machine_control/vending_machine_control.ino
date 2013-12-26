//
// License: BSD
// https://raw.github.com/robotics-in-concert/concert_apps/license/LICENSE
//

#define USE_USBCON;

#include <ros.h>
#include <std_msgs/Int8.h>

int PIN_DRINK1 = 2;
int PIN_DRINK2 = 3;
int drink_order;
bool drink_ordered;

void drinkCb( const std_msgs::Int8& msg)
{
  if (msg.data == 1)
  {
    drink_order = 1;
    digitalWrite(PIN_DRINK1, HIGH);   // blink the led
  }
  else if (msg.data == 2)
  {
    drink_order = 2;
    digitalWrite(PIN_DRINK2, HIGH);   // blink the led
  }
  else
  {
    drink_order = -1;
  }
  drink_ordered = true;
}

//std_msgs::UInt8 order_msg;
ros::Subscriber<std_msgs::Int8> sub_drink_order("~drink_order", drinkCb );

std_msgs::Int8 order_result_msg;
ros::Publisher pub_order_result("~order_result", &order_result_msg);

ros::NodeHandle_<ArduinoHardware, 2, 2, 80, 105> nh;

void setup()
{
  pinMode(PIN_DRINK1, OUTPUT);
  pinMode(PIN_DRINK2, OUTPUT);
  nh.initNode();
  drink_ordered = false;
  drink_order = -1;
  nh.subscribe(sub_drink_order);
  nh.advertise(pub_order_result);
}

void loop()
{
  nh.spinOnce(); // checks for orders
  
  delay(500);
 
  if (drink_ordered)
  {
    if (drink_order == 1)
    {
      digitalWrite(PIN_DRINK1, LOW); // turn off output
    }
    else if (drink_order == 2)
    {
      digitalWrite(PIN_DRINK2, LOW); // turn off output
    }
    order_result_msg.data = drink_order;
    pub_order_result.publish( &order_result_msg );
    drink_ordered = false;
  }
}
