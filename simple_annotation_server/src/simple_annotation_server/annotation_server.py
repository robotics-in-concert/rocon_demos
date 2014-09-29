#!/usr/bin/env python
#
# License: BSD
#   https://raw.github.com/robotics-in-concert/rocon_demos/license/LICENSE
#

import rospy
import ar_track_alvar_msgs.msg as ar_msgs
import simple_annotation_msgs.srv as annotation_srvs
from visualization_msgs.msg import Marker, MarkerArray
import yocs_msgs.msg as yocs_msgs

from .utils import load_annotations_from_file, write_annotations_into_file


class SimpleAnnotationServer(object):

    __slots__ = ['publisher', 'service', 'filename', 'annotation', 'filename']

    def __init__(self):
        pass

    def init(self):
        self.filename = rospy.get_param("~filename")

        if not self.filename:
            self.logerr('Annotation file is required')
            return False

        self.annotation = {}
        load_annotations_from_file(self.annotation, self.filename)
        self._init_publishers()
        self._init_services()
        return True

    def _init_publishers(self):
        self.publisher = {}
        self.publisher['tables'] = rospy.Publisher('tables', yocs_msgs.TableList, latch=True, queue_size=2)
        self.publisher['ar_markers'] = rospy.Publisher('ar_markers', ar_msgs.AlvarMarkers, latch=True, queue_size=2)
        self.publisher['columns'] = rospy.Publisher('columns', yocs_msgs.ColumnList, latch=True, queue_size=2)
        self.publisher['walls'] = rospy.Publisher('walls', yocs_msgs.WallList, latch=True, queue_size=2)

        self.publisher['viz_markers'] = rospy.Publisher('viz_markers', MarkerArray, latch=True, queue_size=2)

    def _init_services(self):
        self.service = {}
        self.service['tables'] = rospy.Service('save_tables', annotation_srvs.SaveTables, self._process_save_tables)
        self.service['ar_markers'] = rospy.Service('save_ar_markers', annotation_srvs.SaveARMarkers, self._process_save_ar_markers)
        self.service['columns'] = rospy.Service('save_columns', annotation_srvs.SaveColumns, self._process_save_columns)
        self.service['walls'] = rospy.Service('save_walls', annotation_srvs.SaveWalls, self._process_save_walls)

    def _process_save_tables(self, req):
        self.annotation['tables'] = req.data
        self.update()
        return annotation_srvs.SaveTablesResponse(True)

    def _process_save_columns(self, req):
        self.annotation['columns'] = req.data
        self.update()
        return annotation_srvs.SaveColumnsResponse(True)

    def _process_save_ar_markers(self, req):
        self.annotation['ar_markers'] = req.data
        self.update()
        return annotation_srvs.SaveARMarkersResponse(True)

    def _process_save_walls(self, req):
        self.annotation['walls'] = req.data
        self.update()
        return annotation_srvs.SaveWallsResponse(True)

    def publish_annotations(self):
        # Tables
        message = yocs_msgs.TableList()
        message.tables = self.annotation['tables']
        self.publisher['tables'].publish(message)

        # AR Markers
        message = ar_msgs.AlvarMarkers()
        message.markers = self.annotation['ar_markers']
        self.publisher['ar_markers'].publish(message)

        # Columns
        message = yocs_msgs.ColumnList()
        message.obstacles = self.annotation['columns']
        self.publisher['columns'].publish(message)

        # Walls
        message = yocs_msgs.WallList()
        message.obstacles = self.annotation['walls']
        self.publisher['walls'].publish(message)

    def publish_visualization_markers(self):
        m_array = MarkerArray()
    
        id = 1

        # Table
        for t in self.annotation['tables']:
            m = Marker()
            m.header.frame_id = '/map'
            m.ns = 'marker'
            m.id = id
            id = id +1

            m.type = Marker.CYLINDER
            m.action = Marker.ADD
            m.pose = t.pose.pose.pose
            m.pose.position.x = t.pose.pose.pose.position.x
            m.pose.position.y = t.pose.pose.pose.position.y
            m.pose.position.z = t.height / 2
            m.scale.x = t.radius
            m.scale.y = t.radius
            m.scale.z = t.height
            m.color.r = 1.0
            m.color.g = 0.0
            m.color.b = 0.0
            m.color.a = 0.5

            m_array.markers.append(m)

            m = Marker()
            m.header.frame_id = '/map'
            m.ns = 'marker'
            m.id = id
            id = id +1

            m.type = Marker.TEXT_VIEW_FACING
            m.action = Marker.ADD
            m.text = t.name
            m.pose.position.x = t.pose.pose.pose.position.x
            m.pose.position.y = t.pose.pose.pose.position.y
            m.pose.position.z = t.height / 2 + 0.5
            m.scale.x = 0.3 
            m.scale.y = 0.3
            m.scale.z = 0.3
            m.color.r = 1.0
            m.color.g = 1.0
            m.color.b = 1.0
            m.color.a = 1.0

            m_array.markers.append(m)


        # AR Marker
        for a in self.annotation['ar_markers']:
            m = Marker()
            m.header.frame_id = '/map'
            m.ns = 'marker'
            m.id = id
            id = id + 1

            m.type = Marker.ARROW
            m.action = Marker.ADD
            m.pose = a.pose.pose
            m.scale.x = 0.5
            m.scale.y = 0.5
            m.scale.z = 0.5
            m.color.r = 0.0
            m.color.g = 1.0
            m.color.b = 1.0
            m.color.a = 0.5
            m_array.markers.append(m)

            m = Marker()
            m.header.frame_id = '/map'
            m.ns = 'marker'
            m.id = id
            id = id +1

            m.type = Marker.TEXT_VIEW_FACING
            m.text = str(a.id)
            m.action = Marker.ADD
            m.pose.position.x = a.pose.pose.position.x
            m.pose.position.y = a.pose.pose.position.y
            m.pose.position.z = a.pose.pose.position.z + 0.5
            m.scale.x = 0.3 
            m.scale.y = 0.3
            m.scale.z = 0.3
            m.color.r = 1.0
            m.color.g = 1.0
            m.color.b = 1.0
            m.color.a = 1.0

            m_array.markers.append(m)

        self.loginfo('publish viz_markers')
        self.publisher['viz_markers'].publish(m_array)

    def update(self):
        self.publish_annotations()
        self.publish_visualization_markers()
        write_annotations_into_file(self.annotation, self.filename)
        self.loginfo('Annotations have been updated.')

        for key in ['tables', 'columns', 'walls', 'ar_markers']:
            self.loginfo('  %s\t: %s' % (str(key), str(len(self.annotation[key]))))

    def spin(self):
        self.publish_annotations()
        self.publish_visualization_markers()
        rospy.spin()

    def loginfo(self, msg):
        rospy.loginfo('Annotation Server : ' + str(msg))

    def logerr(self, msg):
        rospy.logerr('Annotation Server : ' + str(msg))
