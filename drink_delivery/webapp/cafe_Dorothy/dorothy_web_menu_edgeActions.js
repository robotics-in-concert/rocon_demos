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
			
			for (var i in ordered_coffee_list) {
			 console.log(ordered_coffee_list[i]);
			 stage_symbol.$("coffee_sel"+i).show();
			 stage_symbol.$("coffee_sel"+i).html(ordered_coffee_list[i]);
			 
			}
		}
		
      Symbol.bindElementAction(compId, symbolName, "${_Group4}", "click", function(sym, e) {
         // Show an Element.
         //  (sym.$("name") resolves an Edge Animate element name to a DOM
         //  element that can be used with jQuery)
         //sym.$("espresso2").show();
         addCoffeeOrder("Espresso");
        

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_fron_blue}", "click", function(sym, e) {
         sym.play();
         

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_back_blue}", "click", function(sym, e) {
         sym.play();

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
          
          //var ordered_coffee_list = sym.getVariable("ordered_coffee_list");
          
          //ordered_coffee_list[0] = "americano";
          //ordered_coffee_list[1] = "cafelatte";
      	
          //console.log(sym.getVariable("ordered_coffee_list"));
          //console.log(ordered_coffee_list);
          
          //sym.setVariable("addCoffeeOrder", function addCoffeeOrder(){
//  				console.log("addCoffeeOrder function is called");
  //        });

      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_Group3}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Espresso Conpanna");
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_Group2}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Cafe Americano");
      });
      //Edge binding end

      Symbol.bindElementAction(compId, symbolName, "${_Group}", "click", function(sym, e) {
         // insert code for mouse click here
         addCoffeeOrder("Cafe Latte");
      });
      //Edge binding end

		function delCoffeeOrder(number){
  			var stage_symbol = Edge.getComposition(compId).getSymbols(symbolName)[0];
  			stage_symbol.$("coffee_sel0").hide();
         stage_symbol.$("coffee_sel1").hide();
         stage_symbol.$("coffee_sel2").hide();
         stage_symbol.$("coffee_sel3").hide();
         stage_symbol.$("coffee_sel4").hide();
         stage_symbol.$("coffee_sel5").hide();
         stage_symbol.$("coffee_sel6").hide();
         stage_symbol.$("coffee_sel7").hide();
			var ordered_coffee_list = stage_symbol.getVariable("ordered_coffee_list");
			console.log("number is "+number);
			ordered_coffee_list.splice(number,1);
			console.log(ordered_coffee_list);

			for (var i in ordered_coffee_list) {
			 console.log(ordered_coffee_list[i]);
			 stage_symbol.$("coffee_sel"+i).show();
			 stage_symbol.$("coffee_sel"+i).html(ordered_coffee_list[i]);
			}
		}
		
      Symbol.bindElementAction(compId, symbolName, "${_coffee_sel0}", "click", function(sym, e) {
         // insert code for mouse click here
         delCoffeeOrder(0);
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

   })("stage");
   //Edge symbol end:'stage'

})(jQuery, AdobeEdge, "EDGE-1251484");