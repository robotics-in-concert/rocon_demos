/*
   Originally developed by Jonathan Mace(http://brown-ros-pkg.googlecode.com/svn/trunk/experimental/ROSDojo)
   Converted by Jihoon Lee

   Date : Sep 27 2012
 */

require({ packages: [
            { name : "rosdojo", location:"rosdojo"},
            { name : "rosjs", location:"robotwebtools_amd/rosjs"}
            ]
        });

define(["dojo","dojo/_base/declare","dojo/_base/lang","dijit/_WidgetBase","dijit/_TemplatedMixin","dojo/cookie",
        "dojo/text","dijit/form/ComboBox","dijit/form/Button","dijit/Tooltip", "rosdojo/utils/Loader","rosjs/ros","dojo/text!./templates/ConnectionPanel.html"],
function(dojo,declare,lang,_Widget,_TemplatedMixin,cookie,cache,ComboBox,Button,Tooltip,Loader,ROS,template)
{
    var ConnectionPanel =  declare("rosdojo.widgets.ConnectionPanel",[_Widget, _TemplatedMixin], {
    
        templateString : template,
    
        defaultUrls: [ "localhost:9090" ], /* set this to a list of urls that you want to show up by default*/
    
    postCreate : function() {
        if(window.ros == undefined || window.ros == null) {
            window.ros = new ROS();
        }

//        var cssfile = dojo.moduleUrl("rosdojo.widgets","css/roswidgets.css");
        Loader.loadCSS("rosdojo/widgets/css/roswidgets.css");

        // Create the constituent dijit widgets
        var instructions = "Enter the URL of your rosbridge server, in the form hostname:port";
        this.urlLabel.title = instructions;
        this.dropdown = new ComboBox({ title: instructions }, this.dropdownAttach);
        this.connectButton = new Button({}, this.connectButtonAttach);
        this.disconnectButton = new Button({}, this.disconnectButtonAttach);
        
        // Populate the dropdown with previous URL values
        this.setDropdownURLs(this.loadURLs());
        
        // Hide the appropriate parts of the widget
        dojo.style(this.connectButton.domNode, "display", "");
        dojo.style(this.disconnectButton.domNode, "display", "none");
        
        // Connect events
        this.connect(this.dropdown, "onKeyDown", "dropdownKeyPressed");
        this.connect(this.connectButton, "onClick", "connectPressed");
        this.connect(this.disconnectButton, "onClick", "disconnectPressed");

        ros.on('connection',lang.hitch(this,this._onOpen));
        ros.on('close',lang.hitch(this,this._onClose));
        
        // Connect ros connection callbacks
//        this.connect(ros, "onConnecting", "_onConnect");
//        this.connect(ros, "onOpen", "_onOpen");
//        this.connect(ros, "onClose", "_onClose");
    },
    
    dropdownKeyPressed: function(e) {
        if (!this.connecting && !this.dropdown._opened && e.keyCode == dojo.keys.ENTER) {
            this.dropdown._onBlur();
            this.connectButton.onClick();
        } 
    },
    
    connectPressed : function(event) {
        if (this.dropdown.value) {
            var url = this.dropdown.value;
            var i = url.indexOf(":");
            if (i > 0) {
                var host = url.slice(0, i);
                var port = url.slice(i+1, url.length);
                
                try {
                    var connectingurl = 'ws://' + url;
                    ros.connect(connectingurl);
                    this._onConnect();
                    ros.emit('host',host);
                } catch (e) {
                    this.showTooltip(e.message);
                    return;
                }
                try {
                    this.saveURL(url);
                    this.setDropdownURLs();
                } catch (e) {
                    // Do nothing - Error thrown if the object already exists in the
                    // store
                }
            } else {
                this.showTooltip("Expecting a URL of the form <span class='italic'>hostname</span>:<span class='italic'>port</span>");
            }
        }
    },
    
    disconnectPressed : function(event) {
        ros.close();
    },
    
    onConnecting : function() {
        // Hide relevant portions of the widget
        this.dropdown.set('disabled',true);
        this.connectButton.set('disabled',true);
        this.connectButton.set('label',"Connecting...");
    },
    
    onConnected : function() {
        // Show the relevant portions of the widget
        dojo.style(this.connectButton.domNode, "display", "none");
        dojo.style(this.disconnectButton.domNode, "display", "");
        
        // Show the 'connected' tooltip
        var label = "Connected to " + this.dropdown.value;
        this.showTooltip(label);
    },
    
    onDisconnected : function() {
        // Show and hide the relevant portions of the widget
        this.dropdown.set('disabled',false);
        this.connectButton.set('disabled',false);
        this.connectButton.set('label',"Connect");
        dojo.style(this.connectButton.domNode, "display", "");
        dojo.style(this.disconnectButton.domNode, "display", "none");
        
        // Show the 'disconnected' tooltip
        var label = "Disconnected from " + this.dropdown.value;
        this.showTooltip(label);
    },
    
    onUnableToConnect : function() {
        // Show and hide the relevant portions of the widget
        this.dropdown.set('disabled',false);
        this.connectButton.set('disabled',false);
        this.connectButton.set('label',"Connect");
        dojo.style(this.connectButton.domNode, "display", "");
        dojo.style(this.disconnectButton.domNode, "display", "none");
        
        // Show the 'unable to connect' tooltip
        var label = "Unable to connect to " + this.dropdown.value;
        this.showTooltip(label);
    },
    
    // Shows a tooltip for 3 seconds with the message provided
    showTooltip : function(label) {
        if (this.tooltipTimer) {
            window.clearTimeout(this.tooltipTimer);
        }
        window.setTimeout(dojo.hitch(this, this.hideTooltip), 3000);
        Tooltip.show(label,this.tooltipAttachPoint,["after","above","below","before"],false,"");
//        this.tooltip.show(this);
//        dijit.showTooltip(label, this.tooltipAttachPoint, [ "after", "above", "below", "before" ], false, "");
    },
    
    // Immediately hides any tooltip
    hideTooltip : function() {
        Tooltip.hide(this.tooltipAttachPoint);
    },
    
    saveURL : function(url) {
        var urls = this.loadURLs();
        
        // First, remove the url from the list if it's already in it
        var i = urls.indexOf(url);
        if (i >= 0) {
            urls.splice(i, 1);
        }
        
        // Then add the url to the start of the list
        urls.splice(0, 0, url);
        
        // Prune the list if it's longer than 5
        if (urls.length > 5) {
            urls.splice(urls.length - 2, 1);
        }
        
        // Finally save the url list as a cookie
        cookie("rosbridge_connection_urls", dojo.toJson(urls), {});
    },
    
    loadURLs : function() {
        var urls = dojo.fromJson(cookie("rosbridge_connection_urls"));
        if (urls == null) {
            urls = dojo.clone(this.defaultUrls);
        }
        return urls;
    },
    
    setDropdownURLs : function() {
        var urls = this.loadURLs();
        var data = [];
        for ( var i = 0, len = urls.length; i < len; i++) {
            var url = urls[i];
            data.push({
                name : url,
                id : url,
                value : url
            });
        }
        this.dropdown.store.setData(data);
        this.dropdown.set('value',urls[0]);
    },
    
    _onConnect : function() {
        this.connecting = true;
        this.onConnecting();
    },
    
    _onOpen : function() {
        this.connecting = false;
        this.onConnected();
    },
    
    _onClose : function() {
        if (this.connecting == true) {
            this.onUnableToConnect();
        } else {
            this.onDisconnected();
        }
        this.connecting = false;
    }

    });
    return ConnectionPanel;
});
