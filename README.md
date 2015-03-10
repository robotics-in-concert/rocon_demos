# Turtlebot Concert 

### Installation

* Install ROS Indigo.

```
 > sudo apt-get install python-rosdep python-wstool ros-indigo-ros
 > sudo rosdep init
 > rosdep update
```

* Concert PC setup

```
 > sudo apt-get install ros-indigo-rocon-*
 > sudo apt-get install ros-indigo-concert-*
 > mkdir ~/rocon
 > cd ~/rocon
 > wstool init -j5 src https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/turtlebot_concert/concert.rosinstall
 > rosdep install --from-paths src -i -y
 > catkin_make
 > source ~/rocon/devel/setup.bash
```

* Turtlebot setup

```
  > sudo apt-get install ros-indigo-turtlebot-*
  > mkdir ~/turtlebot
  > cd ~/turtlebot
  > wstool init -j5 src https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/turtlebot_concert/turtlebot.rosinstall
  > rosdep install --from-paths src -i -y
  > catkin_make
  > source ~/turtlebot/devel/setup.bash

```

## Concert Mode

* Start concert

```
# nothing is running. 
> roslaunch turtlebot_concert concert.launch --screen
```

* Start turtlebot

```
> roslaunch turtlebot_bringup concert_client.launch concert_whitelist:="[Turtlebot Concert]" --screen
```

* Teleoperate Robots

Select a robot and teleop around. 

```
# Open up a new terminal
> rocon_remocon

# 1. add and select concert. ROS_MASTER_URI=<CONCERT_PC IP> ROS_HOSTNAME=<MY PC>
# 2. Choose role
# 3. Select Concert Teleop 
```

### Teleop turtlebot without concert 

* Start Turtlebot from turtlebot laptop

```
  > roslaunch turtlebot_bringup minimal.launch --screen
```

* From workstation

```
# Open up a new terminal
> rocon_remocon

# 1. select a concert. ROS_MASTER_URI=<TURTLEBOT_IP> ROS_HOSTNAME=<MY PC>
# 2. Choose role
# 3. Select Teleop 
```
