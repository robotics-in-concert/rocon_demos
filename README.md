## Installation

### Preparation

```
> sudo apt-get update
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
> yujin_init_build --underlays="~/rocon" .
> yujin_make --install-rosdeps
> yujin_make
```

### Android Workspace

```
> yujin_init_workspace -j5 ~/android android
```
