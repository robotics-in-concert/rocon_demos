
    var ros = new ROSLIB.Ros();
    var order_pub_topic_type = "/cafe_msgs/OrderList";
    var remote_order_pub_topic_type = "/cafe_msgs/RemoteOrderList";
    var remote_order_update_pub_topic_type = "/cafe_msgs/RemoteOrderUpdate";
    
    /*
    var defaultUrL = ""
    if rocon_interactions.hasOwnProperty('rosbridge_uri'){
        defaultUrL = rocon_interactions.rosbridge_uri;
    }else{
        defaultUrL = 'localhost';
    }
    var order_pub_topic = "list_order";
    var remote_order_pub_topic = "list_remote_order";
    var remote_order_update_pub_topic = "remote_order_update";
    
    if(order_pub_topic in rocon_interactions.remappings)
      order_pub_topic = rocon_interactions.remappings[order_pub_topic];
    
    if(remote_order_pub_topic in rocon_interactions.remappings)
      remote_order_pub_topic = rocon_interactions.remappings[remote_order_pub_topic];
    
    if(remote_order_update_pub_topic in rocon_interactions.remappings)
    	remote_order_update_pub_topic = rocon_interactions.remappings[remote_order_update_pub_topic];
    */
    var defaultUrL = "ws://localhost:9090"

    var nav_div;
    var remote_nav_div;
    var orders_div;
    var remote_orders_div;
    var hero_div;

    var delive_order_client;

    $().ready(function(e){

      // setting ros callbacks()
      //showMainMenu(true);
      settingROSCallbacks();
      settingMainMenu();
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
          serverName : '/kitchen_order',
          actionName : 'simple_delivery_msgs/DeliverOrderAction'
        });

      }

      );
      ros.on('error',function(e) {
        console.log("Error!",e);
      }
      );

      ros.on('close',function() {
        console.log("Connection Close!");
      }
      );
    }

    function settingMainMenu(){
      var table_num = 3
      for (var i = 1; i < table_num+1; i++) {
        $('.sd-main-menu').append('<button type="button" class="btn btn-primary btn-lg btn-block sd-table-' + i + '">Table ' + i + '</button>')  
        $('.sd-table-'+i).click(function(data){
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
    }

    function processRemoteOrderUpdate(msg){
    	$('.'+msg.name).innerHTML = "<b>Name: </b>" + msg.name +
	       "<br/><b>Estimated Time: </b>" + msg.estimated_arrival+" min." +  
	       "<br/><b>Status : </b>" + STATUS_STRING[msg.status];
    }
    
    function processRemoteOrderList(msg) {
    	var i;
    	remote_nav_div.empty();
    	remote_orders_div.empty();
    	var rowdiv = document.createElement('div');
       rowdiv.className = 'row-fluid';
      
    	for(i in msg.remote_orders) {
    		// add into navigation bar
    		var navli = createRemoteOrderLi(msg.remote_orders[i]); 
    		remote_nav_div.append(navli);
    		
    		var div = createRemoteOrderDiv(msg.remote_orders[i]);
           rowdiv.appendChild(div);
    		
           if((i+1) % 3 == 0){
        	   remote_orders_div.append(rowdiv);
        	   rowdiv = document.createElement('div');
        	   rowdiv.className = 'row-fluid';
        	   var hr = document.createElement('hr');
        	   remote_orders_div.append(hr);
             }
    	}
    	remote_orders_div.append(rowdiv);

    }
    
    function createRemoteOrderLi(order){
    	order.order_id = "Remote";
    	order.table_id = "remote order";
       var li = document.createElement('li');
       var p = document.createElement('p');
       p.className = order.name
       p.innerHTML = "<b>Name: </b>" + order.name +
				       "<br/><b>Estimated Time: </b>" + order.estimated_arrival+" min." +  
				       "<br/><b>Status : </b>" + STATUS_STRING[order.status];
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
    function createRemoteOrderDiv(order){
    	var div = document.createElement('div');
        div.className = "span4";
        div.style.border = "thin dotted";
        div.style.padding = "5pt";
        var h = document.createElement('h3');
        h.innerHTML = "Order : " + order.order_id;
        div.appendChild(h);

        var elements_robot= createRowLine('Name: ',order.name || "");
        div.appendChild(elements_robot);

        var elements_table = createRowLine('Extimated Time: ' ,(order.estimated_arrival || "")+ " min.");
        div.appendChild(elements_table);

        var menudiv = createMenuDiv(order.menus);
        div.appendChild(menudiv); 

        $(div).hover(
            function() { this.style.background= "gray"; },
            function() { this.style.background= "";     }
        );

        $(div).click(function() {
          hero_div.empty();
          var hero_element = createHeroDiv(order);
          hero_div.append(hero_element);

        });

        return div;
    }

    function processOrderList(msg) {
      var i;

      nav_div.empty();
      hero_div.empty();
      orders_div.empty();

      var rowdiv = document.createElement('div');
      rowdiv.className = 'row-fluid';

      // create Hero 
      var hero_element = createHeroDiv(msg.orders[0]);
      hero_div.append(hero_element);

      for(i in msg.orders) {
        // add into navigation bar
        var navli = createOrderLi(msg.orders[i]); 
        nav_div.append(navli);

        // add into order lists
        var div = createOrderDiv(msg.orders[i]);
        rowdiv.appendChild(div);

        // next row
        if((i+1) % 3 == 0)
        {
          orders_div.append(rowdiv);
          rowdiv = document.createElement('div');
          rowdiv.className = 'row-fluid';
          var hr = document.createElement('hr');
          orders_div.append(hr);
        }
      }
      orders_div.append(rowdiv);
    }

    function createHeroDiv(order)
    {
      var externaldiv = document.createElement('div');

      if(order == undefined)
      {
        externaldiv.innerHTML = "No Order";
        return externaldiv;
      }

      var h1 = document.createElement('h2');
      h1.innerHTML = "Order : " + (order.order_id || "");
      externaldiv.appendChild(h1);
      if(order.order_id === "Remote"){
    	  var elements_robot= createRowLine('Name : ',order.name || "");
    	  externaldiv.appendChild(elements_robot);
    	  var elements_title = createRow('h5','row-fluid',['Estimated Time','Status'],'span6');
    	  externaldiv.appendChild(elements_title);

    	  var elements = createRow('div','row-fluid',[(order.estimated_arrival || "")+" min.",STATUS_STRING[order.status]],'span6');
    	  externaldiv.appendChild(elements);
       }
      else{
    	  var elements_robot= createRowLine('Robot : ',order.robot_name || "");
          externaldiv.appendChild(elements_robot);

          var elements_title = createRow('h5','row-fluid',['Table','Status'],'span6');
          externaldiv.appendChild(elements_title);

          var elements = createRow('div','row-fluid',[order.table_id || "" ,STATUS_STRING[order.status]],'span6');
          externaldiv.appendChild(elements);
      }

      var menudiv = createMenuDiv(order.menus);
      externaldiv.appendChild(menudiv); 
            
      return externaldiv;
    }

    function createOrderLi(order) {
      var li = document.createElement('li');
      var p = document.createElement('p');
      p.innerHTML = "#" + order.order_id + 
      				   "<br/><b>Table : </b>" + order.table_id + 
      				   "<br/><b>Robot : </b>" + order.robot_name +  
      				   "<br/> Status : </b>" + STATUS_STRING[order.status];
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

    function createOrderDiv(order) {
      var div = document.createElement('div');
      div.className = "span4";
      div.style.border = "thin dotted";
      div.style.padding = "5pt";
      var h = document.createElement('h3');
      h.innerHTML = "Order : " + order.order_id;
      div.appendChild(h);

      var elements_robot= createRowLine('Robot : ',order.robot_name | "");
      div.appendChild(elements_robot);

      var elements_table = createRowLine('Table : ' ,order.table_id | "");
      div.appendChild(elements_table);

      var elements_status = createRowLine('Status : ',STATUS_STRING[order.status] | "");
      div.appendChild(elements_status);

      var menudiv = createMenuDiv(order.menus);
      div.appendChild(menudiv); 

      $(div).hover(
          function() { this.style.background= "gray"; },
          function() { this.style.background= "";     }
      );

      $(div).click(function() {
        hero_div.empty();
        var hero_element = createHeroDiv(order);
        hero_div.append(hero_element);

      });

      return div;
    }

    function createRowLine(name,element)
    {
      var div = createDiv('','row-fluid');
      var title = document.createElement('strong');
      title.className = 'span4';
      title.innerHTML = name; 
      div.appendChild(title);

      var el = createDiv(element,'span8');
//      el.style.marginTop = '10px';
      div.appendChild(el);

      return div;
    }


    function createMenuDiv(menus) 
    {
      var externaldiv = document.createElement('div');
      var div = createRow('h5','row-fluid',['Name','Size','Qty'],'span4');

      externaldiv.appendChild(div);

      var i;
      for(i in menus) {
        var m = menus[i]; 
        var d= createRow('div','row-fluid',[m.name,m.size,m.qty],'span4');
        
        if (m.qty === 0)continue;
        externaldiv.appendChild(d);
      }
      return externaldiv;
    }

    function createRow(rowel,rowclass,elements,elementclass)
    {
      var div = document.createElement(rowel);
      div.className = rowclass;

      var i;
      for(i in elements) { 
        var e = createDiv(elements[i],elementclass);
        div.appendChild(e);
      }
      return div;
    }
    
    function createDiv(text,elementclass) {
      var div = document.createElement('div'); 
      div.className = elementclass;
      div.innerHTML = text;

      return div;
    }
