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
					stage_symbol.$("coffee_sel"+i.toString(10)).show();
					sum_prices += 2300;

				}
				else if(ordered_coffee_list[i] == "Cafe Latte")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/cafelatte.png");
					stage_symbol.$("coffee_sel"+i.toString(10)).show();
					sum_prices += 2700;
				}
				else if(ordered_coffee_list[i] == "Cafe Americano")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/americano.png");
					stage_symbol.$("coffee_sel"+i.toString(10)).show();
					sum_prices += 2500;
				}
				else if(ordered_coffee_list[i] == "Espresso Conpanna")
				{
					stage_symbol.$("coffee_sel"+i.toString(10)).attr("src","images/espresso conpanna.png");
					stage_symbol.$("coffee_sel"+i.toString(10)).show();
					sum_prices += 2500;
				}
				stage_symbol.$("coffee_sel_name"+i.toString(10)).show();
				stage_symbol.$("coffee_sel_name"+i.toString(10)).html(ordered_coffee_list[i]);
			}
			var pricewithcomma = "₩ " + sum_prices.toString(10).replace(/(\d)(?=(?:\d{3})+(?!\d))/g,'$1,'); 
			stage_symbol.$("Price").html(pricewithcomma);
		}
		
		function delCoffeeOrder(number){
			console.log("delCoffeeOrder");
  			var stage_symbol = Edge.getComposition(compId).getSymbols(symbolName)[0];
  			stage_symbol.$("coffee_sel0").hide();
         stage_symbol.$("coffee_sel1").hide();
         stage_symbol.$("coffee_sel2").hide();
         stage_symbol.$("coffee_sel3").hide();
         stage_symbol.$("coffee_sel4").hide();
         stage_symbol.$("coffee_sel5").hide();
         stage_symbol.$("coffee_sel6").hide();
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
	
      Symbol.bindElementAction(compId, symbolName, "${_P1M1}", "click", function(sym, e) {
         addCoffeeOrder("Espresso");
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_fron_blue}", "click", function(sym, e) {
         sym.play();
         

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
			  return qs[key] == undefined ? null : qs[key];
			}
			//console.log("mode");
			sym.$("_01").html(getParam("mode"));
			//open new window
			//window.open("http://m.naver.com", "_self");

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

   })("stage");
   //Edge symbol end:'stage'

})(jQuery, AdobeEdge, "EDGE-1251484");