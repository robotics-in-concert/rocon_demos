/**
 * @file include/colour_signal/opencv/encodings.hpp
 *
 * @brief Image encodings for opencv-ros.
 **/
/*****************************************************************************
** Ifdefs
*****************************************************************************/

#ifndef COLOUR_SIGNAL_ENCODINGS_HPP_
#define COLOUR_SIGNAL_ENCODINGS_HPP_

/*****************************************************************************
** Namespaces
*****************************************************************************/

namespace colour_signal {

/*****************************************************************************
** Encodings
*****************************************************************************/

enum Encoding {
  bgr8,    // CV_8UC3
  // rgb8, // CV_8UC4
  hsv8,
  mono8
};

} // namespace colour_signal


#endif /* COLOUR_SIGNAL_ENCODINGS_HPP_ */
