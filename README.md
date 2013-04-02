rocon_demo
==========

Demo software for rocon milestones.

## Cafe Concert ##

* Works in Hydro!!!

#### Installation ####

 * Create a workspace

```
> mkdir -p ~/cafe_solution
> mkdir -p ~/cafe_solution/src
> cd ~/cafe_solution/src
> catkin_init_workspace
```

* Check out rocon

```
> cd ~/cafe_solution/src
> rosinstall . https://raw.github.com/robotics-in-concert/rocon_demos/hydro-devel/cafe_concert.rosinstall
```

* For easy way of creating workspace. Check out yujin_tools(https://github.com/yujinrobot/yujin_tools/wiki/yujin-init)


#### Compilation ####

```
> cd ~/cafe_solution
> ctkin_make
```

#### Execution ####

* Simple way to launch for demonstration in one computer

```
> source ~/cafe_solution/devel/setup.bash
> rospack profile
> rocon_launch cafe_concert cafe.concert -g
> rosservice call /concert/start_solution
```

* In case simple way does not work
  * Don't forget to source the correct setup.bash
  * Run each command separate terminal

```
> roslaunch cafe_concert concert.launch --port=11311
> roslaunch cafe_database cafe_database_client.launch --port=11313
> roslaunch waiterbot waiter_client.launch --port=11313
> roslaunch waiterbot waiter_client.launch --port=11314
> roslaunch waiterbot waiter_client.launch --port=11315
> rosservice call /concert/start_solution
```

#### Visualization ####

* TODO
