/**
 * @file include/colour_signal/opencv/colours.hpp
 *
 * @brief Colour definitions and structures
 **/
/*****************************************************************************
** Ifdefs
*****************************************************************************/

#ifndef COLOUR_SIGNAL_OPENCV_COLOURS_HPP_
#define COLOUR_SIGNAL_OPENCV_COLOURS_HPP_

/*****************************************************************************
** Includes
*****************************************************************************/

#include <opencv2/opencv.hpp>
#include "encodings.hpp"

/*****************************************************************************
** Namespaces
*****************************************************************************/

namespace colour_signal {

/*****************************************************************************
** Compile Time Classes
*****************************************************************************/

struct Black {
  static const unsigned int red = 0;
  static const unsigned int green = 0;
  static const unsigned int blue = 0;
  static const unsigned int gray_value = 0;
};


struct White {
  static const unsigned int red = 255;
  static const unsigned int green = 255;
  static const unsigned int blue = 255;
  static const unsigned int gray_value = 255;
};

struct DarkGray {
  static const unsigned int red = 30;
  static const unsigned int green = 30;
  static const unsigned int blue = 30;
  static const unsigned int gray_value = 30;
};

struct Red {
  static const unsigned int red = 255;
  static const unsigned int green = 0;
  static const unsigned int blue = 0;
  static const unsigned int gray_value = (red + green + blue)/3;
};

struct Orange {
  static const unsigned int red = 255;
  static const unsigned int green = 102;
  static const unsigned int blue = 0;
  static const unsigned int gray_value = (red + green + blue)/3;
};

struct Green {
  static const unsigned int red = 0;
  static const unsigned int green = 255;
  static const unsigned int blue = 0;
  static const unsigned int gray_value = (red + green + blue)/3;
};

struct Blue {
  static const unsigned int red = 0;
  static const unsigned int green = 0;
  static const unsigned int blue = 255;
  static const unsigned int gray_value = (red + green + blue)/3;
};

/*****************************************************************************
** To Opencv Colour (Scalar) Conversions
*****************************************************************************/

template<typename Col, enum Encoding Enc>
struct CvColour {
private:
  CvColour() {}
};

template<typename Col>
struct CvColour<Col, bgr8> {
  static const cv::Scalar value () {
    static const cv::Scalar scalar(Col::blue, Col::green, Col::red);
    return scalar;
  }
};

template<typename Col>
struct CvColour<Col, mono8> {
  static const cv::Scalar value() {
    static const cv::Scalar scalar(Col::gray_value);
    return scalar;
  }
};


} // namespace colour_signal

#endif /* COLOUR_SIGNAL_OPENCV_COLOURS_HPP_ */
