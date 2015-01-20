# Demo concert
## Services
* Pickup Delivery
    * concert_common_services/delivery
* VM Delivery
    * concert_common_services/delivery
* Welcome
    * concert_common_services/welcome

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
   * Register ros master uri and host name if you want to change it
   
     ```
     > export ROS_HOSTNAME=<your pc ip>
     > export ROS_MASTER_URI=<concert pc ip>
     ```
   * Register concert name if you want to change it
   
     ```
     > export CONCERT_NAME=<concert name>
     ```
   * Importing workflows to rocon_authoring
     * [Install Node and update rocon_authoring tool](https://github.com/robotics-in-concert/rocon_authoring/blob/master/README.md)
     *  Importing workflows in local database.
         *  A workflow file is in service directory and type of its name is ```XXX.json```(Ex. vm_delivery_wf.json, pickup_delivery_wf.js).
         *  User can use command line interface for importing,deleting workflows and showing workflow list.
            ```
            > cd <rocon workspace>/src/rocon_authoring
            > ./rocon_authoring_cli.js -a <workflows fullpath>
            > ./rocon_authoring_cli.js -l
            ```
         *  The option ```-a``` is adding a workflow and ```-l``` is showing list of workflows. you can get workflow full path in ```concert_common_services/services/<service directory>
      

* Running concert
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
       *  If you run concert the first time. you have to import the database about worldcanvas(map, wayporint, etc.)
          * Importing yujin db at worldcanvas
             * Run the pick up service above command
             * Call ros service for importing yujin rnd database to world canvas
                 ```
                 > rosservice call /software/world_canvas/yaml_import "filename: '<rocon_ws>/src/demo_concert/annotations/yujin_rnd_fulldb.yaml'"
                 ```
     * Order by order app
       *  Launch (Web remocon)[http://toyweb.cafe24.com:3008/rocon_web_remocon/index.html]
       *  Add the your concert master ip.(default: localhost)
