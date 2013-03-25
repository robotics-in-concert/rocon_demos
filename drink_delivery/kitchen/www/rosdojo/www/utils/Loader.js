
define(["dojo/_base/declare"],
function(declare) 
{
    var module = declare("rosdojo.utils.Loader",null,{});
    var loadCSS = function(filename) {
          //Load common CSS
           var link = document.createElement('link');
            link.rel = "stylesheet";
             link.href = require.toUrl(filename);
              document.body.appendChild(link);
        };

    module.loadCSS = loadCSS;
    return module;
}
);

