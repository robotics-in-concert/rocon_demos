# Office Gazebo Solution

### Installation

* Install ROS Indigo.

```
 > sudo apt-get install python-rosdep python-wstool ros-indigo-ros
 > sudo rosdep init
 > rosdep update
```

* Workspace setup

```
 > mkdir ~/gazeborocon
 > cd ~/gazeborocon
 > wstool init -j5 src https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/gazebo_concert/gazebo_solution.rosinstall
 > rosdep install --from-paths src -i -y
 > catkin_make
 > source ~/gazeborocon/devel/setup.bash
```

* Convenience

```
 > echo "source ~/gazeborocon/devel/setup.bash" >> ~/.bashrc
```

### Starting Concert 

**Note that it may take longer time when you bring up gazebo very first time**

```
> roslaunch office_sim_solution concert.launch --screen
```

![Image of gazebo](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/gazebo_concert/imgs/gazebo.png)

### Teleoperate Robots

Select a robot and teleop around.

```
# Open up a new terminal
> concert_teleop
```
![Image of teleop](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/gazebo_concert/imgs/teleop.png)
