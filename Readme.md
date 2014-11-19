# Demo concert
## Services
* Delivery
    * concert_common_services/delivery
* Delivery Simulation
    * concert_common_services/delivery_sim
* Welcome
    * concert_common_services/welcome
* Restock
    * concert_services/concert_service_waypoint_navigation

## Rapps
* Robosem Bridge
   * concert_common_rapps/robosem_bridge
* Real Waiterbot 
   * concert_common_rapps/waiter_real
* Simulation Waiterbot
   * concert_common_rapps/waiter_sim
* Dummy Gocart
   * concert_common_rapps/dummy_gocart

## Rocon Install
* https://github.com/robotics-in-concert/rocon_demos/tree/office_concert#concert-pc-installation

## Demo Concert Install
    
    > cd <your rocon workspace>
    > cd src
    > wstool merge https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/rosinstall/demo_concert.rosinstall
    > wstool update -j10
    > cd ..
    > yujin_make --install-rosdeps
    > yujin_make
    > . .bashrc
    
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
     * Run the [rocon_authoring tool](https://github.com/robotics-in-concert/rocon_authoring/blob/master/README.md)
        
        ```
        > roscd rocon_authoring
        > npm update
        > MONGO_URL=mongodb://localhost:27017/cento_authoring PORT=9999 ROS_WS_URL=ws://127.0.0.1:9090 node rocon_authoring.js
        ```
     * Open browser and enter ```http://localhost:9999/``` in adress bar.
     * Hit ```import items``` button and import workflow files in each services directory.
     * Click the loaded workflow and check the blocks.
   * Importing yujin db
     * Call ros service for importing yujin rnd database to world canvas
         ```
         > rosservice call /software/world_canvas/yaml_import "filename: '<rocon_ws>/src/demo_concert/annotations/yujin_rnd_fulldb.yaml'"
         ```
      

* Running
  * Simulation 
  
     ```
     >  rocon_launch demo_concert demo_sim.concert --screen
     ```
  * Real 
  
     ```
     >  rocon_launch demo_concert demo.concert --screen
     ```
  * Launch Service
    * Launch remocon and add the demo concert uri.
    * Select the ```Admin``` in Roles chooser.
    * Double click the ```Concert Service Administartion``` interactions.
    * Choose the service wanted to run and hit ```Enable```
  * Order app
    * Order app is able to run after delivery or delivery_sim service is enabled.
    * Launch remocon and add the demo concert uri.
    * Select the ```Customer``` in Roles chooser.
    * Double click the ```Delivery Order App``` interactions.
  * Monitoring
    * Monitoring is able to run after delivery or delivery_sim service is enabled.
    * Launch remocon and add the demo concert uri.
    * Select the ```Manager``` in Roles chooser.
    * Double click the ```Monitor``` interactions.
