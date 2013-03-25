
define(["dojo/_base/declare",
        "dojo/_base/lang",
        "dijit/_WidgetBase",
        "dojo/dom",
        "dojo/dom-class",
        "./nav2d",
        "rosdojo/utils/Loader",
       ],
function(declare,lang,widgetbase,dom,domClass,Nav2D,Loader)
{
  var navCanvas = declare("rosdojo.navigation.NavigationCanvas",[widgetbase],
    {
      canvasid  : null,
      canvaswidth : 640,
      canvasheight : 480,
      continuous : false,
      image : null,
      serverName : '/move_base',
      mapTopic : '/map',
      mapMetaTopic : '/map_metadata',
      initialPoseTopic : '/initialpose',
      roboticon : null,

      postCreate : function() {
        Loader.loadCSS("rosdojo/navigation/css/navcanvas.css");
        ros.on('connection',lang.hitch(this,this.onConnect));
        ros.on('close',lang.hitch(this,this.onClose));

        // setting canvas
        this.createCanvas();
        domClass.add(this.canvas,"navigation-canvas");

        if(this.roboticon != null) {
          this.robotimg = new Image();
          this.robotimg.src = this.roboticon;
          this.robotsize = 25;
          this.robotinc = -1;
        }
      },

      onConnect : function() {
        if(this.nav2d == null)
          this.createNav2D();
      },

      onClose : function() {
//        delete this.nav2d;
      },

      startup : function() {
      },

      createCanvas : function() {
        this.canvas = document.createElement('canvas');
        this.canvas.id = this.canvasid || this.id+"_canvas";
        this.canvas.width="400";//+this.canvaswidth;
        this.canvas.height="200";//+this.canvasheight;
        this.domNode.appendChild(this.canvas);
        console.log(this.canvas.clientWidth);
        console.log(this.canvas.clientHeight);
      },

      createNav2D : function() {
        this.nav2d = new Nav2D({
          ros:ros,
          canvasID:this.canvas.id,
//          width : this.canvas.width,
//          height : this.canvas.height,
          continuous : this.continuous,
          image : this.image,
          mapTopic : this.mapTopic,
          mapMetaTopic : this.mapMetaTopic,
          initialPoseTopic : this.initialPoseTopic,
          serverName : this.serverName,
//          drawrobot : lang.hitch(this,this.drawrobot),
        });
      },

      initPoseClicked : function() {
        this.nav2d.setmode('init');
      },

      setGoalClicked : function() {
        this.nav2d.setmode('goal');
      },

      cancelGoalClicked : function() {
        this.nav2d.cancel();
      },

      setHeight : function(width,height) {
        this.resize(width,height);
      },

      resize : function(width,height) {
        this.canvas.width=width;
        this.canvas.height=height;
        this.newwidth = width;
        this.newheight = height;
      },

      drawrobot : function(context,robotX,robotY,robotRotZ) {
        if(this.roboticon) {
          context.save();
          context.translate(robotX,robotY);
          context.rotate(robotRotZ);
          context.drawImage(this.robotimg,0,0,this.robotsize,this.robotsize);

          if(this.robotsize >= 30) 
            this.robotinc = -0.1;
          else if(this.robotsize <= 25)
            this.robotinc = 0.1;
          
          this.robotsize += this.robotinc;
          context.restore();
          
        }
        else {
          context.beginPath();
          context.arc(robotX,robotY,10,0,Math.PI * 2, true);
          context.closePath();
          context.fill();
        }
      },

    });

  return navCanvas;
}
);
