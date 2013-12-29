## Installation

### Basic Preparation

* Install [android studio](http://wiki.ros.org/android/Android Studio/Download).
* Don't forget to follow instructions for sdk installs (sdk build tools 18.1.1, api's 13, 15, 18).
* Start android studio one time and update to the latest studio version.
* Update and install all the ros tools:

```
> sudo apt-get update
> sudo apt-get install python-wstool python-rosdep ros-hydro-catkin
> sudo apt-get install --only-upgrade ros-hydro-*
> sudo pip install -U yujin_tools
> rosdep update
```

### Rocon Rosjava Msgs Workspace

This includes message repos (rocon_msgs, yocs_msgs) that rosjava needs to generate.

```
> yujin_init_workspace -j5 ~/rocon_rosjava_msgs rocon-rosjava-msgs
> cd ~/rocon_rosjava_msgs
> yujin_init_build .
> yujin_make --install-rosdeps
> yujin_make
```

### Ces Android Workspace

Currently includes android apps and remocons, simply because I'm likely to make fixes on them while doing this:

```
> yujin_init_workspace -j5 ~/ces_android ces-android
> cd ~/ces_android
> yujin_init_build --underlays="~/rocon_rosjava_msgs/devel" .
> yujin_make
```

## Usage

* Setup a core rocon workspace

```
> yujin_init_workspace -j5 ~/rocon rocon-devel
> cd ~/rocon
> yujin_init_build  .
> yujin_make --install-rosdeps
> yujin_make
> echo export ROS_MASTER_URI=http://192.168.1.3:11311 >> .bashrc
> echo export ROS_IP=192.168.1.3 >> .bashrc
> . .bashrc
```

* Start the app manager

```
> roslaunch rocon_app_manager standalone.launch --screen
```

* In android studio, deploy the listener apk. 
* Start the listener app on the android 
* Connect to your ros master's ip
