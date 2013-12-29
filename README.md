## Installation

### Basic Preparation

* Install [android studio](http://wiki.ros.org/android/Android Studio/Download).
* Don't forget to follow instructions for sdk installs (sdk build tools 18.1.1, api's 13, 15, 18).
* Start android studio one time and update to the latest studio version.

```
> sudo apt-get update
> sudo apt-get install python-wstool python-rosdep ros-hydro-catkin
> sudo apt-get install --only-upgrade ros-hydro-*
> sudo pip install -U yujin_tools
> rosdep update
```

### Rosjava Core Workspace


```
> yujin_init_workspace -j5 ~/rosjava rosjava-core
> cd ~/rosjava
> yujin_init_build .
> yujin_make --install-rosdeps
> yujin_make
```

### Rocon Rosjava Msgs Workspace

This includes message repos (rocon_msgs, yocs_msgs) that rosjava needs to generate.

```
> yujin_init_workspace -j5 ~/rocon_rosjava_msgs rocon-rosjava-msgs
> cd ~/rocon_rosjava_msgs
> yujin_init_build --underlays="~/rosjava/devel" .
> yujin_make --install-rosdeps
> yujin_make
```

### Android Core Workspace

```
> yujin_init_workspace -j5 ~/android android-core
> yujin_init_build --underlays="~/rosjava/devel" .
> yujin_make
```

### Ces Android Workspace

```
> yujin_init_workspace -j5 ~/ces_android ces-android
> yujin_init_build --underlays="~/android/devel;~/rocon_rosjava_msgs/devel;~/rosjava/devel" .
> yujin_make
```
