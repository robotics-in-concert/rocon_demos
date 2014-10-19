var config_mode = 0;

function initConfig(configs){
    $('.oa-ui-connection-info').click(function(){

        config_mode += 1;
        if (config_mode > 2){
            config_mode = 0;
        }
        doConfig(config_mode);

    });
    $(".config-layer").hide();
    doConfig(config_mode);
    settingConfigValue(configs);
}

function settingConfigValue(configs){  
    context = '';
    for (value in configs){
        
        context += '<div class="input-prepend"><span class="add-on span1">'+value+'</span>'
        context += '<input class="span1 config-'+value+'" id="prependedInput" type="text" value="'+configs[value]+'">'
        context += '</div>'
    }
    context += '<button class="span2 btn btn-primary save-config-values" type="button">Save</button>';
    $(".config-layer").append(context);

    $(".save-config-values").click(function(){
        for (value in configs){
            configs[value] = $(".config-"+value).val();
        }
    });
}

function doConfig(mode){
    if (mode == 0 ){
        $(".oa-ui-connection-info").css('opacity',.0);
        $(".config-layer").hide("slide");
    }
    else if(mode == 1){
        $(".oa-ui-connection-info").css('opacity',.8);
        $(".config-layer").hide();
    }
    else{
        $(".config-layer").show("slide");
    }
}