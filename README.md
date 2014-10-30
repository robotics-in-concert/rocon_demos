# Turtlebot Concert 

### Installation

* Install ROS Indigo.

```
 > sudo apt-get install python-rosdep python-wstool ros-indigo-ros
 > sudo rosdep init
 > rosdep update
```

* Workspace setup

```
 > mkdir ~/rocon
 > cd ~/rocon
 > wstool init -j5 src https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/turtlebot_concert/concert.rosinstall
 > rosdep install --from-paths src -i -y
 > catkin_make
 > source ~/rocon/devel/setup.bash
```

* Convenience

```
 > echo "source ~/gazeborocon/devel/setup.bash" >> ~/.bashrc
```

### Starting Concert 

```
# nothing is running. 
> roslaunch turtlebot_concert concert.launch --screen
```

### Start turtlebot

```
> roslaunch turtlebot_bringup concert_client.launch --screen 
```

### Teleoperate Robots

Select a robot and teleop around. 

```
# Open up a new terminal
> rocon_remocon

# 1. select a concert. ROS_MASTER_URI=<concert> ROS_HOSTNAME=<my pc>
# 2. Choose role
# 3. Select Concert Teleop 
```
