var ros = new ROSLIB.Ros();

var kichen_order_action_type = "simple_delivery_msgs/DeliverOrderAction"
var diagnostic_sub_topic_type = "diagnostic_msgs/DiagnosticArray";
var tables_sub_topic_type = "yocs_msgs/TableList"
var robot_status_type = "";

var defaultUrL = ""
if (rocon_interactions.hasOwnProperty('rosbridge_uri')){
    defaultUrL = rocon_interactions.rosbridge_uri;
}else{
    defaultUrL = 'localhost';
}


var diagnostic_sub_topic = "diagnostics_agg";
var tables_sub_topic = "tables";
var kichen_order_action = "kitchen_order"

if(diagnostic_sub_topic in rocon_interactions.remappings)
  diagnostic_sub_topic = rocon_interactions.remappings[diagnostic_sub_topic];

if(tables_sub_topic in rocon_interactions.remappings)
  tables_sub_topic = rocon_interactions.remappings[tables_sub_topic];

if(kichen_order_action in rocon_interactions.remappings)
	kichen_order_action = rocon_interactions.remappings[kichen_order_action];

var nav_div;
var remote_nav_div;
var orders_div;
var remote_orders_div;
var hero_div;

var delive_order_client;

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

  nav_div = $('#nav-orders');
  remote_nav_div = $('#nav-remote-orders');
  orders_div = $('#orders');
  remote_orders_div = $('#remote_orders');
  hero_div = $('#hero-unit');
  
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

function processTableListUpdate(data){
  settingMainMenu(data.tables);
}

function processDiagnostic(data){
  
  for (var i = data.status.length - 1; i >= 0; i--) {
    var name = data.status[i].name;
    if(name === "/Power System/Laptop Battery"){
        var percent = getBattPecent(data.status[i].values);
        //console.log('robot batt: ',percent);
        setBattPecent('.sd-laptop-batt-status',percent);
    }
    else if(name === "/Power System/Battery"){
        var percent = getBattPecent(data.status[i].values);
        //console.log('robot batt: ',percent);
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
    for (var i = 0; i < data.length; i++) {
      var key = data[i].key;
      if(key === 'Percent'){
         percent = data[i].value;
      }
    };
    return percent;
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
      console.log(data.currentTarget.outerText);
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

