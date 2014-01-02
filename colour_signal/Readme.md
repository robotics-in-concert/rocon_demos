## Colour Signal

### Overview

Converts an incoming image stream to hsv format and produces a histogram of the hue. It then looks internally into the percentage of pixels that fall into narrow bounds around blue, green and red hues (since they are are led hues) and compares the difference of the selected hue with the others.

If the difference is significant, it registers it as a led signal.

### Usage

Include `standalone.launch` in your own launcher and configure it via the supplied args. You will
need to configure the image_topic handle and remap your own handles to its enable and result publishers.

Don't forget to enable/disable it for only the periods where you want to actually detect led signals otherwise you will do alot of processing and consume alot of socket bandwidth for no reason (it disables the subscriber when not in use).

### Topics

These are the topics for the main launcher (`standalone.launch`).

*Publishers*

 * *~/result [std_msgs/Bool]* : latched publisher of the signal detection state (0, 1) (only publishes when the state changes)

*Subscribers*

 * *~/enable [std_msgs/Bool]* : enable, disable processing for detection of signal state.
 * *~/image [sensor_msgs/Image]* : handle to the image producer.

### Launchers

 * **Nodes**
  * `standalone.launch` : the official node - hook up to an sensor_msgs/Image producer. 
 * **Test Launchers** 
  * `bgr_histograms.launch` : calculate and plot bgr histograms for the test images.
  * `hsv_histograms.launch` : calculate and plot hsv histograms for the test images. 
  * `hues.launch` : calculates and displays the percentage of bgr hues in the reference images.
  * `debug.launch` : runs the actual node with a fake publisher that switches the signal image every few seconds.

Use standalone.launch by including it and configuring the parameters via the supplied _args_.

### Parameters

*difference_threshold* : used to set a threshold when comparing the difference between the selected hue and other hues
(e.g. green vs blue and green vs red). If this is exceeded, the light signal is considered detected [default: 30]

*frames_in_image_window* : the node collects this many images and only acts if the signal state in all agree 
(makes it robust against getting the odd dirty image) [default: 5].

*selected_hue* : can be "blue", "green" or "red". Green is usually the safest as there is not much 
green in indoor environments, but if you should happen to have a purely green wall behind the led, then
switch it [default: "green"].

*image_topic* : where the image producer can be found (easy to set this param/arg for remapping since you will
usually include standalone.launch rather than writing an own launcher [default: "image"].

## Debugging

Run rqt_logger_state and set it to debug - it will show the hue bin percentages.

## Alternative Possibles

__Back Projection__

* URL : http://docs.opencv.org/doc/tutorials/imgproc/histograms/back_projection/back_projection.html

Get a histogram of the lit led we want (from a HSV sample) and then use back projection to hunt for it in the image.

