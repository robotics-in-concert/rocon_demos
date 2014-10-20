/*
   Jihoon Lee

   Circle Visualizor
 */

REGIONVIZ.Circle = function(options) {
  var that = this;

  options = options || {};
  that.ros = options.ros;
  that.rootObject = options.rootObject;
  var map_origin = options.map_origin;
  that.color = options.color || createjs.Graphics.getRGB(138,54,15,0.6);
  that.pulseColor = createjs.Graphics.getRGB(138,150,15,0.6);
  that.waitColor = createjs.Graphics.getRGB(200,54,15,0.6);
  that.tableTopicName = options.tableTopicName || '/table_pose_list';
  that.tabletopicType = options.tableTopicType || '/yocs_msgs/TableList';
  that.tables = [];
  that.circle_viz = {};
  that.texts = {};
  that.is_initialized = false;

  var stage;
  if (that.rootObject instanceof createjs.Stage) {
    stage = that.rootObject;
  } else {
    stage = that.rootObject.getStage();
  }
  
  
  
 
  that.sub_table = new ROSLIB.Topic({
    ros: that.ros,
    name : that.tableTopicName,
    messageType : that.tableTopicType
  });

  // assumes all tables' name are unique
  that.sub_table.subscribe(function(msg) {
    for(t in that.tables) {
      var table = that.tables[t];
      var flag = false;

      for(mt in msg.tables) { if(msg.tables[mt].name == table.name) flag = true; }

      if(!flag)
      {
        that.rootObject.removeChild(that.circle_viz[table.name]);
        that.rootObject.removeChild(that.texts[table.name]);
        delete that.circle_viz[table.name];
        delete that.texts[table.name];
      }
    }

    for(t in msg.tables) 
    {
      var table = msg.tables[t];
      var x = table.pose.pose.pose.position.x - map_origin.position.x;
      var y = -(table.pose.pose.pose.position.y - map_origin.position.y);
      var o = table.pose.pose.pose.orientation;
      var r = table.radius;
      var name = table.name;

      if(!(t in that.tables)) {
        var circle = createCircle(x,y,r, name);
        var text = createText(x,y,name);
        that.circle_viz[name] = circle;
        that.texts[name] = text;
        that.rootObject.addChild(circle);
        that.rootObject.addChild(text);
      }
      else {
        that.circle_viz[name].x = x;
        that.circle_viz[name].y = y;
        that.texts[name].x = x;
        that.texts[name].y = y;
      }
    }
    that.tables = msg.tables;
    that.is_initialized = true;
    console.log('Viewer : Annotations initialized');
  });
  
  
  var createCircle = function(x,y,radius, name) {
    var circle = new createjs.Shape();
    circle.graphics.beginFill(that.color).drawCircle(0,0,radius);
    circle.x = x;
    circle.y = y;
    circle.radius = radius;
    circle.name = name;
    circle.is_pulse = false;
    circle.defaultScaleX = circle.scaleX;
    circle.defaultScaleY = circle.scaleY;
    circle.growCount = 0;
    circle.growing = true;
    
    createjs.Ticker.addEventListener('tick', function() {
      if(circle.is_pulse) {
        if (circle.growing) {
          circle.scaleX *= 1.025;
          circle.scaleY *= 1.025;
          circle.growing = (++circle.growCount < 10);
        } else {
          circle.scaleX /= 1.025;
          circle.scaleY /= 1.025;
          circle.growing = (--circle.growCount < 0);
        }
      }else {
        circle.scaleX = circle.defaultScaleX;
        circle.scaleY = circle.defaultScaleY;
      }
    });     

    return circle;
  }

  var createText = function(x,y,text)
  {
    var text_object = new createjs.Text(text,"20px Arial","#000000");
    text_object.x = x;
    text_object.y = y;
    text_object.scaleX = 1/ stage.scaleX;//0.3;
    text_object.scaleY = 1/stage.scaleY;//0.3;
    text_object.textBaseline = "center";
    return text_object;
  }
};


REGIONVIZ.Circle.prototype.__proto__ = EventEmitter2.prototype;
