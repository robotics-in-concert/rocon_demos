/*
   Jihoon Lee

   Alvar ar Visualizor
 */

REGIONVIZ.AlvarAR = function(options) {
  var that = this;

  options = options || {};
  that.rootObject = options.rootObject;
  that.ros = options.ros;
  var map_origin = options.map_origin;
  that.color = options.color || createjs.Graphics.getRGB(0,154,205,0.8);
  that.topicName = options.topicName || '/marker_pose_list';
  that.topicType = options.topicType || '/ar_track_alvar_msgs/AlvarMarkers';
  that.markers = {};
  that.marker_viz = {}
  that.texts = {};

  var stage;
  if (that.rootObject instanceof createjs.Stage) {
    stage = that.rootObject;
  } else {
    stage = that.rootObject.getStage();
  }

  that.sub_armarker = new ROSLIB.Topic({
    ros: that.ros,
    name : that.topicName, 
    messageType : that.topicType,
  });

  that.sub_armarker.subscribe(function(msg) {

    // removing markers that are gone.
    for(m in that.markers) {
      var mk = that.markers[m];
      var flag = false;

      for(mm in msg.markers) {  if(msg.markers[mm].id == mk.id)  flag = true;  }

      if(!flag)
      {
        that.rootObject.removeChild(that.marker_viz[mk.id]);
        that.rootObject.removeChild(that.texts[mk.id]);
        delete that.marker_viz[mk.id];
        delete that.texts[mk.id];
      }
    }

    // adding new markers
    for(m in msg.markers)
    {
      var mk = msg.markers[m];
      var x = mk.pose.pose.position.x - map_origin.position.x;
      var y = -(mk.pose.pose.position.y - map_origin.position.y);
      var o = mk.pose.pose.orientation;

      if(!(mk.id in that.markers)) {
        var marker = createMarker(x,y,o);
        var text = createText(x,y,mk.id);
        that.marker_viz[mk.id] = marker;
        that.texts[mk.id] = text;
        that.rootObject.addChild(marker);
        that.rootObject.addChild(text);
      }
      else {
        that.marker_viz[mk.id].x = x;
        that.marker_viz[mk.id].y = y;
        that.marker_viz[mk.id].rotation = getRotation(o);
        that.texts[mk.id].x = x;
        that.texts[mk.id].y = y;
      }
    }
    that.markers = msg.markers;
  });

  var createMarker = function(x,y,orientation) {
    var m = new ROS2D.NavigationArrow({
      size : 20,
      strokeSize : 1,
      fillColor : that.color,
      pulse : false
    });

    m.x = x;
    m.y = y;

    m.rotation = getRotation(orientation); 
    m.scaleX = 1.0 / stage.scaleX;
    m.scaleY = 1.0 / stage.scaleY;

    return m;
  }

  var createText = function(x,y,text)                                 
  {
    var text_object = new createjs.Text(text,"30px Arial","#000000");
    text_object.x = x;
    text_object.y = y;
    text_object.scaleX = 1 / stage.scaleX;
    text_object.scaleY = 1 / stage.scaleY;
    text_object.textBaseline = "center";
    return text_object;
  }

  var getRotation = function(orientation) {
    var quaternion = new ROSLIB.Quaternion(orientation);
    var yaw_n180 = new ROSLIB.Quaternion({ x : 0, y : 0,z : 1, w : 0});
    var roll_n180 = new ROSLIB.Quaternion({ x : 1, y : 0,z : 0, w : 0});

    yaw_n180.invert();
    roll_n180.invert();
    
    quaternion.multiply(roll_n180);
    quaternion.multiply(yaw_n180);
    quaternion.multiply(yaw_n180);

    var rpy = stage.rosQuaternionToGlobalRPY(quaternion);
    var rotation = -rpy.yaw * 180 / Math.PI;
    
    return rotation;
  }

};


REGIONVIZ.AlvarAR.prototype.__proto__ = EventEmitter2.prototype;
