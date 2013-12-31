/**
 * @file /colour_signal/include/colour_signal/histogram_analytics.hpp
 *
 * @brief Analytics for working on rgb histograms of images.
 **/
/*****************************************************************************
** Ifdefs
*****************************************************************************/

#ifndef COLOUR_SIGNAL_HISTOGRAM_ANALYTICS_HPP_
#define COLOUR_SIGNAL_HISTOGRAM_ANALYTICS_HPP_

/*****************************************************************************
** Includes
*****************************************************************************/

#include <vector>
#include <opencv2/opencv.hpp>
#include <ecl/exceptions/standard_exception.hpp>

/*****************************************************************************
** Namespaces
*****************************************************************************/

namespace colour_signal {

/*****************************************************************************
** Interfaces
*****************************************************************************/

/**
 * @brief  Analyses rgb histograms and provides analytics.
 *
 * Analyses rgb histograms and provides analytics.
 *
 **/
class HistogramAnalytics {
public:
  /*********************
   ** C&D's
   **********************/
  HistogramAnalytics (const std::vector<cv::Mat> &histograms) throw(ecl::StandardException); /**< Default constructor. **/
  ~HistogramAnalytics () {}; /**< Default destructor. **/

  void showHistograms(const std::string& title) const;
  std::vector<float> averageIntensities() const { return _average_intensities; }
  std::vector<float> maximumIntensities() const { return _maximum_intensities; }
  std::vector<float> pixelCounts() const { return _pixel_counts; }

private:
  void _generateStatistics();

  const cv::Mat& b_histogram() const { return _histograms.at(0); }
  const cv::Mat& g_histogram() const { return _histograms.at(1); }
  const cv::Mat& r_histogram() const { return _histograms.at(2); }
  const cv::Mat& h_histogram() const { return _histograms.at(0); }
  const cv::Mat& s_histogram() const { return _histograms.at(1); }
  const cv::Mat& v_histogram() const { return _histograms.at(2); }

  std::vector<cv::Mat> _histograms;
  std::vector<float> _average_intensities;
  std::vector<float> _maximum_intensities;
  std::vector<float> _pixel_counts;
};

#endif /* COLOUR_SIGNAL_HISTOGRAM_ANALYTICS_HPP_ */

} // namespace colour_signal
