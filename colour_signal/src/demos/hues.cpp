/**
 * @file src/demos/hues.cpp
 *
 * @brief Get hue breakdown of demo images.
 **/

/*****************************************************************************
** Includes
*****************************************************************************/

#include <string>
#include "../../include/colour_signal/opencv/image.hpp"
#include "../../include/colour_signal/signal_detection.hpp"

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
  ** Args
  **********************/

  ColourImage red_image("./led-red.jpg", true);
  ColourImage blue_image("./led-blue.jpg", true);
  ColourImage green_image("./led-green.jpg", true);
  ColourImage reference_image("./led-reference.jpg", true);

  std::vector<float> red_image_hues = colour_signal::spliceLightSignal(red_image);
  std::vector<float> blue_image_hues = colour_signal::spliceLightSignal(blue_image);
  std::vector<float> green_image_hues = colour_signal::spliceLightSignal(green_image);
  std::vector<float> reference_image_hues = colour_signal::spliceLightSignal(reference_image);

  /*********************
  ** Pretty Print
  **********************/
  std::cout << "Blue Image Hues [BGR]" << std::endl;
  for(unsigned int i = 0; i < blue_image_hues.size(); ++i) {
    std::cout << "  : " << blue_image_hues.at(i)*100.0 << "% " << std::endl;
  }
  std::cout << "Green Image Hues [BGR]" << std::endl;
  for(unsigned int i = 0; i < green_image_hues.size(); ++i) {
    std::cout << "  : " << green_image_hues.at(i)*100.0 << "% " << std::endl;
  }
  std::cout << "Red Image Hues [BGR]" << std::endl;
  for(unsigned int i = 0; i < red_image_hues.size(); ++i) {
    std::cout << "  : " << red_image_hues.at(i)*100.0 << "% " << std::endl;
  }
  std::cout << "Reference Image Hues [BGR]" << std::endl;
  for(unsigned int i = 0; i < reference_image_hues.size(); ++i) {
    std::cout << "  : " << reference_image_hues.at(i)*100.0 << "% " << std::endl;
  }
  return 0;
}
