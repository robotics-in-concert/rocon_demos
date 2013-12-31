/**
 * @file /colour_signal/src/fake_publisher.cpp
 *
 * @brief Fake image publisher for testing the node.
 *
 **/

/*****************************************************************************
** Includes
*****************************************************************************/

#include <opencv2/opencv.hpp>
#include "ros/ros.h"
#include <sensor_msgs/Image.h>
#include <cv_bridge/cv_bridge.h>
#include "../include/colour_signal/opencv/image.hpp"

/*****************************************************************************
** Classes
*****************************************************************************/

class FakeJagi {
public:
  FakeJagi(): switched_on(false) {
    cv::Mat on_image_mat = cv::imread("./led-green.jpg", CV_LOAD_IMAGE_COLOR);
    cv::Mat off_image_mat = cv::imread("./led-reference.jpg", CV_LOAD_IMAGE_COLOR);
    on_image = cv_bridge::CvImage(std_msgs::Header(), "bgr8", on_image_mat);
    off_image = cv_bridge::CvImage(std_msgs::Header(), "bgr8", off_image_mat);
  }

  void _ros_parameters() {}

  void init(ros::NodeHandle &private_node_handle) {
    _image_publisher = private_node_handle.advertise<sensor_msgs::Image>("image", 10, true);
    _publish_timer = private_node_handle.createTimer(ros::Duration(0.1), &FakeJagi::publish_image, this);
    _switch_timer = private_node_handle.createTimer(ros::Duration(3.0), &FakeJagi::switch_image, this);
  }

  void publish_image(const ros::TimerEvent& event) {
    if (switched_on) {
      on_image.header.stamp = ros::Time::now();
      _image_publisher.publish(on_image.toImageMsg());
    } else {
      off_image.header.stamp = ros::Time::now();
      _image_publisher.publish(off_image.toImageMsg());
    }
  }

  void switch_image(const ros::TimerEvent& event) {
    if (switched_on) {
      ROS_INFO_STREAM("FakeLed : switching off");
      switched_on = false;
    } else {
      ROS_INFO_STREAM("FakeLed : switching on");
      switched_on = true;
    }
  }

  void spin() {
    ros::spin();
//    while (ros::ok()) {
//      todo rate sleep
//      ros::spinOnce();
//    }
  }

private:
  bool switched_on;
  cv_bridge::CvImage on_image, off_image;
  ros::Timer _publish_timer, _switch_timer;
  ros::Publisher _image_publisher;

};


/*****************************************************************************
** Main
*****************************************************************************/

int main(int argc, char **argv) {
  ros::init(argc, argv, "fake_led_publisher");
  ros::NodeHandle private_node_handle("~");
  FakeJagi jagi;
  jagi.init(private_node_handle);
  jagi.spin();
  return 0;
}
