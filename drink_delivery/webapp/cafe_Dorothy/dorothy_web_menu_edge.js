/**
 * Adobe Edge: symbol definitions
 */
(function($, Edge, compId){
//images folder
var im='images/';

var fonts = {};


var resources = [
];
var symbols = {
"stage": {
   version: "1.5.0",
   minimumCompatibleVersion: "1.5.0",
   build: "1.5.0.217",
   baseState: "Base State",
   initialState: "Base State",
   gpuAccelerate: false,
   resizeInstances: false,
   content: {
         dom: [
         {
            id:'wood_wallpaper_by_stenosis',
            type:'image',
            rect:['0px','0px','1440px','1136px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"wood_wallpaper_by_stenosis.jpg",'0px','0px']
         },
         {
            id:'rocon_logo',
            type:'image',
            rect:['auto','auto','111.2%','25%','-33.5%','-8%'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"a4_nomal_png_c.png",'50%','50%','649.65px','auto'],
            transform:[[],[],[],['0.4','0.4']]
         },
         {
            id:'oder_management',
            type:'text',
            rect:['-14.3%','60.2%','79.9%','9.6%','auto','auto'],
            opacity:1,
            text:"ROCON Order Management system",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[500,"%"],"rgba(100,61,23,1.00)","200","none","normal"]
         },
         {
            id:'header',
            type:'rect',
            rect:['0px','0px','1440px','80px','auto','auto'],
            opacity:0.9,
            fill:["rgba(57,35,13,1.00)"],
            stroke:[0,"rgba(0,0,0,1)","none"]
         },
         {
            id:'copyright',
            type:'text',
            rect:['0.1%','97.9%','100%','2.1%','auto','auto'],
            text:"Copyright YUJIN ROBOT co., Ltd. All rights reserved including the right of reproduction in whole or in part in any form. mobile",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[70,"%"],"rgba(100,61,23,0.37)","800","none","normal"]
         },
         {
            id:'dorothy_cafe',
            type:'text',
            rect:['89px','10px','324px','59px','auto','auto'],
            text:"Dorothy..cafe",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[320,"%"],"rgba(255,255,255,1.00)","800","none","normal"]
         },
         {
            id:'_01',
            type:'text',
            rect:['auto','10px','auto','auto','32px','auto'],
            text:"01",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[320,"%"],"rgba(255,255,255,1.00)","800","none","normal"]
         },
         {
            id:'table_no',
            type:'text',
            rect:['auto','33px','auto','auto','101px','auto'],
            text:"Table no.",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[100,"%"],"rgba(255,255,255,1.00)","800","none","normal"]
         },
         {
            id:'coffee_slot2',
            type:'image',
            rect:['11.5%','69.6%','152px','102px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'50%','50%','152px','102px'],
            transform:[[],[],[],['0.5','0.5']]
         },
         {
            id:'coffee_slot3',
            type:'image',
            rect:['25.5%','69.6%','152px','102px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'50%','50%','152px','102px'],
            transform:[[],[],[],['0.5','0.5']]
         },
         {
            id:'coffee_slot4',
            type:'image',
            rect:['39.4%','69.6%','152px','102px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'50%','50%','152px','102px'],
            transform:[[],[],[],['0.5','0.5']]
         },
         {
            id:'coffee_slot5',
            type:'image',
            rect:['53.3%','69.6%','152px','102px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'50%','50%','152px','102px'],
            transform:[[],[],[],['0.5','0.5']]
         },
         {
            id:'coffee_slot6',
            type:'image',
            rect:['67.3%','69.6%','152px','102px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'50%','50%','152px','102px'],
            transform:[[],[],[],['0.5','0.5']]
         },
         {
            id:'coffee_slot1',
            type:'image',
            rect:['-21px','69.6%','152px','102px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'50%','50%','152px','102px'],
            transform:[[],[],[],['0.5','0.5']]
         },
         {
            id:'coffee_slot7',
            type:'image',
            rect:['81.2%','69.6%','152px','102px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'50%','50%','152px','102px'],
            transform:[[],[],[],['0.5','0.5']]
         },
         {
            id:'sandwitch_empty',
            type:'image',
            rect:['-77px','74.2%','322px','322px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"sandwitch_empty.png",'50%','50%','322px','322px'],
            transform:[[],[],[],['0.4','0.4']]
         },
         {
            id:'sandwitch_emptyCopy',
            type:'image',
            rect:['11.1%','74.2%','322px','322px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"sandwitch_empty.png",'50%','50%','322px','322px'],
            transform:[[],[],[],['0.4','0.4']]
         },
         {
            id:'checkout_total',
            type:'text',
            rect:['48.6%','79.7%','199px','auto','auto','auto'],
            text:"Check out Total",
            font:['Arial, Helvetica, sans-serif',25,"rgba(100,61,23,1.00)","800","none",""]
         },
         {
            id:'Price',
            type:'text',
            rect:['46.6%','85.7%','225px','auto','auto','auto'],
            text:"₩ 20,000",
            font:['Arial, Helvetica, sans-serif',50,"rgba(100,61,23,1.00)","800","none",""]
         },
         {
            id:'order',
            type:'text',
            rect:['auto','79.7%','115px','auto','13px','auto'],
            text:"Order",
            font:['Arial, Helvetica, sans-serif',25,"rgba(100,61,23,1.00)","800","none",""]
         },
         {
            id:'Group4',
            type:'group',
            rect:['20px','121','152','184','auto','auto'],
            c:[
            {
               id:'espresso',
               type:'image',
               rect:['0px','0px','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"espresso.png",'0px','0px']
            },
            {
               id:'Text',
               type:'text',
               rect:['33px','114px','auto','auto','auto','auto'],
               text:"에스프레소<br>Espresso<br>₩ 2,300",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'coffee_sel0',
            display:'none',
            type:'image',
            rect:['-18px','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"espresso.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel1',
            display:'none',
            type:'image',
            rect:['-18px','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"espresso.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel2',
            display:'none',
            type:'image',
            rect:['184px','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"espresso.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel3',
            display:'none',
            type:'image',
            rect:['284px','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"espresso.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel4',
            display:'none',
            type:'image',
            rect:['384px','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"espresso.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel5',
            display:'none',
            type:'image',
            rect:['488px','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"espresso.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel6',
            display:'none',
            type:'image',
            rect:['584px','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"espresso.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel_name0',
            type:'text',
            rect:['20px','879','69px','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name1',
            type:'text',
            rect:['124px','879px','69px','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name2',
            type:'text',
            rect:['222px','879px','69px','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name3',
            type:'text',
            rect:['324px','879px','69px','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name4',
            type:'text',
            rect:['425px','879px','69px','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name5',
            type:'text',
            rect:['526px','884px','69px','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name6',
            type:'text',
            rect:['632px','884px','69px','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'Group3',
            type:'group',
            rect:['25.1%','121px','180','184','auto','auto'],
            c:[
            {
               id:'TextCopy',
               type:'text',
               rect:['0px','114px','auto','auto','auto','auto'],
               text:"에스프레소 꼰빠냐<br>Espresso Conpanna<br>₩ 2,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'espresso_conpanna2',
               type:'image',
               rect:['14px','0px','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"espresso%20conpanna2.png",'0px','0px']
            }]
         },
         {
            id:'Group2',
            type:'group',
            rect:['51.4%','121px','150','207','auto','auto'],
            c:[
            {
               id:'TextCopy2',
               type:'text',
               rect:['4px','114px','auto','auto','auto','auto'],
               text:"카페 아메리카노<br>Cafe Americano<br>₩ 2,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'americano',
               type:'image',
               rect:['0px','0px','150px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"americano.png",'0px','0px']
            }]
         },
         {
            id:'Group',
            type:'group',
            rect:['auto','121px','152','207','3.3%','auto'],
            c:[
            {
               id:'TextCopy3',
               type:'text',
               rect:['30px','114px','auto','auto','auto','auto'],
               text:"카페 라떼<br>Cafe Latte<br>₩ 2,700",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'cafelatte',
               type:'image',
               rect:['0px','0px','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
            }]
         },
         {
            id:'Group8',
            type:'group',
            rect:['102.9%','10.7%','308','210','auto','auto'],
            c:[
            {
               id:'menu-category-sandwich-italbmt_copy',
               type:'image',
               rect:['0px','0px','308px','140px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"menu-category-sandwich-italbmt%20copy.png",'0px','0px'],
               transform:[]
            },
            {
               id:'TextCopy4',
               type:'text',
               rect:['46px','140px','217px','70px','auto','auto'],
               text:"터키 베이컨 샌드위치<br>Turkey Bacon Sandwitch<br>₩ 4,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'Group7',
            type:'group',
            rect:['151.3%','10.7%','308','211','auto','auto'],
            c:[
            {
               id:'menu-category-sandwich-buffchic_copy',
               type:'image',
               rect:['0px','0px','308px','140px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"menu-category-sandwich-buffchic%20copy.png",'0px','0px'],
               transform:[]
            },
            {
               id:'TextCopy5',
               type:'text',
               rect:['71px','141px','168px','70px','auto','auto'],
               text:"닭가슴살 샌드위치<br>Chiken Sandwitch<br>₩ 4,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'Group6',
            type:'group',
            rect:['102.9%','32.6%','308','204','auto','auto'],
            c:[
            {
               id:'menu-category-sandwich-stkchs_copy',
               type:'image',
               rect:['0px','0px','308px','140px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"menu-category-sandwich-stkchs%20copy.png",'0px','0px'],
               transform:[]
            },
            {
               id:'TextCopy7',
               type:'text',
               rect:['55px','134px','199px','70px','auto','auto'],
               text:"로스트 비프 샌드위치<br>Roast Beef Sandwitch<br>₩ 4,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'Group5',
            type:'group',
            rect:['151.3%','32.6%','308','204','auto','auto'],
            c:[
            {
               id:'menu-category-sandwich-tuna',
               type:'image',
               rect:['0px','0px','308px','140px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"menu-category-sandwich-tuna.png",'0px','0px'],
               transform:[]
            },
            {
               id:'TextCopy6',
               type:'text',
               rect:['42px','134px','226px','70px','auto','auto'],
               text:"허브참치 샌드위치<br>Heb Tuna Sandwitch<br>₩ 4,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'u616-62',
            type:'image',
            rect:['22.4%','57.6%','400px','86px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"u616-6.png",'0%','0%','100%','auto']
         },
         {
            id:'u617-62',
            type:'image',
            rect:['34.6%','57.6%','224px','85px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"u617-6.png",'0%','0%','100%','auto']
         },
         {
            id:'accept_blue',
            type:'image',
            rect:['auto','81.9%','129px','129px','24px','auto'],
            fill:["rgba(0,0,0,0)",im+"accept_blue.png",'0px','0px']
         },
         {
            id:'fron_blue',
            type:'image',
            rect:['79.7%','55.7%','129px','129px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"fron_blue.png",'0px','0px']
         },
         {
            id:'back_blue',
            type:'image',
            rect:['2.6%','55.7%','129px','129px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"back_blue.png",'0px','0px']
         },
         {
            id:'dorothy_logo012',
            type:'image',
            rect:['24px','13px','56px','55px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"dorothy_logo01.png",'0px','0px']
         }],
         symbolInstances: [

         ]
      },
   states: {
      "Base State": {
         "${_Group7}": [
            ["style", "left", '151.25%']
         ],
         "${_Group3}": [
            ["style", "left", '25.14%']
         ],
         "${_oder_management}": [
            ["style", "letter-spacing", '0em'],
            ["style", "bottom", 'auto'],
            ["color", "color", 'rgba(100,61,23,0.49)'],
            ["style", "right", 'auto'],
            ["style", "left", '-14.34%'],
            ["style", "font-size", '120%'],
            ["style", "top", '94.93%'],
            ["style", "opacity", '1'],
            ["style", "text-align", 'center'],
            ["style", "text-indent", '0%'],
            ["style", "height", '3.5%'],
            ["style", "width", '79.9%'],
            ["style", "word-spacing", '0em'],
            ["style", "font-weight", '200']
         ],
         "${_TextCopy4}": [
            ["style", "top", '140px'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "font-size", '20px'],
            ["style", "left", '46px'],
            ["style", "width", '217px']
         ],
         "${_fron_blue}": [
            ["style", "top", '55.7%'],
            ["style", "height", '129px'],
            ["style", "right", 'auto'],
            ["style", "left", '79.72%'],
            ["style", "width", '129px']
         ],
         "${_americano}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_back_blue}": [
            ["style", "height", '129px'],
            ["style", "top", '55.7%'],
            ["style", "left", '2.64%'],
            ["style", "width", '129px']
         ],
         "${_dorothy_logo012}": [
            ["style", "top", '13px'],
            ["style", "height", '55px'],
            ["style", "left", '24px'],
            ["style", "width", '56px']
         ],
         "${_Group4}": [
            ["style", "left", '20px']
         ],
         "${_order}": [
            ["style", "top", '79.67%'],
            ["style", "font-size", '25px'],
            ["style", "right", '13px'],
            ["color", "color", 'rgba(100,61,23,1.00)'],
            ["style", "font-weight", '800'],
            ["style", "left", 'auto'],
            ["style", "width", '115px']
         ],
         "${_TextCopy}": [
            ["style", "top", '114px'],
            ["style", "left", '0px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px']
         ],
         "${_coffee_sel_name3}": [
            ["style", "top", '879px'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "left", '324px'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '69px']
         ],
         "${_Group8}": [
            ["style", "left", '102.92%']
         ],
         "${_sandwitch_emptyCopy}": [
            ["style", "top", '74.18%'],
            ["transform", "scaleY", '0.4'],
            ["transform", "scaleX", '0.4'],
            ["style", "left", '11.09%'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_coffee_slot2}": [
            ["style", "top", '69.61%'],
            ["transform", "scaleY", '0.5'],
            ["transform", "scaleX", '0.5'],
            ["style", "left", '11.5%'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_coffee_sel4}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "left", '384px'],
            ["transform", "scaleX", '0.45']
         ],
         "${_coffee_sel3}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "left", '284px'],
            ["transform", "scaleX", '0.45']
         ],
         "${_coffee_slot5}": [
            ["style", "top", '69.62%'],
            ["transform", "scaleY", '0.5'],
            ["transform", "scaleX", '0.5'],
            ["style", "left", '53.31%'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_wood_wallpaper_by_stenosis}": [
            ["style", "height", '1136px'],
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_menu-category-sandwich-tuna}": [
            ["style", "top", '0px'],
            ["transform", "scaleX", '1'],
            ["transform", "scaleY", '1'],
            ["style", "left", '0px']
         ],
         "${_coffee_sel_name0}": [
            ["style", "letter-spacing", '0px'],
            ["style", "width", '69px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "word-spacing", '0px'],
            ["style", "left", '20px'],
            ["style", "font-size", '21px']
         ],
         "${__01}": [
            ["style", "top", '10px'],
            ["style", "bottom", 'auto'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "right", '32px'],
            ["style", "left", 'auto'],
            ["style", "font-size", '320%']
         ],
         "${_coffee_slot1}": [
            ["style", "top", '69.62%'],
            ["transform", "scaleY", '0.5'],
            ["transform", "scaleX", '0.5'],
            ["style", "left", '-21px'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_accept_blue}": [
            ["style", "top", '81.94%'],
            ["style", "height", '129px'],
            ["style", "right", '24px'],
            ["style", "left", 'auto'],
            ["style", "width", '129px']
         ],
         "${_coffee_sel2}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "left", '184px'],
            ["transform", "scaleX", '0.45']
         ],
         "${_Text}": [
            ["style", "top", '114px'],
            ["style", "left", '33px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px']
         ],
         "${_Stage}": [
            ["color", "background-color", 'rgba(255,255,255,1)'],
            ["style", "overflow", 'hidden'],
            ["style", "height", '100%'],
            ["style", "width", '100%']
         ],
         "${_TextCopy6}": [
            ["style", "top", '134px'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "font-size", '20px'],
            ["style", "left", '42px'],
            ["style", "width", '226px']
         ],
         "${_u617-62}": [
            ["style", "top", '57.57%'],
            ["style", "opacity", '0'],
            ["style", "left", '34.58%'],
            ["style", "background-size", [100,'auto'], {valueTemplate:'@@0@@% @@1@@'} ]
         ],
         "${_espresso}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_coffee_slot3}": [
            ["style", "top", '69.62%'],
            ["transform", "scaleY", '0.5'],
            ["transform", "scaleX", '0.5'],
            ["style", "left", '25.53%'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_copyright}": [
            ["style", "top", '97.89%'],
            ["style", "width", '100%'],
            ["color", "color", 'rgba(100,61,23,0.37)'],
            ["style", "height", '2.11%'],
            ["style", "left", '0.14%'],
            ["style", "font-size", '70%']
         ],
         "${_coffee_slot6}": [
            ["style", "top", '69.62%'],
            ["transform", "scaleY", '0.5'],
            ["transform", "scaleX", '0.5'],
            ["style", "left", '67.33%'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_Group6}": [
            ["style", "left", '102.92%']
         ],
         "${_coffee_sel6}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "left", '584px'],
            ["transform", "scaleX", '0.45']
         ],
         "${_coffee_sel0}": [
            ["style", "top", '69.81%'],
            ["transform", "scaleY", '0.45'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "left", '-18px'],
            ["transform", "scaleX", '0.45']
         ],
         "${_Group2}": [
            ["style", "left", '51.39%']
         ],
         "${_u616-62}": [
            ["style", "top", '57.55%'],
            ["style", "opacity", '1'],
            ["style", "left", '22.36%'],
            ["style", "background-size", [100,'auto'], {valueTemplate:'@@0@@% @@1@@'} ]
         ],
         "${_Group}": [
            ["style", "left", 'auto'],
            ["style", "right", '3.32%']
         ],
         "${_dorothy_cafe}": [
            ["style", "top", '10px'],
            ["style", "width", '324px'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "height", '59px'],
            ["style", "left", '89px'],
            ["style", "font-size", '320%']
         ],
         "${_TextCopy5}": [
            ["style", "top", '141px'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "width", '168px'],
            ["style", "left", '71px'],
            ["style", "font-size", '20px']
         ],
         "${_cafelatte}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_coffee_sel_name5}": [
            ["style", "top", '884px'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "left", '526px'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '69px']
         ],
         "${_coffee_sel_name4}": [
            ["style", "top", '879px'],
            ["style", "letter-spacing", '0px'],
            ["style", "width", '69px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "word-spacing", '0px'],
            ["style", "left", '425px'],
            ["style", "font-size", '21px']
         ],
         "${_coffee_slot7}": [
            ["style", "top", '69.62%'],
            ["transform", "scaleY", '0.5'],
            ["transform", "scaleX", '0.5'],
            ["style", "right", 'auto'],
            ["style", "left", '81.22%'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_TextCopy2}": [
            ["style", "top", '114px'],
            ["style", "text-align", 'center'],
            ["style", "left", '4px'],
            ["style", "font-size", '20px']
         ],
         "${_Group5}": [
            ["style", "left", '151.25%']
         ],
         "${_table_no}": [
            ["style", "top", '33px'],
            ["style", "bottom", 'auto'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "right", '101px'],
            ["style", "left", 'auto'],
            ["style", "font-size", '100%']
         ],
         "${_coffee_sel5}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "left", '488px'],
            ["transform", "scaleX", '0.45']
         ],
         "${_coffee_sel_name6}": [
            ["style", "top", '884px'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "left", '632px'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '69px']
         ],
         "${_TextCopy3}": [
            ["style", "top", '114px'],
            ["style", "left", '30px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px']
         ],
         "${_header}": [
            ["style", "top", '0px'],
            ["color", "background-color", 'rgba(57,35,13,1.00)'],
            ["style", "height", '80px'],
            ["style", "opacity", '0.9'],
            ["style", "left", '0px'],
            ["style", "width", '1440px']
         ],
         "${_sandwitch_empty}": [
            ["style", "top", '74.18%'],
            ["transform", "scaleY", '0.4'],
            ["transform", "scaleX", '0.4'],
            ["style", "left", '-77px'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_coffee_sel1}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "left", '83px'],
            ["transform", "scaleX", '0.45']
         ],
         "${_coffee_sel_name2}": [
            ["style", "top", '879px'],
            ["style", "letter-spacing", '0px'],
            ["style", "width", '69px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "word-spacing", '0px'],
            ["style", "left", '222px'],
            ["style", "font-size", '21px']
         ],
         "${_Price}": [
            ["style", "top", '85.74%'],
            ["style", "font-size", '50px'],
            ["color", "color", 'rgba(100,61,23,1.00)'],
            ["style", "font-weight", '800'],
            ["style", "left", '46.63%'],
            ["style", "width", '225px']
         ],
         "${_coffee_slot4}": [
            ["style", "top", '69.62%'],
            ["transform", "scaleY", '0.5'],
            ["transform", "scaleX", '0.5'],
            ["style", "left", '39.41%'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_espresso_conpanna2}": [
            ["style", "left", '14px'],
            ["style", "top", '0px']
         ],
         "${_checkout_total}": [
            ["style", "top", '79.66%'],
            ["style", "width", '199px'],
            ["color", "color", 'rgba(100,61,23,1.00)'],
            ["style", "font-weight", '800'],
            ["style", "left", '48.58%'],
            ["style", "font-size", '25px']
         ],
         "${_menu-category-sandwich-italbmt_copy}": [
            ["style", "top", '0px'],
            ["transform", "scaleX", '1'],
            ["transform", "scaleY", '1'],
            ["style", "left", '0px']
         ],
         "${_menu-category-sandwich-stkchs_copy}": [
            ["style", "top", '0px'],
            ["transform", "scaleX", '1'],
            ["transform", "scaleY", '1'],
            ["style", "left", '0px']
         ],
         "${_rocon_logo}": [
            ["style", "-webkit-transform-origin", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ],
            ["style", "-moz-transform-origin", [50,50],{valueTemplate:'@@0@@% @@1@@%'}],
            ["style", "-ms-transform-origin", [50,50],{valueTemplate:'@@0@@% @@1@@%'}],
            ["style", "msTransformOrigin", [50,50],{valueTemplate:'@@0@@% @@1@@%'}],
            ["style", "-o-transform-origin", [50,50],{valueTemplate:'@@0@@% @@1@@%'}],
            ["style", "bottom", '-8.04%'],
            ["transform", "scaleX", '0.4'],
            ["style", "right", '-33.47%'],
            ["style", "left", 'auto'],
            ["style", "width", '111.17%'],
            ["style", "top", 'auto'],
            ["transform", "scaleY", '0.4'],
            ["style", "height", '25%'],
            ["style", "background-size", [649.65,'auto'], {valueTemplate:'@@0@@px @@1@@'} ],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ],
            ["style", "opacity", '1']
         ],
         "${_menu-category-sandwich-buffchic_copy}": [
            ["style", "top", '0px'],
            ["transform", "scaleX", '1'],
            ["transform", "scaleY", '1'],
            ["style", "left", '0px']
         ],
         "${_TextCopy7}": [
            ["style", "top", '134px'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "width", '199px'],
            ["style", "left", '55px'],
            ["style", "font-size", '20px']
         ],
         "${_coffee_sel_name1}": [
            ["style", "top", '879px'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "left", '124px'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '69px']
         ]
      }
   },
   timelines: {
      "Default Timeline": {
         fromState: "Base State",
         toState: "",
         duration: 2000,
         autoPlay: true,
         timeline: [
            { id: "eid1800", tween: [ "style", "${_u616-62}", "opacity", '0', { fromValue: '1'}], position: 0, duration: 1000 },
            { id: "eid1801", tween: [ "style", "${_u616-62}", "opacity", '1', { fromValue: '0.000000'}], position: 1000, duration: 1000 },
            { id: "eid1813", tween: [ "style", "${_coffee_sel2}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid1810", tween: [ "style", "${_coffee_sel1}", "top", '69.63%', { fromValue: '69.63%'}], position: 0, duration: 0 },
            { id: "eid1764", tween: [ "style", "${_Group3}", "left", '-74.07%', { fromValue: '25.14%'}], position: 0, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1777", tween: [ "style", "${_Group3}", "left", '25.1%', { fromValue: '-74.07%'}], position: 1000, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1817", tween: [ "style", "${_coffee_sel6}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid1812", tween: [ "style", "${_coffee_sel1}", "left", '83px', { fromValue: '83px'}], position: 0, duration: 0 },
            { id: "eid1816", tween: [ "style", "${_coffee_sel5}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid1815", tween: [ "style", "${_coffee_sel4}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid1814", tween: [ "style", "${_coffee_sel3}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid1766", tween: [ "style", "${_Group6}", "left", '3.75%', { fromValue: '102.92%'}], position: 0, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1774", tween: [ "style", "${_Group6}", "left", '102.92%', { fromValue: '3.75%'}], position: 1000, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1759", tween: [ "style", "${_Group8}", "left", '3.75%', { fromValue: '102.92%'}], position: 0, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1773", tween: [ "style", "${_Group8}", "left", '102.92%', { fromValue: '3.75%'}], position: 1000, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1823", tween: [ "style", "${_coffee_sel_name0}", "font-size", '21px', { fromValue: '21px'}], position: 0, duration: 0 },
            { id: "eid1824", tween: [ "style", "${_coffee_sel_name3}", "font-size", '21px', { fromValue: '21px'}], position: 0, duration: 0 },
            { id: "eid1807", tween: [ "style", "${_coffee_sel0}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid1763", tween: [ "style", "${_Group4}", "left", '-694px', { fromValue: '20px'}], position: 0, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1776", tween: [ "style", "${_Group4}", "left", '20px', { fromValue: '-694px'}], position: 1000, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1808", tween: [ "style", "${_coffee_sel1}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid1761", tween: [ "style", "${_Group5}", "left", '52.08%', { fromValue: '151.25%'}], position: 0, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1775", tween: [ "style", "${_Group5}", "left", '151.25%', { fromValue: '52.08%'}], position: 1000, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1762", tween: [ "style", "${_Group2}", "left", '-47.82%', { fromValue: '51.39%'}], position: 0, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1772", tween: [ "style", "${_Group2}", "left", '51.35%', { fromValue: '-47.82%'}], position: 1000, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1757", tween: [ "style", "${_Group}", "right", '102.52%', { fromValue: '3.32%'}], position: 0, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1778", tween: [ "style", "${_Group}", "right", '3.35%', { fromValue: '102.52%'}], position: 1000, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1758", tween: [ "style", "${_Group7}", "left", '52.08%', { fromValue: '151.25%'}], position: 0, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1771", tween: [ "style", "${_Group7}", "left", '151.25%', { fromValue: '52.08%'}], position: 1000, duration: 1000, easing: "easeOutQuint" },
            { id: "eid1819", tween: [ "style", "${_coffee_sel_name1}", "font-size", '21px', { fromValue: '21px'}], position: 0, duration: 0 },
            { id: "eid1825", tween: [ "style", "${_coffee_sel_name2}", "font-size", '21px', { fromValue: '21px'}], position: 0, duration: 0 },
            { id: "eid1803", tween: [ "style", "${_u617-62}", "opacity", '1', { fromValue: '0'}], position: 0, duration: 1000 },
            { id: "eid1804", tween: [ "style", "${_u617-62}", "opacity", '0', { fromValue: '1'}], position: 1000, duration: 1000 }         ]
      }
   }
}
};


Edge.registerCompositionDefn(compId, symbols, fonts, resources);

/**
 * Adobe Edge DOM Ready Event Handler
 */
$(window).ready(function() {
     Edge.launchComposition(compId);
});
})(jQuery, AdobeEdge, "EDGE-1251484");
