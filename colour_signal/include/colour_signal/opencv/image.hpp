/**
 * @file include/colour_signal/opencv/image.hpp
 *
 * @brief Convenience class for simplifying opencv image manipulation.
 *
 * Opencv notes:
 *
 *   m = Scalar(b,g,r) -> note that for colour images, order is b,g,r!
 *
 * @todo This would be useful in yocs.
 **/
/*****************************************************************************
** Ifdefs
*****************************************************************************/

#ifndef COLOUR_SIGNAL_IMAGE_HPP_
#define COLOUR_SIGNAL_IMAGE_HPP_

/*****************************************************************************
** Includes
*****************************************************************************/

#include <opencv2/opencv.hpp>
#include "encodings.hpp"
#include "text.hpp"
#include "circle.hpp"

/*****************************************************************************
** Namespaces
*****************************************************************************/

namespace colour_signal {

/*****************************************************************************
** Images
*****************************************************************************/

template <typename Derived>
class Image {
public:
  static const Encoding encoding = Derived::encoding;
  unsigned int width() const { return image.cols; }
  unsigned int height() const { return image.rows; }

  const cv::Mat& cvImageObject() const { return image; }

  template<typename Colour>
  void fill();
  template<typename Colour>
  void draw(const Text<Colour> &text, const unsigned int &u, const unsigned int &v);
  template<typename Colour>
  void draw(const Circle<Colour> &circle, const unsigned int &u, const unsigned int &v);

protected:
  cv::Mat image;
};

class Bgr8Image : public Image<Bgr8Image> {
public:
  Bgr8Image(const unsigned int &width = 640, const unsigned int &height = 480);
  static const Encoding encoding = bgr8;
private:
};

class Mono8Image : public Image<Mono8Image> {
public:
  Mono8Image(const unsigned int &width = 640, const unsigned int &height = 480);
  static const Encoding encoding = mono8;
private:
};

/*****************************************************************************
** Typedefs
*****************************************************************************/

typedef Bgr8Image ColourImage;
typedef Mono8Image GrayScaleImage;

/*****************************************************************************
** Template Implementations
*****************************************************************************/

template <typename Derived>
template <typename Colour>
void Image<Derived>::fill() {
  image = CvColour<Colour,bgr8>::value();
}

template <typename Derived>
template <typename Colour>
void Image<Derived>::draw(const Text<Colour> &text, const unsigned int &u, const unsigned int &v) {
  cv::Point text_origin((u - text.size.width/2), v);
  cv::putText( image, text.str(), text_origin, text.font_face, text.font_scale,
               CvColour<Colour,encoding>::value(), text.thickness, text.line_type );
}

template <typename Derived>
template <typename Colour>
void Image<Derived>::draw(const Circle<Colour> &circle, const unsigned int &u, const unsigned int &v) {
  cv::circle(image, cv::Point(u, v), circle.radius, CvColour<Colour,encoding>::value(), circle.thickness, circle.line_type);
}


} // namespace colour_signal

#endif /* COLOUR_SIGNAL_IMAGE_HPP_ */
