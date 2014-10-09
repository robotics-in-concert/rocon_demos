var ros = new ROSLIB.Ros();

var send_order_pub_type = "simple_delivery_msgs/DeliveryOrder"
var delivery_status_sub_type = "simple_delivery_msgs/DeliveryStatus";

var defaultUrL = "";
var discard_btn_list = "";
var table = "";

//parameter setting
if (rocon_interactions.hasOwnProperty('rosbridge_uri')){
    defaultUrL = rocon_interactions.rosbridge_uri;
}else{
    defaultUrL = 'localhost';
}

if (rocon_interactions.parameters.hasOwnProperty('extra_data')){
    table = rocon_interactions.parameters.extra_data;
}else{
    table = "1";
}

// remapping rules setting
//pub, sub
var send_order_pub_topic = "send_order";
var delivery_status_sub_topic = "delivery_status";
var send_order_publisher;

if(delivery_status_sub_topic in rocon_interactions.remappings)
  delivery_status_sub_topic = rocon_interactions.remappings[delivery_status_sub_topic];

if(send_order_pub_topic in rocon_interactions.remappings)
  send_order_pub_topic = rocon_interactions.remappings[send_order_pub_topic];

// public variable
var row_max_num = 3;
var robot_status;

var robot_status_list = {
                              "STATE_INITIALIZATION" :'Initialization',
                              "STATE_GOTO_KITCHEN"    : 'GOTO_KITCHEN',
                              "STATE_AT_KITCHEN"      : 'AT_KITCHEN',
                              "STATE_GOTO_TABLE"      : 'GOTO_TABLE',
                              "STATE_AT_TABLE"         : 'AT_TABLE',
                              "STATE_ON_ERROR"         :'ON_ERROR',
                             };

var delivery_status_list = {
                              10 : "IDLE",
                              20 : "GO_TO_FRONTDESK",
                              30 : "ARRIVAL_AT_FRONTDESK",
                              40 : "WAITING_FOR_FRONTDESK",
                              51 : "GO_TO_RECEIVER",
                              52 : "ARRIVAL_AT_RECEIVER",
                              53 : "WAITING_CONFIRM_RECEIVER",
                              54 : "COMPLETE_DELIVERY",
                              60 : "COMPLETE_ALL_DELIVERY",
                              70 : "RETURN_TO_DOCK",
                              80 : "COMPELTE_RETURN",
                             };
delivery_status_list[-10] = "ERROR"

var menu_list = {
                    "coke":{"name":'coke',
                     "disable_img":"coke_disable.png",
                     "img":"coke.png",},
                     "beer":{"name":'beer',
                     "disable_img":"beer_disable.png",
                     "img":"beer.png",},
                     "welchis":{"name":'welchis',
                     "disable_img":"welchis_disable.png",
                     "img":"welchis.png"},
                    }

//ui
var currentDiv = 0;
var divList = []
//order
var uuid = "";
var cur_order_list = [];
var is_showing_modal = false;

$().ready(function(e){
  initDiv();  
  // setting ros callbacks
  settingROSCallbacks();
  ros.connect(defaultUrL);
});

function initDiv(){
  for (k = 0  ;k < $('.oa-ui').length ; k ++){
    class_list = $('.oa-ui')[k].classList;
    target_class_name = class_list[class_list.length - 1];
    divList.push($('.'+target_class_name))
  }

  updateDiv(currentDiv);
  initMenu();

  //set event
  $(".oa-ui-prev-btn").click(function(){
    prevDiv = currentDiv - 1;
    updateDiv(prevDiv);
  });

  $(".oa-ui-next-btn").click(function(){
    nextDiv = currentDiv + 1;
    updateDiv(nextDiv);
  });

  $('.modal-order-confirm').click(function(){
    sendOrder();
    nextDiv = currentDiv + 1;
    updateDiv(nextDiv);
  });
}

function initMenu(){
  $(".menu-drink-img-group").html("");
  context = "";
  for (menu in menu_list){
    templete = '<img src="./img/'+ menu_list[menu].disable_img +'" class="menu-drink-img ' + menu_list[menu].name +'">'
    context += templete
  }
  $(".menu-drink-img-group").html(context);

  $(".menu-drink-img").click(function(data){
    class_name = data.currentTarget.classList[data.currentTarget.classList.length -1];
    console.log(class_name);
    img_src = $("img."+class_name).attr("src");
    
    //more nice
    if(img_src.indexOf("_disable")>0){
      $("img."+class_name).attr("src",img_src.split("_disable.png")[0]+".png");
      cur_order_list.push(class_name);
    }
    else{
      $("img."+class_name).attr("src",img_src.split(".png")[0]+"_disable.png");
      idx = jQuery.inArray( class_name, cur_order_list)
      cur_order_list.splice(idx,1);
    }
    console.log(cur_order_list);
  });
}

function updateDiv(target_div){
    $('.oa-ui').hide();
    
    div_flow=1;
    
    if(currentDiv === target_div){ //refresh
      div_flow = 0;
      
      divList[target_div].show();
      currentDiv = target_div;
    }
    
    else if(currentDiv > target_div){ //back
      div_flow = -1; 
      
      if (target_div < 0){
       target_div += divList.length;
      }
      if (divList[target_div].selector.indexOf("on-delivery-layer") > 0){
        console.log("Play");
        $(".video-rocon-adv")[0].play();
        
        divList[target_div].show();
        currentDiv = target_div;
      }
      else{
        $(".video-rocon-adv")[0].load();
        deliveryProgressControl(0);
        divList[target_div].show();
        currentDiv = target_div;  
      }
    }
    else{ //forward
      div_flow = 1; 
      
      if (target_div >= divList.length){
        target_div -= divList.length;
      }
      
      if (divList[target_div].selector.indexOf("on-delivery-layer") > 0){
        console.log("Play");
        $(".video-rocon-adv")[0].play();
        
        divList[target_div].show();
        currentDiv = target_div;
      }
      else if (divList[target_div].selector.indexOf("ordered-layer") > 0){
        if (is_showing_modal === true){
          is_showing_modal = false;
          divList[target_div].show();
          currentDiv = target_div;
        }
        else{
          is_showing_modal = true;
          showConfrimModal();  
          divList[currentDiv].show();
        }
      }
      else{
        $(".video-rocon-adv")[0].load();
        deliveryProgressControl(0);
        divList[target_div].show();
        currentDiv = target_div;
      }  
    }
}


function deliveryProgressControl(video_src){
  if(video_src == 1){ //first step
    console.log("play 1");
    $(".video-delivery-progress-1")[0].play();
    $(".video-delivery-progress-1").show();
    
    $(".video-delivery-progress-2")[0].load();
    $(".video-delivery-progress-2").hide();
  }
  else if(video_src == 2){ //secend step
    console.log("play 2");
    $(".video-delivery-progress-2")[0].play();
    $(".video-delivery-progress-2").show();
    
    $(".video-delivery-progress-1")[0].load();
    $(".video-delivery-progress-1").hide();
  }
  else{ //all stop
    console.log("stop 1 and stop 2");
    $(".video-delivery-progress-1")[0].load();
    $(".video-delivery-progress-1").show();
    $(".video-delivery-progress-2")[0].load();
  }

}

function showConfrimModal(){
  console.log("showConfrimModal");
  $('.modal-order-list').html("");
  
  context = '<p class="modal-drink-img-group">';
  for (var i = cur_order_list.length - 1; i >= 0; i--) {
    menu = cur_order_list[i];
    templete = '<img src="./img/'+ menu_list[menu].img +'" class="modal-drink-img">';
    context += templete;
  };
  context += "</p>";
  
  $('.modal-order-list').html(context);
  $('#confirm-modal').modal('show');
}

function sendOrder(){
  console.log("send_order: ", cur_order_list);
  uuid = generateUUID()
  var order = new ROSLIB.Message({
    order_id : uuid,
    receivers : [{location: table+"", qty : 1, menus:cur_order_list}]
  });
  console.log("order: ",order, send_order_publisher)

  send_order_publisher.publish(order)
}

function settingROSCallbacks(){
  ros.on('connection',function() {
    console.log("Connected");
    // subscribe to order list    
    var delivery_status_listener = new ROSLIB.Topic({
      ros : ros,
      name : delivery_status_sub_topic,
      messageType: delivery_status_sub_type
      });
    delivery_status_listener.subscribe(processDeliveryStatusUpdate);

    //setting publisher
    send_order_publisher = new ROSLIB.Topic({
        ros : ros,
        name : send_order_pub_topic,
        messageType : send_order_pub_type
    });
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
};

function processDeliveryStatusUpdate(data){
  console.log(data);
  if (data.order_id == uuid) {
    if (data.status >= 20 && data.status <= 40){
      deliveryProgressControl(1); 
    }
    else if(data.status == 51){
      deliveryProgressControl(2);
    }
    else if(data.status == 52){
      nextDiv = currentDiv + 1;
      updateDiv(nextDiv);
    }
    else if(data.status == 60){
      nextDiv = currentDiv + 1;
      updateDiv(nextDiv);
    }
  }
  else{
    console.log(uuid)
    console.log(data.uuid)
    console.log('other delivery status')
  }
};

function showDeliberyStatus(data){
  $(".sd-delivery-status-layer").html("");
  Object.keys(data).forEach(function(item){
    $(".sd-delivery-status-layer").append('<h1 class="sd-delivery-status-msg">'+item+': '+data[item]+'</h1>');
  });
};

function processRobotStatusUpdate(data){
  robot_status = data.data;
  $(".sd-robot-status").text($(".sd-robot-status").text().split(':')[0]+': ' + robot_status);
  if(robot_status === robot_status_list.STATE_AT_KITCHEN){
    $(".sd-table-list").prop('disabled',false);
  }
  else{
    $(".sd-table-list").prop('disabled',true);
  }
};

function processFilterSortMenu(data){
  var menu = [];
  var sortable = [];
  //filter
  for (var i = 0; i < data.length; i++) {
    var allow_flag = true;
    var disard_btns = "";
    if( typeof(discard_btn_list) === "string"){
       disard_btns = discard_btn_list.replace(/\[/g,'').replace(/\]/g,'').replace(/\s/g,'').split(',');
    }
    else if(typeof(discard_btn_list) === "object"){
      disard_btns = discard_btn_list;
    }
     
    disard_btns.forEach(function(discard_name){
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
};

function processTableListUpdate(data){
  var menu = processFilterSortMenu(data.tables);
  settingMainMenu(menu);
};

function processDiagnosticUpdate(data){
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
};

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
  var row_num = 0;
  $('.sd-main-menu').html('');
  for (var i = 0; i < data.length; i++) {
    var table_name = data[i].name;
    if(i % row_max_num === 0){
      row_num += 1;
      $('.sd-main-menu').append('<div class="row-fluid sd-table-row-num-' + row_num + '">');
    }
    $('.sd-table-row-num-' + row_num).append('<button type="button" class="span4 btn btn-primary btn-large sd-table-list sd-table-' + table_name + '">' + table_name + '</button>')  
    $('.sd-table-'+table_name).click(function(data){
      var order_location = data.currentTarget.outerText
      $('.sd-goal-msg').text(order_location);      
      //send order
      uuid = generateUUID()
      var order = new ROSLIB.Message({
        order_id : uuid,
        receivers : [{location: order_location.split("table")[1], qty : 1}]
      });
      console.log("order: ",order, send_order_publisher)

      send_order_publisher.publish(order)
      showMainMenu(false);
    });
  };
};

function showMainMenu(flag){
    if(flag === true){
      $('.sd-main-menu-layer').show();
      $('.sd-delivery-status').hide();
    }
    else{
      $('.sd-main-menu-layer').hide();
      $('.sd-delivery-status').show();
    }
};

