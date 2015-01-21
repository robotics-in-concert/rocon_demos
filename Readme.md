# Demo concert
## Services
* Pickup Delivery
    * concert_common_services/pickup_delivery
* VM Delivery
    * concert_common_services/vm_delivery
* Welcome
    * concert_common_services/welcome

## Installation
#### Rocon Install
* https://github.com/robotics-in-concert/rocon#installation

#### Demo Concert Install
    
    > cd <your rocon workspace>
    > cd src
    > wstool merge https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/rosinstall/demo_concert.rosinstall
    > wstool update -j10
    > cd ..
    > yujin_make --install-rosdeps
    > yujin_make
    > . .bashrc
    
#### Authoring tool installation

* [Install Node](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager#ubuntu-debian-linux-mint-elementary-os-etc)
* Install rocon_authoring dependency

   > roscd rocon_authoring
   > rocon_authoring
   > npm update
* Note that `npm update` would ask sudo access to install node-canvas dependency

## Preparation

* Configure ROS environment variables and concert name
  ```
  > export ROS_HOSTNAME=<your pc ip>
  > export ROS_MASTER_URI=<concert pc ip>
  > export CONCERT_NAME=<concert name>
  ```
*  Import workflows in local database
   ```
   > roscd rocon_authoring
   > ./rocon_authoring_cli.js -a <FULL_PATH_TO_WORKFLOW>
   ```
   * Demo concert includes three workflows
      * <Path to concert_common_services>/services/pickup_delivery/pickup_delivery_wf.json
      * <Path to concert_common_services>/services/vm_delivery/vm_delivery_wf.json
      * <Path to concert_common_services>/services/welcom/welcom_wf.json
   * Use the following command to verify whether workflows are loaded or not.
   
   > ./rocon_authoring_cli.js -l

## Execution
  * Pick up service 
      * Set the pick up service environment
         
          ```
          > cd <rocon_ws>/src/demo_concert/configuration
          > source pickup_online_webapp.sh
          ```
      * Launch pick up service with following command
         
          ```
          >  rocon_launch demo_concert pickup_sim.concert --screen
          ```
       *  If you run concert the first time, you have to import the database about worldcanvas(map, wayporint, etc.)
          * Importing yujin db at worldcanvas
             * Run the pick up service with above command
             * Call ros service for importing yujin rnd database to world canvas
                  
                  ```
                  > rosservice call /software/world_canvas/yaml_import "filename: '<rocon_ws>/src/demo_concert/annotations/yujin_rnd_fulldb.yaml'"
                  ```
  * Pick up oreder by order app
       *  Launch [Web remocon](http://toyweb.cafe24.com:3008/rocon_web_remocon/index.html)
          ![web remocon intro](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/imgs/web_remocon_intro.png)
       *  Hit the ```+``` and add the your master ip of concert (default: ws://localhost:9090)
       *  Click the ```connect``` to connect concert
          ![add master](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/imgs/web_remocon_add_master_ip.png)
          
       *  For launching order app, choose the role ```customer```, interaction ```pickup delivery order``` and start app
          ![pickup order app launching](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/imgs/web_remocon_monitoring_app_launch.png)
          ![pickup order app](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/imgs/web_remocon_order_app.png)
          
       *  Similary, for launching monitoring app, choose the role ```manager```, interaction ```pickup delivery monitor``` and start app
          ![pickup monitoring launching](https://github.com/robotics-in-concert/rocon_demos/blob/demo_concert/imgs/web_remocon_monitoring_app_launch.png)
          ![pickup monitoring](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/imgs/web_remocon_monitoring_app.png)
       *  Hit any point button in order app for send pick up order to robot, and check robot movement(triangle) in the monitoring app
