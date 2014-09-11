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
* It is necessary process for using robot in delivery service. 
* Preparing
 * Robot side
   + Launch turtlebot
   
     ```
     > roslaunch turtlebot_bringup minimal.launch --screen
     ```
   
    + Launch gmapping app 
   
     ```
     > roslaunch turtlebot_navigation gmapping_demo.launch --screen
     ```
   
 * Monitoring PC side 
   + Map building monitoring
   
     ```
     > source /opt/ros/<ros-version>/setup.bash
     > export ROS_MASTER_URI=http://<robot ip>:11311
     > roslaunch turtlebot_rviz_launchers view_navigation.launch --screen
     ```
    + Robot control by keyboard
   
     ```
     > source /opt/ros/<ros-version>/setup.bash
     > export ROS_MASTER_URI=http://<robot ip>:11311
     > roslaunch turtlebot_teleop keyboard_teleop.launch --screen
     ```
* Making Map
  * If preparing is finished, move the turtlebot by keyboard.
  * Save the map if the making map finished.
   + save map
  
     ```
     > source /opt/ros/<ros-version>/setup.bash
     > export ROS_MASTER_URI=http://<robot ip>:11311
     > rosrun map_server map_saver -f <saved map diectory path>/<map name>
     ```
  * The first saved map contain the needless part.Thus, it is croped for using easily.
   + crop map
  
     ```
     > rosrun map_server crop_map -f <saved map diectory path>/<map name> 
     ```
  * Move the map file(<name>.yaml, <name>.pgm) to ```maps``` directory in concert.

* Map Annotating
  * Saving special point in the map in order to sementic navigation through android app.
   + Install ```rocon remocon```
     * http://files.yujinrobot.com/android/apks/rocon_remocon_release_indigo.apk
   + Install ```map annotation```
     * http://files.yujinrobot.com/android/apks/map_annotation_release_indigo.apk
  * Launch office concert so as to run database service.
  
   ```
   > rocon_lauch office_concert office_sim.concert --screen
   ```
  
  * Launch rocon remocon
    * Add IP of launched concert
    * Select office concert
    * Select role as office manager
  * Launch map annotation
    * Check obtainging map about office.
    * Register table, pickup, docking station position.
    * Register ar marker above docking position.


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
 * run the rocon_remocon through bleow command
 
 ```
 > rocon_remocon
 ```
 * Hit the "Add" button and put the MASTER_URI and HOST_NAME. If you launched concert in same PC, you can use the default value,"localhost" or pc ip instead of localhost.
 * Select "Office Concert" and double click
 * Doule click "Cafe Manager"
 * Doule click "Cafe Monitor" 

 


 

