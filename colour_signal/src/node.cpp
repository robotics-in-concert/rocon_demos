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

#include "ros/ros.h"
#include "std_msgs/Bool.h"
#include <sstream>

/*****************************************************************************
** Classes
*****************************************************************************/

class Jagi {
public:
  Jagi() : _enabled(false) {}

  void init(ros::NodeHandle &private_node_handle) {
    _result_publisher = private_node_handle.advertise<std_msgs::Bool>("result", 10, true);
    _enable_subscriber = private_node_handle.subscribe("enable", 10, &Jagi::enableCallback, this);
    _timer = private_node_handle.createTimer(ros::Duration(5.0), &Jagi::detection_stub, this);
  }

  void spin() {
    ros::spin();
//    while (ros::ok()) {
//      todo rate sleep
//      ros::spinOnce();
//    }
  }

  void detection_stub(const ros::TimerEvent& event) {
    static bool last_result = false;
    std_msgs::Bool msg;
    if ( _enabled ) {
      if (last_result) {
        ROS_INFO_STREAM("ColourSignal : lost");
        last_result = false;
        msg.data = false;
        _result_publisher.publish(msg);
      } else {
        ROS_INFO_STREAM("ColourSignal : detected");
        last_result = true;
        msg.data = true;
        _result_publisher.publish(msg);
      }
    }
  }

private:
  void enableCallback(const std_msgs::Bool::ConstPtr &msg) {
    if (msg->data) {
      ROS_INFO_STREAM("ColourSignal : enabled");
      _enabled = true;
    } else {
      ROS_INFO_STREAM("ColourSignal : disabled");
      _enabled = false;
    }
  }
  bool _enabled;
  ros::Timer _timer;
  ros::Publisher _result_publisher;
  ros::Subscriber _enable_subscriber;
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
