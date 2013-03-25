
define(["dojo/_base/declare",
        "dijit/_WidgetBase",
        "dijit/form/DropDownButton",
        "dijit/DropDownMenu",
        "dijit/MenuItem",
        "dojo/on",
        "./NavigationControl",
        ],
function(declare,widgetbase,DropDownButton,DropDownMenu,MenuItem,TooltipDialog,on,NavControl)
{
    var popup = declare("rosdojo.navigation.NavigationPopup",[widgetbase],
        {
            postCreate : function()
            {
//                this.navControl = new NavControl({});
                var menu = new DropDownMenu({});
                var initMenu = new MenuItem({label: "Init Pose"});
                var setGoalMenu = new MenuItem({label: "Set Goal"});
                var cancelMenu = new MenuItem({label: "Cancel Goal"});
                menu.addChild(initMenu);
                menu.addChild(setGoalMenu);
                menu.addChild(cancelMenu);
                
                dojo.connect(initMenu,"onClick",this,"initPoseClicked");
                dojo.connect(setGoalMenu,"onClick",this,"setGoalClicked");
                dojo.connect(cancelMenu,"onClick",this,"cancelGoalClicked");

                var button = new DropDownButton({
                    label : "Open",
                    dropDown : menu,
                    });

                this.domNode.appendChild(button.domNode);

            },

            createPopupButton : function(content) 
            {
                this.popupButton = new DropDownButton({disable:false,dropDownPosition:["below","before"]});
                var dialog = new TooltipDialog({});
                this.navControl = new NavControl({});
                dialog.attr('content',content);
                this.popupButton.attr('dropDown',dialog);
                this.domNode.appendChild(this.popupButton.domNode);
            },

            initPoseClicked : function(e){},
            setGoalClicked : function(e) {},
            cancelGoalClicked : function(e) {},

        });
        return popup;
});
