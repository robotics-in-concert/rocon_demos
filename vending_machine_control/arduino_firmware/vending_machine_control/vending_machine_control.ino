//
// License: BSD
// https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
//

#include <Adafruit_NeoPixel.h>
#define USE_USBCON;
#include <ros.h>
#include <std_msgs/Empty.h>
#include <std_msgs/Int8.h>

int PIN_DRINK1 = 2;
int PIN_DRINK2 = 3;
int PIN_NEOPIXEL = 4; // neopixel
int drink_order;
bool drink_ordered;
bool dispensing_drink;
int trigger_time = 500;
int dispensing_time = 4000;
int elapsed_drink_time = 0;
int dispensed_signal_time = 1000;

// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(40, PIN_NEOPIXEL, NEO_GRB + NEO_KHZ800);

void drinkCB( const std_msgs::Int8& msg)
{
  if (!drink_ordered) // only trigger dispensing, if it is not already in progress
  {
    if (msg.data == 1)
    {
      drink_order = 1;
      digitalWrite(PIN_DRINK1, HIGH); // blink the led
    }
    else if (msg.data == 2)
    {
      drink_order = 2;
      digitalWrite(PIN_DRINK2, HIGH); // blink the led
    }
    else
    {
      drink_order = -1;
    }
    drink_ordered = true;
  }
}

ros::Subscriber<std_msgs::Int8> sub_drink_order("~drink_order", drinkCB );
std_msgs::Int8 order_result_msg;
ros::Publisher pub_order_result("~order_result", &order_result_msg);
ros::NodeHandle_<ArduinoHardware, 2, 2, 80, 105> nh;

void setup()
{
  pinMode(PIN_DRINK1, OUTPUT);
  pinMode(PIN_DRINK2, OUTPUT);
  nh.initNode();
  drink_ordered = false;
  dispensing_drink = false;
  elapsed_drink_time = 0;
  drink_order = -1;
  nh.subscribe(sub_drink_order);
  nh.advertise(pub_order_result);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
  
  while(!nh.connected())
  {
    nh.spinOnce();
    // blink orange to signal controller is not connected to ROS yet
//    colorFlush(strip.Color(255, 165, 0), 500);
    colorFlush(strip.Color(0, 255, 0), 500);
    colorFlush(strip.Color(0, 0, 0), 0);
    delay(500);
  }
  
  nh.getParam("~trigger_time", &trigger_time, 1);
  nh.getParam("~dispensing_time", &dispensing_time, 1);
  nh.getParam("~dispensed_signal_time", &dispensed_signal_time, 1);
  delay(500); // give some time to retrieve the parameters
    
  // blink green to signal controller is connected to ROS and fully ready
  colorFlush(strip.Color(255, 0, 0), 500);
  colorFlush(strip.Color(0, 0, 0), 0);
}

void loop()
{
  nh.spinOnce(); // checks for orders
  
  if (nh.connected())
  {
    if (dispensing_drink)
    {
      if (elapsed_drink_time >= dispensing_time)
      {
//        colorFlush(strip.Color(0, 0, 255), dispensed_signal_time); // signal drink has been dispensed
        colorFlush(strip.Color(0, 255, 0), dispensed_signal_time);
        colorFlush(strip.Color(0, 0, 0), 0); // signal drink has been dispensed
        order_result_msg.data = drink_order;
        pub_order_result.publish( &order_result_msg ); // send out message about dispensed drink
        
        elapsed_drink_time = 0;
        dispensing_drink = false;
        drink_ordered = false;
      }
      else
      {
        elapsed_drink_time += 500;
        delay(500);
      }
    }
    else if (drink_ordered)
    {
      delay(trigger_time); // keep drink triggers on long enough for the VM to trigger
      
      if (drink_order == 1)
      {
        digitalWrite(PIN_DRINK1, LOW); // turn off output
      }
      else if (drink_order == 2)
      {
        digitalWrite(PIN_DRINK2, LOW); // turn off output
      }
      dispensing_drink = true;
    }
    else
    {
      delay(500);
    }
  }
  else
  {
     // blink orange to signal controller is not connected anymore
//    colorFlush(strip.Color(255, 165, 0), 500);
    colorFlush(strip.Color(0, 255, 0), 500);
    colorFlush(strip.Color(0, 0, 0), 0);
    delay(500);
  }
}

// Fill all dots
void colorFlush(uint32_t c, uint32_t wait)
{
  for(uint16_t i=0; i<strip.numPixels(); i++)
  {
      strip.setPixelColor(i, c);
  }
  strip.show();
  delay(wait);
}
