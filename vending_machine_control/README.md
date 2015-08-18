
Vending Machine Control
=======================

You must install the Arduino udev rule to make the board available on the default port `/dev/arduino_yun`:

$ roscd vending_machine_control
$ sudo cp resources/udev/60-arduino.rules /etc/udev/rules.d

and then restart udev rule, replug the USB cable.
