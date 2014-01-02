/**
 * @file src/lib/signal_detection.cpp
 *
 * @brief Implementation for signal detection methods.
 **/

/*****************************************************************************
** Includes
*****************************************************************************/

#include "../../include/colour_signal/signal_detection.hpp"

/*****************************************************************************
** Namespaces
*****************************************************************************/

namespace colour_signal {

std::vector<float> spliceLightSignal(Hsv8Image &image) {
  // hue histogram
  cv::Mat histogram = image.histograms()[0];
  float blue_count = 0, green_count = 0, red_count = 0, pixel_count = 0;
  for(int intensity = 0; intensity < histogram.rows; intensity++)
  {
    const float value = static_cast<int>(histogram.at<float>(intensity,0));
    pixel_count += value;
    if ( intensity > 45 && intensity < 75 ) {
      green_count += value;
    } else if ( intensity > 105 && intensity < 135 ) {
      blue_count += value;
    } else if ( intensity > 0 && intensity < 15 ) {
      red_count += value;
    } else if ( intensity > 240 && intensity < 255 ) {
      red_count += value;
    }
  }
  std::vector<float> blue_green_red;
  blue_green_red.push_back(blue_count/pixel_count);
  blue_green_red.push_back(green_count/pixel_count);
  blue_green_red.push_back(red_count/pixel_count);
  return blue_green_red;
}

} // namespace colour_signal
