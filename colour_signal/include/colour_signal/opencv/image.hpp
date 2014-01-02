/**
 * @file include/colour_signal/opencv/image.hpp
 *
 * @brief Convenience class for simplifying opencv image manipulation.
 *
 * Opencv notes:
 *
 *   m = Scalar(b,g,r) -> note that for colour images, order is b,g,r!
 *
 * @todo This is really quite a mess - would like to work out a useful
 * Image class framework at some point in time. Mostly we need to handle
 *
 * - bgr8
 * - mono8
 * - hsv(8)
 *
 * We typically never deal with alpha in the robotics world.
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

// Local
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
  /**
   * @brief Default constructor.
   *
   * A good guideline : child classes should never instantiate this parent and
   * leave the cv::Mat image variable undefined. When whatever construction
   * does take place and leaves that variable undefined, throw an exception
   * so we don't have a zombie (uninitialised) object floating around.
   */
  Image() {}
  Image(const cv::Mat& image) : image(image) {}
  static const Encoding encoding = Derived::encoding;
  unsigned int width() const { return image.cols; }
  unsigned int height() const { return image.rows; }

  const cv::Mat& cvImageObject() const { return image; }

  void save(const std::string& filename) {
    // This actually returns an int (for errors I guess), but can't find any
    // docs on the int values it represents.
    // todo : upgrade this to opencv2 functions
    // cvSaveImage(filename.c_str(),image);
  }

  /**
   * @brief Get histograms of the three channels.
   *
   * These will return bgr, or hsv histograms depending on the image storage type.
   * Remember that hue histograms have range [0,179], all others [0, 255]
   *
   * @return vector of histograms in single column cv::Mat format.
   */
  std::vector<cv::Mat> histograms() const {
    std::vector<cv::Mat> planes, generated_histograms;
    split(image, planes);  // todo should only generate one plane for mono8 (needs testing)
    for (unsigned int i = 0; i < planes.size(); ++i) {
      int number_of_bins = 255;
      if (i == 0 && Image<Derived>::encoding == hsv8) {
        // hue histograms only have range [0, 179]
        number_of_bins = 179;
      }
      float range[] = { 0, number_of_bins }; // 1 bin for each value...
      const float* histRange = { range };
      bool uniform = true; bool do_not_accumulate = false;
      cv::Mat hist;
      cv::calcHist( &planes[i], 1, 0, cv::Mat(), hist, 1, &number_of_bins, &histRange, uniform, do_not_accumulate );
      generated_histograms.push_back(hist);
    }
    return generated_histograms;
  }

  /**
   * Not really the greatest place to have drawing functions. Always best to
   * separate container vs algorithm vs debugging concerns. But this ain't no
   * serious library yet.
   *
   * http://docs.opencv.org/doc/tutorials/imgproc/histograms/histogram_calculation/histogram_calculation.html
   */
  template<typename Colour>
  void fill();
  template<typename Colour>
  void draw(const Text<Colour> &text, const unsigned int &u, const unsigned int &v);
  template<typename Colour>
  void draw(const Circle<Colour> &circle, const unsigned int &u, const unsigned int &v);

protected:
  cv::Mat image;
};


class Hsv8Image : public Image<Hsv8Image> {
public:
  Hsv8Image(const std::string& filename);
  Hsv8Image(const cv::Mat& img);
  static const Encoding encoding = hsv8;
private:
};

class Bgr8Image : public Image<Bgr8Image> {
public:
  Bgr8Image(const unsigned int &width = 640, const unsigned int &height = 480);
  Bgr8Image(const std::string& filename);
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
