/*
   Jihoon Lee

  Circle Annotator 
  - OccupancyGridClient
  - Annotator

 */

ANNOTATOR.AlvarAr= function(options) {
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

  this.clear = function()
  {
    that.rootObject.removeChild(that.marker);
    that.marker = null;
    that.selected = null;
  }

  this.rootObject.addEventListener('mousedown',function(event) {
    that.clear();
    // convert to ROS coordinates
    var pose = getPose(event);
    var mouse_ondrag = false;
    var marker;
    var x = pose.position.x - map_origin.position.x;
    var y = -(pose.position.y - map_origin.position.y);

    event.onMouseMove = function(move_event) {
      var move_pose = getPose(move_event);

      if(mouse_ondrag) {
        var angle = Math.atan2((move_pose.position.y - pose.position.y), (move_pose.position.x- pose.position.x));
        marker.rotation = - angle * 180 / Math.PI + 90;
        
      }
      else {
        mouse_ondrag = true;
        marker = new ROS2D.NavigationArrow({
            size : 20,
            strokeSize : 1,
            fillColor : createjs.Graphics.getRGB(255,64,128,1.0),
            pulse : false
          });
        marker.x = x;
        marker.y = y;
        marker.scaleX = 1.0 / stage.scaleX;
        marker.scaleY = 1.0 / stage.scaleY;
        marker.rotation = stage.rosQuaternionToGlobalTheta(pose.orientation);
        that.rootObject.addChild(marker);
      }
    }
    event.onMouseUp = function(up_event) {
      if(mouse_ondrag) {
        var up_pose = getPose(up_event);
        var angle = Math.atan2((up_pose.position.y - pose.position.y), (up_pose.position.x- pose.position.x));
        marker.rotation = - angle * 180 / Math.PI + 90;

        var quaternion = new ROSLIB.Quaternion();
        var yaw_180 = new ROSLIB.Quaternion({ x : 0, y : 0,z : 1, w : 0});
        var roll_180 = new ROSLIB.Quaternion({ x : 1, y : 0,z : 0, w : 0});
        quaternion.multiply(yaw_180);
        quaternion.multiply(yaw_180);
        quaternion.multiply(roll_180);

        angle -= (Math.PI/2);

        var orientation = stage.globalRPYTorosQuaternion(0,angle,0);
        quaternion.multiply(orientation);
        quaternion.normalize();
        var ox = pose.position.x;
        var oy = pose.position.y;

        that.emit('add',{x:ox,y:oy,orientation: quaternion});        
        that.selected ={x:ox,y:oy,orientation: quaternion};
        that.marker = marker;
      }
    }
  });
}

ANNOTATOR.AlvarAr.prototype.__proto__ = EventEmitter2.prototype;
