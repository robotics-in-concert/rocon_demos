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
            id:'sandwitch_slot0',
            type:'image',
            tag:'img',
            rect:['-77px','74.1%','322px','322px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"sandwitch_empty.png",'50%','50%','322px','322px'],
            transform:[[],[],[],['0.4','0.4']]
         },
         {
            id:'sandwitch_slot1',
            type:'image',
            tag:'img',
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
            rect:['46.2%','85.7%','225px','auto','auto','auto'],
            text:"₩ 0",
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
            id:'coffee_sel0',
            type:'image',
            tag:'img',
            rect:['-2.9%','69.6%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel1',
            type:'image',
            tag:'img',
            rect:['-2.5%','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel2',
            type:'image',
            tag:'img',
            rect:['25.6%','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel3',
            type:'image',
            tag:'img',
            rect:['39.4%','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel4',
            type:'image',
            tag:'img',
            rect:['53.3%','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel5',
            type:'image',
            tag:'img',
            rect:['67.8%','69.5%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel6',
            type:'image',
            tag:'img',
            rect:['81.1%','69.8%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel_name0',
            type:'text',
            rect:['2.8%','77.4%','9.6%','3.7%','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'sandwich_sel_name0',
            type:'text',
            rect:['3.3%','80.6%','18.5%','3.7%','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'sandwich_sel_name1',
            type:'text',
            rect:['23.9%','80.6%','18.5%','3.7%','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name1',
            type:'text',
            rect:['16.7%','67.8%','9.6%','3.7%','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name2',
            type:'text',
            rect:['30.8%','77.4%','9.6%','3.7%','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name3',
            type:'text',
            rect:['45%','77.4%','9.6%','3.7%','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name4',
            type:'text',
            rect:['59%','77.4%','9.6%','3.7%','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name5',
            type:'text',
            rect:['73.1%','77.8%','9.6%','3.7%','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name6',
            type:'text',
            rect:['87.8%','77.8%','69px','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',[120,"%"],"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'COFFEE_TITLE',
            type:'image',
            rect:['22.4%','57.6%','400px','86px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"u616-6.png",'0%','0%','100%','auto']
         },
         {
            id:'SANDWITCH_TITLE',
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
         },
         {
            id:'P1M1',
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
            id:'P1M2',
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
            id:'P1M3',
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
            id:'P1M4',
            type:'group',
            rect:['-123.2%','121px','152','207','auto','auto'],
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
            id:'P1M5',
            type:'group',
            rect:['21px','359','151','183','auto','auto'],
            c:[
            {
               id:'cappuccino',
               type:'image',
               rect:['0px','0px','151px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cappuccino.png",'0px','0px']
            },
            {
               id:'TextCopy9',
               type:'text',
               rect:['22px','113px','auto','auto','auto','auto'],
               text:"카푸치노<br>Cappuccino<br>₩ 2,700",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P1M6',
            type:'group',
            rect:['27.1%','359','152','183','auto','auto'],
            c:[
            {
               id:'TextCopy10',
               type:'text',
               rect:['2px','113px','148px','auto','auto','auto'],
               text:"카라멜 라떼<br>Caramel Latte<br>₩ 2,800",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'cafelatteCopy',
               type:'image',
               rect:['0px','0px','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
            }]
         },
         {
            id:'P1M7',
            type:'group',
            rect:['51.3%','359','152','183','auto','auto'],
            c:[
            {
               id:'TextCopy11',
               type:'text',
               rect:['0px','113px','152px','auto','auto','auto'],
               text:"헤이즐넛 라떼<br>Hazelnut Latte<br>₩ 2,800",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'cafelatteCopy2',
               type:'image',
               rect:['0px','0px','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
            }]
         },
         {
            id:'P1M8',
            type:'group',
            rect:['76.3%','359','152','183','auto','auto'],
            c:[
            {
               id:'TextCopy12',
               type:'text',
               rect:['22px','113px','auto','auto','auto','auto'],
               text:"바닐라 라떼<br>Vanilla Latte<br>₩ 3,000",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'cafelatteCopy4',
               type:'image',
               rect:['0px','0px','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
            }]
         },
         {
            id:'P2M1',
            type:'group',
            rect:['26.7%','358px','154','188','auto','auto'],
            c:[
            {
               id:'cafemocha',
               type:'image',
               rect:['0px','0px','154px','112px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafemocha.png",'0px','0px']
            },
            {
               id:'TextCopy8',
               type:'text',
               rect:['22px','118px','auto','auto','auto','auto'],
               text:"카페 모카<br>Cafe Mocha<br>₩ 3,200",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P2M2',
            type:'group',
            rect:['26.7%','358px','154','188','auto','auto'],
            c:[
            {
               id:'cafemochaCopy',
               type:'image',
               rect:['0px','0px','154px','112px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafemocha.png",'0px','0px']
            },
            {
               id:'TextCopy13',
               type:'text',
               rect:['-3px','118px','auto','auto','auto','auto'],
               text:"카라멜 모카<br>Caramel Mocha<br>₩ 3,200",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P2M3',
            type:'group',
            rect:['26.7%','358px','154','188','auto','auto'],
            c:[
            {
               id:'cafemochaCopy2',
               type:'image',
               rect:['0px','0px','154px','112px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafemocha.png",'0px','0px']
            },
            {
               id:'TextCopy14',
               type:'text',
               rect:['22px','118px','auto','auto','auto','auto'],
               text:"화이트 모카<br>White Mocha<br>₩ 3,200",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P3M1',
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
            id:'P3M2',
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
               text:"닭가슴살 샌드위치<br>Cicken Sandwitch<br>₩ 4,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P3M3',
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
            id:'P3M4',
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
         }],
         symbolInstances: [

         ]
      },
   states: {
      "Base State": {
         "${_TextCopy9}": [
            ["style", "top", '113px'],
            ["style", "text-align", 'center'],
            ["style", "left", '22px'],
            ["style", "font-size", '20px']
         ],
         "${_sandwitch_slot1}": [
            ["style", "top", '74.18%'],
            ["transform", "scaleY", '0.4'],
            ["transform", "scaleX", '0.4'],
            ["style", "left", '11.09%'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_oder_management}": [
            ["style", "letter-spacing", '0em'],
            ["style", "bottom", 'auto'],
            ["color", "color", 'rgba(100,61,23,0.49)'],
            ["style", "right", 'auto'],
            ["style", "left", '-14.34%'],
            ["style", "font-size", '120%'],
            ["style", "top", '94.93%'],
            ["style", "font-weight", '200'],
            ["style", "text-align", 'center'],
            ["style", "text-indent", '0%'],
            ["style", "height", '3.5%'],
            ["style", "width", '79.9%'],
            ["style", "word-spacing", '0em'],
            ["style", "opacity", '1']
         ],
         "${_TextCopy16}": [
            ["style", "top", '118px'],
            ["style", "left", '22px'],
            ["style", "font-size", '20px']
         ],
         "${_fron_blue}": [
            ["style", "top", '55.7%'],
            ["style", "height", '129px'],
            ["style", "right", 'auto'],
            ["style", "left", '79.72%'],
            ["style", "width", '129px']
         ],
         "${_TextCopy12}": [
            ["style", "top", '113px'],
            ["style", "left", '22px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px']
         ],
         "${_americano}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_TextCopy8}": [
            ["style", "top", '118px'],
            ["style", "left", '22px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px']
         ],
         "${_dorothy_logo012}": [
            ["style", "height", '55px'],
            ["style", "top", '13px'],
            ["style", "left", '24px'],
            ["style", "width", '56px']
         ],
         "${_order}": [
            ["style", "top", '79.67%'],
            ["style", "width", '115px'],
            ["style", "font-weight", '800'],
            ["color", "color", 'rgba(100,61,23,1.00)'],
            ["style", "right", '13px'],
            ["style", "left", 'auto'],
            ["style", "font-size", '25px']
         ],
         "${_TextCopy}": [
            ["style", "top", '114px'],
            ["style", "text-align", 'center'],
            ["style", "left", '0px'],
            ["style", "font-size", '20px']
         ],
         "${_cafelatteCopy2}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_TextCopy11}": [
            ["style", "top", '113px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px'],
            ["style", "left", '0px'],
            ["style", "width", '152px']
         ],
         "${_coffee_sel_name3}": [
            ["style", "top", '67.78%'],
            ["style", "letter-spacing", '0px'],
            ["style", "width", '9.59%'],
            ["style", "text-indent", '0px'],
            ["style", "height", '3.7%'],
            ["style", "word-spacing", '0px'],
            ["style", "left", '44.86%'],
            ["style", "font-size", '21px']
         ],
         "${_cappuccino}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_cafemocha}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_P2M2}": [
            ["style", "left", '132.52%'],
            ["style", "top", '119px']
         ],
         "${_coffee_sel4}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '53.33%'],
            ["transform", "scaleX", '0.45']
         ],
         "${_coffee_sel3}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '39.44%'],
            ["transform", "scaleX", '0.45']
         ],
         "${_P1M3}": [
            ["style", "left", '51.39%']
         ],
         "${_coffee_sel5}": [
            ["style", "top", '69.54%'],
            ["transform", "scaleY", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '67.5%'],
            ["transform", "scaleX", '0.45']
         ],
         "${_menu-category-sandwich-tuna}": [
            ["style", "top", '0px'],
            ["transform", "scaleY", '1'],
            ["style", "left", '0px'],
            ["transform", "scaleX", '1']
         ],
         "${_coffee_sel_name0}": [
            ["style", "top", '67.78%'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '3.7%'],
            ["style", "left", '2.64%'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '9.59%']
         ],
         "${__01}": [
            ["style", "top", '10px'],
            ["style", "bottom", 'auto'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "right", '32px'],
            ["style", "left", 'auto'],
            ["style", "font-size", '320%']
         ],
         "${_accept_blue}": [
            ["style", "top", '81.94%'],
            ["style", "height", '129px'],
            ["style", "right", '24px'],
            ["style", "left", 'auto'],
            ["style", "width", '129px']
         ],
         "${_header}": [
            ["style", "top", '0px'],
            ["color", "background-color", 'rgba(57,35,13,1.00)'],
            ["style", "height", '80px'],
            ["style", "opacity", '0.9'],
            ["style", "left", '0px'],
            ["style", "width", '1440px']
         ],
         "${_Text}": [
            ["style", "top", '114px'],
            ["style", "text-align", 'center'],
            ["style", "left", '33px'],
            ["style", "font-size", '20px']
         ],
         "${_espresso_conpanna2}": [
            ["style", "left", '14px'],
            ["style", "top", '0px']
         ],
         "${_cafemochaCopy2}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_TextCopy6}": [
            ["style", "top", '134px'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "width", '226px'],
            ["style", "left", '42px'],
            ["style", "font-size", '20px']
         ],
         "${_P2M3}": [
            ["style", "left", '157.08%'],
            ["style", "top", '119px']
         ],
         "${_TextCopy14}": [
            ["style", "top", '118px'],
            ["style", "left", '22px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px']
         ],
         "${_espresso}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_copyright}": [
            ["style", "top", '97.89%'],
            ["style", "font-size", '70%'],
            ["color", "color", 'rgba(100,61,23,0.37)'],
            ["style", "height", '2.11%'],
            ["style", "left", '0.14%'],
            ["style", "width", '100%']
         ],
         "${_sandwitch_slot0}": [
            ["style", "top", '74.09%'],
            ["transform", "scaleY", '0.4'],
            ["transform", "scaleX", '0.4'],
            ["style", "left", '-77px'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_sandwich_sel_name1}": [
            ["style", "top", '80.55%'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '3.7%'],
            ["style", "left", '23.88%'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '18.49%']
         ],
         "${_Price}": [
            ["style", "top", '85.74%'],
            ["style", "width", '225px'],
            ["color", "color", 'rgba(100,61,23,1.00)'],
            ["style", "font-weight", '800'],
            ["style", "left", '46.21%'],
            ["style", "font-size", '50px']
         ],
         "${_cafelatteCopy}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_coffee_sel6}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "display", 'block'],
            ["style", "opacity", '1'],
            ["style", "left", '81.25%'],
            ["transform", "scaleX", '0.45']
         ],
         "${_sandwich_sel_name0}": [
            ["style", "top", '80.55%'],
            ["style", "letter-spacing", '0px'],
            ["style", "width", '18.49%'],
            ["style", "text-indent", '0px'],
            ["style", "height", '3.7%'],
            ["style", "word-spacing", '0px'],
            ["style", "left", '3.33%'],
            ["style", "font-size", '21px']
         ],
         "${_cafelatteCopy4}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_coffee_sel0}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '-2.89%'],
            ["transform", "scaleX", '0.45']
         ],
         "${_coffee_sel2}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '25.56%'],
            ["transform", "scaleX", '0.45']
         ],
         "${_TextCopy5}": [
            ["style", "top", '141px'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "font-size", '20px'],
            ["style", "left", '71px'],
            ["style", "width", '168px']
         ],
         "${_P3M2}": [
            ["style", "left", '251.75%'],
            ["style", "top", '10.65%']
         ],
         "${_menu-category-sandwich-buffchic_copy}": [
            ["style", "top", '0px'],
            ["transform", "scaleY", '1'],
            ["style", "left", '0px'],
            ["transform", "scaleX", '1']
         ],
         "${_P1M6}": [
            ["style", "left", '27.08%']
         ],
         "${_TextCopy17}": [
            ["style", "top", '118px'],
            ["style", "left", '22px'],
            ["style", "font-size", '20px']
         ],
         "${_wood_wallpaper_by_stenosis}": [
            ["style", "height", '1136px'],
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_menu-category-sandwich-stkchs_copy}": [
            ["style", "top", '0px'],
            ["transform", "scaleY", '1'],
            ["style", "left", '0px'],
            ["transform", "scaleX", '1']
         ],
         "${_P3M1}": [
            ["style", "left", '205.09%'],
            ["style", "top", '10.65%']
         ],
         "${_P2M1}": [
            ["style", "left", '106.1%'],
            ["style", "top", '119px']
         ],
         "${_back_blue}": [
            ["style", "top", '55.7%'],
            ["style", "height", '129px'],
            ["style", "left", '2.64%'],
            ["style", "width", '129px']
         ],
         "${_dorothy_cafe}": [
            ["style", "top", '10px'],
            ["style", "font-size", '320%'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "height", '59px'],
            ["style", "left", '89px'],
            ["style", "width", '324px']
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
            ["style", "opacity", '1'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ],
            ["style", "background-size", [649.65,'auto'], {valueTemplate:'@@0@@px @@1@@'} ]
         ],
         "${_P3M3}": [
            ["style", "left", '203.67%'],
            ["style", "top", '32.55%']
         ],
         "${_cafemochaCopy}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_TextCopy4}": [
            ["style", "top", '140px'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "width", '217px'],
            ["style", "left", '46px'],
            ["style", "font-size", '20px']
         ],
         "${_P1M5}": [
            ["style", "left", '21px']
         ],
         "${_COFFEE_TITLE}": [
            ["style", "top", '57.55%'],
            ["style", "opacity", '0.99000000953674'],
            ["style", "left", '22.36%'],
            ["style", "background-size", [100,'auto'], {valueTemplate:'@@0@@% @@1@@'} ]
         ],
         "${_cafelatte}": [
            ["style", "left", '0px'],
            ["style", "top", '0px']
         ],
         "${_P1M4}": [
            ["style", "left", '75.56%'],
            ["style", "right", 'auto']
         ],
         "${_SANDWITCH_TITLE}": [
            ["style", "top", '57.57%'],
            ["style", "opacity", '0'],
            ["style", "left", '34.58%'],
            ["style", "background-size", [100,'auto'], {valueTemplate:'@@0@@% @@1@@'} ]
         ],
         "${_table_no}": [
            ["style", "top", '33px'],
            ["style", "bottom", 'auto'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "right", '101px'],
            ["style", "left", 'auto'],
            ["style", "font-size", '100%']
         ],
         "${_TextCopy13}": [
            ["style", "top", '118px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px'],
            ["style", "left", '-3px'],
            ["style", "width", '160px']
         ],
         "${_TextCopy2}": [
            ["style", "top", '114px'],
            ["style", "left", '4px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px']
         ],
         "${_coffee_sel_name5}": [
            ["style", "top", '67.78%'],
            ["style", "letter-spacing", '0px'],
            ["style", "width", '9.59%'],
            ["style", "text-indent", '0px'],
            ["style", "height", '3.7%'],
            ["style", "word-spacing", '0px'],
            ["style", "left", '72.92%'],
            ["style", "font-size", '21px']
         ],
         "${_TextCopy10}": [
            ["style", "top", '113px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px'],
            ["style", "left", '2px'],
            ["style", "width", '148px']
         ],
         "${_coffee_sel_name2}": [
            ["style", "top", '67.78%'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '3.7%'],
            ["style", "left", '30.69%'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '9.59%']
         ],
         "${_coffee_sel_name4}": [
            ["style", "top", '67.78%'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '3.7%'],
            ["style", "left", '58.89%'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '9.59%']
         ],
         "${_coffee_sel_name6}": [
            ["style", "top", '67.78%'],
            ["style", "letter-spacing", '0em'],
            ["style", "width", '69px'],
            ["style", "text-indent", '0%'],
            ["style", "height", '42px'],
            ["style", "word-spacing", '0em'],
            ["style", "left", '87%'],
            ["style", "font-size", '131.25%']
         ],
         "${_TextCopy3}": [
            ["style", "top", '114px'],
            ["style", "text-align", 'center'],
            ["style", "left", '30px'],
            ["style", "font-size", '20px']
         ],
         "${_TextCopy15}": [
            ["style", "top", '118px'],
            ["style", "width", '132px'],
            ["style", "left", '22px'],
            ["style", "font-size", '20px']
         ],
         "${_coffee_sel1}": [
            ["style", "top", '69.63%'],
            ["transform", "scaleY", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '11.67%'],
            ["transform", "scaleX", '0.45']
         ],
         "${_P1M2}": [
            ["style", "left", '25.14%']
         ],
         "${_P3M4}": [
            ["style", "left", '252%'],
            ["style", "top", '32.55%']
         ],
         "${_P1M8}": [
            ["style", "left", '76.25%']
         ],
         "${_checkout_total}": [
            ["style", "top", '79.66%'],
            ["style", "font-size", '25px'],
            ["color", "color", 'rgba(100,61,23,1.00)'],
            ["style", "font-weight", '800'],
            ["style", "left", '48.58%'],
            ["style", "width", '199px']
         ],
         "${_menu-category-sandwich-italbmt_copy}": [
            ["style", "top", '0px'],
            ["transform", "scaleY", '1'],
            ["style", "left", '0px'],
            ["transform", "scaleX", '1']
         ],
         "${_P1M1}": [
            ["style", "left", '20px']
         ],
         "${_P1M7}": [
            ["style", "left", '51.25%']
         ],
         "${_Stage}": [
            ["color", "background-color", 'rgba(255,255,255,1)'],
            ["style", "width", '100%'],
            ["style", "height", '100%'],
            ["style", "overflow", 'hidden']
         ],
         "${_TextCopy7}": [
            ["style", "top", '134px'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "font-size", '20px'],
            ["style", "left", '55px'],
            ["style", "width", '199px']
         ],
         "${_coffee_sel_name1}": [
            ["style", "top", '67.78%'],
            ["style", "letter-spacing", '0px'],
            ["style", "width", '9.59%'],
            ["style", "text-indent", '0px'],
            ["style", "height", '3.7%'],
            ["style", "word-spacing", '0px'],
            ["style", "left", '16.67%'],
            ["style", "font-size", '21px']
         ]
      }
   },
   timelines: {
      "Default Timeline": {
         fromState: "Base State",
         toState: "",
         duration: 2000,
         autoPlay: false,
         timeline: [
            { id: "eid1902", tween: [ "style", "${_P1M8}", "left", '-22.92%', { fromValue: '76.25%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1976", tween: [ "style", "${_P1M8}", "left", '-122.44%', { fromValue: '-22.92%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1991", tween: [ "style", "${_P1M8}", "left", '-122.44%', { fromValue: '-122.44%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1915", tween: [ "style", "${_P2M3}", "left", '53.19%', { fromValue: '157.08%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1967", tween: [ "style", "${_P2M3}", "left", '-46.33%', { fromValue: '53.19%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1982", tween: [ "style", "${_P2M3}", "left", '-46.33%', { fromValue: '-46.33%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1896", tween: [ "style", "${_P1M6}", "left", '-72.09%', { fromValue: '27.08%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1970", tween: [ "style", "${_P1M6}", "left", '-171.61%', { fromValue: '-72.09%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1985", tween: [ "style", "${_P1M6}", "left", '-171.61%', { fromValue: '-171.61%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1942", tween: [ "style", "${_P3M1}", "left", '104.34%', { fromValue: '205.09%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1974", tween: [ "style", "${_P3M1}", "left", '4.82%', { fromValue: '104.34%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1989", tween: [ "style", "${_P3M1}", "left", '4.82%', { fromValue: '4.82%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2109", tween: [ "style", "${_coffee_sel6}", "display", 'block', { fromValue: 'block'}], position: 0, duration: 0 },
            { id: "eid1893", tween: [ "style", "${_P1M5}", "left", '-693px', { fromValue: '21px'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1973", tween: [ "style", "${_P1M5}", "left", '-1410px', { fromValue: '-693px'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1988", tween: [ "style", "${_P1M5}", "left", '-1410px', { fromValue: '-1410px'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1800", tween: [ "style", "${_COFFEE_TITLE}", "opacity", '0', { fromValue: '0.99000000953674'}], position: 1000, duration: 1000 },
            { id: "eid1801", tween: [ "style", "${_COFFEE_TITLE}", "opacity", '0.000000', { fromValue: '0.000000'}], position: 2000, duration: 0 },
            { id: "eid1908", tween: [ "style", "${_P2M1}", "left", '3.33%', { fromValue: '106.1%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1965", tween: [ "style", "${_P2M1}", "left", '-96.19%', { fromValue: '3.33%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1980", tween: [ "style", "${_P2M1}", "left", '-96.25%', { fromValue: '-96.25%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1763", tween: [ "style", "${_P1M1}", "left", '-694px', { fromValue: '20px'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1962", tween: [ "style", "${_P1M1}", "left", '-1411px', { fromValue: '-694px'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1977", tween: [ "style", "${_P1M1}", "left", '-1411px', { fromValue: '-1411px'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1946", tween: [ "style", "${_P3M2}", "left", '151%', { fromValue: '251.75%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1972", tween: [ "style", "${_P3M2}", "left", '51.48%', { fromValue: '151%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1987", tween: [ "style", "${_P3M2}", "left", '51.48%', { fromValue: '51.48%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2007", tween: [ "style", "${_P1M4}", "left", '-23.64%', { fromValue: '75.56%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid2008", tween: [ "style", "${_P1M4}", "left", '-123.16%', { fromValue: '-23.64%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid2009", tween: [ "style", "${_P1M4}", "left", '-123.16%', { fromValue: '-123.16%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1950", tween: [ "style", "${_P3M4}", "left", '151.25%', { fromValue: '252%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1975", tween: [ "style", "${_P3M4}", "left", '51.73%', { fromValue: '151.25%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1990", tween: [ "style", "${_P3M4}", "left", '51.73%', { fromValue: '51.73%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1914", tween: [ "style", "${_P2M2}", "left", '28.24%', { fromValue: '132.52%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1969", tween: [ "style", "${_P2M2}", "left", '-71.28%', { fromValue: '28.24%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1984", tween: [ "style", "${_P2M2}", "left", '-71.28%', { fromValue: '-71.28%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1764", tween: [ "style", "${_P1M2}", "left", '-74.07%', { fromValue: '25.14%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1963", tween: [ "style", "${_P1M2}", "left", '-173.59%', { fromValue: '-74.07%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1978", tween: [ "style", "${_P1M2}", "left", '-173.59%', { fromValue: '-173.59%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1762", tween: [ "style", "${_P1M3}", "left", '-47.82%', { fromValue: '51.39%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1964", tween: [ "style", "${_P1M3}", "left", '-147.34%', { fromValue: '-47.82%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1979", tween: [ "style", "${_P1M3}", "left", '-147.34%', { fromValue: '-147.34%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1803", tween: [ "style", "${_SANDWITCH_TITLE}", "opacity", '1', { fromValue: '0'}], position: 1000, duration: 1000 },
            { id: "eid1804", tween: [ "style", "${_SANDWITCH_TITLE}", "opacity", '1', { fromValue: '1'}], position: 2000, duration: 0 },
            { id: "eid1900", tween: [ "style", "${_P1M7}", "left", '-47.92%', { fromValue: '51.25%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1971", tween: [ "style", "${_P1M7}", "left", '-147.44%', { fromValue: '-47.92%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1986", tween: [ "style", "${_P1M7}", "left", '-147.44%', { fromValue: '-147.44%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid1938", tween: [ "style", "${_P3M3}", "left", '102.92%', { fromValue: '203.67%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1968", tween: [ "style", "${_P3M3}", "left", '3.4%', { fromValue: '102.92%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1983", tween: [ "style", "${_P3M3}", "left", '3.4%', { fromValue: '3.4%'}], position: 2000, duration: 0, easing: "easeOutQuint" }         ]
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
