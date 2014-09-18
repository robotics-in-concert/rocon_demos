# Office Gazebo Solution

### Installation

1. Install ROS Indigo.

```
 > sudo apt-get install python-rosdep python-wstool ros-indigo-ros
 > sudo rosdep init
 > rosdep update
```

2. Workspace setup

```
 > mkdir ~/gazeborocon
 > cd ~/gazeborocon
 > wstool init -j5 src https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/gazebo_concert/gazebo_solution.rosinstall
 > rosdep install --from-paths src -i -y
 > catkin_make
 > source ~/gazeborocon/devel/setup.bash
```

3. Convenience

```
 > echo "source ~/gazeborocon/devel/setup.bash" >> ~/.bashrc
```

### Starting Concert 

**Note that it may take longer time when you bring up gazebo very first time**

```
> roslaunch office_sim_solution concert.launch --screen
```

### Teleoperate Robots

Select a robot and teleop around

```
> concert_teleop
```
