
define(["dojo/_base/declare",
        "dojo/_base/lang",
        "dojo/dom-class",
        "dojo/dom-style",
        "dijit/_WidgetBase",
        "mjpegcanvasjs/mjpegcanvas",
        ],
function(declare,lang,domClass,domStyle,_widgetbase,MjpegCanvas)
{
    var MjpegViewer = declare("rosdojo.widgets.MjpegViewer2",[_widgetbase], {

        topic : null,
        url: null,
        port : 8080,
        quality : 100,
        width: 320,
        height: 240,

        postCreate : function() {
            domClass.add(this.domNode,'mjpegviewer');            
            domStyle.set(this.domNode,"width",this.width+"px");
            domStyle.set(this.domNode,"height",this.height+"px");
        },

        startup : function() {
          this.createStream(url);
        },

        createStream : function(url) {
          var img = document.createElement('img');
          img.src = "http://" + url + ":" + this.port + "/stream?topic=" + this.topic + "?width="+this.width+"?height="+this.height+"?quality="+this.quality;
          img.style.width = this.width + "px";
          img.style.height = this.height + "px";
          this.domNode.appendChild(img);
          this.img = img;

        },

        removeImg : function() {
          this.domNode.innerHTML="";
        },

    });

    return MjpegViewer;
}
);
