/*
   Jihoon Lee

   Circle Visualizor
 */

REGIONVIZ.Circle = function(options) {
  var that = this;

  options = options || {};
  that.rootObject = options.rootObject;
  var map_origin = options.map_origin;
  that.instance_tags = options.instance_tags;
  that.color = createjs.Graphics.getRGB(138,54,15,0.6);
  that.worldlib = options.worldlib || new Worldlib({ ros: options.ros});
  that.circles = {};
  that.new_circles = {};
  that.texts = {};
  that.new_texts = {};

  var stage;
  if (that.rootObject instanceof createjs.Stage) {
    stage = that.rootObject;
  } else {
    stage = that.rootObject.getStage();
  }

  var createCircle = function(x,y,radius,id,name) {
    var circle = new createjs.Shape();
    circle.graphics.beginFill(that.color).drawCircle(0,0,radius);
    circle.x = x;
    circle.y = y;
    circle.instance_id = id;
    circle.instance_name = name;

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
//    text_object.lineWidth = 30;
//    text_object.maxWidth = 30;
    return text_object;
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

  var ParseDescription = function(instance) {
    var parse_desc = this;
    this.instance = instance;

    this.parse = function(description) {
      var instance = parse_desc.instance;
      var region = JSON.parse(description.descriptors[0].data);
      var radius = region['radius'];
      var x = instance.pose.pose.pose.position.x - map_origin.position.x;
      var y = -(instance.pose.pose.pose.position.y - map_origin.position.y);
      
      that.new_texts[instance.instance_id] = createText(x,y,instance.name);
      that.new_circles[instance.instance_id] = createCircle(x,y,radius,instance.instance_id,instance.name);
    }
  }

  var cleanup = function() {
    for(var c in that.circles)
    {
      if(!(c in that.new_circles)) {
        that.rootObject.removeChild(that.texts[c]);
        that.rootObject.removeChild(that.circles[c]);
        delete that.texts[c];
        delete that.circles[c];
      }
    }
    for(var c in that.new_circles)
    {
      if(!(c in that.circles)) {
        that.texts[c] = that.new_texts[c];
        that.circles[c] = that.new_circles[c];
        that.rootObject.addChild(that.circles[c]);
        that.rootObject.addChild(that.texts[c]);
      }
    }

    that.emit('update',that.circles);
    that.new_circles = {};
    that.new_texts = {}
  }

  window.setInterval(updates,1000);
 // window.setTimeout(cleanup,5000);
  window.setInterval(cleanup,1000);
};


REGIONVIZ.Circle.prototype.__proto__ = EventEmitter2.prototype;
