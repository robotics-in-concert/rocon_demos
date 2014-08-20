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
    * https://docs.google.com/a/yujinrobot.com/document/d/1kZdSd3vDlq8_bFOO5chYN0bt4RtYgEQFqAcEEjs0Jd0/edit
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
  
