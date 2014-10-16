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
// delivery_status_list = {
//10 : "IDLE",
//20 : "GO_TO_FRONTDESK",
//30 : "ARRIVAL_AT_FRONTDESK",
//40 : "WAITING_FOR_FRONTDESK",
//51 : "GO_TO_RECEIVER",
//52 : "ARRIVAL_AT_RECEIVER",
//53 : "WAITING_CONFIRM_RECEIVER",
//54 : "COMPLETE_DELIVERY",
//60 : "COMPLETE_ALL_DELIVERY",
//70 : "RETURN_TO_DOCK",
//80 : "COMPELTE_RETURN",
//-10 : "ERROR"

//menu item setting
var menu_list = {
                    "water":{"name":'water',
                     "disable_img":"./img/water_disable.png",
                     "img_qty_1"   :"./img/water_qty_1.png",
                     "img_qty_2"   :"./img/water_qty_2.png",},
                    "juice":{"name":'juice',
                     "disable_img" :"./img/juice_disable.png",
                     "img_qty_1"    :"./img/juice_qty_1.png",
                     "img_qty_2"    :"./img/juice_qty_2.png",},
                    "coffee":{"name":'coffee',
                     "disable_img"  :"./img/coffee_disable.png",
                     "img_qty_1"    :"./img/coffee_qty_1.png",
                     "img_qty_2"    :"./img/coffee_qty_2.png"},
                    }

//ui setting
var currentDiv = 0;
var divList = []
var img_path = "./img/"

//order setting
var uuid = "";
var cur_order_list = [];
var is_showing_modal = false;

$().ready(function(e){

  initDiv();
  initIntro();
  initMenu();
  initEvent();

  // setting ros callbacks
  settingROSCallbacks();
  ros.connect(defaultUrL);
});

function initEvent(){
  //set event
  // common
  $(".oa-ui-prev-btn").click(function(){
    prevDiv = currentDiv - 1;
    updateDiv(prevDiv);
  });

  $(".oa-ui-next-btn").click(function(){
    nextDiv = currentDiv + 1;
    updateDiv(nextDiv);
  });

  // title-layer
  $(".title-layer").click(function(){
    nextDiv = currentDiv + 1;
    updateDiv(nextDiv);
  });

  // intro-layer
  $(".intro-layer-img-button").mouseup(function(){
    console.log("mouse up");
    $(".intro-layer-img-button").attr('src','./img/intro_button_release.png');
    nextDiv = currentDiv + 1;
    updateDiv(nextDiv);
  });
  $(".intro-layer-img-button").mousedown(function(){
    console.log("mouse down");
    $(".intro-layer-img-button").attr('src','./img/intro_button_press.png');
  });

  //menu-layer

  $("img."+'cancel-img-btn').mouseup(function(){
    $("img."+'cancel-img-btn').attr('src','./img/cancel_release.png');
    nextDiv = currentDiv - 1;
    updateDiv(nextDiv);
  });
  $("img."+'cancel-img-btn').mousedown(function(){
    $("img."+'cancel-img-btn').attr('src','./img/cancel_press.png');
  });

  $("img."+'order-img-btn').mouseup(function(){
    $("img."+'order-img-btn').attr('src','./img/order_release.png');
    nextDiv = currentDiv + 1;
    updateDiv(nextDiv);
  });
  $("img."+'order-img-btn').mousedown(function(){
    $("img."+'order-img-btn').attr('src','./img/order_press.png');
  });
 
  //modal
  $('#confirm-modal').on('hide', function () {
    console.log("modal hide");
    is_showing_modal = false;
  });

   $("img.yes-img-btn").mouseup(function(){
    $('img.yes-img-btn').attr('src','./img/yes_release.png');
    sendOrder();
    nextDiv = currentDiv + 1;
    updateDiv(nextDiv);
  });
  $("img.yes-img-btn").mousedown(function(){
    $('img.yes-img-btn').attr('src','./img/yes_press.png');
  });
  
  $("img.no-img-btn").mouseup(function(){
    $('img.no-img-btn').attr('src','./img/no_release.png');
  });
  $("img.no-img-btn").mousedown(function(){
    $('img.no-img-btn').attr('src','./img/no_press.png');
  });

}

function initDiv(){
  for (k = 0  ;k < $('.oa-ui').length ; k ++){
    class_list = $('.oa-ui')[k].classList;
    target_class_name = class_list[class_list.length - 1];
    $('.'+target_class_name).css("height",$( window ).height());
    $('.'+target_class_name).css("width",$( window ).width());

    $('.test-width').html($( window ).width());
    $('.test-height').html($( window ).height());
    
    divList.push($('.'+target_class_name))
  }
  updateDiv(currentDiv);
}

function initMenu(){
  //init menu layer
  $(".menu-layer-drink-img-group").html("");
  context = "";
  for (menu in menu_list){
    templete = '<img src='+ menu_list[menu].disable_img +' class="menu-layer-drink-img ' + menu_list[menu].name +'">'
    context += templete
  }
  $(".menu-layer-drink-img-group").html(context);

  $("img."+'cancel-img-btn').attr("src",'./img/cancel_disable.png');
  $("img."+'order-img-btn').attr("src",'./img/order_disable.png');

  cur_order_list = []

  //init menu layer event
  $(".menu-layer-drink-img").click(function(data){
    console.log(data.currentTarget.classList)
    class_name = data.currentTarget.classList[data.currentTarget.classList.length -1];
    img_src = $("img."+class_name).attr("src");
    console.log(class_name)
    if (cur_order_list.length > 1){
      for (var i = cur_order_list.length - 1; i >= 0; i--) {
        idx = jQuery.inArray( class_name, cur_order_list)
        if (idx >= 0 ){
          cur_order_list.splice(idx,1);
          $("img."+class_name).attr("src",menu_list[class_name].disable_img);
        }  
      };
    }
    else{
      if(img_src.indexOf("_disable")>0){
        $("img."+class_name).attr("src", menu_list[class_name].img_qty_1);
        cur_order_list.push(class_name);
      }
      else if(img_src.indexOf("_qty_1")>0){
        $("img."+class_name).attr("src", menu_list[class_name].img_qty_2);
        cur_order_list.push(class_name);
      }
      else{
        $("img."+class_name).attr("src",menu_list[class_name].disable_img);
        idx = jQuery.inArray( class_name, cur_order_list)
        cur_order_list.splice(idx,1);
        cur_order_list.splice(idx,1);
      }
    }

    if( cur_order_list.length === 0){
      $("img."+'cancel-img-btn').attr("src",'./img/cancel_disable.png');
      $("img."+'order-img-btn').attr("src",'./img/order_disable.png');
    }
    else{
      $("img."+'cancel-img-btn').attr("src",'./img/cancel_release.png');
      $("img."+'order-img-btn').attr("src",'./img/order_release.png');
    }
  });
  
}

function initIntro(){
  $('.intro-layer-location-name').html("This table is [Table "+table+"]");
}

function updateDiv(target_div){
    $('.oa-ui').hide();
    
    div_flow=1;
    
    if(currentDiv === target_div){ //refresh
      div_flow = 0;
      
      if (divList[currentDiv].selector.indexOf("on-delivery-layer") > 0){
        //post proc
        console.log("Play ad");
        $(".video-rocon-adv")[0].play();
        divList[target_div].show();
        currentDiv = target_div;
      }
      else{
        divList[target_div].show();
        currentDiv = target_div;  
      }
      
    }
    
    else if(currentDiv > target_div){ //back
      div_flow = -1; 
      
      if (target_div < 0){
       target_div += divList.length;
      }

      if (divList[currentDiv].selector.indexOf("arrival-layer") > 0){
        console.log("Play ad");
        $(".video-rocon-adv")[0].play();
        divList[target_div].show();
        currentDiv = target_div;
      }

      if (divList[currentDiv].selector.indexOf("menu-layer") > 0){
        //post proc
        initMenu()
        divList[0].show();
        currentDiv = 0;
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
      
      if (divList[currentDiv].selector.indexOf("ordered-layer") > 0){
        //post proc
        console.log("Play ad");
        $(".video-rocon-adv")[0].play();
        deliveryProgressControl(1);
        divList[target_div].show();
        currentDiv = target_div;
      }
      else if (divList[currentDiv].selector.indexOf("menu-layer") > 0){
        //post proc
        if (is_showing_modal === true){
          is_showing_modal = false;
          divList[target_div].show();
          currentDiv = target_div;
          waittingUpdateDiv(3000);
        }
        else{
          is_showing_modal = true;
          showConfrimModal();  
          divList[currentDiv].show();
        }
      }
      else if (divList[currentDiv].selector.indexOf("arrival-layer") > 0){
          waittingUpdateDiv(3000);
          divList[target_div].show();
          currentDiv = target_div;
      }
      else if (divList[currentDiv].selector.indexOf("delivery-end-layer") > 0){
        //post proc
        initMenu();
        cur_order_list = [];

        divList[target_div].show();
        currentDiv = target_div;
      }
      else{
        //post proc
        console.log("none post proc")
        $(".video-rocon-adv")[0].load();
        deliveryProgressControl(0);
        divList[target_div].show();
        currentDiv = target_div;
      }  
    }
}

function waittingUpdateDiv(timeout){
  console.log("waittingUpdateDiv");
  
  setTimeout(function(){
    nextDiv = currentDiv + 1;
    updateDiv(nextDiv)
  },timeout);
}

function deliveryProgressControl(video_src){

  if(video_src == 1){ //first step
    console.log("play 1: prepairing");
    $("img."+'on-delivery-layer-status-img').attr('src','./img/prepairing_status.png');
    $("img."+'on-delivery-layer-status-img').show();
  }
  else if(video_src == 2){ //secend step
    console.log("play 2: delivery");
    $("img."+'on-delivery-layer-status-img').attr('src','./img/on_delivery_status.png');
    $("img."+'on-delivery-layer-status-img').show();
  }
  else{ //all stop
    console.log("stop 1 and stop 2");
    $("img."+'on-delivery-layer-status-img').hide();
  }
}

function showConfrimModal(){
  console.log("showConfrimModal");
  $('.modal-drink-img-group').html("");
  
  context = '';
  for (var i = cur_order_list.length - 1; i >= 0; i--) {
    menu = cur_order_list[i];
    templete = '<img src='+ menu_list[menu].img_qty_1 +' class="modal-drink-img">';
    context += templete;
  };  
  $('.modal-drink-img-group').html(context);
  $('#confirm-modal').modal('show');
}

function sendOrder(){
  console.log("send_order: ", cur_order_list);
  uuid = generateUUID()
  var order = new ROSLIB.Message({
    order_id : uuid,
    receivers : [{location: table+"", qty : 1, menus:cur_order_list}]
  });
  send_order_publisher.publish(order)
  console.log("order: ",order, send_order_publisher)
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
