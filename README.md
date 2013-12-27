## Installation

### Basic Preparation

```
> sudo apt-get update
> sudo apt-get install python-wstool python-rosdep ros-hydro-catkin
> sudo apt-get install --only-upgrade ros-hydro-*
> sudo pip install -U yujin_tools
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

### Rosjava Core Workspace


```
> yujin_init_workspace -j5 ~/rosjava rosjava
> cd ~/rosjava
> yujin_init_build .
> yujin_make --install-rosdeps
> yujin_make
```

### Android Core Workspace

```
> yujin_init_workspace -j5 ~/android android
> yujin_init_build --underlays="~/rosjava/devel" .
> yujin_make
```

### Rocon Rosjava Workspace

This needs to include a few message repos that rosjava needs to generate.

```
> yujin_init_workspace -j5 ~/rocon_rosjava rocon-rosjava
> cd ~/rocon_rosjava
> yujin_init_build --underlays="~/rosjava/devel;~/rocon/devel" .
> yujin_make --install-rosdeps
> yujin_make
```

### Rocon Android Workspace

```
> yujin_init_workspace -j5 ~/rocon_android rocon-android
> yujin_init_build --underlays="~/android/devel;~/rocon_rosjava/devel;~/rosjava/devel;~/rocon/devel" .
> yujin_make
```
