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
 ** Hsv8Image Image
 *****************************************************************************/

Hsv8Image::Hsv8Image(const std::string& filename)
{
//  std::cout << "Loading image" << std::endl;
  //image = cv::imread(filename, CV_LOAD_IMAGE_COLOR);
  cv::Mat bgr_image = cv::imread(filename, CV_LOAD_IMAGE_COLOR);
  cv::cvtColor(bgr_image, image, CV_BGR2HSV);
//  std::cout << "  Filename: " << filename << std::endl;
//  if ( image.data == NULL ) {
//    std::cout << "  Reading image failed" << std::endl;
//  } else {
//    std::cout << "  Coloumns: " << image.cols << std::endl;
//    std::cout << "  Rows: " << image.rows << std::endl;
//  }
}

/**
 * This assumes you are pumping in an appropriate bgr8 mat.
 *
 * todo : we should find a way of checking the mat encoding.
 *
 * @param img
 */
Hsv8Image::Hsv8Image(const cv::Mat& img)
{
  cv::cvtColor(img, image, CV_BGR2HSV);
}


/*****************************************************************************
 ** Bgr8 Image
 *****************************************************************************/

Bgr8Image::Bgr8Image(const unsigned int &width, const unsigned int &height)
{
  image.create(height, width, CV_8UC3); // CV_8UC4 is rgba8
  image = CvColour<Black, bgr8>::value(); // default fill black
}

Bgr8Image::Bgr8Image(const std::string& filename)
{
  image = cv::imread(filename, CV_LOAD_IMAGE_COLOR);
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
