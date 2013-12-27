## Installation

### Preparation

```
> sudo apt-get update
> sudo apt-get install python-wstool python-rosdep ros-hydro-catkin
> sudo apt-get install --only-upgrade ros-hydro-*
> rosdep update
```

### Rocon Workspace

```
> yujin_init_workspace -j5 ~/rocon rocon-devel
> cd ~/rocon
> yujin_init_build .
> yujin_make --install-rosdeps
> yujin_make
```

### Rosjava Workspace

This needs to include a few message repos that rosjava needs to generate.

```
> yujin_init_workspace -j5 ~/rosjava https://raw.github.com/robotics-in-concert/rocon_demos/ces_android/rocon_rosjava.rosinstall
> cd ~/rosjava
> yujin_init_build --underlays="~/rocon/devel" .
> yujin_make --install-rosdeps
> yujin_make
```

### Android Workspace

```
> yujin_init_workspace -j5 ~/android android
> yujin_init_build --underlays="~/rosjava/devel;~/rocon/devel" .
> yujin_make
```
