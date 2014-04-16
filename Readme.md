
# How to start Cafe Simulation

## Preparation

#### install

<pre>
> sudo apt-get install ros-hydro-turtlebot ros-hydro-rocon ros-hydro-unique-identifier ros-hydro-bondpy ros-hydro-ar-track-alvar ros-hydro-kobuki-soft
</pre>

- Setup workspace using this rosinstall file

<pre>
https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/cafe_concert/cafe_concert/rosinstalls/concert_master.rosinstall
</pre>

- Compile it

- Starts up Cafe simulation

<pre>
> rocon_launch cafe_concert cafe_sim.concert --screen
</pre>


