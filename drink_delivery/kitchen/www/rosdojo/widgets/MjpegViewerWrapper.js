  
define(["dojo/_base/declare", "dojo/_base/lang","dojo/dom-class","dojo/dom-style",
        "dijit/_WidgetBase","dijit/_TemplatedMixin","dojo/cookie",
        "dojo/text","dijit/form/ComboBox","dijit/form/Button","dijit/Tooltip",
        "rosdojo/utils/Loader","dojo/text!./templates/MjpegViewerWrapper.html",
        ],
function(declare,lang,domClass,domStyle,_Widget,_TemplatedMixin,cookie,cache,ComboBox,Button,Tooltip,Loader,template)
{
  var wrapper = declare("rosdojo.widgets.MjpegViewerWrapper",[_Widget,_TemplatedMixin], {
    templateString : template,
    quality : 100,
    width: 320,
    height:240,
    defaultUrls: ["http://localhost:8080/stream?topic=/camera/rgb/image_color"],

    postCreate: function() {
      Loader.loadCSS("rosdojo/widgets/css/roswidgets.css");

      domClass.add(this.domNode,"mjpegviewer");

      var instruction = "Enter the URL of mjpeg server";
        this.urlLabel.title = instruction;
      this.dropdown = new ComboBox({ title: instruction }, this.dropdownAttach);
      this.startButton = new Button({label:"Start"}, this.startAttach);
      this.stopButton = new Button({label:"Stop"}, this.stopAttach);

      // Hide the appropriate parts of the widget
      domStyle.set(this.startButton.domNode, "display", "");
      domStyle.set(this.stopButton.domNode, "display", "none");      

      // Populate the dropdown with previous URL values
      this.setDropdownURLs(this.loadURLs());

      // Connect events
      this.connect(this.dropdown, "onKeyDown", "dropdownKeyPressed");
      this.connect(this.startButton, "onClick", "startPressed");
      this.connect(this.stopButton, "onClick", "stopPressed");
                                                                           
    },


    dropdownKeyPressed: function(e) {
      if(!this.dropdown._opened && e.keyCode == dojo.keys.ENTER) {
          this.dropdown._onBlur();
      } 
    },

    startPressed : function(e) {
      if(this.dropdown.value) {
        var url = this.dropdown.value;
        this.updateView(url);
        domStyle.set(this.startButton.domNode, "display", "none");
        domStyle.set(this.stopButton.domNode, "display", "");      
      }
    },


    stopPressed : function(e) {
      this.removeImg();
      domStyle.set(this.startButton.domNode, "display", "");
      domStyle.set(this.stopButton.domNode, "display", "none");      

                  
    },

    updateView : function(url) {
      console.log("url = ",url);
      if(url) {
        this.createImg(url);
      }
    },


    createImg: function(url) {
      var ctr = document.createElement('center');
      var img = document.createElement('img');

      this.img = img;
      img.src = url;//"http://" + url + ":" + this.port + "/stream?topic=" + this.topic + "?width="+this.width+"?height="+this.height+"?quality="+this.quality;
      img.style.width = this.width+"px";
      img.style.height = this.height+"px";
      ctr.appendChild(img);
      this.domNode.appendChild(ctr);
      this.ctr = ctr;
    },  
      
    removeImg: function() {
      this.domNode.removeChild(this.ctr);
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
      cookie("mjpegserver_urls", dojo.toJson(urls), {});
    },  

    loadURLs : function() {
      var urls = dojo.fromJson(dojo.cookie("mjpegserver_urls"));

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

    });
  return wrapper;
});
  
