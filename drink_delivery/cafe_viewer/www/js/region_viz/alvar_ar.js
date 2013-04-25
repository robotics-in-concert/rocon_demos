/*
   Jihoon Lee

   Alvar ar Visualizor
 */

REGIONVIZ.AlvarAR = function(options) {
  var that = this;

  options = options || {};
  that.rootObject = options.rootObject;
  var map_origin = options.map_origin;
  that.instance_tags = options.instance_tags;
  that.color = createjs.Graphics.getRGB(0,154,205,0.8);
  that.worldlib = options.worldlib || new Worldlib({ ros: options.ros});
  that.markers = {};
  that.new_markers = {};
  that.texts = {};
  that.new_texts = {};

  var stage;
  if (that.rootObject instanceof createjs.Stage) {
    stage = that.rootObject;
  } else {
    stage = that.rootObject.getStage();
  }

  var updates = function() {
    that.worldlib.worldObjectInstanceTagSearch(that.instance_tags,
      function(instances)
      {
        for(var i in instances) {
          
          var func = new ParseDescription(instances[i]);

          that.worldlib.getWorldObjectDescription(instances[i].description_id,func.parse);
        }
      }
    );
  }

  var createMarker = function(x,y,orientation) {
    var m = new ROS2D.NavigationArrow({
      size : 20,
      strokeSize : 1,
      fillColor : that.color,
      pulse : false
    });

    m.x = x;
    m.y = y;

    var quaternion = new ROSLIB.Quaternion(orientation);
    var yaw_n180 = new ROSLIB.Quaternion({ x : 0, y : 0,z : 1, w : 0});
    var roll_n180 = new ROSLIB.Quaternion({ x : 1, y : 0,z : 0, w : 0});

    yaw_n180.invert();
    roll_n180.invert();
    
    quaternion.multiply(roll_n180);
    quaternion.multiply(yaw_n180);
    quaternion.multiply(yaw_n180);

    var rpy = stage.rosQuaternionToGlobalRPY(quaternion);
    m.rotation = -rpy.yaw * 180 / Math.PI;
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


  var ParseDescription = function(instance) {
    var parse_desc = this;
    this.instance = instance;

    this.parse = function(description) {
      var instance = parse_desc.instance;
      var region = JSON.parse(description.descriptors[0].data);
      var marker = region['marker'];
      var x = marker.pose.pose.position.x - map_origin.position.x;
      var y = -(marker.pose.pose.position.y - map_origin.position.y);
      var m = createMarker(x,y,marker.pose.pose.orientation);

      that.new_markers[instance.instance_id] = m;
      that.new_texts[instance.instance_id] = createText(x,y,marker.id);
    }
  }

  var cleanup = function() {
    for(var m in that.markers)
    {
      if(!(c in that.new_markers)) {
        that.rootObject.removeChild(that.texts[m]);
        that.rootObject.removeChild(that.markers[m]);
        delete that.texts[m];
        delete that.markers[m];
      }
    }
    for(var c in that.new_markers)
    {
      if(!(c in that.markers)) {
        that.texts[c] = that.new_texts[c];
        that.markers[c] = that.new_markers[c];
        that.rootObject.addChild(that.markers[c]);
        that.rootObject.addChild(that.texts[c]);
      }
    }

    that.emit('update',that.texts);
    that.new_texts = {}
    that.new_markers = {}
  }

  window.setInterval(updates,1000);
 // window.setTimeout(cleanup,5000);
  window.setInterval(cleanup,1000);
};


REGIONVIZ.AlvarAR.prototype.__proto__ = EventEmitter2.prototype;
