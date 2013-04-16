/* 
 * Modified version of the rosserial IR Ranger example
 * 
 * This example is calibrated for the Sharp GP2Y0A21YK.
 */

#include <ros.h>
#include <ros/time.h>
#include <kobuki_arduino_msgs/RangersFixed.h>

ros::NodeHandle  nh;
kobuki_arduino_msgs::RangersFixed rangers_msg;
ros::Publisher pub_range( "rangers_data", &rangers_msg);

unsigned long last_rangers_time, rangers_timing, last_blink_time, blink_timing, now;
boolean led_on;
int val;

void setup()
{
  nh.initNode();
  nh.advertise(pub_range);
  
  rangers_msg.header.frame_id = "kobuki_rangers";
  rangers_timing = 500; // ms
  last_rangers_time = 0;
  blink_timing = 500; // ms
  last_blink_time = 0;
  pinMode(13, OUTPUT);
  led_on = false;
}

void loop()
{
  // publish the range value every 50 milliseconds,
  // since it takes that long for the sensor to stabilize
  now = millis();
  if ((now - last_rangers_time) > rangers_timing)
  {
    last_rangers_time = now;
    rangers_msg.header.stamp = nh.now();
    rangers_msg.range1 = analogRead(0);
    rangers_msg.range2 = analogRead(1);
    rangers_msg.range3 = analogRead(2);
    rangers_msg.range4 = analogRead(3);
    rangers_msg.range5 = analogRead(4);
    rangers_msg.range6 = analogRead(5);
    rangers_msg.range7 = analogRead(6);
    rangers_msg.range8 = analogRead(7);
    rangers_msg.range9 = analogRead(8);
    rangers_msg.range10 = analogRead(9);
    rangers_msg.range11 = analogRead(10);
    pub_range.publish(&rangers_msg);
  }
  nh.spinOnce();
    
  // Alive signal
  if ((now - last_blink_time) > blink_timing)
  {
    last_blink_time =  now;
    if (led_on)
    {
      digitalWrite(13, LOW);   // turn LED off
      led_on = false;
    }
    else
    {
      digitalWrite(13, HIGH);   // turn LED on
      led_on = true;
    }
  }
}

