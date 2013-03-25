
define(["dojo/_base/declare",
        "dojo/_base/lang",
        "dijit/_WidgetBase",
        "dijit/_TemplatedMixin",
        "dojo/dom",
        "dojo/dom-class",
        "dojo/text!./templates/Arrows.html",
        ],
function(declare, lang,widgetbase,_TemplatedMixin,dom,domClass,template)
{
    var ctrl = declare("rosdojo.controller.Arrows",[widgetbase, _TemplatedMixin], {
            templateString : template,

            linear : null,
            angular : null,
            buttons : null,
            topic : '/cmd_vel',
            messageType : '/geometry_msgs/Twist',

            postCreate : function() {
                ros.on('connection',lang.hitch(this,this.onConnect));
                ros.on('close',lang.hitch(this,this.onClose));

                this.publisher = new ros.Topic({
                    name : this.topic,
                    messageType : this.messageType,
                });
                this.msg = new ros.Message({ angular : this.angular, linear : this.linear});

                // Set the default linear and angular variables
        	    this.reset();
	    
        	    // Create the controls
        		this.createButtons();
                
            },

            onConnect : function() {
        		for (var i = 0; i < this.buttons.length; i++) {
		        	this.buttons[i].set('disabled',false);
        		}
                this.pubTimer = window.setInterval(lang.hitch(this,this.pub),500);

              this.connect(window,"keydown","onKeyDown");
              this.connect(window,"keyup","onKeyUp");

            },

            onClose : function() {
        		for (var i = 0; i < this.buttons.length; i++) {
		        	this.buttons[i].set('disabled',true);
        		}
                window.clearInterval(this.pubTimer);

              this.disconnect(window,"keydown","onKeyDown");
              this.disconnect(window,"keyup","onKeyUp");

            },

            createButtons : function() {
            	this.buttons = [];
            	
            	// Create buttons for the rest of the controls
            	this.buttons.push(this.createButton(this.forwardAttach, "Forward", 38));
            	this.buttons.push(this.createButton(this.reverseAttach, "Reverse", 40));
            	this.buttons.push(this.createButton(this.turnleftAttach, "Turn Left", 37));
            	this.buttons.push(this.createButton(this.turnrightAttach, "Turn Right", 39));

        		  for (var i = 0; i < this.buttons.length; i++) {
		        	  this.buttons[i].set('disabled',true);
          		}



            },

            createButton: function(attachPoint, label, keyCode) {                                   
            	var button = new dijit.form.Button({ label: label, disabled: true }, attachPoint);
            	var pressed = dojo.hitch(this, "onMouseDown", keyCode);
            	var unpressed = dojo.hitch(this, "onMouseUp", keyCode);
            	this.connect(button, "onMouseDown", pressed);
            	this.connect(button, "onMouseUp", unpressed);
            	this.connect(button.domNode, "touchstart", pressed); /* for ipad */
            	this.connect(button.domNode, "touchend", unpressed); /* for ipad */
            	return button;
            },


            reset: function() {
                this.linear = { x: 0, y: 0, z: 0 };
                this.angular = { x: 0, y: 0, z: 0 };
            },


            onKeyDown : function(event) { this.movePressed(event.keyCode); },
            onKeyUp : function(event) { this.moveUnPressed(event.keyCode); },
            onMouseDown: function(keycode, event) { this.movePressed(keycode); event.preventDefault(); },
            onMouseUp: function(keycode, event) { this.moveUnPressed(keycode); event.preventDefault(); },
            movePressed: function(keyCode, evt) {
            	this.handleKey(keyCode);
            	this.pub();
            },
            
            moveUnPressed: function(keyCode, evt) {
            	this.reset();
            	this.pub();
            },
            handleKey: function(keyCode) {
            	switch (keyCode) {
            		case 37: /* left */ this.angular.z = 1; break;
            		case 39: /* right */ this.angular.z = -1; break;
            		case 38: /* up */ this.linear.x = .25; break;
            		case 40: /* down */ this.linear.x = -.25; break;
            	}
            },

            pub: function() {
                this.msg.angular = this.angular;
                this.msg.linear = this.linear;
                this.publisher.publish(this.msg);
            },

        });

    return ctrl;
});
