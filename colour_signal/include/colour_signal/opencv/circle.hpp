/**
 * @file include/colour_signal/opencv/circle.hpp
 *
 * @brief Circle objects for drawing onto an opencv image canvas.
 *
 **/
/*****************************************************************************
** Ifdefs
*****************************************************************************/

#ifndef COLOUR_SIGNAL_OPENCV_UTILS_CIRCLE_HPP_
#define COLOUR_SIGNAL_OPENCV_UTILS_CIRCLE_HPP_

/*****************************************************************************
** Includes
*****************************************************************************/

#include "colours.hpp"

/*****************************************************************************
** Namespaces
*****************************************************************************/

namespace colour_signal {

/*****************************************************************************
** Interfaces
*****************************************************************************/

/**
 * @brief Draw text with baseline centred at u,v.
 */
template <typename Colour>
class Circle {
public:
  Circle(const unsigned int &r = 1);
  template <typename OtherColour> Circle(const Circle<OtherColour> &circle);

  template <typename Derived>
  friend class Image;

  /*********************
  ** Public Parameters
  **********************/
  unsigned int radius;

private:
  int thickness, line_type;

};

/*****************************************************************************
** Template Implementations
*****************************************************************************/

template<typename Color>
Circle<Color>::Circle(const unsigned int &r) :
  radius(r),
  thickness(1),
  line_type(CV_AA) // LineType either 8 or CV_AA?

{
}

template<typename Color>
template <typename OtherColour>
Circle<Color>::Circle(const Circle<OtherColour> &circle) :
  radius(circle.radius),
  thickness(circle.thickness),
  line_type(circle.line_typeCV_AA) // LineType either 8 or CV_AA?

{
}

} // namespace colour_signal

#endif /* COLOUR_SIGNAL_OPENCV_CIRCLE_HPP_ */
