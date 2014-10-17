var ros = new ROSLIB.Ros();
var defaultUrL = rocon_interactions.rosbridge_uri;
var robot1 = rocon_interactions.parameters['robot1'];
var robot2 = rocon_interactions.parameters['robot2'];
var robot3 = rocon_interactions.parameters['robot3'];

var viewer;
var gridClient;
var circle_region_poller;
var ar_region_poller;
var annotator;

var order_list_sub_topic_name = '/order_list'
var order_list_sub_topic_type = 'simple_delivery_msgs/OrderList'


$().ready(function(e) {

  initHeader();
  initViewer()
  nav_div= $('#nav-orders');
  var nw = $('#nav-wrapper');
  nw.css('margin-top','20pt');
});

function initHeader()
{
  settingROSCallbacks();
  ros.connect(defaultUrL);
  $('#focusedInput').val(''+defaultUrL);
}

function initViewer() {

  viewer = createViewer();
  gridClient = addMap(viewer);
  addRegionViz(viewer,gridClient);
  addNavigators(viewer,gridClient);
}

function createViewer() {
  div = $('#view');
  div.css('margin-top','20pt');

  var width = div.width();
  var half_window = $(document).height() -200;
  var height = half_window;// < 200?200:half_window;

  viewer = new ROS2D.Viewer({
    divID : 'view',
    width: width,
    height: height,
    background: '#DDDDDD'
  });

  viewer.scene.mouseEnabled = true;
  createjs.Touch.enable(viewer.scene);
  

  $(window).resize(function(e) {
    var half_window = $(document).height()-200;
    var height = half_window;// < 200?200:half_window;

    viewer.resizeCanvas(width,height);
    viewer.scaleToDimensions(gridClient.currentGrid.width, gridClient.currentGrid.height);
  });

  return viewer;
}

function addMap(viewer) {
  var continuous = false;
  var map_topic = rocon_interactions.remappings['map'] || 'map';

  gridClient = new ROS2D.OccupancyGridClient({
    ros : ros,
    topic : map_topic,
    rootObject : viewer.scene,
  });

  // Scale the canvas to fit to the map
  gridClient.on('change', function(map_origin) {
    viewer.scaleToDimensions(gridClient.currentGrid.width, gridClient.currentGrid.height);
  });
  return gridClient;
}

function addNavigators(viewer,gridClient) {

  var robot1_name = robot1;
  var robot2_name = robot2;
  var robot3_name = robot3;
  var robot1_pose_topic = '/' + robot1 + '/robot_pose';
  var robot2_pose_topic = '/' + robot2 + '/robot_pose';
  var robot3_pose_topic = '/' + robot3 + '/robot_pose';
  
  gridClient.on('change', function(map_origin) {
    var robot1 = new ROS2D.Robot({
      ros: ros,
      map_origin : map_origin,
      name       : robot1_name,
      size       : 20,
      topicName  : robot1_pose_topic, 
      topicType  : 'geometry_msgs/PoseStamped',
      fillColor  : createjs.Graphics.getRGB(255,64,128,0.66),
      rootObject : viewer.scene
    });

    var robot2 = new ROS2D.Robot({
      ros: ros,
      map_origin : map_origin,
      name       : robot2_name,
      size       : 20,
      topicName  : robot2_pose_topic,
      topicType  : 'geometry_msgs/PoseStamped',
      fillColor  : createjs.Graphics.getRGB(100,64,255,0.66),
      rootObject : viewer.scene
    });
     var robot3 = new ROS2D.Robot({
      ros: ros,
      map_origin : map_origin,
      name       : robot3_name,
      size       : 20,
      topicName  : robot3_pose_topic,
      topicType  : 'geometry_msgs/PoseStamped',
      fillColor  : createjs.Graphics.getRGB(100,64,255,0.66),
      rootObject : viewer.scene
    });

  });
}

function addRegionViz(viewer,gridClient)
{
  var table_topic = rocon_interactions.remappings['tables'] || 'tables';
  var order_topic = rocon_interactions.remappings['list_order'] || 'list_order';
  var ar_marker_topic = rocon_interactions.remappings['ar_markers'] || 'ar_markers';
  gridClient.on('change', function(map_origin) {
    circle_region_poller = new REGIONVIZ.Circle({
      ros: ros,
      map_origin : map_origin,
      rootObject : viewer.scene,
      tableTopicName : table_topic,
      orderTopicName : order_topic
    });

    ar_region_poller = new REGIONVIZ.AlvarAR({
      ros: ros,
      map_origin : map_origin,
      rootObject : viewer.scene,
      topicName : ar_marker_topic
    });

  });
}

function settingROSCallbacks()                      
{
  ros.on('connection',function() {
    console.log("Connected");
    // subscribe to order list                                                       
    $('#focusedInput').val('Connected');
    $('#focusedInput').attr('disabled',true);

    var listener = new ROSLIB.Topic({
      ros : ros,
      name : order_pub_topic,
      messageType: order_pub_topic_type
      });
    listener.subscribe(processOrderList);

    var order_list_listener = new ROSLIB.Topic({
      ros : ros,
      name : order_list_sub_topic_name,
      messageType: order_list_sub_topic_type
    });
    order_list_listener.subscribe(processOrderList);

    }
  );
  ros.on('error',function(e) {
    console.log("Error!",e);
  }
  );
                                               
  ros.on('close',function() {
    console.log("Connection Close!");
    $('#focusedInput').val('Disconnected');
  }
  );

}

function processOrderList(msg) {
  var i;
  nav_div.empty();
  for(i in msg.orders) {
      // add into navigation bar
      var navli = createOrderLi(msg.orders[i]); 
      nav_div.append(navli);
  }
}

function createOrderLi(order) {
  var li = document.createElement('li');
  var p = document.createElement('p');
  p.innerHTML = "#" + order.order_id + 
             "<br/><b> Robot : </b>" + order.robot_name +  
             "<br/><b> Status : </b>" + order.status
             "<br/><b> menu : </b>" + order.menus.toString();
  li.appendChild(p);

  $(li).hover(
      function() { this.style.background= "gray"; },
      function() { this.style.background= "";     }
  );
  $(li).click(function() {
    hero_div.empty();
    var hero_element = createHeroDiv(order);
    hero_div.append(hero_element);
  });

  return li;
}
