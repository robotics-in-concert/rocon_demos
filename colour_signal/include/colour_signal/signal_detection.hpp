/**
 * @file /colour_signal/include/colour_signal/signal_detection.hpp
 *
 * @brief Methods used to detect a colour signal (binary result).
 **/
/*****************************************************************************
** Ifdefs
*****************************************************************************/

#ifndef COLOUR_SIGNAL_DETECTION_HPP_
#define COLOUR_SIGNAL_DETECTION_HPP_

/*****************************************************************************
** Includes
*****************************************************************************/

#include "opencv/image.hpp"
#include "histogram_analytics.hpp"
#include <ecl/exceptions/standard_exception.hpp>

/*****************************************************************************
** Namespaces
*****************************************************************************/

namespace colour_signal {

/*****************************************************************************
** Interfaces
*****************************************************************************/

/**
 * @brief Feed me an image and detect if it is a green signal (green flood).
 *
 * This just looks for a majority in the green intensity when compared to
 * red and blue channels. Not too bright, but sufficient for some purposes.
 *
 * Constraint - requires a generally varied background. Would fail probably
 * if you tried lighting up a green led against a purely green background
 * in which case your green pixel intensities would if anything, go down since
 * the led's themselves show up as white.
 *
 * @param image : colour image to process (must be converted to hsv).
 * @return three percentages for blue, green, red.
 */
std::vector<float> spliceLightSignal(ColourImage &image);

} // namespace colour_signal

#endif /* COLOUR_SIGNAL_DETECTION_HPP_ */
