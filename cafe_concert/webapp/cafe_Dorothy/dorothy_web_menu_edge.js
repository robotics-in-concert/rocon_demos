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
            id:'rocon_logo',
            type:'image',
            rect:['21.7%','84%','111.2%','284px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"a4_nomal_png_c.png",'50%','50%','649.65px','auto'],
            transform:[[],[],[],['0.4','0.4']]
         },
         {
            id:'oder_management',
            type:'text',
            rect:['-10px','93.2%','48.1%','19px','auto','auto'],
            opacity:1,
            text:"ROCON Order Management system",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[500,"%"],"rgba(100,61,23,1.00)","200","none","normal"]
         },
         {
            id:'status_text',
            type:'text',
            rect:['8px','94.6%','99.1%','19px','auto','auto'],
            opacity:1,
            text:"Status: ",
            align:"left",
            font:['Arial, Helvetica, sans-serif',[100,"%"],"rgba(100,61,23,1.00)","200","none","normal"]
         },
         {
            id:'copyright',
            type:'text',
            rect:['0.1%','98%','100%','24px','auto','auto'],
            text:"Copyright YUJIN ROBOT co., Ltd. All rights reserved including the right of reproduction in whole or in part in any form. mobile",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[70,"%"],"rgba(100,61,23,0.37)","800","none","normal"]
         },
         {
            id:'sandwitch_slot0',
            type:'image',
            tag:'img',
            rect:['-81px','76.8%','322px','322px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"sandwitch_empty.png",'50%','50%','322px','322px'],
            transform:[[],[],[],['0.4','0.4']]
         },
         {
            id:'sandwitch_slot1',
            type:'image',
            tag:'img',
            rect:['10.5%','76.9%','322px','322px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"sandwitch_empty.png",'50%','50%','322px','322px'],
            transform:[[],[],[],['0.4','0.4']]
         },
         {
            id:'checkout_total',
            type:'text',
            rect:['48%','81.3%','199px','auto','auto','auto'],
            text:"Check out Total",
            font:['Arial, Helvetica, sans-serif',25,"rgba(100,61,23,1.00)","800","none",""]
         },
         {
            id:'Price',
            type:'text',
            rect:['45.6%','86.2%','225px','auto','auto','auto'],
            text:"₩ 0",
            font:['Arial, Helvetica, sans-serif',50,"rgba(100,61,23,1.00)","800","none",""]
         },
         {
            id:'order',
            type:'text',
            rect:['auto','81.3%','115px','auto','17px','auto'],
            text:"Order",
            font:['Arial, Helvetica, sans-serif',25,"rgba(100,61,23,1.00)","800","none",""]
         },
         {
            id:'coffee_sel0',
            type:'image',
            tag:'img',
            rect:['-28px','70.7%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel1',
            type:'image',
            tag:'img',
            rect:['10.6%','70.7%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel2',
            type:'image',
            tag:'img',
            rect:['24.5%','70.7%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel3',
            type:'image',
            tag:'img',
            rect:['38.4%','70.7%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel4',
            type:'image',
            tag:'img',
            rect:['52.3%','70.7%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel5',
            type:'image',
            tag:'img',
            rect:['66.5%','70.7%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel6',
            type:'image',
            tag:'img',
            rect:['80.2%','70.7%','152px','102px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
            transform:[[],[],[],['0.45','0.45']]
         },
         {
            id:'coffee_sel_name0',
            type:'text',
            rect:['1.6%','69.3%','9.6%','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'sandwich_sel_name0',
            type:'text',
            rect:['2.8%','82%','18.5%','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'sandwich_sel_name1',
            type:'text',
            rect:['23.3%','82%','18.5%','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name1',
            type:'text',
            rect:['15.6%','69.3%','9.6%','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name2',
            type:'text',
            rect:['29.7%','69.3%','9.6%','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name3',
            type:'text',
            rect:['43.8%','69.3%','9.6%','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name4',
            type:'text',
            rect:['57.9%','69.3%','9.6%','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name5',
            type:'text',
            rect:['71.9%','69.3%','9.6%','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',19.2,"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'coffee_sel_name6',
            type:'text',
            rect:['86%','69.3%','69px','42px','auto','auto'],
            font:['Arial, Helvetica, sans-serif',[120,"%"],"rgba(0,0,0,1)","normal","none",""]
         },
         {
            id:'COFFEE_TITLE',
            type:'image',
            rect:['21.6%','53.4%','55.6%','86px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"u616-6.png",'50%','50%','400px','auto']
         },
         {
            id:'SANDWITCH_TITLE',
            type:'image',
            rect:['33.8%','51.5%','31.1%','10%','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"u617-6.png",'50%','50%','224px','auto']
         },
         {
            id:'accept_blue',
            type:'image',
            rect:['auto','83.1%','129px','129px','28px','auto'],
            fill:["rgba(0,0,0,0)",im+"accept_blue.png",'0px','0px'],
            filter:[0,0,1,1,0,0,0,0,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'fron_blue',
            type:'image',
            rect:['auto','51.9%','129px','129px','22px','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"fron_blue.png",'0px','0px'],
            filter:[0,0,1,1,0,0,0,0,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'back_blue',
            display:'none',
            type:'image',
            rect:['14px','734px','129px','129px','auto','auto'],
            opacity:1,
            fill:["rgba(0,0,0,0)",im+"back_blue.png",'0px','0px'],
            filter:[0,0,1,1,0,0,0,0,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'P1M1',
            type:'group',
            rect:['20px','8.6%','152','184','auto','auto'],
            c:[
            {
               id:'espresso',
               type:'image',
               rect:['0px','0%','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"espresso.png",'0px','0px']
            },
            {
               id:'Text',
               type:'text',
               rect:['33px','62%','auto','auto','auto','auto'],
               text:"에스프레소<br>Espresso<br>₩ 2,300",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P1M2',
            type:'group',
            rect:['25.1%','8.6%','180','184','auto','auto'],
            c:[
            {
               id:'TextCopy',
               type:'text',
               rect:['0px','62%','auto','auto','auto','auto'],
               text:"에스프레소 꼰빠냐<br>Espresso Conpanna<br>₩ 2,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'espresso_conpanna2',
               type:'image',
               rect:['14px','0%','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"espresso%20conpanna2.png",'0px','0px']
            }]
         },
         {
            id:'P1M3',
            type:'group',
            rect:['51.4%','8.6%','150','207','auto','auto'],
            c:[
            {
               id:'TextCopy2',
               type:'text',
               rect:['4px','55.1%','auto','auto','auto','auto'],
               text:"카페 아메리카노<br>Cafe Americano<br>₩ 2,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'americano',
               type:'image',
               rect:['0px','0%','150px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"americano.png",'0px','0px']
            }]
         },
         {
            id:'P1M4',
            type:'group',
            rect:['-123.2%','8.6%','152','207','auto','auto'],
            c:[
            {
               id:'TextCopy3',
               type:'text',
               rect:['30px','55.1%','auto','auto','auto','auto'],
               text:"카페 라떼<br>Cafe Latte<br>₩ 2,700",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'cafelatte',
               type:'image',
               rect:['0px','0%','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
            }]
         },
         {
            id:'P1M5',
            type:'group',
            rect:['21px','29.4%','151','183','auto','auto'],
            c:[
            {
               id:'cappuccino',
               type:'image',
               rect:['0px','0%','151px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cappuccino.png",'0px','0px']
            },
            {
               id:'TextCopy9',
               type:'text',
               rect:['22px','61.8%','auto','auto','auto','auto'],
               text:"카푸치노<br>Cappuccino<br>₩ 2,700",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P1M6',
            type:'group',
            rect:['27.1%','29.4%','152','183','auto','auto'],
            c:[
            {
               id:'TextCopy10',
               type:'text',
               rect:['2px','61.8%','148px','auto','auto','auto'],
               text:"카라멜 라떼<br>Caramel Latte<br>₩ 2,800",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'cafelatteCopy',
               type:'image',
               rect:['0px','0%','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
            }]
         },
         {
            id:'P1M7',
            type:'group',
            rect:['51.3%','29.4%','152','183','auto','auto'],
            c:[
            {
               id:'TextCopy11',
               type:'text',
               rect:['0px','61.8%','152px','auto','auto','auto'],
               text:"헤이즐넛 라떼<br>Hazelnut Latte<br>₩ 2,800",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'cafelatteCopy2',
               type:'image',
               rect:['0px','0%','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
            }]
         },
         {
            id:'P1M8',
            type:'group',
            rect:['76.3%','29.4%','152','183','auto','auto'],
            c:[
            {
               id:'TextCopy12',
               type:'text',
               rect:['22px','61.8%','auto','auto','auto','auto'],
               text:"바닐라 라떼<br>Vanilla Latte<br>₩ 3,000",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            },
            {
               id:'cafelatteCopy4',
               type:'image',
               rect:['0px','0%','152px','102px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
            }]
         },
         {
            id:'P2M1',
            type:'group',
            rect:['26.7%','25.3%','154','188','auto','auto'],
            c:[
            {
               id:'cafemocha',
               type:'image',
               rect:['0px','0%','154px','112px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafemocha.png",'0px','0px']
            },
            {
               id:'TextCopy8',
               type:'text',
               rect:['22px','62.8%','auto','auto','auto','auto'],
               text:"카페 모카<br>Cafe Mocha<br>₩ 3,200",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P2M2',
            type:'group',
            rect:['26.7%','25.3%','154','188','auto','auto'],
            c:[
            {
               id:'cafemochaCopy',
               type:'image',
               rect:['0px','0%','154px','112px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafemocha.png",'0px','0px']
            },
            {
               id:'TextCopy13',
               type:'text',
               rect:['-3px','62.8%','auto','auto','auto','auto'],
               text:"카라멜 모카<br>Caramel Mocha<br>₩ 3,200",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P2M3',
            type:'group',
            rect:['26.7%','25.3%','154','188','auto','auto'],
            c:[
            {
               id:'cafemochaCopy2',
               type:'image',
               rect:['0px','0%','154px','112px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"cafemocha.png",'0px','0px']
            },
            {
               id:'TextCopy14',
               type:'text',
               rect:['22px','62.8%','auto','auto','auto','auto'],
               text:"화이트 모카<br>White Mocha<br>₩ 3,200",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P3M1',
            type:'group',
            rect:['102.9%','8.6%','308','210','auto','auto'],
            c:[
            {
               id:'menu-category-sandwich-italbmt_copy',
               type:'image',
               rect:['0px','0%','308px','140px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"menu-category-sandwich-italbmt%20copy.png",'0px','0px'],
               transform:[]
            },
            {
               id:'TextCopy4',
               type:'text',
               rect:['46px','66.7%','217px','70px','auto','auto'],
               text:"터키 베이컨 샌드위치<br>Turkey Bacon Sandwitch<br>₩ 4,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P3M2',
            type:'group',
            rect:['151.3%','8.6%','308','211','auto','auto'],
            c:[
            {
               id:'menu-category-sandwich-buffchic_copy',
               type:'image',
               rect:['0px','0%','308px','140px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"menu-category-sandwich-buffchic%20copy.png",'0px','0px'],
               transform:[]
            },
            {
               id:'TextCopy5',
               type:'text',
               rect:['71px','66.8%','168px','70px','auto','auto'],
               text:"닭가슴살 샌드위치<br>Cicken Sandwitch<br>₩ 4,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P3M3',
            type:'group',
            rect:['102.9%','30.2%','308','204','auto','auto'],
            c:[
            {
               id:'menu-category-sandwich-stkchs_copy',
               type:'image',
               rect:['0px','0%','308px','140px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"menu-category-sandwich-stkchs%20copy.png",'0px','0px'],
               transform:[]
            },
            {
               id:'TextCopy7',
               type:'text',
               rect:['55px','65.7%','199px','70px','auto','auto'],
               text:"로스트 비프 샌드위치<br>Roast Beef Sandwitch<br>₩ 4,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'P3M4',
            type:'group',
            rect:['151.3%','30.2%','308','204','auto','auto'],
            c:[
            {
               id:'menu-category-sandwich-tuna',
               type:'image',
               rect:['0px','0%','308px','140px','auto','auto'],
               fill:["rgba(0,0,0,0)",im+"menu-category-sandwich-tuna.png",'0px','0px'],
               transform:[]
            },
            {
               id:'TextCopy6',
               type:'text',
               rect:['42px','65.7%','226px','70px','auto','auto'],
               text:"허브참치 샌드위치<br>Heb Tuna Sandwitch<br>₩ 4,500",
               align:"center",
               font:['Arial, Helvetica, sans-serif',20,"rgba(0,0,0,1)","normal","none",""]
            }]
         },
         {
            id:'Rectangle',
            display:'none',
            type:'rect',
            rect:['-0.8%','798px','100.4%','506px','auto','auto'],
            opacity:0.9,
            fill:["rgba(57,35,13,1)"],
            stroke:[0,"rgba(0,0,0,0.00)","none"]
         },
         {
            id:'dorothy_logo012Copy',
            display:'none',
            type:'image',
            rect:['32.6%','72.2%','34.7%','17.3%','auto','auto'],
            opacity:0.4,
            fill:["rgba(0,0,0,0)",im+"dorothy_logo01.png",'50%','50%','250px','245.01px']
         },
         {
            id:'Text2',
            display:'none',
            type:'text',
            rect:['28.2%','949px','43.9%','2.6%','auto','auto'],
            text:"주문 상태를 확인하세요.",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[180,"%"],"rgba(255,255,255,1.00)","500","none","normal"]
         },
         {
            id:'Text2Copy',
            display:'none',
            type:'text',
            rect:['11.9%','823px','76.1%','13.6%','auto','auto'],
            text:"주문이 완료 되었습니다. <br>감사합니다.",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[220,"%"],"rgba(255,255,255,1.00)","700","none","normal"]
         },
         {
            id:'Text3',
            display:'none',
            type:'text',
            rect:['118px','285','auto','auto','auto','auto'],
            text:"주문 완료",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[220,"%"],"rgba(57,35,13,1.00)","bold","none","normal"]
         },
         {
            id:'Text4',
            display:'none',
            type:'text',
            rect:['auto','283px','225px','auto','4.6%','auto'],
            text:"주문 처리중",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[220,"%"],"rgba(57,35,13,1)","bold","none","normal"]
         },
         {
            id:'Text4Copy',
            display:'none',
            type:'text',
            rect:['auto','705px','182px','56px','6.9%','auto'],
            text:"주문 준비중",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[220,"%"],"rgba(57,35,13,1)","bold","none","normal"]
         },
         {
            id:'Text4Copy2',
            display:'none',
            type:'text',
            rect:['71px','705px','182px','56px','auto','auto'],
            text:"주문 서빙중",
            align:"center",
            font:['Arial, Helvetica, sans-serif',[220,"%"],"rgba(57,35,13,1)","bold","none","normal"]
         },
         {
            id:'_03_pp_anwansoon',
            display:'none',
            type:'image',
            rect:['20px','114px','154px','154px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"03_pp_anwansoon.png",'0px','0px']
         },
         {
            id:'nfc_logo',
            display:'none',
            type:'image',
            rect:['137px','164px','200px','55px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"nfc_logo.png",'0px','0px']
         },
         {
            id:'_410_anwansoon2',
            display:'none',
            type:'image',
            rect:['auto','499px','199px','199px','6.4%','auto'],
            fill:["rgba(0,0,0,0)",im+"410_anwansoon.png",'0px','0px']
         },
         {
            id:'Kobuki_00',
            display:'none',
            type:'image',
            rect:['63px','473px','195px','239px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"Kobuki_00.png",'0px','0px']
         },
         {
            id:'_114_anwansoonfge',
            display:'none',
            type:'image',
            rect:['auto','150px','130px','130px','18.3%','auto'],
            fill:["rgba(0,0,0,0)",im+"114_anwansoonfge.png",'0px','0px']
         },
         {
            id:'a4_nomal_png_a',
            display:'none',
            type:'image',
            rect:['auto','105px','104px','163px','8.2%','auto'],
            fill:["rgba(0,0,0,0)",im+"a4_nomal_png_a.png",'0px','0px']
         },
         {
            id:'s1p1',
            display:'none',
            type:'ellipse',
            rect:['39.7%','289px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'s1p2',
            display:'none',
            type:'ellipse',
            rect:['46.3%','290px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'s1p3',
            display:'none',
            type:'ellipse',
            rect:['53.1%','290px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'s1p4',
            display:'none',
            type:'ellipse',
            rect:['59.8%','290px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'s1p1Copy',
            display:'none',
            type:'ellipse',
            rect:['78.3%','337px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'s1p2Copy',
            display:'none',
            type:'ellipse',
            rect:['78.3%','380px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'s1p3Copy',
            display:'none',
            type:'ellipse',
            rect:['78.3%','423px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'s1p4Copy',
            display:'none',
            type:'ellipse',
            rect:['78.3%','465px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'s1p1Copy2',
            display:'none',
            type:'ellipse',
            rect:['59.9%','582px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'s1p2Copy2',
            display:'none',
            type:'ellipse',
            rect:['53.2%','582px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'s1p3Copy2',
            display:'none',
            type:'ellipse',
            rect:['46.4%','582px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'s1p4Copy2',
            display:'none',
            type:'ellipse',
            rect:['39.7%','582px','21px','22px','auto','auto'],
            borderRadius:["50%","50%","50%","50%"],
            fill:["rgba(67,222,254,1.00)"],
            stroke:[0,"rgba(0, 0, 0, 0)","none"],
            filter:[0,0,1,1,0,0,0,7.1664663461538,"rgba(0,0,0,0)",0,0,0]
         },
         {
            id:'Rectangle2',
            display:'none',
            type:'rect',
            rect:['0%','80px','100%','61.8%','auto','auto'],
            opacity:0.9,
            fill:["rgba(57,35,13,1.00)"],
            stroke:[0,"rgba(57,35,13,1.00)","none"]
         },
         {
            id:'Text5',
            display:'none',
            type:'text',
            rect:['14%','352px','70.8%','6.8%','auto','auto'],
            text:"아래 메뉴로 주문 하시겠습니까?<br>금액을 확인해 주세요.",
            align:"center",
            font:['Arial, Helvetica, sans-serif',40,"rgba(255,255,255,1.00)","normal","none",""]
         },
         {
            id:'Text6',
            display:'none',
            type:'text',
            rect:['auto','45.1%','auto','auto','20.8%','auto'],
            text:"주문완료",
            align:"left",
            font:['Arial, Helvetica, sans-serif',30,"rgba(255,255,255,1.00)","800","none","normal"]
         },
         {
            id:'Text7',
            display:'none',
            type:'text',
            rect:['18.3%','45.1%','auto','auto','auto','auto'],
            text:"다시주문",
            align:"left",
            font:['Arial, Helvetica, sans-serif',30,"rgba(255,255,255,1.00)","800","none","normal"]
         },
         {
            id:'delete',
            display:'none',
            type:'image',
            rect:['15.5%','49.5%','145px','144px','auto','auto'],
            fill:["rgba(0,0,0,0)",im+"delete.png",'0px','0px']
         },
         {
            id:'accept_blue2',
            display:'none',
            type:'image',
            rect:['auto','49.5%','145px','145px','17.2%','auto'],
            fill:["rgba(0,0,0,0)",im+"accept_blue.png",'0px','0px']
         },
         {
            id:'header',
            type:'rect',
            rect:['0px','0px','2391px','80px','auto','auto'],
            opacity:0.9,
            fill:["rgba(57,35,13,1.00)"],
            stroke:[0,"rgba(57,35,13,1.00)","none"]
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
         "${_s1p4Copy2}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '582px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "left", '39.72%'],
            ["style", "width", '21px']
         ],
         "${_TextCopy9}": [
            ["style", "top", '61.75%'],
            ["style", "left", '22px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px']
         ],
         "${_sandwitch_slot1}": [
            ["style", "top", '76.89%'],
            ["transform", "scaleY", '0.4'],
            ["transform", "scaleX", '0.4'],
            ["style", "left", '10.51%'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_oder_management}": [
            ["style", "letter-spacing", '0em'],
            ["style", "bottom", 'auto'],
            ["color", "color", 'rgba(100,61,23,0.49)'],
            ["style", "right", 'auto'],
            ["style", "left", '-10px'],
            ["style", "font-size", '120%'],
            ["style", "top", '93.15%'],
            ["style", "opacity", '1'],
            ["style", "text-align", 'center'],
            ["style", "text-indent", '0%'],
            ["style", "height", '20px'],
            ["style", "width", '48.07%'],
            ["style", "word-spacing", '0em'],
            ["style", "font-weight", '200']
         ],
         "${_Text4Copy}": [
            ["style", "top", '705px'],
            ["style", "height", '56px'],
            ["style", "right", '6.94%'],
            ["style", "bottom", 'auto'],
            ["style", "display", 'none'],
            ["style", "opacity", '0.2'],
            ["style", "left", 'auto'],
            ["style", "width", '182px']
         ],
         "${__114_anwansoonfge}": [
            ["style", "top", '150px'],
            ["style", "height", '130px'],
            ["style", "right", '18.33%'],
            ["style", "bottom", 'auto'],
            ["style", "display", 'none'],
            ["style", "opacity", '0.2'],
            ["style", "left", 'auto'],
            ["style", "width", '130px']
         ],
         "${_TextCopy15}": [
            ["style", "top", '118px'],
            ["style", "font-size", '20px'],
            ["style", "left", '22px'],
            ["style", "width", '132px']
         ],
         "${_accept_blue2}": [
            ["style", "top", '-12.19%'],
            ["style", "display", 'none'],
            ["style", "height", '145px'],
            ["style", "right", '17.22%'],
            ["style", "left", 'auto'],
            ["style", "width", '145px']
         ],
         "${_TextCopy12}": [
            ["style", "top", '61.75%'],
            ["style", "text-align", 'center'],
            ["style", "left", '22px'],
            ["style", "font-size", '20px']
         ],
         "${_americano}": [
            ["style", "left", '0px'],
            ["style", "top", '0%']
         ],
         "${_P2M1}": [
            ["style", "left", '106.1%'],
            ["style", "top", '8.42%']
         ],
         "${_P1M8}": [
            ["style", "left", '76.25%'],
            ["style", "top", '29.43%']
         ],
         "${_menu-category-sandwich-buffchic_copy}": [
            ["transform", "scaleX", '1'],
            ["style", "top", '0%'],
            ["style", "left", '0px'],
            ["transform", "scaleY", '1']
         ],
         "${_back_blue}": [
            ["style", "top", '734px'],
            ["style", "width", '129px'],
            ["style", "display", 'none'],
            ["style", "height", '129px'],
            ["style", "opacity", '0'],
            ["style", "left", '14px'],
            ["subproperty", "filter.saturate", '0']
         ],
         "${_dorothy_logo012}": [
            ["style", "top", '13px'],
            ["style", "height", '55px'],
            ["style", "left", '24px'],
            ["style", "width", '56px']
         ],
         "${_s1p1Copy}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '337px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "left", '78.33%'],
            ["style", "width", '21px']
         ],
         "${_s1p2Copy2}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '582px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "left", '53.19%'],
            ["style", "width", '21px']
         ],
         "${_coffee_sel_name2}": [
            ["style", "top", '69.26%'],
            ["style", "letter-spacing", '0px'],
            ["style", "width", '9.59%'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "word-spacing", '0px'],
            ["style", "left", '29.66%'],
            ["style", "font-size", '21px']
         ],
         "${_TextCopy}": [
            ["style", "top", '61.96%'],
            ["style", "left", '0px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px']
         ],
         "${_table_no}": [
            ["style", "top", '33px'],
            ["style", "bottom", 'auto'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "right", '101px'],
            ["style", "left", 'auto'],
            ["style", "font-size", '100%']
         ],
         "${_cafelatteCopy2}": [
            ["style", "left", '0px'],
            ["style", "top", '0%']
         ],
         "${_TextCopy11}": [
            ["style", "top", '61.75%'],
            ["style", "text-align", 'center'],
            ["style", "width", '152px'],
            ["style", "left", '0px'],
            ["style", "font-size", '20px']
         ],
         "${_coffee_sel_name3}": [
            ["style", "top", '69.26%'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "left", '43.83%'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '9.59%']
         ],
         "${_cappuccino}": [
            ["style", "left", '0px'],
            ["style", "top", '0%']
         ],
         "${_Text3}": [
            ["color", "color", 'rgba(57,35,13,1.00)'],
            ["style", "left", '118px'],
            ["style", "display", 'none']
         ],
         "${_cafemocha}": [
            ["style", "left", '0px'],
            ["style", "top", '0%']
         ],
         "${_checkout_total}": [
            ["style", "top", '81.27%'],
            ["style", "width", '199px'],
            ["color", "color", 'rgba(100,61,23,1.00)'],
            ["style", "font-weight", '800'],
            ["style", "left", '48%'],
            ["style", "font-size", '25px']
         ],
         "${_P1M1}": [
            ["style", "left", '20px']
         ],
         "${_coffee_sel_name5}": [
            ["style", "top", '69.26%'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "left", '71.89%'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '9.59%']
         ],
         "${_coffee_sel3}": [
            ["style", "top", '70.74%'],
            ["transform", "scaleY", '0.45'],
            ["transform", "scaleX", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '38.41%']
         ],
         "${_P1M5}": [
            ["style", "left", '21px'],
            ["style", "top", '29.43%']
         ],
         "${_TextCopy6}": [
            ["style", "top", '65.69%'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "font-size", '20px'],
            ["style", "left", '42px'],
            ["style", "width", '226px']
         ],
         "${_P3M4}": [
            ["style", "top", '30.21%'],
            ["style", "left", '252%'],
            ["style", "display", 'block']
         ],
         "${_P1M3}": [
            ["style", "left", '51.39%']
         ],
         "${_coffee_sel5}": [
            ["style", "top", '70.67%'],
            ["transform", "scaleY", '0.45'],
            ["transform", "scaleX", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '66.47%']
         ],
         "${_menu-category-sandwich-tuna}": [
            ["transform", "scaleX", '1'],
            ["style", "top", '0%'],
            ["style", "left", '0px'],
            ["transform", "scaleY", '1']
         ],
         "${_espresso_conpanna2}": [
            ["style", "left", '14px'],
            ["style", "top", '0%']
         ],
         "${__03_pp_anwansoon}": [
            ["style", "top", '114px'],
            ["style", "display", 'none'],
            ["style", "height", '154px'],
            ["style", "left", '20px'],
            ["style", "width", '154px']
         ],
         "${_Price}": [
            ["style", "top", '86.15%'],
            ["style", "font-size", '50px'],
            ["color", "color", 'rgba(100,61,23,1.00)'],
            ["style", "font-weight", '800'],
            ["style", "left", '45.63%'],
            ["style", "width", '225px']
         ],
         "${__01}": [
            ["style", "top", '10px'],
            ["style", "bottom", 'auto'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "right", '32px'],
            ["style", "left", 'auto'],
            ["style", "font-size", '320%']
         ],
         "${_s1p3Copy}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '423px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "left", '78.33%'],
            ["style", "width", '21px']
         ],
         "${_Text2Copy}": [
            ["style", "top", '823px'],
            ["style", "width", '76.12%'],
            ["style", "display", 'none'],
            ["style", "height", '13.55%'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "font-weight", '700'],
            ["style", "left", '11.94%'],
            ["style", "font-size", '220%']
         ],
         "${_coffee_sel_name4}": [
            ["style", "top", '69.26%'],
            ["style", "letter-spacing", '0px'],
            ["style", "width", '9.59%'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "word-spacing", '0px'],
            ["style", "left", '57.86%'],
            ["style", "font-size", '21px']
         ],
         "${_accept_blue}": [
            ["style", "top", '83.11%'],
            ["style", "width", '129px'],
            ["style", "right", '28px'],
            ["style", "height", '129px'],
            ["style", "opacity", '1'],
            ["style", "left", 'auto'],
            ["subproperty", "filter.saturate", '1']
         ],
         "${_Text6}": [
            ["style", "top", '-16.65%'],
            ["style", "display", 'none'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "right", '20.83%'],
            ["style", "left", 'auto'],
            ["style", "font-size", '30px']
         ],
         "${_header}": [
            ["color", "background-color", 'rgba(57,35,13,1.00)'],
            ["style", "top", '0px'],
            ["style", "opacity", '0.9'],
            ["style", "height", '80px'],
            ["color", "border-color", 'rgba(57,35,13,1.00)'],
            ["style", "left", '0px'],
            ["style", "width", '2391px']
         ],
         "${_Text}": [
            ["style", "top", '61.96%'],
            ["style", "left", '33px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px']
         ],
         "${_Text2}": [
            ["style", "top", '949px'],
            ["style", "font-size", '180%'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "display", 'none'],
            ["style", "height", '2.55%'],
            ["style", "font-weight", '500'],
            ["style", "left", '28.19%'],
            ["style", "width", '43.89%']
         ],
         "${_Stage}": [
            ["color", "background-color", 'rgba(255,255,255,1)'],
            ["style", "min-width", '100%'],
            ["style", "overflow", 'scroll'],
            ["style", "height", '1414px'],
            ["style", "max-width", '100%'],
            ["style", "width", '100%']
         ],
         "${_cafemochaCopy2}": [
            ["style", "left", '0px'],
            ["style", "top", '0%']
         ],
         "${_s1p4}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '290px'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "left", '59.8%'],
            ["style", "width", '21px']
         ],
         "${_P2M3}": [
            ["style", "left", '157.08%'],
            ["style", "top", '8.42%']
         ],
         "${_TextCopy14}": [
            ["style", "top", '62.77%'],
            ["style", "text-align", 'center'],
            ["style", "left", '22px'],
            ["style", "font-size", '20px']
         ],
         "${_Rectangle2}": [
            ["style", "top", '-794px'],
            ["color", "background-color", 'rgba(57,35,13,1.00)'],
            ["style", "display", 'none'],
            ["color", "border-color", 'rgba(57,35,13,1.00)'],
            ["style", "left", '0%'],
            ["style", "opacity", '0.9']
         ],
         "${_P1M2}": [
            ["style", "left", '25.14%']
         ],
         "${_coffee_sel_name0}": [
            ["style", "top", '69.26%'],
            ["style", "letter-spacing", '0px'],
            ["style", "width", '9.59%'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "word-spacing", '0px'],
            ["style", "left", '1.61%'],
            ["style", "font-size", '21px']
         ],
         "${_copyright}": [
            ["style", "top", '98%'],
            ["style", "width", '100%'],
            ["color", "color", 'rgba(100,61,23,0.37)'],
            ["style", "height", '24px'],
            ["style", "left", '0.14%'],
            ["style", "font-size", '70%']
         ],
         "${_Kobuki_00}": [
            ["style", "top", '473px'],
            ["style", "display", 'none'],
            ["style", "height", '239px'],
            ["style", "opacity", '0.2'],
            ["style", "left", '63px'],
            ["style", "width", '195px']
         ],
         "${_espresso}": [
            ["style", "left", '0px'],
            ["style", "top", '0%']
         ],
         "${_sandwitch_slot0}": [
            ["style", "top", '76.82%'],
            ["transform", "scaleY", '0.4'],
            ["transform", "scaleX", '0.4'],
            ["style", "left", '-81px'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_s1p2}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '290px'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "left", '46.33%'],
            ["style", "width", '21px']
         ],
         "${_P1M4}": [
            ["style", "left", '75.56%'],
            ["style", "right", 'auto']
         ],
         "${_TextCopy10}": [
            ["style", "top", '61.75%'],
            ["style", "text-align", 'center'],
            ["style", "width", '148px'],
            ["style", "left", '2px'],
            ["style", "font-size", '20px']
         ],
         "${_cafelatteCopy4}": [
            ["style", "left", '0px'],
            ["style", "top", '0%']
         ],
         "${_cafelatteCopy}": [
            ["style", "left", '0px'],
            ["style", "top", '0%']
         ],
         "${_coffee_sel6}": [
            ["style", "top", '70.74%'],
            ["transform", "scaleY", '0.45'],
            ["style", "display", 'block'],
            ["style", "opacity", '1'],
            ["style", "left", '80.22%'],
            ["transform", "scaleX", '0.45']
         ],
         "${_delete}": [
            ["style", "top", '-12.19%'],
            ["style", "display", 'none'],
            ["style", "height", '144px'],
            ["style", "left", '15.48%'],
            ["style", "width", '145px']
         ],
         "${_Text4}": [
            ["style", "top", '283px'],
            ["style", "right", '4.58%'],
            ["style", "bottom", 'auto'],
            ["style", "display", 'none'],
            ["style", "opacity", '0.2'],
            ["style", "left", 'auto'],
            ["style", "width", '225px']
         ],
         "${_TextCopy2}": [
            ["style", "top", '55.07%'],
            ["style", "text-align", 'center'],
            ["style", "left", '4px'],
            ["style", "font-size", '20px']
         ],
         "${_coffee_sel0}": [
            ["style", "top", '70.74%'],
            ["transform", "scaleY", '0.45'],
            ["transform", "scaleX", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '-28px']
         ],
         "${_P3M2}": [
            ["style", "top", '8.56%'],
            ["style", "left", '251.75%'],
            ["style", "display", 'block']
         ],
         "${_TextCopy5}": [
            ["style", "top", '66.82%'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "width", '168px'],
            ["style", "left", '71px'],
            ["style", "font-size", '20px']
         ],
         "${_rocon_logo}": [
            ["style", "-webkit-transform-origin", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ],
            ["style", "-moz-transform-origin", [50,50],{valueTemplate:'@@0@@% @@1@@%'}],
            ["style", "-ms-transform-origin", [50,50],{valueTemplate:'@@0@@% @@1@@%'}],
            ["style", "msTransformOrigin", [50,50],{valueTemplate:'@@0@@% @@1@@%'}],
            ["style", "-o-transform-origin", [50,50],{valueTemplate:'@@0@@% @@1@@%'}],
            ["style", "bottom", 'auto'],
            ["transform", "scaleX", '0.4'],
            ["style", "right", 'auto'],
            ["style", "left", '21.68%'],
            ["style", "width", '111.17%'],
            ["style", "top", '83.96%'],
            ["transform", "scaleY", '0.4'],
            ["style", "height", '284px'],
            ["style", "background-size", [649.65,'auto'], {valueTemplate:'@@0@@px @@1@@'} ],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ],
            ["style", "opacity", '1']
         ],
         "${_SANDWITCH_TITLE}": [
            ["style", "top", '51.48%'],
            ["style", "opacity", '0'],
            ["style", "left", '33.82%'],
            ["style", "display", 'block'],
            ["style", "background-size", [224,'auto'], {valueTemplate:'@@0@@px @@1@@'} ],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ],
            ["style", "height", '10%']
         ],
         "${_fron_blue}": [
            ["style", "top", '51.9%'],
            ["style", "width", '129px'],
            ["style", "height", '129px'],
            ["style", "right", '22px'],
            ["style", "display", 'block'],
            ["style", "opacity", '1'],
            ["style", "left", 'auto'],
            ["subproperty", "filter.saturate", '1']
         ],
         "${_P1M6}": [
            ["style", "left", '27.08%'],
            ["style", "top", '29.43%']
         ],
         "${_TextCopy17}": [
            ["style", "top", '118px'],
            ["style", "left", '22px'],
            ["style", "font-size", '20px']
         ],
         "${_cafelatte}": [
            ["style", "left", '0px'],
            ["style", "top", '0%']
         ],
         "${_COFFEE_TITLE}": [
            ["style", "top", '53.38%'],
            ["style", "opacity", '1'],
            ["style", "background-size", [400,'auto'], {valueTemplate:'@@0@@px @@1@@'} ],
            ["style", "left", '21.6%'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
         ],
         "${_P3M1}": [
            ["style", "top", '8.56%'],
            ["style", "left", '205.09%'],
            ["style", "display", 'block']
         ],
         "${_TextCopy16}": [
            ["style", "top", '118px'],
            ["style", "left", '22px'],
            ["style", "font-size", '20px']
         ],
         "${_Text4Copy2}": [
            ["style", "top", '705px'],
            ["style", "display", 'none'],
            ["style", "height", '56px'],
            ["style", "opacity", '0.2'],
            ["style", "left", '71px'],
            ["style", "width", '182px']
         ],
         "${_dorothy_cafe}": [
            ["style", "top", '10px'],
            ["style", "width", '324px'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "height", '59px'],
            ["style", "left", '89px'],
            ["style", "font-size", '320%']
         ],
         "${_s1p2Copy}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '380px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "left", '78.33%'],
            ["style", "width", '21px']
         ],
         "${_coffee_sel4}": [
            ["style", "top", '70.74%'],
            ["transform", "scaleY", '0.45'],
            ["transform", "scaleX", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '52.3%']
         ],
         "${_cafemochaCopy}": [
            ["style", "left", '0px'],
            ["style", "top", '0%']
         ],
         "${_Text7}": [
            ["style", "top", '-16.65%'],
            ["style", "display", 'none'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "left", '18.33%'],
            ["style", "font-size", '30px']
         ],
         "${_TextCopy13}": [
            ["style", "top", '62.77%'],
            ["style", "text-align", 'center'],
            ["style", "width", '160px'],
            ["style", "left", '-3px'],
            ["style", "font-size", '20px']
         ],
         "${_TextCopy4}": [
            ["style", "top", '66.67%'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "font-size", '20px'],
            ["style", "left", '46px'],
            ["style", "width", '217px']
         ],
         "${__410_anwansoon2}": [
            ["style", "top", '499px'],
            ["style", "height", '199px'],
            ["style", "right", '6.39%'],
            ["style", "bottom", 'auto'],
            ["style", "display", 'none'],
            ["style", "opacity", '0.2'],
            ["style", "left", 'auto'],
            ["style", "width", '199px']
         ],
         "${_Text5}": [
            ["style", "top", '-521px'],
            ["style", "font-size", '40px'],
            ["style", "text-align", 'center'],
            ["color", "color", 'rgba(255,255,255,1.00)'],
            ["style", "height", '6.79%'],
            ["style", "display", 'none'],
            ["style", "left", '14.03%'],
            ["style", "width", '70.84%']
         ],
         "${_nfc_logo}": [
            ["style", "top", '164px'],
            ["style", "height", '55px'],
            ["style", "display", 'none'],
            ["style", "left", '137px'],
            ["style", "width", '200px']
         ],
         "${_s1p4Copy}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '465px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "left", '78.33%'],
            ["style", "width", '21px']
         ],
         "${_sandwich_sel_name0}": [
            ["style", "top", '81.98%'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "left", '2.75%'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '18.49%']
         ],
         "${_coffee_sel2}": [
            ["style", "top", '70.74%'],
            ["transform", "scaleY", '0.45'],
            ["transform", "scaleX", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '24.53%']
         ],
         "${_s1p1Copy2}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '582px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "left", '59.86%'],
            ["style", "width", '21px']
         ],
         "${_a4_nomal_png_a}": [
            ["style", "top", '105px'],
            ["style", "height", '163px'],
            ["style", "right", '8.19%'],
            ["style", "bottom", 'auto'],
            ["style", "display", 'none'],
            ["style", "opacity", '0.2'],
            ["style", "left", 'auto'],
            ["style", "width", '104px']
         ],
         "${_Rectangle}": [
            ["style", "top", '796px'],
            ["style", "height", '506px'],
            ["color", "border-color", 'rgba(0,0,0,0.00)'],
            ["style", "display", 'none'],
            ["style", "opacity", '0.9'],
            ["style", "left", '-0.27%'],
            ["style", "width", '100.41%']
         ],
         "${_sandwich_sel_name1}": [
            ["style", "top", '81.98%'],
            ["style", "letter-spacing", '0px'],
            ["style", "width", '18.49%'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "word-spacing", '0px'],
            ["style", "left", '23.31%'],
            ["style", "font-size", '21px']
         ],
         "${_s1p1}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '289px'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "left", '39.66%'],
            ["style", "width", '21px']
         ],
         "${_coffee_sel_name6}": [
            ["style", "top", '69.26%'],
            ["style", "letter-spacing", '0em'],
            ["style", "font-size", '131.25%'],
            ["style", "text-indent", '0%'],
            ["style", "height", '42px'],
            ["style", "left", '85.97%'],
            ["style", "word-spacing", '0em'],
            ["style", "width", '69px']
         ],
         "${_TextCopy3}": [
            ["style", "top", '55.07%'],
            ["style", "left", '30px'],
            ["style", "text-align", 'center'],
            ["style", "font-size", '20px']
         ],
         "${_s1p3}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '290px'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "left", '53.13%'],
            ["style", "width", '21px']
         ],
         "${_status_text}": [
            ["style", "letter-spacing", '0em'],
            ["style", "bottom", 'auto'],
            ["color", "color", 'rgba(100,61,23,0.49)'],
            ["style", "right", 'auto'],
            ["style", "left", '8px'],
            ["style", "font-size", '100%'],
            ["style", "top", '94.64%'],
            ["style", "font-weight", '200'],
            ["style", "text-align", 'left'],
            ["style", "text-indent", '0%'],
            ["style", "height", '20px'],
            ["style", "width", '99.05%'],
            ["style", "word-spacing", '0em'],
            ["style", "opacity", '1']
         ],
         "${_coffee_sel1}": [
            ["style", "top", '70.74%'],
            ["transform", "scaleY", '0.45'],
            ["transform", "scaleX", '0.45'],
            ["style", "opacity", '1'],
            ["style", "left", '10.64%']
         ],
         "${_dorothy_logo012Copy}": [
            ["style", "top", '72.21%'],
            ["style", "height", '17.33%'],
            ["style", "left", '32.64%'],
            ["style", "display", 'none'],
            ["style", "opacity", '0.4'],
            ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ],
            ["style", "width", '34.73%']
         ],
         "${_P3M3}": [
            ["style", "top", '30.21%'],
            ["style", "left", '203.67%'],
            ["style", "display", 'block']
         ],
         "${_TextCopy8}": [
            ["style", "top", '62.77%'],
            ["style", "text-align", 'center'],
            ["style", "left", '22px'],
            ["style", "font-size", '20px']
         ],
         "${_menu-category-sandwich-stkchs_copy}": [
            ["transform", "scaleX", '1'],
            ["style", "top", '0%'],
            ["style", "left", '0px'],
            ["transform", "scaleY", '1']
         ],
         "${_s1p3Copy2}": [
            ["color", "background-color", 'rgba(67,222,254,1.00)'],
            ["style", "top", '582px'],
            ["style", "display", 'none'],
            ["style", "opacity", '1'],
            ["style", "height", '22px'],
            ["subproperty", "filter.blur", '7.1664663461538px'],
            ["style", "left", '46.39%'],
            ["style", "width", '21px']
         ],
         "${_menu-category-sandwich-italbmt_copy}": [
            ["transform", "scaleX", '1'],
            ["style", "top", '0%'],
            ["style", "left", '0px'],
            ["transform", "scaleY", '1']
         ],
         "${_order}": [
            ["style", "top", '81.27%'],
            ["style", "font-size", '25px'],
            ["style", "right", '17px'],
            ["color", "color", 'rgba(100,61,23,1.00)'],
            ["style", "font-weight", '800'],
            ["style", "left", 'auto'],
            ["style", "width", '115px']
         ],
         "${_P1M7}": [
            ["style", "left", '51.25%'],
            ["style", "top", '29.43%']
         ],
         "${_P2M2}": [
            ["style", "left", '132.52%'],
            ["style", "top", '8.42%']
         ],
         "${_TextCopy7}": [
            ["style", "top", '65.69%'],
            ["style", "text-align", 'center'],
            ["style", "height", '70px'],
            ["style", "width", '199px'],
            ["style", "left", '55px'],
            ["style", "font-size", '20px']
         ],
         "${_coffee_sel_name1}": [
            ["style", "top", '69.26%'],
            ["style", "letter-spacing", '0px'],
            ["style", "font-size", '21px'],
            ["style", "text-indent", '0px'],
            ["style", "height", '42px'],
            ["style", "left", '15.64%'],
            ["style", "word-spacing", '0px'],
            ["style", "width", '9.59%']
         ]
      }
   },
   timelines: {
      "Default Timeline": {
         fromState: "Base State",
         toState: "",
         duration: 6000,
         autoPlay: true,
         timeline: [
            { id: "eid1764", tween: [ "style", "${_P1M2}", "left", '-74.07%', { fromValue: '25.14%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1963", tween: [ "style", "${_P1M2}", "left", '-173.59%', { fromValue: '-74.07%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1978", tween: [ "style", "${_P1M2}", "left", '-173.59%', { fromValue: '-173.59%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2211", tween: [ "style", "${_s1p2}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid2200", tween: [ "style", "${_s1p2}", "display", 'none', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2202", tween: [ "style", "${_s1p2}", "display", 'block', { fromValue: 'none'}], position: 3250, duration: 0 },
            { id: "eid2162", tween: [ "style", "${__114_anwansoonfge}", "opacity", '1', { fromValue: '0.20000000298023224'}], position: 3000, duration: 1000 },
            { id: "eid2212", tween: [ "style", "${_s1p3}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid2199", tween: [ "style", "${_s1p3}", "display", 'none', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2203", tween: [ "style", "${_s1p3}", "display", 'block', { fromValue: 'none'}], position: 3500, duration: 0 },
            { id: "eid2144", tween: [ "style", "${_nfc_logo}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid1942", tween: [ "style", "${_P3M1}", "left", '104.34%', { fromValue: '205.09%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1974", tween: [ "style", "${_P3M1}", "left", '4.82%', { fromValue: '104.34%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1989", tween: [ "style", "${_P3M1}", "left", '4.82%', { fromValue: '4.82%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2135", tween: [ "style", "${_dorothy_logo012Copy}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2281", tween: [ "style", "${_delete}", "top", '49.55%', { fromValue: '-12.19%'}], position: 2059, duration: 821, easing: "easeOutBounce" },
            { id: "eid2217", tween: [ "style", "${_s1p3Copy}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid2218", tween: [ "style", "${_s1p3Copy}", "display", 'none', { fromValue: 'none'}], position: 4000, duration: 0 },
            { id: "eid2219", tween: [ "style", "${_s1p3Copy}", "display", 'block', { fromValue: 'none'}], position: 4500, duration: 0 },
            { id: "eid2265", tween: [ "style", "${_Rectangle}", "left", '-0.27%', { fromValue: '-0.27%'}], position: 3000, duration: 0 },
            { id: "eid2149", tween: [ "style", "${_Text4}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2152", tween: [ "style", "${_Text4Copy2}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2213", tween: [ "style", "${_s1p4}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid2198", tween: [ "style", "${_s1p4}", "display", 'none', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2204", tween: [ "style", "${_s1p4}", "display", 'block', { fromValue: 'none'}], position: 3750, duration: 0 },
            { id: "eid1914", tween: [ "style", "${_P2M2}", "left", '28.24%', { fromValue: '132.52%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1969", tween: [ "style", "${_P2M2}", "left", '-71.28%', { fromValue: '28.24%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1984", tween: [ "style", "${_P2M2}", "left", '-71.28%', { fromValue: '-71.28%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2259", tween: [ "subproperty", "${_accept_blue}", "filter.saturate", '1', { fromValue: '1'}], position: 0, duration: 0 },
            { id: "eid2260", tween: [ "subproperty", "${_accept_blue}", "filter.saturate", '0', { fromValue: '1'}], position: 2500, duration: 0 },
            { id: "eid2243", tween: [ "style", "${_Rectangle2}", "display", 'block', { fromValue: 'none'}], position: 2059, duration: 0 },
            { id: "eid2250", tween: [ "style", "${_Rectangle2}", "display", 'block', { fromValue: 'block'}], position: 2567, duration: 0 },
            { id: "eid2294", tween: [ "style", "${_Rectangle2}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0, easing: "easeOutBounce" },
            { id: "eid2007", tween: [ "style", "${_P1M4}", "left", '-23.64%', { fromValue: '75.56%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid2008", tween: [ "style", "${_P1M4}", "left", '-123.16%', { fromValue: '-23.64%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid2009", tween: [ "style", "${_P1M4}", "left", '-123.16%', { fromValue: '-123.16%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2150", tween: [ "style", "${__410_anwansoon2}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2132", tween: [ "style", "${_Text2}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid1915", tween: [ "style", "${_P2M3}", "left", '53.19%', { fromValue: '157.08%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1967", tween: [ "style", "${_P2M3}", "left", '-46.33%', { fromValue: '53.19%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1982", tween: [ "style", "${_P2M3}", "left", '-46.33%', { fromValue: '-46.33%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2237", tween: [ "style", "${_back_blue}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid2238", tween: [ "style", "${_back_blue}", "display", 'block', { fromValue: 'none'}], position: 49, duration: 0 },
            { id: "eid2139", tween: [ "style", "${_back_blue}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0 },
            { id: "eid1896", tween: [ "style", "${_P1M6}", "left", '-72.09%', { fromValue: '27.08%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1970", tween: [ "style", "${_P1M6}", "left", '-171.61%', { fromValue: '-72.09%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1985", tween: [ "style", "${_P1M6}", "left", '-171.61%', { fromValue: '-171.61%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2138", tween: [ "style", "${_SANDWITCH_TITLE}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0 },
            { id: "eid2228", tween: [ "style", "${_s1p3Copy2}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid2229", tween: [ "style", "${_s1p3Copy2}", "display", 'none', { fromValue: 'none'}], position: 5000, duration: 0 },
            { id: "eid2230", tween: [ "style", "${_s1p3Copy2}", "display", 'block', { fromValue: 'none'}], position: 5500, duration: 0 },
            { id: "eid2235", tween: [ "style", "${_s1p1Copy2}", "opacity", '1', { fromValue: '1'}], position: 5000, duration: 0 },
            { id: "eid2126", tween: [ "subproperty", "${_fron_blue}", "filter.saturate", '0', { fromValue: '1'}], position: 1000, duration: 1000 },
            { id: "eid2151", tween: [ "style", "${_Kobuki_00}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2241", tween: [ "style", "${_Text7}", "display", 'block', { fromValue: 'none'}], position: 2059, duration: 0 },
            { id: "eid2247", tween: [ "style", "${_Text7}", "display", 'block', { fromValue: 'block'}], position: 2567, duration: 0 },
            { id: "eid2291", tween: [ "style", "${_Text7}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0, easing: "easeOutBounce" },
            { id: "eid2141", tween: [ "style", "${_P3M4}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0 },
            { id: "eid1762", tween: [ "style", "${_P1M3}", "left", '-47.82%', { fromValue: '51.39%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1964", tween: [ "style", "${_P1M3}", "left", '-147.34%', { fromValue: '-47.82%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1979", tween: [ "style", "${_P1M3}", "left", '-147.34%', { fromValue: '-147.34%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2239", tween: [ "style", "${_accept_blue2}", "display", 'block', { fromValue: 'none'}], position: 2059, duration: 0 },
            { id: "eid2245", tween: [ "style", "${_accept_blue2}", "display", 'block', { fromValue: 'block'}], position: 2567, duration: 0 },
            { id: "eid2289", tween: [ "style", "${_accept_blue2}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0, easing: "easeOutBounce" },
            { id: "eid1900", tween: [ "style", "${_P1M7}", "left", '-47.92%', { fromValue: '51.25%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1971", tween: [ "style", "${_P1M7}", "left", '-147.44%', { fromValue: '-47.92%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1986", tween: [ "style", "${_P1M7}", "left", '-147.44%', { fromValue: '-147.44%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2234", tween: [ "style", "${_s1p1Copy2}", "display", 'block', { fromValue: 'none'}], position: 5000, duration: 0 },
            { id: "eid1902", tween: [ "style", "${_P1M8}", "left", '-22.92%', { fromValue: '76.25%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1976", tween: [ "style", "${_P1M8}", "left", '-122.44%', { fromValue: '-22.92%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1991", tween: [ "style", "${_P1M8}", "left", '-122.44%', { fromValue: '-122.44%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2147", tween: [ "style", "${__114_anwansoonfge}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2153", tween: [ "style", "${_Text4Copy}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid1893", tween: [ "style", "${_P1M5}", "left", '-693px', { fromValue: '21px'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1973", tween: [ "style", "${_P1M5}", "left", '-1410px', { fromValue: '-693px'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1988", tween: [ "style", "${_P1M5}", "left", '-1410px', { fromValue: '-1410px'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2156", tween: [ "style", "${_Kobuki_00}", "opacity", '0.2', { fromValue: '0.2'}], position: 3000, duration: 0 },
            { id: "eid2167", tween: [ "style", "${_Kobuki_00}", "opacity", '1', { fromValue: '0.20000000298023224'}], position: 5000, duration: 1000 },
            { id: "eid2154", tween: [ "style", "${__410_anwansoon2}", "opacity", '0.2', { fromValue: '0.2'}], position: 3000, duration: 0 },
            { id: "eid2164", tween: [ "style", "${__410_anwansoon2}", "opacity", '1', { fromValue: '0.20000000298023224'}], position: 4000, duration: 1000 },
            { id: "eid2244", tween: [ "style", "${_Text5}", "display", 'block', { fromValue: 'none'}], position: 2059, duration: 0 },
            { id: "eid2249", tween: [ "style", "${_Text5}", "display", 'block', { fromValue: 'block'}], position: 2567, duration: 0 },
            { id: "eid2293", tween: [ "style", "${_Text5}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0, easing: "easeOutBounce" },
            { id: "eid2158", tween: [ "style", "${_Text4Copy2}", "opacity", '0.2', { fromValue: '0.2'}], position: 3000, duration: 0 },
            { id: "eid2166", tween: [ "style", "${_Text4Copy2}", "opacity", '1', { fromValue: '0.20000000298023224'}], position: 5000, duration: 1000 },
            { id: "eid1946", tween: [ "style", "${_P3M2}", "left", '151%', { fromValue: '251.75%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1972", tween: [ "style", "${_P3M2}", "left", '51.48%', { fromValue: '151%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1987", tween: [ "style", "${_P3M2}", "left", '51.48%', { fromValue: '51.48%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2282", tween: [ "style", "${_Rectangle2}", "top", '79px', { fromValue: '-794px'}], position: 2059, duration: 821, easing: "easeOutBounce" },
            { id: "eid2242", tween: [ "style", "${_delete}", "display", 'block', { fromValue: 'none'}], position: 2059, duration: 0 },
            { id: "eid2248", tween: [ "style", "${_delete}", "display", 'block', { fromValue: 'block'}], position: 2567, duration: 0 },
            { id: "eid2290", tween: [ "style", "${_delete}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0, easing: "easeOutBounce" },
            { id: "eid2131", tween: [ "style", "${_Rectangle}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2277", tween: [ "style", "${_Text6}", "top", '45.09%', { fromValue: '-16.65%'}], position: 2059, duration: 821, easing: "easeOutBounce" },
            { id: "eid2128", tween: [ "style", "${_back_blue}", "opacity", '1', { fromValue: '0'}], position: 0, duration: 1000 },
            { id: "eid2231", tween: [ "style", "${_s1p2Copy2}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid2232", tween: [ "style", "${_s1p2Copy2}", "display", 'none', { fromValue: 'none'}], position: 5000, duration: 0 },
            { id: "eid2233", tween: [ "style", "${_s1p2Copy2}", "display", 'block', { fromValue: 'none'}], position: 5250, duration: 0 },
            { id: "eid1803", tween: [ "style", "${_SANDWITCH_TITLE}", "opacity", '1', { fromValue: '0'}], position: 1000, duration: 1000 },
            { id: "eid1804", tween: [ "style", "${_SANDWITCH_TITLE}", "opacity", '1', { fromValue: '1'}], position: 2000, duration: 0 },
            { id: "eid2300", tween: [ "style", "${_Rectangle}", "opacity", '1', { fromValue: '0.9'}], position: 5950, duration: 50 },
            { id: "eid2236", tween: [ "style", "${_fron_blue}", "display", 'none', { fromValue: 'block'}], position: 2000, duration: 0 },
            { id: "eid2137", tween: [ "style", "${_fron_blue}", "display", 'none', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2161", tween: [ "style", "${_Text4}", "opacity", '1', { fromValue: '0.20000000298023224'}], position: 3000, duration: 1000 },
            { id: "eid2240", tween: [ "style", "${_Text6}", "display", 'block', { fromValue: 'none'}], position: 2059, duration: 0 },
            { id: "eid2246", tween: [ "style", "${_Text6}", "display", 'block', { fromValue: 'block'}], position: 2567, duration: 0 },
            { id: "eid2292", tween: [ "style", "${_Text6}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0, easing: "easeOutBounce" },
            { id: "eid2224", tween: [ "style", "${_s1p1Copy}", "opacity", '1', { fromValue: '1'}], position: 4000, duration: 0 },
            { id: "eid2225", tween: [ "style", "${_s1p4Copy2}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid2226", tween: [ "style", "${_s1p4Copy2}", "display", 'none', { fromValue: 'none'}], position: 5000, duration: 0 },
            { id: "eid2227", tween: [ "style", "${_s1p4Copy2}", "display", 'block', { fromValue: 'none'}], position: 5750, duration: 0 },
            { id: "eid2223", tween: [ "style", "${_s1p1Copy}", "display", 'block', { fromValue: 'none'}], position: 4000, duration: 0 },
            { id: "eid1938", tween: [ "style", "${_P3M3}", "left", '102.92%', { fromValue: '203.67%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1968", tween: [ "style", "${_P3M3}", "left", '3.4%', { fromValue: '102.92%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1983", tween: [ "style", "${_P3M3}", "left", '3.4%', { fromValue: '3.4%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2201", tween: [ "style", "${_s1p1}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2143", tween: [ "style", "${_P3M1}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0 },
            { id: "eid2197", tween: [ "style", "${_s1p1}", "opacity", '1', { fromValue: '1'}], position: 3000, duration: 0 },
            { id: "eid2109", tween: [ "style", "${_coffee_sel6}", "display", 'block', { fromValue: 'block'}], position: 0, duration: 0 },
            { id: "eid2163", tween: [ "style", "${_a4_nomal_png_a}", "opacity", '1', { fromValue: '0.20000000298023224'}], position: 3000, duration: 1000 },
            { id: "eid2280", tween: [ "style", "${_Text5}", "top", '352px', { fromValue: '-521px'}], position: 2059, duration: 821, easing: "easeOutBounce" },
            { id: "eid2133", tween: [ "style", "${_Text2Copy}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2266", tween: [ "style", "${_Rectangle}", "top", '796px', { fromValue: '796px'}], position: 3000, duration: 0 },
            { id: "eid2279", tween: [ "style", "${_Text7}", "top", '45.09%', { fromValue: '-16.65%'}], position: 2059, duration: 821, easing: "easeOutBounce" },
            { id: "eid1950", tween: [ "style", "${_P3M4}", "left", '151.25%', { fromValue: '252%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1975", tween: [ "style", "${_P3M4}", "left", '51.73%', { fromValue: '151.25%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1990", tween: [ "style", "${_P3M4}", "left", '51.73%', { fromValue: '51.73%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2130", tween: [ "subproperty", "${_back_blue}", "filter.saturate", '1', { fromValue: '0'}], position: 0, duration: 1000 },
            { id: "eid1800", tween: [ "style", "${_COFFEE_TITLE}", "opacity", '0', { fromValue: '1'}], position: 1000, duration: 1000 },
            { id: "eid1801", tween: [ "style", "${_COFFEE_TITLE}", "opacity", '0.000000', { fromValue: '0.000000'}], position: 2000, duration: 0 },
            { id: "eid2146", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2125", tween: [ "style", "${_fron_blue}", "opacity", '0', { fromValue: '1'}], position: 1000, duration: 1000 },
            { id: "eid2148", tween: [ "style", "${_a4_nomal_png_a}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2145", tween: [ "style", "${__03_pp_anwansoon}", "display", 'block', { fromValue: 'none'}], position: 3000, duration: 0 },
            { id: "eid2263", tween: [ "style", "${_accept_blue}", "opacity", '1', { fromValue: '1'}], position: 0, duration: 0 },
            { id: "eid2264", tween: [ "style", "${_accept_blue}", "opacity", '0.50350952148438', { fromValue: '1'}], position: 2500, duration: 0 },
            { id: "eid1908", tween: [ "style", "${_P2M1}", "left", '3.33%', { fromValue: '106.1%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1965", tween: [ "style", "${_P2M1}", "left", '-96.19%', { fromValue: '3.33%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1980", tween: [ "style", "${_P2M1}", "left", '-96.25%', { fromValue: '-96.25%'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2142", tween: [ "style", "${_P3M2}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0 },
            { id: "eid2155", tween: [ "style", "${_Text4Copy}", "opacity", '0.2', { fromValue: '0.2'}], position: 3000, duration: 0 },
            { id: "eid2165", tween: [ "style", "${_Text4Copy}", "opacity", '1', { fromValue: '0.20000000298023224'}], position: 4000, duration: 1000 },
            { id: "eid2140", tween: [ "style", "${_P3M3}", "display", 'none', { fromValue: 'block'}], position: 3000, duration: 0 },
            { id: "eid2214", tween: [ "style", "${_s1p4Copy}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid2215", tween: [ "style", "${_s1p4Copy}", "display", 'none', { fromValue: 'none'}], position: 4000, duration: 0 },
            { id: "eid2216", tween: [ "style", "${_s1p4Copy}", "display", 'block', { fromValue: 'none'}], position: 4750, duration: 0 },
            { id: "eid2220", tween: [ "style", "${_s1p2Copy}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
            { id: "eid2221", tween: [ "style", "${_s1p2Copy}", "display", 'none', { fromValue: 'none'}], position: 4000, duration: 0 },
            { id: "eid2222", tween: [ "style", "${_s1p2Copy}", "display", 'block', { fromValue: 'none'}], position: 4250, duration: 0 },
            { id: "eid1763", tween: [ "style", "${_P1M1}", "left", '-694px', { fromValue: '20px'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1962", tween: [ "style", "${_P1M1}", "left", '-1411px', { fromValue: '-694px'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
            { id: "eid1977", tween: [ "style", "${_P1M1}", "left", '-1411px', { fromValue: '-1411px'}], position: 2000, duration: 0, easing: "easeOutQuint" },
            { id: "eid2278", tween: [ "style", "${_accept_blue2}", "top", '49.55%', { fromValue: '-12.19%'}], position: 2059, duration: 821, easing: "easeOutBounce" }         ]
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
