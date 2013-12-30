/**
 * @file src/lib/image.cpp
 *
 * @brief Implementation for images.
 **/

/*****************************************************************************
 ** Includes
 *****************************************************************************/

#include "../../include/colour_signal/opencv/image.hpp"

/*****************************************************************************
 ** Namespaces
 *****************************************************************************/

namespace colour_signal
{

/*****************************************************************************
 ** Colour Image
 *****************************************************************************/

Bgr8Image::Bgr8Image(const unsigned int &width, const unsigned int &height)
{
  image.create(height, width, CV_8UC3); // CV_8UC4 is rgba8
  image = CvColour<Black, bgr8>::value(); // default fill black
}

/*****************************************************************************
 ** GrayScale Image
 *****************************************************************************/

Mono8Image::Mono8Image(const unsigned int &width, const unsigned int &height)
{
  image.create(height, width, CV_8UC1);
  image = cv::Scalar(128);
}

}

