/* 
 * Analog input test
 */

const int nr_of_irs = 11;
const int ir_pins[nr_of_irs] = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
unsigned long last_rangers_time, rangers_timing, last_blink_time, blink_timing, now;
boolean led_on;
int val;

void setup()
{
  rangers_timing = 500; // ms
  last_rangers_time = 0;
  blink_timing = 500; // ms
  last_blink_time = 0;
  pinMode(13, OUTPUT);
  led_on = false;
  Serial.begin(57600);
}

void loop()
{
  // publish the range value every 50 milliseconds,
  // since it takes that long for the sensor to stabilize
  now = millis();
  if ((now - last_rangers_time) > rangers_timing)
  {
    last_rangers_time = now;
    Serial.println("vvvvvvvvvvvvvvvvvvv");
    for (unsigned int ir = 0; ir < nr_of_irs; ++ir)
    {
      val = analogRead(ir_pins[ir]);
      Serial.print("analog read ");
      Serial.print(ir, DEC);
      Serial.print(":");
      Serial.print("\t");
      Serial.println(val, DEC);
    }   
  }
    
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
