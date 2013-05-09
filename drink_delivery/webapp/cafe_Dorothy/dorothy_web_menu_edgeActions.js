/***********************
* Adobe Edge Animate Composition Actions
*
* Edit this file with caution, being careful to preserve 
* function signatures and comments starting with 'Edge' to maintain the 
* ability to interact with these actions from within Adobe Edge Animate
*
***********************/
(function($, Edge, compId){
var Composition = Edge.Composition, Symbol = Edge.Symbol; // aliases for commonly used Edge classes
	
   //Edge symbol: 'stage'
   (function(symbolName) {
      Symbol.bindTriggerAction(compId, symbolName, "Default Timeline", 0, function(sym, e) {
         sym.stop();
      });
      //Edge binding end

      

      Symbol.bindTriggerAction(compId, symbolName, "Default Timeline", 1000, function(sym, e) {
         sym.stop();

      });
      //Edge binding end
		
		//When user select coffee, push new coffee order to list and refresh coffee slot
		function addCoffeeOrder(coffeeName){
			var stage_symbol = Edge.getComposition(compId).getSymbols(symbolName)[0];
			var ordered_coffee_list = stage_symbol.getVariable("ordered_coffee_list");

			if(ordered_coffee_list.length < 7) {
				ordered_coffee_list.push(coffeeName);
			}
			console.log(ordered_coffee_list);
			updateCoffeeOrder();
		}
		
		function addSandwichOrder(sandwichName){
			var stage_symbol = Edge.getComposition(compId).getSymbols(symbolName)[0];
			var ordered_sandwich_list = stage_symbol.getVariable("ordered_sandwich_list");

			if(ordered_sandwich_list.length < 2) {
				ordered_sandwich_list.push(sandwichName);
			}
			console.log(ordered_sandwich_list);
			updateSandwichOrder();
		}
		
		function updateCoffeeOrder(){
			console.log("UpdateCoffeeOrder");
			var stage_symbol = Edge.getComposition(compId).getSymbols(symbolName)[0];
			var ordered_coffee_list = stage_symbol.getVariable("ordered_coffee_list");
			var sum_prices = 0;

			for (var i in ordered_coffee_list) {
				console.log("coffee_sel_name"+i.toString(10)+" "+ordered_coffee_list[i]);
				if(ordered_coffee_list[i] == "Espresso")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/espresso.png");
					sum_prices += 2300;

				}
				else if(ordered_coffee_list[i] == "Cafe Latte")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/cafelatte.png");
					sum_prices += 2700;
				}
				else if(ordered_coffee_list[i] == "Cafe Americano")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/americano.png");
					sum_prices += 2500;
				}
				else if(ordered_coffee_list[i] == "Espresso Conpanna")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/espresso conpanna2.png");
					sum_prices += 2500;
				}
				else if(ordered_coffee_list[i] == "Cappuccino")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/cappuccino.png");
					sum_prices += 2700;
				}
				else if(ordered_coffee_list[i] == "Caramel Latte")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/cafelatte.png");
					sum_prices += 2800;
				}
				else if(ordered_coffee_list[i] == "Hazelnut Latte")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/cafelatte.png");
					sum_prices += 2800;
				}
				else if(ordered_coffee_list[i] == "Vanilla Latte")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/cafelatte.png");
					sum_prices += 3000;
				}
				else if(ordered_coffee_list[i] == "Cafe Mocha")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/cafemocha.png");
					sum_prices += 3200;
				}
				else if(ordered_coffee_list[i] == "Caramel Mocha")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/cafemocha.png");
					sum_prices += 3200;
				}
				else if(ordered_coffee_list[i] == "White Mocha")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/cafemocha.png");
					sum_prices += 3200;
				}
				stage_symbol.$("coffee_sel_name"+i.toString(10)).show();
				stage_symbol.$("coffee_sel_name"+i.toString(10)).html(ordered_coffee_list[i]);
			}
			stage_symbol.setVariable("sum_coffee_price",sum_prices);
			updatePrice();
		}
		
		function updateSandwichOrder(){
			var stage_symbol = Edge.getComposition(compId).getSymbols(symbolName)[0];
			var ordered_sandwich_list = stage_symbol.getVariable("ordered_sandwich_list");
			var sum_prices = 0;

			for (var i in ordered_sandwich_list) {
				console.log("sandwich_name"+i.toString(10)+" "+ordered_sandwich_list[i]);
				stage_symbol.$("sandwitch_slot"+i.toString(10)).attr("src","images/sandwitch.png");
				sum_prices += 4500;
				stage_symbol.$("sandwich_sel_name"+i.toString(10)).show();
				stage_symbol.$("sandwich_sel_name"+i.toString(10)).html(ordered_sandwich_list[i]);
			}
			stage_symbol.setVariable("sum_sandwich_price",sum_prices);
			updatePrice();
		}
		
		function updatePrice(){
			var stage_symbol = Edge.getComposition(compId).getSymbols(symbolName)[0];
			var sum_coffee_price = stage_symbol.getVariable("sum_coffee_price");
			var sum_sandwich_price = stage_symbol.getVariable("sum_sandwich_price");
			console.log("sum_coffee:"+sum_coffee_price);
			console.log("sum_sandwich_price:"+sum_sandwich_price);
			var total = sum_coffee_price+sum_sandwich_price;
			var pricewithcomma = "₩ " + total.toString(10).replace(/(\d)(?=(?:\d{3})+(?!\d))/g,'$1,'); 
			stage_symbol.$("Price").html(pricewithcomma);
		}
		
		function delCoffeeOrder(number){
			console.log("delCoffeeOrder");
  			var stage_symbol = Edge.getComposition(compId).getSymbols(symbolName)[0];
  			stage_symbol.$("coffee_sel0").attr("src","images/coffee_empty2.png");
  			stage_symbol.$("coffee_sel1").attr("src","images/coffee_empty2.png");
  			stage_symbol.$("coffee_sel2").attr("src","images/coffee_empty2.png");
  			stage_symbol.$("coffee_sel3").attr("src","images/coffee_empty2.png");
  			stage_symbol.$("coffee_sel4").attr("src","images/coffee_empty2.png");
  			stage_symbol.$("coffee_sel5").attr("src","images/coffee_empty2.png");
  			stage_symbol.$("coffee_sel6").attr("src","images/coffee_empty2.png");
         stage_symbol.$("coffee_sel_name0").hide();
         stage_symbol.$("coffee_sel_name1").hide();
         stage_symbol.$("coffee_sel_name2").hide();
         stage_symbol.$("coffee_sel_name3").hide();
         stage_symbol.$("coffee_sel_name4").hide();
         stage_symbol.$("coffee_sel_name5").hide();
         stage_symbol.$("coffee_sel_name6").hide();
			var ordered_coffee_list = stage_symbol.getVariable("ordered_coffee_list");
			console.log("number is "+number);
			ordered_coffee_list.splice(number,1);
			console.log(ordered_coffee_list);

			updateCoffeeOrder()
		}
		
		function delSandwichOrder(number){
			console.log("delSandwichOrder");
  			var stage_symbol = Edge.getComposition(compId).getSymbols(symbolName)[0];
  			stage_symbol.$("sandwitch_slot0").attr("src","images/sandwitch_empty.png");
  			stage_symbol.$("sandwitch_slot1").attr("src","images/sandwitch_empty.png");
         stage_symbol.$("sandwich_sel_name0").hide();
         stage_symbol.$("sandwich_sel_name1").hide();
			var ordered_sandwich_list = stage_symbol.getVariable("ordered_sandwich_list");
			console.log("number is "+number);
			ordered_sandwich_list.splice(number,1);
			console.log(ordered_sandwich_list);

			updateSandwichOrder();
		}
	
      Symbol.bindElementAction(compId, symbolName, "${_P1M1}", "click", function(sym, e) {
         addCoffeeOrder("Espresso");
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_fron_blue}", "click", function(sym, e) {
         //previous position of timeline animation(-1)
         if(sym.getPosition() == -1) {
         	sym.play(1);
			}
         else {
         	sym.play();
         }
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_back_blue}", "click", function(sym, e) {
         sym.playReverse();

      });
      //Edge binding end

      Symbol.bindTriggerAction(compId, symbolName, "Default Timeline", 2000, function(sym, e) {
         sym.stop();

      });
      //Edge binding end

      Symbol.bindSymbolAction(compId, symbolName, "creationComplete", function(sym, e) {
        // insert code to be run when the symbol is created here
      	//reference for selected coffee list array
		   sym.setVariable("ordered_coffee_list", new Array());
		   sym.setVariable("ordered_sandwich_list", new Array());
		   sym.setVariable("sum_coffee_price", 0);
		   sym.setVariable("sum_sandwich_price", 0);

			function getParam(key){
				var url = location.href;
				var parameters = [];    
				var qs = null;
				// url has parameter's
				if ( url.indexOf("?") != -1 ){
					qs = {};
					parameters = url.substring(url.indexOf("?")+1, url.length).split("&");
					for ( var k =0; k < parameters.length; k++ ){
						if ( parameters[k].split("=")[1].split('').join('').length > 0 ){
							qs[parameters[k].split("=")[0]] = parameters[k].split("=")[1];
						}
					}
			  }
			  if (qs == null)
			  	return "";
			  else {
			  	//console.log(qs[key]);
			  	return qs[key];
			  }
			}

			var tableID = getParam("tableid");
			console.log("tableID" + tableID);
			sym.setVariable("tableID", tableID);
			sym.$("_01").html(tableID);
			var masterUri = getParam("concertaddress");
			console.log(masterUri);
			if (masterUri == "")
				masterUri = "ws://222.100.124.85:9090";
			else
				masterUri = "ws://"+masterUri+":9090";
			sym.$("status_text").html("Concert master address: "+masterUri+" version:201305091812");

			//open new window
			//window.open("http://m.naver.com", "_self");

			yepnope({
         	nope:['include/EventEmitter2/eventemitter2.js'] ,
         	complete: eventemitterLoaded
         });

         yepnope({
         	nope:['include/roslib.js'] ,
         	complete: init_ros
         });

         function eventemitterLoaded (){
         	console.log("eventemitter2.js is loaded");
         }

         function init_ros (){
         	console.log("roslib.js is loaded");
         	var ros = new ROSLIB.Ros();
         	ros.connect(masterUri);
         	sym.setVariable("ROS", ros);
				ros.on('connection',function() {
				 	console.log('Connection made!');
				 	sym.$("status_text").html("Connected with "+masterUri);
				});
				ros.on('close',function() {
				 //log.innerHTML += 'Disconnected from ' + host + ' <br/>';
				});

				ros.on('error', function(error) {
					 console.log(error);
			   });

			}

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P1M2}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Espresso Conpanna");
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P1M3}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Cafe Americano");
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P1M4}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Cafe Latte");
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_coffee_sel1}", "click", function(sym, e) {
         // insert code for mouse click here
         delCoffeeOrder(1);
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_coffee_sel2}", "click", function(sym, e) {
         // insert code for mouse click here
         delCoffeeOrder(2);
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_coffee_sel3}", "click", function(sym, e) {
         // insert code for mouse click here
         delCoffeeOrder(3);
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_coffee_sel4}", "click", function(sym, e) {
         // insert code for mouse click here
         delCoffeeOrder(4);
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_coffee_sel5}", "click", function(sym, e) {
         // insert code for mouse click here
         delCoffeeOrder(5);
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_coffee_sel6}", "click", function(sym, e) {
         // insert code for mouse click here
         delCoffeeOrder(6);
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_coffee_sel0}", "click", function(sym, e) {
         // insert code for mouse click here
         delCoffeeOrder(0);

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P1M5}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Cappuccino");
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P1M6}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Caramel Latte");

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P1M7}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Hazelnut Latte");

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P1M8}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Vanilla Latte");

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P2M1}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Cafe Mocha");

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P2M2}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Caramel Mocha");

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P2M3}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("White Mocha");

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P3M1}", "click", function(sym, e) {
         // insert code for mouse click here
         addSandwichOrder("Turkey Bacon Sandwitch");

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P3M2}", "click", function(sym, e) {
         // insert code for mouse click here
         addSandwichOrder("Cicken Sandwitch");

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P3M3}", "click", function(sym, e) {
         // insert code for mouse click here
         addSandwichOrder("Roast Beef Sandwitch");

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_P3M4}", "click", function(sym, e) {
         // insert code for mouse click here
         addSandwichOrder("Hub Tuna Sandwitch");

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_sandwitch_slot0}", "click", function(sym, e) {
         // insert code for mouse click here
         delSandwichOrder(0);

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_sandwitch_slot1}", "click", function(sym, e) {
         // insert code for mouse click here
         delSandwichOrder(1);

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_accept_blue}", "click", function(sym, e) {
// play the timeline from the given position (ms or label)
sym.play(2059);
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "document", "compositionReady", function(sym, e) {
         sym.$('Stage').css('background-image','url(images/wood_wallpaper_by_stenosis.jpg)');

      });
      //Edge binding end

      Symbol.bindTriggerAction(compId, symbolName, "Default Timeline", 3948, function(sym, e) {
         // play the timeline from the given position (ms or label)
         sym.play(3000);
         // insert code here

      });
      //Edge binding end

      Symbol.bindTriggerAction(compId, symbolName, "Default Timeline", 4950, function(sym, e) {
         // play the timeline from the given position (ms or label)
         sym.play(4000);
         // insert code here

      });
      //Edge binding end

      Symbol.bindTriggerAction(compId, symbolName, "Default Timeline", 5950, function(sym, e) {
         // play the timeline from the given position (ms or label)
         sym.play(5000);
         // insert code here

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_delete}", "click", function(sym, e) {
         // play the timeline from the given position (ms or label)
         sym.play(0000);
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_accept_blue2}", "click", function(sym, e) {
         // play the timeline from the given position (ms or label)
         sym.play(3000);
         
         var ros = sym.getVariable("ROS");
			var UserOrderClient = new ROSLIB.ActionClient({
			 ros : ros,
			 serverName : '/cafe_taskcoordinator/send_order',
			 actionName : 'cafe_msgs/UserOrderAction'
			});
			var tableID = sym.getVariable("tableID");
			var tableID_num = parseInt(tableID);

			var menus = new Array();
			var ordered_coffee_list = sym.getVariable("ordered_coffee_list");
			var ordered_sandwich_list = sym.getVariable("ordered_sandwich_list");
			for (var i in ordered_coffee_list) {
				var foundDuplicatedMenu = false;
				for (var j in menus) {
					if (ordered_coffee_list[i] == menus[j].name) {
						menus[j].qty++;
						foundDuplicatedMenu = true;
						break;
					}
				}
				if (foundDuplicatedMenu == false) {
					var menu = new ROSLIB.Message({
						name : ordered_coffee_list[i],
						size : 1,
						qty : 1
					});
					menus.push(menu);
				}
			}
			for (var i in ordered_sandwich_list) {
				var foundDuplicatedMenu = false;
				for (var j in menus) {
					if (ordered_sandwich_list[i] == menus[j].name) {
						menus[j].qty++;
						foundDuplicatedMenu = true;
						break;
					}
				}
				if (foundDuplicatedMenu == false) {
					var menu = new ROSLIB.Message({
						name : ordered_sandwich_list[i],
						size : 1,
						qty : 1
					});
					menus.push(menu);
				}
			}
			//console.log(menus);			
			var goal = new ROSLIB.Goal({
			 actionClient : UserOrderClient,
			 goalMessage : {
				order : {
				table_id : tableID_num, 
				menus : menus,
				}
			 }
			});
			// Print out their output into the terminal.
			goal.on('feedback', function(feedback) {
				//console.log('Feedback :' + feedback.status);
				if (feedback.status == 1)
					sym.$("status_text").html("Waiterbot is going to kitchen.");
				else if (feedback.status == 2) {
					sym.play(4000);
					sym.$("status_text").html("Waiterbot is arrived at kitchen.");
				}
				else if (feedback.status == 3)
					sym.$("status_text").html("Waiterbot is waiting for foods at kitchen.");
				else if (feedback.status == 4) {
					sym.play(5000);
					sym.$("status_text").html("Waiterbot is in delivery.");
				}
				else if (feedback.status == 5)
					sym.$("status_text").html("Waiterbot is arrived at the table.");
				else if (feedback.status == 6) {
					sym.$("status_text").html("Waiterbot is waiting for user confirmation.");
					sym.play(6000);
				}
				else if (feedback.status == 7) {
					sym.$("status_text").html("Delivery service is completed.");
					sym.play(0);
				}
				else
					console.log(feedback.status);
			});
			goal.on('result', function(result) {
				console.log(result);
				//console.log('Final Result: ' + result.sequence);
			});
			console.log("goal.send()");
			goal.send();
			sym.$("status_text").html("Order is received.");
// stop the timeline at the given position (ms or label)
         

      });
      //Edge binding end

      Symbol.bindTriggerAction(compId, symbolName, "Default Timeline", 2904, function(sym, e) {
         sym.stop();

      });
      //Edge binding end

      Symbol.bindTriggerAction(compId, symbolName, "Default Timeline", 3000, function(sym, e) {
         // insert code here
      });
      //Edge binding end

   })("stage");
   //Edge symbol end:'stage'

})(jQuery, AdobeEdge, "EDGE-1251484");