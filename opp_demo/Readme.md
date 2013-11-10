
# How to start Teleop via Concert 

## Preparation
### Concert Master side

- install

<pre>
> sudo apt-get install ros-hydro-turtlebot ros-hydro-rocon ros-hydro-unique-identifier
</pre>

- Setup workspace using this rosinstall file

<pre>
https://raw.github.com/robotics-in-concert/rocon_demos/hydro-devel/opp_demo/rosinstalls/concert_master.rosinstall
</pre>

- Compile it

- Starts up Concert Master

<pre>
> roslaunch concert_tutorial concert.launch
</pre>

### Robot side ===

- install

<pre>
> sudo apt-get install ros-hydro-turtlebot ros-hydro-rocon ros-hydro-unique-identifier
</pre>

- Setup workspace using waiterbot.rosinstall

<pre>
https://raw.github.com/robotics-in-concert/rocon_demos/hydro-devel/opp_demo/rosinstalls/waiterbot.rosinstall
</pre>

- Compile it

- Setup env variables

<pre>
> export ROBOT_NAME=<YOUR ROBOT NAME>
> export ROBOT_HUB_WHITELIST="<CONCERT_NAME>"
</pre>

- Starts up robot

<pre>
> roslaunch turtlebot_bringup minimal_with_appmanager.launch
</pre>

## Starting Teleop service ==

- Enable Teleop service

<pre>
> rosservice call /concert/service/enable '{concertservice_name: Teleop, enable: true }'
</pre>

## Useful service or topics ==

* rosservice call /concert/resource_status
* rostopic echo /concert/list_concert_services

