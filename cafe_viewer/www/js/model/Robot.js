/**
 * @author Jihoon Lee - jihoonlee.in@gmail.com
 */

/**
 * A robot visulizes the pose of robot as a directed triangle
 * @constructor
 * @param options - object iwth following keys:
 *   * ros - the ROSLIB.Ros connection handle
 *   * map_origin (optional) - the origin of map(ROSLIB.Pose)
 *   * name      (optional) -  the name of robot
 *   * topicName  (optional) - the robot pose topic name
 *   * topicType  (optional) - the type of robot pose topic(geometry_msgs/Pose, geometry_msgs/PoseStamped)
 *   * size       (optional) - the size of the marker
 *   * strokeSize (optional) - the size of the outline
 *   * strokeColor (optional) - the createjs color for the stroke
 *   * fillColor (optional) - the createjs color for the fill
 *   * pulse      (optional) - if the marker should "pulse" over time 
 *   * rootObject (optional) - the root object to add the click listeners to and render robot markers to
 */
ROS2D.Robot = function(options) {
  var robot = this;
  options = options || {};
  robot.ros = options.ros;
  robot.rootObject = options.rootObject;
  robot.map_origin = options.map_origin || new ROSLIB.Pose();
  robot.topicName = options.topicName || 'robot_pose';
  robot.topicType = options.topicType || 'geometry_msgs/Pose';
  robot.size = options.size || 8;
  robot.strokeSize = options.strokeSize || 1;
  robot.strokeColor = options.strokeColor || createjs.Graphics.getRGB(0, 0, 0); 
  robot.fillColor = options.fillColor || createjs.Graphics.getRGB(255, 64, 128, 0.66); 
  robot.pulse = options.pulse || true;
  robot.name  = options.name  || '';

  // get a handle to the stage
  var stage;
  if (robot.rootObject instanceof createjs.Stage) {
    stage = robot.rootObject;
  } else {
    stage = robot.rootObject.getStage();
  }


  robot.marker = new ROS2D.NavigationArrow({
          size : robot.size,                                     
          strokeSize : robot.strokeSize,
          strokeColor : robot.strokeColor,
          fillColor : robot.fillColor, 
          pulse : robot.pulse
      });
  robot.marker.visible = false;
  robot.marker.scaleX = 1.0 / stage.scaleX;
  robot.marker.scaleY = 1.0 / stage.scaleY;

  robot.text = new createjs.Text(robot.name,"15px Arial","#000000");
  robot.text.visible = false;
  robot.text.scaleX = 1.0 / stage.scaleX;
  robot.text.scaleY = 1.0 / stage.scaleY;
  robot.text.textBaseline = "center";

  robot.rootObject.addChild(robot.marker);
  robot.rootObject.addChild(robot.text);

  robot.poseListener = new ROSLIB.Topic({
    ros: robot.ros,
    name: robot.topicName,
    messageType : robot.topicType,
    throttle_rate : 100
  });

  var initScaleSet;
  robot.poseListener.subscribe(function(pose) {
    robot.marker.x = pose.pose.position.x - robot.map_origin.position.x;
    robot.marker.y = -(pose.pose.position.y - robot.map_origin.position.y);
    robot.marker.rotation = stage.rosQuaternionToGlobalTheta(pose.pose.orientation);

    robot.text.x = pose.pose.position.x - robot.map_origin.position.x;
    robot.text.y = -(pose.pose.position.y - robot.map_origin.position.y);

    if(!initScaleSet) {
      robot.marker.visible = true;
      robot.text.visible = true;


      initScaleSet = true;
    }
  });

};
