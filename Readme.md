# Demo concert
## Installation
#### Rocon Install
* https://github.com/robotics-in-concert/rocon#installation
* Troubleshooting
  * When following error occurred, please refer to [installation of ros](http://wiki.ros.org/indigo/Installation/Ubuntu)

#### Demo Concert Install
```    
    > cd <your rocon workspace>
    > cd src
    (Try to launch simulation demo concert)
    > wstool merge https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/rosinstall/demo_concert_sim.rosinstall
    (Try to launch real demo concert)
    > wstool merge https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/rosinstall/demo_concert.rosinstall
    
    > wstool update -j10
    > cd ..
    > yujin_make --install-rosdeps
    > yujin_make
    > . .bashrc
```    
#### Workflow engine installation

1. [Install Node](https://github.com/joyent/node/wiki/Installing-Node.js-via-package-manager#ubuntu-debian-linux-mint-elementary-os-etc)
2. Install concert_workflow_engine_blockly dependency

```  
    > roscd concert_workflow_engine_blockly
    > npm update
```

3. Note that `npm update` would ask sudo access to install node-canvas dependency
    
## Preparation

* Configure ROS environment variables and concert name
```
     > export ROS_HOSTNAME=<your pc ip> (ex. export ROS_HOSTNAME=192.168.10.24)
     > export ROS_MASTER_URI=<concert pc ip> (ex. export ROS_HOSTNAME=http://192.168.10.24:11311)
     > export CONCERT_NAME=<concert name>  (ex. export CONCERT_NAME=demo_concert)
```

## Execution

#### Pick up only solution
* Configure the pick up service environment
```    
    > roscd demo_concert/configurations
    > source pickup_online_webapp.sh
```    

* Import world canvas database
 * Launch the concert for importing world canvas annotation.
 
      ```    
      > roslaunch demo_concert concert.launch --screen
      ```
 * Open new termianl.
  
      ```
      > cd <your rocon workspace>
      > . .bashrc
      > rosservice call /software/world_canvas/yaml_import `rospack find demo_concert`/annotations/yujin_rnd_fulldb.yaml
      ``` 
 * When you check following message,terminate concert by ```ctrl+c```.
  
      ```
      result: True
      message: ''
      ```

* Start pick up service with following command
```         
    >  rocon_launch demo_concert pickup_sim.concert --screen
```    
   
* Pickup order
   * Open Web Remocon(http://remocon.robotconcert.org)
   ![web remocon intro](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/imgs/web_remocon_intro.png)

   *  Click the ```+``` and add the your master ip of concert (default: ws://localhost:9090)
   *  Click the ```connect``` to connect concert
   ![add master](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/imgs/web_remocon_add_master_ip.png)
          
   *  To open order app, choose the role ```customer```, interaction ```pickup delivery order``` and start app
      ![pickup order app launching](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/imgs/web_remocon_monitoring_app_launch.png)
      ![pickup order app](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/imgs/web_remocon_order_app.png)
          
* Delivery Monitor
   * To launch delivery monitor app, choose the role ```manager```, interaction ```pickup delivery monitor``` and start app
   ![pickup monitoring launching](https://github.com/robotics-in-concert/rocon_demos/blob/demo_concert/imgs/web_remocon_monitoring_app_launch.png)
   ![pickup monitoring](https://raw.githubusercontent.com/robotics-in-concert/rocon_demos/demo_concert/imgs/web_remocon_monitoring_app.png)

