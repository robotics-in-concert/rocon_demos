/**
 * @file src/demos/hues.cpp
 *
 * @brief Get hue breakdown of demo images.
 **/

/*****************************************************************************
** Includes
*****************************************************************************/

#include <ros/ros.h>
#include <ros/package.h>
#include <string>
#include "../../include/colour_signal/opencv/image.hpp"
#include "../../include/colour_signal/signal_detection.hpp"

/*****************************************************************************
** Namespaces
*****************************************************************************/

using colour_signal::Hsv8Image;

/*****************************************************************************
** Main
*****************************************************************************/

int main(int argc, char **argv) {

  /*********************
  ** Ros
  **********************/
  ros::init(argc, argv, "hues");
  ros::NodeHandle private_node_handle("~");

  /*********************
  ** Images
  **********************/
  std::string reference_image_filename, blue_image_filename, green_image_filename, red_image_filename;
  blue_image_filename = ros::package::getPath("colour_signal") + "/images/led-blue.jpg";
  green_image_filename = ros::package::getPath("colour_signal") + "/images/led-green.jpg";
  red_image_filename = ros::package::getPath("colour_signal") + "/images/led-red.jpg";
  reference_image_filename = ros::package::getPath("colour_signal") + "/images/led-reference.jpg";

  /*********************
  ** Images
  **********************/
  ROS_INFO_STREAM("FakeLed : loading image [" << blue_image_filename << "]");
  ROS_INFO_STREAM("FakeLed : loading image [" << green_image_filename << "]");
  ROS_INFO_STREAM("FakeLed : loading image [" << red_image_filename << "]");
  ROS_INFO_STREAM("FakeLed : loading image [" << reference_image_filename << "]");

  Hsv8Image blue_image(blue_image_filename);
  Hsv8Image green_image(green_image_filename);
  Hsv8Image red_image(red_image_filename);
  Hsv8Image reference_image(reference_image_filename);

  std::vector<float> red_image_hues = colour_signal::spliceLightSignal(red_image);
  std::vector<float> blue_image_hues = colour_signal::spliceLightSignal(blue_image);
  std::vector<float> green_image_hues = colour_signal::spliceLightSignal(green_image);
  std::vector<float> reference_image_hues = colour_signal::spliceLightSignal(reference_image);

  /*********************
  ** Pretty Print
  **********************/
  ROS_INFO_STREAM("Blue Image Hues [BGR]");
  for(unsigned int i = 0; i < blue_image_hues.size(); ++i) {
    ROS_INFO_STREAM("  : " << blue_image_hues.at(i)*100.0 << "% ");
  }
  ROS_INFO_STREAM("Green Image Hues [BGR]");
  for(unsigned int i = 0; i < green_image_hues.size(); ++i) {
    ROS_INFO_STREAM("  : " << green_image_hues.at(i)*100.0 << "% ");
  }
  ROS_INFO_STREAM("Red Image Hues [BGR]");
  for(unsigned int i = 0; i < red_image_hues.size(); ++i) {
    ROS_INFO_STREAM("  : " << red_image_hues.at(i)*100.0 << "% ");
  }
  ROS_INFO_STREAM("Reference Image Hues [BGR]");
  for(unsigned int i = 0; i < reference_image_hues.size(); ++i) {
    ROS_INFO_STREAM("  : " << reference_image_hues.at(i)*100.0 << "% ");
  }
  return 0;
}
