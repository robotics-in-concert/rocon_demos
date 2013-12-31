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

ColourImage::ColourImage(const std::string& filename)
{
//  std::cout << "Loading image" << std::endl;
  image = cv::imread(filename, CV_LOAD_IMAGE_COLOR);
//  std::cout << "  Filename: " << filename << std::endl;
//  if ( image.data == NULL ) {
//    std::cout << "  Reading image failed" << std::endl;
//  } else {
//    std::cout << "  Coloumns: " << image.cols << std::endl;
//    std::cout << "  Rows: " << image.rows << std::endl;
//  }
}

ColourImage::ColourImage(const cv::Mat& image) : Image<ColourImage>(image) {}

/*****************************************************************************
 ** Bgr8 Image
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

} // namepsace colour_signal
