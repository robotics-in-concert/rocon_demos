var dummy_green_button_publisher = "";
function initDummyGreenButton(option){
	var _ros = option.ros;
	console.log(_ros);
	var _green_button_pub_topic_type = option.topic_type;
	var _green_button_pub_topic_name = option.topic_name;	
 	dummy_green_button_publisher = new ROSLIB.Topic({
      	ros : _ros,
      	name : _green_button_pub_topic_name,
      	messageType: _green_button_pub_topic_type
    });
};

function pubDummyGreenButtonPressingSignal(){
	 console.log("pubDummyGreenButtonPressingSignal");
	 var signal = new ROSLIB.Message({
		  	values: [false, true, false, false],
		  });
	 if(dummy_green_button_publisher !== ''){
	 	dummy_green_button_publisher.publish(signal);
	 	console.log("pressing publish");
	 	setTimeout(pubDummyGreenButtonReleasingSignal, 500);
	 }
	 else{
	 	console.log("un publish");
	 }
	 
};

function pubDummyGreenButtonReleasingSignal(){
	 var signal = new ROSLIB.Message({
		  values: [true, true, false, false],
		  });
	 if(dummy_green_button_publisher !== ''){
	 	dummy_green_button_publisher.publish(signal);
	 	console.log("release publish");
	 }
	 else{
	 	console.log("release  un publish");
	 }
};