/**
 * @file /colour_signal/src/node.cpp
 *
 * @brief Node that manages the ros api interface.
 *
 * Grunt vision processing is done by the vision library beneath it. This
 * just shuffles around incoming and outgoings and manages the state.
 **/

/*****************************************************************************
** Includes
*****************************************************************************/

#include <ros/ros.h>
#include <std_msgs/Bool.h>
#include <sensor_msgs/Image.h>
#include <sensor_msgs/image_encodings.h>
#include <cv_bridge/cv_bridge.h>
#include "../include/colour_signal/opencv/image.hpp"
#include "../include/colour_signal/signal_detection.hpp"

/*****************************************************************************
** Classes
*****************************************************************************/

class Jagi {
public:
  static const unsigned int threshold = 30;

  Jagi() : _enabled(false), _signalled(false) {}

  void init(ros::NodeHandle &private_node_handle) {
    /*********************
    ** Ros Api
    **********************/
    _result_publisher = private_node_handle.advertise<std_msgs::Bool>("result", 10, true);
    _enable_subscriber = private_node_handle.subscribe("enable", 10, &Jagi::enableCallback, this);
    // _image_subscriber configured when enabling.

    /*********************
    ** Parameters
    **********************/
    bool auto_enable = false;
    ros::param::param<bool>("~auto_enable", auto_enable, false);
    std_msgs::BoolPtr auto_enable_msg(new std_msgs::Bool());
    auto_enable_msg->data = auto_enable;
    enableCallback(auto_enable_msg);
  }

  void spin() {
    ros::spin();
//    while (ros::ok()) {
//      todo rate sleep
//      ros::spinOnce();
//    }
  }

private:
  void imageCallback(const sensor_msgs::Image::ConstPtr &msg) {
    if ( !_enabled ) {
      return;
    }
    //ROS_INFO_STREAM("ColourSignal : received image");
    cv_bridge::CvImageConstPtr cv_ptr;
    try {
      cv_ptr = cv_bridge::toCvShare(
          msg,
          sensor_msgs::image_encodings::BGR8);
    }
    catch (cv_bridge::Exception& e)
    {
      ROS_ERROR("cv_bridge exception: %s", e.what());
      return;
    }
    bool convert_to_hsv = true;
    colour_signal::ColourImage image(cv_ptr->image, convert_to_hsv);
    std::vector<float> hues = colour_signal::spliceLightSignal(image);
    float average_green_difference = (2*hues.at(1) - hues.at(0) - hues.at(2))*100.0/2.0;
    bool last_signal_state = _signalled;
    if (average_green_difference > threshold) {
      _signalled = true;
    } else {
      _signalled = false;
    }
    if (last_signal_state != _signalled) {
      if(_signalled) {
        ROS_INFO_STREAM("ColourSignal : detected");
      } else {
        ROS_INFO_STREAM("ColourSignal : lost");
      }
      std_msgs::Bool msg;
      msg.data = _signalled;
      _result_publisher.publish(msg);
    }
    ROS_DEBUG_STREAM("ColourSignal: hues [" << hues.at(0)*100 << "," << hues.at(1)*100 << "," << hues.at(2) << "]");
  }

  void enableCallback(const std_msgs::Bool::ConstPtr &msg) {
    if (msg->data) {
      ROS_INFO_STREAM("ColourSignal : enabled");
      ros::NodeHandle private_node_handle("~");
      _image_subscriber = private_node_handle.subscribe("image", 10, &Jagi::imageCallback, this);
      _enabled = true;
    } else {
      ROS_INFO_STREAM("ColourSignal : disabled");
      _image_subscriber.shutdown();
      _enabled = false;
    }
  }
  bool _enabled;
  bool _signalled;
  ros::Publisher _result_publisher;
  ros::Subscriber _enable_subscriber, _image_subscriber;
};

/*****************************************************************************
** Main
*****************************************************************************/

int main(int argc, char **argv) {
  ros::init(argc, argv, "colour_signal");
  ros::NodeHandle private_node_handle("~");
  Jagi jagi;
  jagi.init(private_node_handle);
  jagi.spin();
  return 0;
}
