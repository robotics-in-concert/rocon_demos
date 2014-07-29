var ros = new ROSLIB.Ros();

var kichen_order_action_type = "simple_delivery_msgs/DeliverOrderAction"
var diagnostic_sub_topic_type = "diagnostic_msgs/DiagnosticArray";
var tables_sub_topic_type = "yocs_msgs/TableList"
var robot_status_sub_topic_type = "std_msgs/String";

var defaultUrL = "";
var discard_menu_list = [];

//parameter setting
if (rocon_interactions.hasOwnProperty('rosbridge_uri')){
    defaultUrL = rocon_interactions.rosbridge_uri;
}else{
    defaultUrL = 'localhost';
}

if (rocon_interactions.parameters.hasOwnProperty('discard_btn_name')){
    discard_menu_list = rocon_interactions.parameters.discard_btn_name;
}else{
    discard_menu_list = [];
}

// remapping rules setting
//pub, sub
var diagnostic_sub_topic = "diagnostics_agg";
var tables_sub_topic = "tables";
var robot_status_sub_topic = "robot_status"

//action
var kichen_order_action = "kitchen_order"


if(diagnostic_sub_topic in rocon_interactions.remappings)
  diagnostic_sub_topic = rocon_interactions.remappings[diagnostic_sub_topic];

if(tables_sub_topic in rocon_interactions.remappings)
  tables_sub_topic = rocon_interactions.remappings[tables_sub_topic];

if(robot_status_sub_topic in rocon_interactions.remappings)
  robot_status_sub_topic = rocon_interactions.remappings[robot_status_sub_topic];

if(kichen_order_action in rocon_interactions.remappings)
	kichen_order_action = rocon_interactions.remappings[kichen_order_action];


var delive_order_client;
var robot_status;
var robot_status_list = {
                              "STATE_INITIALIZATION" :'Initialization',
                              "STATE_GOTO_KITCHEN"    : 'GOTO_KITCHEN',
                              "STATE_AT_KITCHEN"      : 'AT_KITCHEN',
                              "STATE_GOTO_TABLE"      : 'GOTO_TABLE',
                              "STATE_AT_TABLE"         : 'AT_TABLE',
                              "STATE_ON_ERROR"         :'ON_ERROR',
                             };

$().ready(function(e){
  // setting ros callbacks()
  showMainMenu(true);
  settingROSCallbacks();
  
  ros.connect(defaultUrL);

  $('#connectbtn').on('click',function(e) {
      var va = $('#focusedInput').val();
      ros.connect(va);
      return false;
  });
  
});

function settingROSCallbacks()
{
  ros.on('connection',function() {
    console.log("Connected");
    // subscribe to order list
    
    delive_order_client = new ROSLIB.ActionClient({
      ros : ros,
      serverName : kichen_order_action,
      actionName : kichen_order_action_type
    });
    
    var diagnostic_listener = new ROSLIB.Topic({
      ros : ros,
      name : diagnostic_sub_topic,
      messageType: diagnostic_sub_topic_type
      });
    diagnostic_listener.subscribe(processDiagnostic);

    var tables_listener = new ROSLIB.Topic({
      ros : ros,
      name : tables_sub_topic,
      messageType: tables_sub_topic_type
      });
    tables_listener.subscribe(processTableListUpdate);

    var robot_status_listener = new ROSLIB.Topic({
      ros : ros,
      name : robot_status_sub_topic,
      messageType: robot_status_sub_topic_type
      });
    robot_status_listener.subscribe(processRobotStatusUpdate);

  }

  );
  ros.on('error',function(e) {
    console.log("Error!",e);
  }
  );

  ros.on('close',function() {
    console.log("Connection Close!");
    //alert("ROS Connection Close!");
  }
  );
}

function processRobotStatusUpdate(data){
  robot_status = data.data;
  $(".sd-robot-status").text($(".sd-robot-status").text().split(':')[0]+': ' + robot_status);
  if(robot_status === robot_status_list.STATE_AT_KITCHEN){
    $(".btn").prop('disabled',false);
  }
  else{
    $(".btn").prop('disabled',true);
  }
}

function processFilterSortMenu(data){
  var menu = [];
  var sortable = [];
  //filter
  for (var i = 0; i < data.length; i++) {
    var allow_flag = true;
    discard_menu_list.forEach(function(discard_name){
      if (discard_name.indexOf(data[i].name) == -1){
        allow_flag = allow_flag&true;
      }
      else{
        allow_flag = allow_flag&false;
      }      
    });
    if(allow_flag){
      menu.push(data[i]);
    }
    else{
    }
  };
  //sort by name
  sortable_menu = menu.sort(function (a,b) {
    if (a.name < b.name)
       return -1;
    if (a.name > b.name)
       return 1;
  });
  return sortable_menu;
}

function processTableListUpdate(data){
  var menu = processFilterSortMenu(data.tables);
  settingMainMenu(menu);
}

function processDiagnostic(data){
  for (var i = data.status.length - 1; i >= 0; i--) {
    var name = data.status[i].name;
    if(name === "/Power System/Laptop Battery"){
        var percent = getBattPecent(data.status[i].values);
        setBattPecent('.sd-laptop-batt-status',percent);
    }
    else if(name === "/Power System/Battery"){
        var percent = getBattPecent(data.status[i].values);
        setBattPecent('.sd-robot-batt-status',percent);
    }
  }
  
};

function setBattPecent(obj, data){
    var text = $(obj).text();
    $(obj).text(text.split(':')[0]+': ' + data+' %');
}

function getBattPecent(data){
    var percent = '-1';
    var charge = -1;
    var capacity = -1;
    for (var i = 0; i < data.length; i++) {
      var key = data[i].key;
      if(key === 'Charge (Ah)'){
         charge = data[i].value;
      }
      else if(key === 'Capacity (Ah)'){
         capacity = data[i].value;
      }
    };
    if( charge === -1 || capacity === -1){
      percent = -1;  
    }
    else{
      percent = 100 * charge / capacity;
    } 
    return percent.toFixed(2);
};

function settingMainMenu(data){
  var row_max_num = 3
  var row_num = 0;
  for (var i = 0; i < data.length; i++) {
    var table_name = data[i].name;
    if(i%row_max_num === 0){
      row_num += 1;
      $('.sd-main-menu').append('<div class="row-fluid sd-table-row-num-' + row_num + '">');
    }
    $('.sd-table-row-num-' + row_num).append('<button type="button" class="span4 btn btn-primary btn-large sd-table-' + table_name + '">' + table_name + '</button>')  
    
    $('.sd-table-'+table_name).click(function(data){

      var order_location = data.currentTarget.outerText
      var goal = new ROSLIB.Goal({
        actionClient : delive_order_client,
        goalMessage : {
          location : order_location
        }
      });
      goal.on('feedback', function(feedback) {
        console.log(feedback);
        $('.sd-delivery-status-msg').text(feedback.status);
      });
      goal.on('result', function(result) {
        console.log(result);
        showMainMenu(true);
      });

      goal.send();
      showMainMenu(false);
  
    });
  };
};

function showMainMenu(flag){
    if(flag === true){
      $('.sd-main-menu').show();
      $('.sd-delivery-status').hide();
    }
    else{
      $('.sd-main-menu').hide();
      $('.sd-delivery-status').show();
    }
};

