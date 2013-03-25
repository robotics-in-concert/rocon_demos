
define(["dojo/_base/declare",
        "dijit/_WidgetBase",
        "dijit/form/Button",
        "dojo/on",
        ],
function(declare,widgetbase,Button,on)
{
    var navc = declare("rosdojo.navigation.NavigationControl",[widgetbase],
        { 
            postCreate : function() {
                this.initButton = new Button({label:"Init Pose"});
                this.setGoalButton = new Button({label:"Set Goal"});
                this.cancelGoalButton = new Button({label:"Cancel Goal"});


                this.domNode.appendChild(this.initButton.domNode);
                this.addNewLine();
                this.domNode.appendChild(this.setGoalButton.domNode);
                this.addNewLine();
                this.domNode.appendChild(this.cancelGoalButton.domNode);
                dojo.connect(this.initButton,"onClick",this,"initPoseClicked");
                dojo.connect(this.setGoalButton,"onClick",this,"setGoalClicked");
                dojo.connect(this.cancelGoalButton,"onClick",this,"cancelGoalClicked");
            },

            addNewLine : function() 
            {
                var br = document.createElement('br');
                this.domNode.appendChild(br);
            },

            initPoseClicked : function(e){},
            setGoalClicked : function(e) {},
            cancelGoalClicked : function(e) {},
        });
    return navc;
}
);
