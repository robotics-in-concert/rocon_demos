/**
 * @file src/demos/histograms.cpp
 *
 * @brief Test the image thresholding functions with a test image.
 **/

/*****************************************************************************
** Includes
*****************************************************************************/

#include <ros/ros.h>
#include <boost/shared_ptr.hpp>
#include <ros/package.h>
#include <string>
#include "../../include/colour_signal/opencv/image.hpp"
#include "../../include/colour_signal/opencv/text.hpp"
#include "../../include/colour_signal/opencv/colours.hpp"
#include "../../include/colour_signal/histogram_analytics.hpp"

/*****************************************************************************
** Namespaces
*****************************************************************************/

using colour_signal::Hsv8Image;
using colour_signal::Bgr8Image;

/*****************************************************************************
** Functions
*****************************************************************************/

template<typename Image>
void showImages(const Image& blue_image,
                    const Image& green_image,
                    const Image& red_image,
                    const Image& reference_image) {


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
}

template<typename Image>
void showHistograms(const Image& blue_image,
                    const Image& green_image,
                    const Image& red_image,
                    const Image& reference_image) {
  colour_signal::HistogramAnalytics red_histograms(red_image.histograms());
  colour_signal::HistogramAnalytics blue_histograms(blue_image.histograms());
  colour_signal::HistogramAnalytics green_histograms(green_image.histograms());
  colour_signal::HistogramAnalytics reference_histograms(reference_image.histograms());

  red_histograms.showHistograms("Red");
  blue_histograms.showHistograms("Blue");
  green_histograms.showHistograms("Green");
  reference_histograms.showHistograms("Reference");
}

void cleanupWindows() {
  cv::destroyWindow("Red");
  cv::destroyWindow("Blue");
  cv::destroyWindow("Green");
  cv::destroyWindow("Reference");
  cv::destroyWindow("Histograms [Red]");
  cv::destroyWindow("Histograms [Blue]");
  cv::destroyWindow("Histograms [Green]");
  cv::destroyWindow("Histograms [Reference]");
}

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

  if (convert_to_hsv) {
    Hsv8Image blue_image(blue_image_filename);
    Hsv8Image green_image(green_image_filename);
    Hsv8Image red_image(red_image_filename);
    Hsv8Image reference_image(reference_image_filename);
    showImages(blue_image, green_image, red_image, reference_image);
    showHistograms(blue_image, green_image, red_image, reference_image);
  } else {
    Bgr8Image red_image(red_image_filename);
    Bgr8Image blue_image(blue_image_filename);
    Bgr8Image green_image(green_image_filename);
    Bgr8Image reference_image(reference_image_filename);
    showHistograms(blue_image, green_image, red_image, reference_image);
  }

//  Bgr8Image red_image; red_image.fill<colour_signal::Red>();
//  Bgr8Image blue_image; blue_image.fill<colour_signal::Blue>();
//  Bgr8Image green_image; green_image.fill<colour_signal::Green>();


  cv::waitKey(0);
  cleanupWindows();

  return 0;
}
