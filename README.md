rocon_demo
==========

Demo software for rocon milestones.

## Cafe Concert ##

* Works in Hydro!!!

#### Pre-requisite

```
sudo apt-get install postgresql python-psycopg2
sudo apt-get install ros-groovy-turtlebot
sudo apt-get install ros-groovy-turtlebot-apps
sudo apt-get install ros-groovy-turtlebot-viz
sudo apt-get install ros-groovy-rospy-message-converter
sudo apt-get install ros-groovy-rocon
rosdep install rocon_hub
rosdep install rocon_concert
```

#### Installation ####

 * Create a workspace

```
> mkdir -p ~/cafe_solution
> mkdir -p ~/cafe_solution/src
> cd ~/cafe_solution/src
> catkin_init_workspace
```

* Checkout rocon

```
> cd ~/cafe_solution/src
> wstool init . https://raw.github.com/robotics-in-concert/rocon_demos/hydro-devel/cafe_concert.rosinstall
```

* For easy way of creating workspace. Check out yujin_tools(https://github.com/yujinrobot/yujin_tools/wiki/yujin-init)


#### Compilation ####

```
> cd ~/cafe_solution
> catkin_make
```

#### Preparation for World Model Database ####

Postgresql setting for spatial world model in local machine. In order to start the cafe demo solution,
the database should contain 'Dock', 'Kitchen', 'Table1'~'Table8'. Please store the data by following instruction.

* Follow the installation instruction in the SWM ros wiki for spatial world model setting.
  * http://www.ros.org/wiki/spatial_world_model
  * Postgresql require some configuration to allow remote access. Please check the link below to enable remote access.
  * https://kb.mediatemple.net/questions/1237/How+do+I+enable+remote+access+to+my+PostgreSQL+server%3F#dv

* Bring up the annotation app.

```
> roslaunch cafe_rapps annotation.launch
```

* Bring up the rocon_webnotator table handler interface
** files:///<PATH_TO_WORKSPACE>/rocon_webnotator/www/table_handler.html

* Annotate 'Dock', 'Kitchen', and Tables.
* Done.

#### Execution ####

* Simple way to launch a demo solution in one computer

```
> source ~/cafe_solution/devel/setup.bash
> rospack profile
> rocon_launch cafe_concert cafe.concert
> rosservice call /concert/start_solution
```
