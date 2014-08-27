# How to start Office Simulation

## Preparation

### Device List
* Concert PC (x1)
 * ubuntu 12.04 (TBD update 14.04)
* Turtlebot (x1)
 * turtlebot main
 * netboock
* Docking station (x1)
* AR marker (x3)
 * AR paired (x2)
 * on docking station (x1)
* Android tablet (x1)
 * for map building
 * for annotation
 * for android remocon

### Concert PC Installation
* Ros installation (hydro)
  * https://docs.google.com/a/yujinrobot.com/document/d/1kZdSd3vDlq8_bFOO5chYN0bt4RtYgEQFqAcEEjs0Jd0/edit
* Additional package install
  * yujin_tools
    * https://github.com/yujinrobot/yujin_tools
  * roslint
    * http://wiki.ros.org/roslint
    * ```> sudo apt-get install ros-<version>-roslint```
* Rocon Install
  * First, Set up ```yujin_tools```,if you do not install one.
  ```
  
  > yujin_init_workspace rocon_ws https://raw.githubusercontent.com/robotics-in-concert/rocon/hydro-devel/rocon.rosinstall
  > cd rocon_ws
  > yujin_init_build .
  > . .bashrc
  > yujin_make --install-rosdeps
  > yujin_make
  > . .bashrc
  ```
* Office concert install
  
  ```
  > cd rocon_ws
  > cd src
  > wstool merge https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/office_concert/office_concert/rosinstalls/office_concert.rosinstall
  > wstool update -j5
  > cd ..
  > yujin_make --install-rosdeps
  > yujin_make
  > . .bashrc
  ```
### Map Building

## Run

### Office Concert Launch
* Launch concert

```
>  rocon_launch office_concert office_sim.concert --screen
```

* Launch the dummy task manager

```
> rocon_launch office_rapp office_task_manager_sim.launch --screen
```

* Launch the dummy order app

```
> rocon_launch office_rapp office_order_app_sim.launch --screen
```

* Launch the monitoring viewer
 * run the bleow command
 
 ```
 > rocon_remocon
 ```
 * Hit the "Add" button and put the MASTER_URI and HOST_NAME. If you launched concert in same PC, you can use the default value,"localhost" or pc ip instead of localhost.
 * Select "Office Concert" and double click
 * Doule click "Cafe Manager"
 * Doule click "Cafe Monitor" 

 


 

