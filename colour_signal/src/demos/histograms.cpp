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

  ColourImage red_image("./led-red.jpg");
  ColourImage blue_image("./led-blue.jpg");
  ColourImage green_image("./led-green.jpg");
  ColourImage reference_image("./led-reference.jpg");

//  Bgr8Image red_image; red_image.fill<colour_signal::Red>();
//  Bgr8Image blue_image; blue_image.fill<colour_signal::Blue>();
//  Bgr8Image green_image; green_image.fill<colour_signal::Green>();

  colour_signal::HistogramAnalytics red_histograms(red_image.bgrHistograms());
  colour_signal::HistogramAnalytics blue_histograms(blue_image.bgrHistograms());
  colour_signal::HistogramAnalytics green_histograms(green_image.bgrHistograms());
  colour_signal::HistogramAnalytics reference_histograms(reference_image.bgrHistograms());

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
