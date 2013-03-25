
define(["dojo/_base/declare",
        "dojo/_base/lang",
        "dijit/_WidgetBase",
        "dijit/form/Button",
        "dojo/on",
        "./NavigationControl",
        ],
function(declare,lang,widgetbase,Button,on,NavControl)
{
    var popup = declare("rosdojo.navigation.NavigationPopup",[widgetbase],
        {
            postCreate : function()
            {
                ros.on('connection',lang.hitch(this,this.onConnect));
                ros.on('close',lang.hitch(this,this.onClose));
                this.createButtons(); 
                
                dojo.connect(this.initButton,"onClick",this,"initPoseClicked");
                dojo.connect(this.goalButton,"onClick",this,"setGoalClicked");
                dojo.connect(this.cancelButton,"onClick",this,"cancelGoalClicked");

                this.initButton.set('disabled',true);
                this.goalButton.set('disabled',true);
                this.cancelButton.set('disabled',true);

                this.domNode.appendChild(this.initButton.domNode);
                this.domNode.appendChild(this.goalButton.domNode);
                this.domNode.appendChild(this.cancelButton.domNode);
            },

            onConnect : function() {
                this.initButton.set('disabled',false);
                this.goalButton.set('disabled',false);
                this.cancelButton.set('disabled',false);
            },

            onClose : function() {
                this.initButton.set('disabled',true);
                this.goalButton.set('disabled',true);
                this.cancelButton.set('disabled',true);
            },

            createButtons : function() 
            {
                this.initButton = new Button({ label:'Init Pose'});
                this.goalButton = new Button({label:'Set Goal'});
                this.cancelButton = new Button({label:'Cancel Goal'});
            },

            initPoseClicked : function(e){},
            setGoalClicked : function(e) {},
            cancelGoalClicked : function(e) {},

        });
        return popup;
});
