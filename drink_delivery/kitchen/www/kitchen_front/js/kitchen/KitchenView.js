/* 
   Jihoon Lee
    Date : 10.04.2012
 */

define(["dojo/_base/declare",
        "dojo/_base/lang",
        "dijit/_WidgetBase",
        "dojo/dom-style",
        "dojo/on",
        "dojox/grid/DataGrid",
        "dojo/data/ItemFileWriteStore",
        "dijit/form/Button",
        "rosdojo/utils/Loader",
        "dijit/Tooltip",
        ],
function(declare,lang,widgetbase,domStyle,on,DataGrid,Store,Button,Loader,Tooltip)
{
    var KitchenView = declare("kitchen.KitchenView",[widgetbase],
        {

            list_task_topic : '/list_tasks',
            list_task_type  : 'demo_msgs/ListTasks',


            current_tasks : {},

            postCreate : function() {
                Loader.loadCSS("dojox/grid/resources/Grid.css");
                Loader.loadCSS("dojox/grid/resources/claroGrid.css");

                this.updateTopic = new ros.Topic({
                    name : this.list_task_topic,
                    messageType : this.list_task_type,
                    });
        
                this.createDataGrid();
//                this.createButton();

                ros.on('error',function(e) { console.log(e);});
                ros.on('connection',lang.hitch(this,this.onConnect)); 
                ros.on('close',lang.hitch(this,this.onClose));
            },

            onConnect : function() {
//                this.updateAppList();
//                this.intervalInt = window.setInterval(lang.hitch(this,this.updateAppList),1000);
                this.updateTopic.subscribe(lang.hitch(this,this.updateTask));
//                this.updateTaskList();
            },

            onClose : function() {
//                window.clearInterval(this.intervalInt);
                var data = this.createData([]);
                this.currentStore.close();
                this.currentStore = new Store({data:data});
                this.grid.setStore(this.currentStore);
            },

            onClick : function(e) {
                e.selectedObject = this.current_app_list[e.rowIndex];
            },

            createDataGrid : function() {
                var data = this.createData([]); 

                var that = this;
                var layout = [ 
                               {name : "Name", field : "name",width:'70px'},
                               {name : "Status", field : "status",width:'70px'},
                             ];

                
                this.currentStore = new Store({data:data}); 

                this.grid = new DataGrid({
                    id: 'grid',
                    store : this.currentStore,
                    structure :layout,
                    rowSelector : '20px'
                    });
                domStyle.set(this.grid.domNode,"height","300px");
                domStyle.set(this.grid.domNode,"width","95%");
                domStyle.set(this.domNode,"margin","10px");

                this.domNode.appendChild(this.grid.domNode);
                this.grid.startup();
            },

            createButton : function() {
                this.button = new Button({label:"Get App lists"});
                this.connect(this.button,"onClick","updateAppList");
                this.domNode.appendChild(this.button.domNode);
            },

            updateTask : function(msg) {
                var data = this.createData(msg.tasks);
                this.currentStore.close();
                this.currentStore = new Store({data:data});
                this.grid.setStore(this.currentStore);
            },

            createData : function(tasks) {
                var data = {
                    identifier : 'name',
                    items : [],
                };

                for( n in tasks) { 
                    var t = tasks[n];
                    var i = { 
                              name : t.task_id,
                              status : t.status,
                            };
                    data.items.push(i);
                }
                this.current_app_list = tasks;
                return data;
            },
        });
    return KitchenView;
}
);
