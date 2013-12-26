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

var order_pub_topic = "/list_order";
var order_pub_topic_type = "/cafe_msgs/OrderList";

var nav_div;

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
