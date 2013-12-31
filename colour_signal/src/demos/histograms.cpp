/**
 * @file src/demos/image_scan.cpp
 *
 * @brief Test the image thresholding functions with a test image.
 **/

/*****************************************************************************
** Includes
*****************************************************************************/

#include <string>
#include <ecl/command_line.hpp>
#include "../../include/colour_signal/opencv/image.hpp"
#include "../../include/colour_signal/opencv/text.hpp"
#include "../../include/colour_signal/opencv/colours.hpp"

/*****************************************************************************
** Namespaces
*****************************************************************************/

using colour_signal::ColourImage;
using colour_signal::Bgr8Image;

/*****************************************************************************
** Main
*****************************************************************************/

int main(int argc, char **argv) {

  ColourImage red_image("./led-red.jpg");
  ColourImage blue_image("./led-blue.jpg");
  ColourImage green_image("./led-green.jpg");
  ColourImage reference_image("./led-reference.jpg");

//  Bgr8Image red_image; red_image.fill<colour_signal::Red>();
//  Bgr8Image blue_image; blue_image.fill<colour_signal::Blue>();
//  Bgr8Image green_image; green_image.fill<colour_signal::Green>();

  red_image.showHistograms("Red");
  blue_image.showHistograms("Blue");
  green_image.showHistograms("Green");
  reference_image.showHistograms("Reference");
  cv::waitKey(0);
  cv::destroyWindow("Red");
  cv::destroyWindow("Blue");
  cv::destroyWindow("Green");
  cv::destroyWindow("Reference");
  cv::destroyWindow("Histograms [Red]");
  cv::destroyWindow("Histograms [Blue]");
  cv::destroyWindow("Histograms [Green]");
  cv::destroyWindow("Histograms [Reference]");

  /*********************
  ** ShowTime
  **********************/
//  std::string window_name("Colour Images");
//  cv::namedWindow(window_name.c_str());
//  cv::imshow(window_name, red_image.cvImageObject());
//  cv::waitKey(0); // wait for a user keypress
//  cv::imshow(window_name, blue_image.cvImageObject());
//  cv::waitKey(0); // wait for a user keypress
//  cv::imshow(window_name, green_image.cvImageObject());
//  cv::waitKey(0); // wait for a user keypress
//  cv::destroyWindow(window_name.c_str());

  return 0;
}
