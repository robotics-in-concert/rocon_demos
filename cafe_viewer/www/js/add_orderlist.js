var STATUS_STRING = ['IDLE',
                     'GO_TO_KITCHEN',
                     'ARRIVE_KITCHEN',
                     'WAITING_FOR_KITCHEN',
                     'IN_DELIVERY',
                     'ARRIVE TABLE',
                     'WAITING USER CONFIRM',
                     'COMPLETE DELIVERY',
                     'RETURN TO DOCK',
                     'END DELIVERY',
                     'ERROR'];

var order_pub_topic = rocon_interactions.remappings['list_order'] || 'list_order';
var order_pub_topic_type = "/cafe_msgs/OrderList";

var remote_order_pub_topic = rocon_interactions.remappings['list_remote_order'] || 'list_remote_order';
var remote_order_pub_topic_type = "/cafe_msgs/RemoteOrderList";

var remote_order_update_pub_topic = rocon_interactions.remappings['remote_order_update'] || 'remote_order_update';
var remote_order_update_pub_topic_type = "/cafe_msgs/RemoteOrderUpdate";

var nav_div;
var remote_nav_div;

function processOrderList(msg) {

  nav_div.empty();

  for(var i in msg.orders) {
    // add into navigation bar
    var navli = createOrderLi(msg.orders[i]); 
    nav_div.append(navli);

  }
}

function createOrderLi(order) {
  var li = document.createElement('li');
  var p = document.createElement('p');
  p.innerHTML = "# " + order.order_id + " - Table : " + order.table_id + " - Robot : " + order.robot_name +  "<br/> Status : " + STATUS_STRING[order.status];
  li.appendChild(p);
                                                                                                                                                              
  $(li).hover(
      function() { this.style.background= "gray"; },
      function() { this.style.background= "";     }
  );
  $(li).click(function() {
//    hero_div.empty();
//    var hero_element = createHeroDiv(order);
//    hero_div.append(hero_element);
  });
                                                                                                                                                              
  return li;
}

function processRemoteOrderUpdate(msg){
	$('.'+msg.name).innerHTML = "<b>Name: </b>" + msg.name +
       "<br/><b>Estimated Time: </b>" + msg.estimated_arrival+" min." +  
       "<br/><b>Status : </b>" + STATUS_STRING[msg.status];
}

function processRemoteOrderList(msg) {
	var i;
	console.log("Call processRemoteOrderList");
	remote_nav_div.empty();
	for(i in msg.remote_orders) {
		var navli = createRemoteOrderLi(msg.remote_orders[i]); 
		remote_nav_div.append(navli);
	}
}

function createRemoteOrderLi(order){
	order.order_id = "Remote";
	order.table_id = "remote order";
   var li = document.createElement('li');
   var p = document.createElement('p');
   p.innerHTML = "<b>Name: </b>" + order.name +
			       "<br/><b>Estimated Time: </b>" + order.estimated_arrival+" min." +  
			       "<br/><b>Status : </b>" + STATUS_STRING[order.status];
   li.appendChild(p);
   $(li).hover(
        function() { this.style.background= "gray"; },
        function() { this.style.background= "";     }
    );
    return li;
  }
