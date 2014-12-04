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

### Befor Start

Make sure gazebo server has updated it's database properly.

```
> gzserver 
```

Then wait for 2~3 mins until it finishes database update. Once it finishes, make sure gzclient shows empty zone properly.

```
# in another terminal
> gzclient 
```

### Starting Concert 

**Note that it may take longer time when you bring up gazebo very first time**

```
# nothing is running. 
> roslaunch office_sim_solution concert.launch --screen
```

![Image of gazebo](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/gazebo_concert/imgs/gazebo.png)

### Teleoperate Robots

Select a robot and teleop around. Note that only Dangen(TurtleBot) provides camera stream. Kobuki and segbot do not have camera stream.

```
# Open up a new terminal
> concert_teleop
```
![Image of teleop](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/gazebo_concert/imgs/teleop.png)

### Test Dummy furo

```
# Open up a new termianl 
> roslaunch dummy_furo concert_client.launch simulation:=true --screen --port=11315
```

To test real robot, simulation:=false

### Rocon Remocon

1. Launch rocon remocon 
![Image of remocon](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/gazebo_concert/imgs/rocon_remocon.png)

```
# Open up a new terminal
> rocon_remocon 
```

2. Add Concert
![Image of add](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/gazebo_concert/imgs/add_concert.png)

3. Select role and start available apps

![Image of role](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/gazebo_concert/imgs/role.png)
![Image of user](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/gazebo_concert/imgs/user.png)
