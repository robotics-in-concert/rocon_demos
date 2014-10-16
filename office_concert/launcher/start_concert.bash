#!/bin/bash
exec gnome-terminal -x bash -c "source ~/research/ros/waiterbot/devel/setup.bash; roslaunch office_concert concert.launch --screen"
