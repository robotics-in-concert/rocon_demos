## Issues

### Large 'X Left of Marker' Errors

* I reproduced the algorithm in python on my machine with the same sensor - very reliable calculations.
 * Guessing there's something in the code, or in the configuration of the ar_alvar_markers that is wrong.
 * Is the `marker_size` parameter set correctly?
* This code is here, instructions on how to use it below.

### Getting the Robot Pose

No problem.

* We need more information than the magnitude of the distance.
* This is ok, we can use the position x, y, z and still avoid the orientation.
 * Lots of extra power in these extra variables!
* Calculation of angles and target relative pose (position and heading) example code in the script.


## Usage

### Running the Script

My example code is pretty atrocious - trying to stay awake inbetween naps, but it works.

```
> roslaunch openni_launch openni.launch
> roslaunch ar_alvar_testies testies.launch
> roscd ar_alvar_testies
> ./testies.py
```

This will show you all the calculated variables for both left and right ar markers (make sure the 'sideways E' is the right marker!). I set these markers 26cm apart.

### Understanding the Script

The calculated target x, z and heading is relative to the camera rgb pose (z forward, x to the right).
In the script I've set the target location 40cm in front of the wall and inbetween the markers.

### Problems with the Script - Not Very Wide Angle

It doesn't have a very wide angle range - does playing around with the tracking error parameters help this? 

### Problems with the Script

Gets false positive measurements when a marker is at the edge. Here the z-value is wrong (really too small). Should be easy to filter these out (i.e. anything below z=20) since we don't get that close anyway.

