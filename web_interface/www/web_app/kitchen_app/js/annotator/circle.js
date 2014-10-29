/*
   Jihoon Lee

  Circle Annotator 
  - OccupancyGridClient
  - Annotator

 */

ANNOTATOR.Circle= function(options) {
  var that = this;
  var ros = options.ros;
  var map_origin = options.map_origin;
  this.rootObject = options.rootObject || new createjs.Container();


  var stage;
  if (that.rootObject instanceof createjs.Stage) {
    stage = that.rootObject;
  } else {
    stage = that.rootObject.getStage();
  }

  var getPose = function(event) {
    var coords = stage.globalToRos(event.stageX,event.stageY);
    var pose = new ROSLIB.Pose({
        position : new ROSLIB.Vector3(coords)
      });

    pose.position.x = pose.position.x + map_origin.position.x;
    pose.position.y = pose.position.y + map_origin.position.y;

    return pose;
  }

  var createCircle = function(x,y,radius) {
    var circle = new createjs.Shape();
    circle.graphics.beginFill("red").drawCircle(0,0,radius);
    circle.x = x;
    circle.y = y;

    return circle;
  }

  this.clear = function()
  {
    that.rootObject.removeChild(that.circle);
    that.circle = null;
    that.selected = null;
  }

  this.rootObject.addEventListener('mousedown',function(event) {
    that.clear();
    // convert to ROS coordinates
    var pose = getPose(event);
    var mouse_ondrag = false;
    var circle;
    var x = pose.position.x - map_origin.position.x;
    var y = -(pose.position.y - map_origin.position.y);

    event.onMouseMove = function(move_event) {
      var move_pose = getPose(move_event);

      move_pose.position.subtract(pose.position);
      var mag = Math.sqrt(move_pose.position.x * move_pose.position.x  + move_pose.position.y * move_pose.position.y);
      console.log(mag);

      if(mouse_ondrag) {
        circle.graphics.clear();
        circle.graphics.beginFill("red").drawCircle(0,0,mag);
        circle.x = x;
        circle.y = y; 
      }
      else {
        circle = createCircle(x,y,mag);
        mouse_ondrag = true;
        that.rootObject.addChild(circle);
      }
    }
    event.onMouseUp = function(up_event) {

      if(mouse_ondrag) {
        var up_pose = getPose(up_event);
        up_pose.position.subtract(pose.position);
        var mag = Math.sqrt(up_pose.position.x * up_pose.position.x  + up_pose.position.y * up_pose.position.y);

        circle.graphics.clear();
        circle.graphics.beginFill("red").drawCircle(0,0,mag);
        circle.x = x;
        circle.y = y; 

        that.circle = circle;
        that.emit('add',{x:x,y:y,radius:mag});

        var ox = pose.position.x;
        var oy = pose.position.y;
        that.selected = {x:ox,y:oy,radius:mag};
      }
    }
  });
}

ANNOTATOR.Circle.prototype.__proto__ = EventEmitter2.prototype;
