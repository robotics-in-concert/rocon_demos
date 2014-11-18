# Demo concert
## Services
* Delivery
* Delivery Simulation
* Welcome
* Restock
## Demo Concert Install
  ```
  > cd <your rocon workspace>
  > cd src
  > wstool merge https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/rosinstall/demo_concert.rosinstall
  > wstool update -j10
  > cd ..
  > yujin_make --install-rosdeps
  > yujin_make
  > . .bashrc
  ```
## Run
* Preparing
   * Register ros master uri and host name
     ```
     > export ROS_HOSTNAME=<your pc ip>
     > export ROS_MASTER_URI=<concert pc ip>
     ```
   * Register concert name
     ```
     > export HUB_WHITELIST=<concert name>
     ```
   * Setting rocon authoring tool
     * Run the rocon_authoring tool
       * https://github.com/robotics-in-concert/rocon_authoring/blob/master/README.md
     * Open browser and enter ```http://localhost:9999/``` in url.
     * Hit ```import items``` button and import workflow files in each services.
     * Check the loaded blocks

* Running
  * Simulation 
   ```
   >  rocon_launch office_concert office_sim.concert --screen
   ```
  * Real 
   ```
   >  rocon_launch office_concert office.concert --screen
   ```
  * Launch Service
  * Order app
  * Monitoring
