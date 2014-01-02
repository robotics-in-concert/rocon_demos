/**
 * @file src/demos/histograms.cpp
 *
 * @brief Test the image thresholding functions with a test image.
 **/

/*****************************************************************************
** Includes
*****************************************************************************/

#include <ros/ros.h>
#include <ros/package.h>
#include <string>
#include "../../include/colour_signal/opencv/image.hpp"
#include "../../include/colour_signal/opencv/text.hpp"
#include "../../include/colour_signal/opencv/colours.hpp"
#include "../../include/colour_signal/histogram_analytics.hpp"

/*****************************************************************************
** Namespaces
*****************************************************************************/

using colour_signal::ColourImage;
using colour_signal::Bgr8Image;

/*****************************************************************************
** Main
*****************************************************************************/

int main(int argc, char **argv) {

  /*********************
  ** Ros
  **********************/
  ros::init(argc, argv, "histograms");
  ros::NodeHandle private_node_handle("~");

  /*********************
  ** Params
  **********************/
  bool convert_to_hsv;
  ros::param::param<bool>("~convert_to_hsv", convert_to_hsv, false);

  /*********************
  ** Images
  **********************/
  std::string reference_image_filename, blue_image_filename, green_image_filename, red_image_filename;
  blue_image_filename = ros::package::getPath("colour_signal") + "/images/led-blue.jpg";
  green_image_filename = ros::package::getPath("colour_signal") + "/images/led-green.jpg";
  red_image_filename = ros::package::getPath("colour_signal") + "/images/led-red.jpg";
  reference_image_filename = ros::package::getPath("colour_signal") + "/images/led-reference.jpg";

  ColourImage red_image(red_image_filename, convert_to_hsv);
  ColourImage blue_image(blue_image_filename, convert_to_hsv);
  ColourImage green_image(green_image_filename, convert_to_hsv);
  ColourImage reference_image(reference_image_filename, convert_to_hsv);

//  Bgr8Image red_image; red_image.fill<colour_signal::Red>();
//  Bgr8Image blue_image; blue_image.fill<colour_signal::Blue>();
//  Bgr8Image green_image; green_image.fill<colour_signal::Green>();

  colour_signal::HistogramAnalytics red_histograms(red_image.histograms());
  colour_signal::HistogramAnalytics blue_histograms(blue_image.histograms());
  colour_signal::HistogramAnalytics green_histograms(green_image.histograms());
  colour_signal::HistogramAnalytics reference_histograms(reference_image.histograms());

  /*********************
  ** Showtime
  **********************/

  cv::namedWindow("Red", CV_WINDOW_AUTOSIZE );
  cv::namedWindow("Green", CV_WINDOW_AUTOSIZE );
  cv::namedWindow("Blue", CV_WINDOW_AUTOSIZE );
  cv::namedWindow("Reference", CV_WINDOW_AUTOSIZE );
  cv::imshow("Red", red_image.cvImageObject() );
  cv::imshow("Green", green_image.cvImageObject() );
  cv::imshow("Blue", blue_image.cvImageObject() );
  cv::imshow("Reference", reference_image.cvImageObject() );

  red_histograms.showHistograms("Red");
  blue_histograms.showHistograms("Blue");
  green_histograms.showHistograms("Green");
  reference_histograms.showHistograms("Reference");

  /*********************
  ** Cleanup
  **********************/
  // a ros::spin() doesn't work - images don't get shown properly. Not sure why.
  cv::waitKey(0);
  cv::destroyWindow("Red");
  cv::destroyWindow("Blue");
  cv::destroyWindow("Green");
  cv::destroyWindow("Reference");
  cv::destroyWindow("Histograms [Red]");
  cv::destroyWindow("Histograms [Blue]");
  cv::destroyWindow("Histograms [Green]");
  cv::destroyWindow("Histograms [Reference]");

  return 0;
}
