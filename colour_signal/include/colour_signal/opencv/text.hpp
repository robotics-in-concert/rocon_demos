/**
 * @file include/colour_signal/opencv/text.hpp
 *
 * @brief Text manipulation objects for drawing on images.
 **/
/*****************************************************************************
** Ifdefs
*****************************************************************************/

#ifndef COLOUR_SIGNAL_TEXT_HPP_
#define COLOUR_SIGNAL_TEXT_HPP_

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
class Text {
public:
  Text(const std::string &text="");
  template <typename OtherColour> Text(const Text<OtherColour> &text);

  const std::string& str() const { return data; }
  void operator=(const std::string &text);
  void operator=(const unsigned int &num);

  template <typename Derived>
  friend class Image;

  /*********************
  ** Public Parameters
  **********************/
  double font_scale;

private:
  int font_face, thickness, baseline, line_type;
  std::string data;
  cv::Size size;

};

/*****************************************************************************
** Template Implementations
*****************************************************************************/

template<typename Color>
Text<Color>::Text(const std::string &text) :
  font_scale(0.5),
  font_face(cv::FONT_HERSHEY_SCRIPT_SIMPLEX),
  thickness(1),
  baseline(0),
  line_type(CV_AA), // LineType either 8 or CV_AA?
  data(text)
{
  size = cv::getTextSize(data, font_face, font_scale, thickness, &baseline);
}

template<typename Color>
template <typename OtherColour>
Text<Color>::Text(const Text<OtherColour> &text) :
  font_scale(0.5),
  font_face(cv::FONT_HERSHEY_SCRIPT_SIMPLEX),
  thickness(1),
  baseline(0),
  line_type(CV_AA), // LineType either 8 or CV_AA?
  data(text.str())
{
  size = cv::getTextSize(data, font_face, font_scale, thickness, &baseline);
}

template<typename Color>
void Text<Color>::operator=(const std::string &text) {
  data = text;
  size = cv::getTextSize(data, font_face, font_scale, thickness, &baseline);
}

template<typename Color>
void Text<Color>::operator=(const unsigned int &num) {
  std::ostringstream stream;
  stream << num;
  data = stream.str();
  size = cv::getTextSize(data, font_face, font_scale, thickness, &baseline);
}

} // namespace colour_signal

#endif /* COLOUR_SIGNAL_TEXT_HPP_ */
