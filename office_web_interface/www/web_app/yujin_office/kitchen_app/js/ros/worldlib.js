/**
 * Author: Russell Toris
 * Version: February 22, 2013
 */

var Worldlib = function(options) {
  var worldlib = this;
  options = options || {};
  worldlib.ros = options.ros;
  worldlib.clientIP = options.clientIP;
  worldlib.user = options.user || 'anonymous';

  // get the client's IP address if it was not given
  if (!worldlib.clientIP) {
    var request = new XMLHttpRequest();
    request.onreadystatechange = function() {
      if (request.readyState == 4 && request.status == 200) {
        var json = JSON.parse(request.responseText);
        worldlib.clientIP = json.ip;
      }
    };
    request.open('GET', 'http://jsonip.com/', true);
    request.send();
  }

  // actionlib is used to communicate with the world_model
  var cwoi = new ROSLIB.ActionClient({
    ros : worldlib.ros,
    serverName : '/spatial_world_model/create_world_object_instance',
    actionName : 'worldlib/CreateWorldObjectInstanceAction'
  });
  var uwoi = new ROSLIB.ActionClient({
    ros : worldlib.ros,
    serverName : '/spatial_world_model/update_world_object_instance',
    actionName : 'worldlib/UpdateWorldObjectInstanceAction'
  });
  var woits = new ROSLIB.ActionClient({
    ros : worldlib.ros,
    serverName : '/spatial_world_model/world_object_instance_tag_search',
    actionName : 'worldlib/WorldObjectInstanceTagSearchAction'
  });
  var cwod = new ROSLIB.ActionClient({
    ros : worldlib.ros,
    serverName : '/spatial_world_model/create_world_object_description',
    actionName : 'worldlib/CreateWorldObjectDescriptionAction'
  });
  var gwod = new ROSLIB.ActionClient({
    ros : worldlib.ros,
    serverName : '/spatial_world_model/get_world_object_description',
    actionName : 'worldlib/GetWorldObjectDescriptionAction'
  });

  // insert a new instance into the world model
  worldlib.createWorldObjectInstance = function(instance, callback) {
    // create the insertion goal
    var goal = new ROSLIB.Goal({
      actionClient : cwoi,
      goalMessage : {
        instance : instance
      } 
    });
    // define the callback
    goal.on('result', function(result) {
      callback(result.instance_id);
    });
    // send the insertion
    goal.send();
  };

  // search for all instances with the given array of tags
  worldlib.worldObjectInstanceTagSearch = function(tags, callback) {
    // create the search goal
    var goal = new ROSLIB.Goal({
      actionClient : woits,
      goalMessage : {
        tags : tags
      }
    });
    // define the callback
    goal.on('result', function(result) {
      callback(result.instances);
    });
    // send the search
    goal.send();
  };

  // get the WorldObjectDescription associated with the given ID
  worldlib.getWorldObjectDescription = function(descriptionId, callback) {
    // create the search goal
    var goal = new ROSLIB.Goal({
      actionClient : gwod,
      goalMessage : {
        description_id : descriptionId
      }
    });
    // define the callback
    goal.on('result', function(result) {
      callback(result.description);
    });
    // send the search
    goal.send();
  };
  
  //insert a new description into the world model
  worldlib.createWorldObjectDescription = function(description, callback) {
    // create the insertion goal
    var goal = new ROSLIB.Goal({
      actionClient : cwod, 
      goalMessage : {
        description : description
      }
    });
    // define the callback
    goal.on('result', function(result) {
      callback(result.description_id);
    });
    // send the insertion
    goal.send();
  };
};
