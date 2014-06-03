/**
 * Adobe Edge: symbol definitions
 */
(function($, Edge, compId){
//images folder
var im='images/';

var fonts = {};
var opts = {};
var resources = [
];
var symbols = {
"stage": {
    version: "3.0.0",
    minimumCompatibleVersion: "3.0.0",
    build: "3.0.0.322",
    baseState: "Base State",
    scaleToFit: "none",
    centerStage: "none",
    initialState: "Base State",
    gpuAccelerate: false,
    resizeInstances: false,
    content: {
            dom: [
            {
                id: 'rocon_logo',
                type: 'image',
                rect: ['21.7%', '84%','111.2%','284px','auto', 'auto'],
                opacity: 1,
                fill: ["rgba(0,0,0,0)",im+"a4_nomal_png_c.png",'50%','50%','649.65px','auto'],
                transform: [[],[],[],['0.4','0.4']]
            },
            {
                id: 'oder_management',
                type: 'text',
                rect: ['-10px', '93.2%','48.1%','19px','auto', 'auto'],
                opacity: 1,
                text: "ROCON Order Management System",
                align: "center",
                font: ['Arial, Helvetica, sans-serif', [500, "%"], "rgba(100,61,23,1.00)", "200", "none", "normal"]
            },
            {
                id: 'status_text',
                type: 'text',
                rect: ['8px', '94.6%','99.1%','19px','auto', 'auto'],
                opacity: 1,
                text: "Status: ",
                align: "left",
                font: ['Arial, Helvetica, sans-serif', [100, "%"], "rgba(100,61,23,1.00)", "200", "none", "normal"]
            },
            {
                id: 'copyright',
                type: 'text',
                rect: ['0.1%', '98%','100%','24px','auto', 'auto'],
                text: "Copyright YUJIN ROBOT co., Ltd. All rights reserved including the right of reproduction in whole or in part in any form. mobile",
                align: "center",
                font: ['Arial, Helvetica, sans-serif', [70, "%"], "rgba(100,61,23,0.37)", "800", "none", "normal"]
            },
            {
                id: 'sandwitch_slot0',
                type: 'image',
                tag: 'img',
                rect: ['-81px', '76.8%','322px','322px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"sandwitch_empty.png",'50%','50%','322px','322px'],
                transform: [[],[],[],['0.4','0.4']]
            },
            {
                id: 'sandwitch_slot1',
                type: 'image',
                tag: 'img',
                rect: ['10.5%', '76.9%','322px','322px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"sandwitch_empty.png",'50%','50%','322px','322px'],
                transform: [[],[],[],['0.4','0.4']]
            },
            {
                id: 'checkout_total',
                type: 'text',
                rect: ['48%', '81.3%','199px','auto','auto', 'auto'],
                text: "Checkout Total",
                font: ['Arial, Helvetica, sans-serif', 25, "rgba(100,61,23,1.00)", "800", "none", ""]
            },
            {
                id: 'Price',
                type: 'text',
                rect: ['45.6%', '86.2%','225px','auto','auto', 'auto'],
                text: "₩ 0",
                font: ['Arial, Helvetica, sans-serif', 50, "rgba(100,61,23,1.00)", "800", "none", ""]
            },
            {
                id: 'order',
                type: 'text',
                rect: ['auto', '81.3%','160px','auto','8px', 'auto'],
                text: "Place Order",
                font: ['Arial, Helvetica, sans-serif', 25, "rgba(100,61,23,1.00)", "800", "none", ""]
            },
            {
                id: 'coffee_sel0',
                type: 'image',
                tag: 'img',
                rect: ['-28px', '70.7%','152px','102px','auto', 'auto'],
                opacity: 1,
                fill: ["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
                transform: [[],[],[],['0.45','0.45']]
            },
            {
                id: 'coffee_sel1',
                type: 'image',
                tag: 'img',
                rect: ['10.6%', '70.7%','152px','102px','auto', 'auto'],
                opacity: 1,
                fill: ["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
                transform: [[],[],[],['0.45','0.45']]
            },
            {
                id: 'coffee_sel2',
                type: 'image',
                tag: 'img',
                rect: ['24.5%', '70.7%','152px','102px','auto', 'auto'],
                opacity: 1,
                fill: ["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
                transform: [[],[],[],['0.45','0.45']]
            },
            {
                id: 'coffee_sel3',
                type: 'image',
                tag: 'img',
                rect: ['38.4%', '70.7%','152px','102px','auto', 'auto'],
                opacity: 1,
                fill: ["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
                transform: [[],[],[],['0.45','0.45']]
            },
            {
                id: 'coffee_sel4',
                type: 'image',
                tag: 'img',
                rect: ['52.3%', '70.7%','152px','102px','auto', 'auto'],
                opacity: 1,
                fill: ["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
                transform: [[],[],[],['0.45','0.45']]
            },
            {
                id: 'coffee_sel5',
                type: 'image',
                tag: 'img',
                rect: ['66.5%', '70.7%','152px','102px','auto', 'auto'],
                opacity: 1,
                fill: ["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
                transform: [[],[],[],['0.45','0.45']]
            },
            {
                id: 'coffee_sel6',
                display: 'block',
                type: 'image',
                tag: 'img',
                rect: ['80.2%', '70.7%','152px','102px','auto', 'auto'],
                opacity: 1,
                fill: ["rgba(0,0,0,0)",im+"coffee_empty2.png",'0px','0px'],
                transform: [[],[],[],['0.45','0.45']]
            },
            {
                id: 'coffee_sel_name0',
                type: 'text',
                rect: ['1.6%', '69.3%','9.6%','42px','auto', 'auto'],
                font: ['Arial, Helvetica, sans-serif', 19.2, "rgba(0,0,0,1)", "normal", "none", ""]
            },
            {
                id: 'sandwich_sel_name0',
                type: 'text',
                rect: ['2.8%', '82%','18.5%','42px','auto', 'auto'],
                font: ['Arial, Helvetica, sans-serif', 19.2, "rgba(0,0,0,1)", "normal", "none", ""]
            },
            {
                id: 'sandwich_sel_name1',
                type: 'text',
                rect: ['23.3%', '82%','18.5%','42px','auto', 'auto'],
                font: ['Arial, Helvetica, sans-serif', 19.2, "rgba(0,0,0,1)", "normal", "none", ""]
            },
            {
                id: 'coffee_sel_name1',
                type: 'text',
                rect: ['15.6%', '69.3%','9.6%','42px','auto', 'auto'],
                font: ['Arial, Helvetica, sans-serif', 19.2, "rgba(0,0,0,1)", "normal", "none", ""]
            },
            {
                id: 'coffee_sel_name2',
                type: 'text',
                rect: ['29.7%', '69.3%','9.6%','42px','auto', 'auto'],
                font: ['Arial, Helvetica, sans-serif', 19.2, "rgba(0,0,0,1)", "normal", "none", ""]
            },
            {
                id: 'coffee_sel_name3',
                type: 'text',
                rect: ['43.8%', '69.3%','9.6%','42px','auto', 'auto'],
                font: ['Arial, Helvetica, sans-serif', 19.2, "rgba(0,0,0,1)", "normal", "none", ""]
            },
            {
                id: 'coffee_sel_name4',
                type: 'text',
                rect: ['57.9%', '69.3%','9.6%','42px','auto', 'auto'],
                font: ['Arial, Helvetica, sans-serif', 19.2, "rgba(0,0,0,1)", "normal", "none", ""]
            },
            {
                id: 'coffee_sel_name5',
                type: 'text',
                rect: ['71.9%', '69.3%','9.6%','42px','auto', 'auto'],
                font: ['Arial, Helvetica, sans-serif', 19.2, "rgba(0,0,0,1)", "normal", "none", ""]
            },
            {
                id: 'coffee_sel_name6',
                type: 'text',
                rect: ['86%', '69.3%','69px','42px','auto', 'auto'],
                font: ['Arial, Helvetica, sans-serif', [120, "%"], "rgba(0,0,0,1)", "normal", "none", ""]
            },
            {
                id: 'COFFEE_TITLE',
                type: 'image',
                rect: ['21.6%', '53.4%','55.6%','86px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"u616-6.png",'50%','50%','400px','auto']
            },
            {
                id: 'SANDWITCH_TITLE',
                display: 'block',
                type: 'image',
                rect: ['33.8%', '51.5%','31.1%','10%','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"u617-6.png",'50%','50%','224px','auto']
            },
            {
                id: 'accept_blue',
                type: 'image',
                rect: ['auto', '83.1%','129px','129px','28px', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"accept_blue.png",'0px','0px'],
                filter: [0, 0, 1, 1, 0, 0, 0, 0, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 'fron_blue',
                display: 'block',
                type: 'image',
                rect: ['auto', '51.9%','129px','129px','22px', 'auto'],
                opacity: 1,
                fill: ["rgba(0,0,0,0)",im+"fron_blue.png",'0px','0px'],
                filter: [0, 0, 1, 1, 0, 0, 0, 0, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 'back_blue',
                display: 'none',
                type: 'image',
                rect: ['14px', '734px','129px','129px','auto', 'auto'],
                opacity: 1,
                fill: ["rgba(0,0,0,0)",im+"back_blue.png",'0px','0px'],
                filter: [0, 0, 1, 1, 0, 0, 0, 0, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 'P1M1',
                type: 'group',
                rect: ['20px', '8.6%','152','184','auto', 'auto'],
                c: [
                {
                    id: 'espresso',
                    type: 'image',
                    rect: ['0px', '0%','152px','102px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"espresso.png",'0px','0px']
                },
                {
                    id: 'Text',
                    type: 'text',
                    rect: ['33px', '62%','auto','auto','auto', 'auto'],
                    text: "에스프레소<br>Espresso<br>₩ 2,300",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                }]
            },
            {
                id: 'P1M2',
                type: 'group',
                rect: ['25.1%', '8.6%','180','184','auto', 'auto'],
                c: [
                {
                    id: 'TextCopy',
                    type: 'text',
                    rect: ['0px', '62%','auto','auto','auto', 'auto'],
                    text: "에스프레소 꼰빠냐<br>Espresso Conpanna<br>₩ 2,500",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                },
                {
                    id: 'espresso_conpanna2',
                    type: 'image',
                    rect: ['14px', '0%','152px','102px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"espresso%20conpanna2.png",'0px','0px']
                }]
            },
            {
                id: 'P1M3',
                type: 'group',
                rect: ['51.4%', '8.6%','150','207','auto', 'auto'],
                c: [
                {
                    id: 'TextCopy2',
                    type: 'text',
                    rect: ['4px', '55.1%','auto','auto','auto', 'auto'],
                    text: "카페 아메리카노<br>Cafe Americano<br>₩ 2,500",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                },
                {
                    id: 'americano',
                    type: 'image',
                    rect: ['0px', '0%','150px','102px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"americano.png",'0px','0px']
                }]
            },
            {
                id: 'P1M4',
                type: 'group',
                rect: ['-123.2%', '8.6%','152','207','auto', 'auto'],
                c: [
                {
                    id: 'TextCopy3',
                    type: 'text',
                    rect: ['30px', '55.1%','auto','auto','auto', 'auto'],
                    text: "카페 라떼<br>Cafe Latte<br>₩ 2,700",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                },
                {
                    id: 'cafelatte',
                    type: 'image',
                    rect: ['0px', '0%','152px','102px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
                }]
            },
            {
                id: 'P1M5',
                type: 'group',
                rect: ['21px', '29.4%','151','183','auto', 'auto'],
                c: [
                {
                    id: 'cappuccino',
                    type: 'image',
                    rect: ['0px', '0%','151px','102px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"cappuccino.png",'0px','0px']
                },
                {
                    id: 'TextCopy9',
                    type: 'text',
                    rect: ['22px', '61.8%','auto','auto','auto', 'auto'],
                    text: "카푸치노<br>Cappuccino<br>₩ 2,700",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                }]
            },
            {
                id: 'P1M6',
                type: 'group',
                rect: ['27.1%', '29.4%','152','183','auto', 'auto'],
                c: [
                {
                    id: 'TextCopy10',
                    type: 'text',
                    rect: ['2px', '61.8%','148px','auto','auto', 'auto'],
                    text: "카라멜 라떼<br>Caramel Latte<br>₩ 2,800",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                },
                {
                    id: 'cafelatteCopy',
                    type: 'image',
                    rect: ['0px', '0%','152px','102px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
                }]
            },
            {
                id: 'P1M7',
                type: 'group',
                rect: ['51.3%', '29.4%','152','183','auto', 'auto'],
                c: [
                {
                    id: 'TextCopy11',
                    type: 'text',
                    rect: ['0px', '61.8%','152px','auto','auto', 'auto'],
                    text: "헤이즐넛 라떼<br>Hazelnut Latte<br>₩ 2,800",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                },
                {
                    id: 'cafelatteCopy2',
                    type: 'image',
                    rect: ['0px', '0%','152px','102px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
                }]
            },
            {
                id: 'P1M8',
                type: 'group',
                rect: ['76.3%', '29.4%','152','183','auto', 'auto'],
                c: [
                {
                    id: 'TextCopy12',
                    type: 'text',
                    rect: ['22px', '61.8%','auto','auto','auto', 'auto'],
                    text: "바닐라 라떼<br>Vanilla Latte<br>₩ 3,000",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                },
                {
                    id: 'cafelatteCopy4',
                    type: 'image',
                    rect: ['0px', '0%','152px','102px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"cafelatte.png",'0px','0px']
                }]
            },
            {
                id: 'P2M1',
                type: 'group',
                rect: ['26.7%', '25.3%','154','188','auto', 'auto'],
                c: [
                {
                    id: 'cafemocha',
                    type: 'image',
                    rect: ['0px', '0%','154px','112px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"cafemocha.png",'0px','0px']
                },
                {
                    id: 'TextCopy8',
                    type: 'text',
                    rect: ['22px', '62.8%','auto','auto','auto', 'auto'],
                    text: "카페 모카<br>Cafe Mocha<br>₩ 3,200",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                }]
            },
            {
                id: 'P2M2',
                type: 'group',
                rect: ['26.7%', '25.3%','154','188','auto', 'auto'],
                c: [
                {
                    id: 'cafemochaCopy',
                    type: 'image',
                    rect: ['0px', '0%','154px','112px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"cafemocha.png",'0px','0px']
                },
                {
                    id: 'TextCopy13',
                    type: 'text',
                    rect: ['-3px', '62.8%','auto','auto','auto', 'auto'],
                    text: "카라멜 모카<br>Caramel Mocha<br>₩ 3,200",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                }]
            },
            {
                id: 'P2M3',
                type: 'group',
                rect: ['26.7%', '25.3%','154','188','auto', 'auto'],
                c: [
                {
                    id: 'cafemochaCopy2',
                    type: 'image',
                    rect: ['0px', '0%','154px','112px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"cafemocha.png",'0px','0px']
                },
                {
                    id: 'TextCopy14',
                    type: 'text',
                    rect: ['22px', '62.8%','auto','auto','auto', 'auto'],
                    text: "화이트 모카<br>White Mocha<br>₩ 3,200",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                }]
            },
            {
                id: 'P3M1',
                display: 'block',
                type: 'group',
                rect: ['102.9%', '8.6%','308','210','auto', 'auto'],
                c: [
                {
                    id: 'menu-category-sandwich-italbmt_copy',
                    type: 'image',
                    rect: ['0px', '0%','308px','140px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"menu-category-sandwich-italbmt%20copy.png",'0px','0px']
                },
                {
                    id: 'TextCopy4',
                    type: 'text',
                    rect: ['46px', '66.7%','217px','70px','auto', 'auto'],
                    text: "터키 베이컨 샌드위치<br>Turkey Bacon Sandwich<br>₩ 4,500",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                }]
            },
            {
                id: 'P3M2',
                display: 'block',
                type: 'group',
                rect: ['151.3%', '8.6%','308','211','auto', 'auto'],
                c: [
                {
                    id: 'menu-category-sandwich-buffchic_copy',
                    type: 'image',
                    rect: ['0px', '0%','308px','140px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"menu-category-sandwich-buffchic%20copy.png",'0px','0px']
                },
                {
                    id: 'TextCopy5',
                    type: 'text',
                    rect: ['71px', '66.8%','168px','70px','auto', 'auto'],
                    text: "닭가슴살 샌드위치<br>Chicken Sandwich<br>₩ 4,500",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                }]
            },
            {
                id: 'P3M3',
                display: 'block',
                type: 'group',
                rect: ['102.9%', '30.2%','308','204','auto', 'auto'],
                c: [
                {
                    id: 'menu-category-sandwich-stkchs_copy',
                    type: 'image',
                    rect: ['0px', '0%','308px','140px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"menu-category-sandwich-stkchs%20copy.png",'0px','0px']
                },
                {
                    id: 'TextCopy7',
                    type: 'text',
                    rect: ['55px', '65.7%','199px','70px','auto', 'auto'],
                    text: "로스트 비프 샌드위치<br>Roast Beef Sandwich<br>₩ 4,500",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                }]
            },
            {
                id: 'P3M4',
                display: 'block',
                type: 'group',
                rect: ['151.3%', '30.2%','308','204','auto', 'auto'],
                c: [
                {
                    id: 'menu-category-sandwich-tuna',
                    type: 'image',
                    rect: ['0px', '0%','308px','140px','auto', 'auto'],
                    fill: ["rgba(0,0,0,0)",im+"menu-category-sandwich-tuna.png",'0px','0px']
                },
                {
                    id: 'TextCopy6',
                    type: 'text',
                    rect: ['42px', '65.7%','226px','70px','auto', 'auto'],
                    text: "허브참치 샌드위치<br>Herb Tuna Sandwich<br>₩ 4,500",
                    align: "center",
                    font: ['Arial, Helvetica, sans-serif', 20, "rgba(0,0,0,1)", "normal", "none", ""]
                }]
            },
            {
                id: 'Rectangle',
                display: 'none',
                type: 'rect',
                rect: ['-0.8%', '798px','100.4%','506px','auto', 'auto'],
                opacity: 0.9,
                fill: ["rgba(57,35,13,1)"],
                stroke: [0,"rgba(0,0,0,0.00)","none"]
            },
            {
                id: 'Text2Copy',
                display: 'none',
                type: 'text',
                rect: ['11.9%', '823px','76.1%','13.6%','auto', 'auto'],
                text: "Thank you!<br> Come again!",
                align: "center",
                font: ['Arial, Helvetica, sans-serif', [400, "%"], "rgba(255,255,255,1.00)", "700", "none", "normal"]
            },
            {
                id: 'Text3',
                display: 'none',
                type: 'text',
                rect: ['118px', '285','auto','auto','auto', 'auto'],
                text: "Order Complete",
                align: "center",
                font: ['Arial, Helvetica, sans-serif', [220, "%"], "rgba(57,35,13,1.00)", "bold", "none", "normal"]
            },
            {
                id: 'Text4',
                display: 'none',
                type: 'text',
                rect: ['auto', '283px','225px','auto','4.6%', 'auto'],
                text: "Order Processing",
                align: "center",
                font: ['Arial, Helvetica, sans-serif', [220, "%"], "rgba(57,35,13,1)", "bold", "none", "normal"]
            },
            {
                id: 'Text4Copy',
                display: 'none',
                type: 'text',
                rect: ['auto', '705px','182px','56px','6.9%', 'auto'],
                text: "Preparing Order",
                align: "center",
                font: ['Arial, Helvetica, sans-serif', [220, "%"], "rgba(57,35,13,1)", "bold", "none", "normal"]
            },
            {
                id: 'Text4Copy2',
                display: 'none',
                type: 'text',
                rect: ['71px', '705px','182px','56px','auto', 'auto'],
                text: "Serving Order",
                align: "center",
                font: ['Arial, Helvetica, sans-serif', [220, "%"], "rgba(57,35,13,1)", "bold", "none", "normal"]
            },
            {
                id: '_03_pp_anwansoon',
                display: 'none',
                type: 'image',
                rect: ['20px', '114px','154px','154px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"03_pp_anwansoon.png",'0px','0px']
            },
            {
                id: 'nfc_logo',
                display: 'none',
                type: 'image',
                rect: ['137px', '164px','200px','55px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"nfc_logo.png",'0px','0px']
            },
            {
                id: '_410_anwansoon2',
                display: 'none',
                type: 'image',
                rect: ['auto', '499px','199px','199px','6.4%', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"410_anwansoon.png",'0px','0px']
            },
            {
                id: 'Kobuki_00',
                display: 'none',
                type: 'image',
                rect: ['63px', '473px','195px','239px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"Kobuki_00.png",'0px','0px']
            },
            {
                id: '_114_anwansoonfge',
                display: 'none',
                type: 'image',
                rect: ['auto', '150px','130px','130px','18.3%', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"114_anwansoonfge.png",'0px','0px']
            },
            {
                id: 'a4_nomal_png_a',
                display: 'none',
                type: 'image',
                rect: ['auto', '105px','104px','163px','8.2%', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"a4_nomal_png_a.png",'0px','0px']
            },
            {
                id: 's1p1',
                display: 'none',
                type: 'ellipse',
                rect: ['39.7%', '289px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 's1p2',
                display: 'none',
                type: 'ellipse',
                rect: ['46.3%', '290px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 's1p3',
                display: 'none',
                type: 'ellipse',
                rect: ['53.1%', '290px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 's1p4',
                display: 'none',
                type: 'ellipse',
                rect: ['59.8%', '290px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 's1p1Copy',
                display: 'none',
                type: 'ellipse',
                rect: ['78.3%', '337px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 's1p2Copy',
                display: 'none',
                type: 'ellipse',
                rect: ['78.3%', '380px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 's1p3Copy',
                display: 'none',
                type: 'ellipse',
                rect: ['78.3%', '423px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 's1p4Copy',
                display: 'none',
                type: 'ellipse',
                rect: ['78.3%', '465px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 's1p1Copy2',
                display: 'none',
                type: 'ellipse',
                rect: ['59.9%', '582px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 's1p2Copy2',
                display: 'none',
                type: 'ellipse',
                rect: ['53.2%', '582px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 's1p3Copy2',
                display: 'none',
                type: 'ellipse',
                rect: ['46.4%', '582px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 's1p4Copy2',
                display: 'none',
                type: 'ellipse',
                rect: ['39.7%', '582px','21px','22px','auto', 'auto'],
                borderRadius: ["50%", "50%", "50%", "50%"],
                fill: ["rgba(67,222,254,1.00)"],
                stroke: [0,"rgba(0, 0, 0, 0)","none"],
                filter: [0, 0, 1, 1, 0, 0, 0, 7.1664663461538, "rgba(0,0,0,0)", 0, 0, 0]
            },
            {
                id: 'header',
                type: 'rect',
                rect: ['0px', '0px','2391px','80px','auto', 'auto'],
                opacity: 0.9,
                fill: ["rgba(57,35,13,1.00)"],
                stroke: [0,"rgba(57,35,13,1.00)","none"]
            },
            {
                id: 'dorothy_cafe',
                type: 'text',
                rect: ['89px', '10px','324px','59px','auto', 'auto'],
                text: "Dorothy..Cafe",
                align: "center",
                font: ['Arial, Helvetica, sans-serif', [320, "%"], "rgba(255,255,255,1.00)", "800", "none", "normal"]
            },
            {
                id: '_01',
                type: 'text',
                rect: ['auto', '10px','auto','auto','32px', 'auto'],
                text: "01",
                align: "center",
                font: ['Arial, Helvetica, sans-serif', [320, "%"], "rgba(255,255,255,1.00)", "800", "none", "normal"]
            },
            {
                id: 'table_no',
                type: 'text',
                rect: ['auto', '25px','auto','auto','101px', 'auto'],
                text: "Table",
                align: "center",
                font: ['Arial, Helvetica, sans-serif', [150, "%"], "rgba(255,255,255,1.00)", "800", "none", "normal"]
            },
            {
                id: 'dorothy_logo012',
                type: 'image',
                rect: ['24px', '13px','56px','55px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"dorothy_logo01.png",'0px','0px']
            },
            {
                id: 'Rectangle2Copy2',
                display: 'none',
                type: 'rect',
                rect: ['0%', '80px','100%','61.8%','auto', 'auto'],
                opacity: 0.9,
                fill: ["rgba(57,35,13,1.00)"],
                stroke: [0,"rgba(57,35,13,1.00)","none"]
            },
            {
                id: 'Text5Copy2',
                display: 'none',
                type: 'text',
                rect: ['14%', '352px','70.8%','6.8%','auto', 'auto'],
                text: "Select a payment method ",
                align: "center",
                font: ['Arial, Helvetica, sans-serif', 40, "rgba(255,255,255,1.00)", "normal", "none", ""]
            },
            {
                id: 'Text6Copy2',
                display: 'none',
                type: 'text',
                rect: ['auto', '45.1%','auto','auto','15.6%', 'auto'],
                text: "Place Order",
                align: "left",
                font: ['Arial, Helvetica, sans-serif', 30, "rgba(255,255,255,1.00)", "800", "none", "normal"]
            },
            {
                id: 'Text7Copy2',
                display: 'none',
                type: 'text',
                rect: ['19.6%', '45.1%','auto','auto','auto', 'auto'],
                text: "Cancel",
                align: "left",
                font: ['Arial, Helvetica, sans-serif', 30, "rgba(255,255,255,1.00)", "800", "none", "normal"]
            },
            {
                id: 'deleteCopy2',
                display: 'none',
                type: 'image',
                rect: ['15.5%', '49.5%','145px','144px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"delete.png",'0px','0px']
            },
            {
                id: 'accept_blue_payment',
                display: 'none',
                type: 'image',
                rect: ['auto', '49.5%','145px','145px','17.2%', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"accept_blue.png",'0px','0px']
            },
            {
                id: 'ROCON_BANK_CARD',
                display: 'block',
                type: 'image',
                rect: ['52px', '-649px','145px','145px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"0030_anwansoon.png",'0px','0px']
            },
            {
                id: 'YUJINMASTER',
                display: 'block',
                type: 'image',
                rect: ['1282px', '-199px','145px','145px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"0034_anwansoon.png",'0px','0px']
            },
            {
                id: 'ROCON_BANK_DESC',
                display: 'block',
                type: 'text',
                rect: ['294px', '-622px','454px','auto','auto', 'auto'],
                text: "YUJIN MasterCard<br>1234-2345-3456-4567",
                align: "left",
                font: ['Arial, Helvetica, sans-serif', 40, "rgba(160,160,160,1.00)", "normal", "none", "normal"]
            },
            {
                id: 'accept',
                display: 'block',
                type: 'image',
                rect: ['43px', '-601px','63px','63px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"accept.png",'0px','0px']
            },
            {
                id: 'acceptCopy',
                display: 'none',
                type: 'image',
                rect: ['46px', '-601px','63px','63px','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"accept.png",'0px','0px']
            },
            {
                id: 'YUJINMASTER_DESC',
                display: 'block',
                type: 'text',
                rect: ['298px', '-478px','454px','auto','auto', 'auto'],
                text: "ROCON BANK<br>1234-2345-3456-4567",
                align: "left",
                font: ['Arial, Helvetica, sans-serif', 40, "rgba(160,160,160,1.00)", "normal", "none", "normal"]
            },
            {
                id: 'yujinrobot_ci_png_b_white',
                display: 'block',
                type: 'image',
                rect: ['21.7%', '75.9%','61.4%','13%','auto', 'auto'],
                fill: ["rgba(0,0,0,0)",im+"yujinrobot_ci_png_b_white.png",'0%','0%','100%','auto']
            }],
            symbolInstances: [

            ]
        },
    states: {
        "Base State": {
            "${_s1p4Copy2}": [
                ["color", "background-color", 'rgba(67,222,254,1.00)'],
                ["style", "top", '582px'],
                ["style", "height", '22px'],
                ["style", "opacity", '1'],
                ["style", "display", 'none'],
                ["subproperty", "filter.blur", '7.17px'],
                ["style", "left", '39.72%'],
                ["style", "width", '21px']
            ],
            "${_P1M4}": [
                ["style", "left", '75.56%'],
                ["style", "right", 'auto']
            ],
            "${_Text5Copy2}": [
                ["style", "top", '-697px'],
                ["style", "font-size", '40px'],
                ["style", "text-align", 'center'],
                ["color", "color", 'rgba(255,255,255,1.00)'],
                ["style", "height", '6.79%'],
                ["style", "display", 'none'],
                ["style", "left", '7.92%'],
                ["style", "width", '83.07%']
            ],
            "${_yujinrobot_ci_png_b_white}": [
                ["style", "top", '74.75%'],
                ["style", "display", 'block'],
                ["style", "height", '15.7%'],
                ["style", "background-size", [100,'auto'], {valueTemplate:'@@0@@% @@1@@'} ],
                ["style", "left", '21.53%'],
                ["style", "width", '58.34%']
            ],
            "${_sandwitch_slot1}": [
                ["style", "top", '76.89%'],
                ["transform", "scaleY", '0.4'],
                ["transform", "scaleX", '0.4'],
                ["style", "left", '10.51%'],
                ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ]
            ],
            "${_coffee_sel5}": [
                ["style", "top", '70.67%'],
                ["transform", "scaleY", '0.45'],
                ["transform", "scaleX", '0.45'],
                ["style", "opacity", '1'],
                ["style", "left", '66.47%']
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
            "${_table_no}": [
                ["style", "top", '25px'],
                ["style", "bottom", 'auto'],
                ["color", "color", 'rgba(255,255,255,1.00)'],
                ["style", "right", '101px'],
                ["style", "left", 'auto'],
                ["style", "font-size", '150%']
            ],
            "${__01}": [
                ["style", "top", '10px'],
                ["style", "bottom", 'auto'],
                ["color", "color", 'rgba(255,255,255,1.00)'],
                ["style", "right", '32px'],
                ["style", "left", 'auto'],
                ["style", "font-size", '320%']
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
            "${_coffee_sel4}": [
                ["style", "top", '70.74%'],
                ["transform", "scaleY", '0.45'],
                ["transform", "scaleX", '0.45'],
                ["style", "opacity", '1'],
                ["style", "left", '52.3%']
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
            "${_TextCopy16}": [
                ["style", "top", '118px'],
                ["style", "left", '22px'],
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
            "${_checkout_total}": [
                ["style", "top", '81.27%'],
                ["style", "width", '199px'],
                ["color", "color", 'rgba(100,61,23,1.00)'],
                ["style", "font-weight", '800'],
                ["style", "left", '48%'],
                ["style", "font-size", '25px']
            ],
            "${_Text6Copy}": [
                ["style", "top", '-16.65%'],
                ["style", "display", 'none'],
                ["color", "color", 'rgba(255,255,255,1.00)'],
                ["style", "right", '20.83%'],
                ["style", "left", 'auto'],
                ["style", "font-size", '30px']
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
            "${_Stage}": [
                ["color", "background-color", 'rgba(255,255,255,1)'],
                ["style", "min-width", '100%'],
                ["style", "overflow", 'scroll'],
                ["style", "height", '1414px'],
                ["style", "max-width", '100%'],
                ["style", "width", '100%']
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
            "${_P3M3}": [
                ["style", "display", 'block'],
                ["style", "left", '203.67%'],
                ["style", "top", '30.21%']
            ],
            "${_TextCopy8}": [
                ["style", "top", '62.77%'],
                ["style", "text-align", 'center'],
                ["style", "left", '22px'],
                ["style", "font-size", '20px']
            ],
            "${_dorothy_logo012}": [
                ["style", "top", '13px'],
                ["style", "height", '55px'],
                ["style", "left", '24px'],
                ["style", "width", '56px']
            ],
            "${_cafemochaCopy}": [
                ["style", "left", '0px'],
                ["style", "top", '0%']
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
            "${_order}": [
                ["style", "top", '81.26%'],
                ["style", "font-size", '25px'],
                ["style", "right", '8px'],
                ["color", "color", 'rgba(100,61,23,1.00)'],
                ["style", "font-weight", '800'],
                ["style", "left", 'auto'],
                ["style", "width", '160px']
            ],
            "${_TextCopy}": [
                ["style", "top", '61.96%'],
                ["style", "left", '0px'],
                ["style", "text-align", 'center'],
                ["style", "font-size", '20px']
            ],
            "${_Price}": [
                ["style", "top", '86.15%'],
                ["style", "font-size", '50px'],
                ["color", "color", 'rgba(100,61,23,1.00)'],
                ["style", "font-weight", '800'],
                ["style", "left", '45.63%'],
                ["style", "width", '225px']
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
                ["style", "display", 'none'],
                ["color", "color", 'rgba(57,35,13,1.00)'],
                ["style", "left", '57px'],
                ["style", "top", '283px']
            ],
            "${_cafemocha}": [
                ["style", "left", '0px'],
                ["style", "top", '0%']
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
            "${_P2M3}": [
                ["style", "top", '8.42%'],
                ["style", "left", '157.08%']
            ],
            "${_acceptCopy}": [
                ["style", "top", '-601px'],
                ["style", "height", '63px'],
                ["style", "display", 'none'],
                ["style", "left", '46px'],
                ["style", "width", '63px']
            ],
            "${_TextCopy9}": [
                ["style", "top", '61.75%'],
                ["style", "left", '22px'],
                ["style", "text-align", 'center'],
                ["style", "font-size", '20px']
            ],
            "${_P1M3}": [
                ["style", "left", '51.39%']
            ],
            "${_P1M8}": [
                ["style", "top", '29.43%'],
                ["style", "left", '76.25%']
            ],
            "${_menu-category-sandwich-tuna}": [
                ["style", "top", '0%'],
                ["transform", "scaleX", '1'],
                ["transform", "scaleY", '1'],
                ["style", "left", '0px']
            ],
            "${_menu-category-sandwich-stkchs_copy}": [
                ["style", "top", '0%'],
                ["transform", "scaleX", '1'],
                ["transform", "scaleY", '1'],
                ["style", "left", '0px']
            ],
            "${__03_pp_anwansoon}": [
                ["style", "top", '114px'],
                ["style", "display", 'none'],
                ["style", "height", '154px'],
                ["style", "left", '20px'],
                ["style", "width", '154px']
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
            "${_Text7Copy2}": [
                ["style", "top", '-16.65%'],
                ["style", "display", 'none'],
                ["color", "color", 'rgba(255,255,255,1.00)'],
                ["style", "left", '18.19%'],
                ["style", "font-size", '30px']
            ],
            "${_TextCopy10}": [
                ["style", "top", '61.75%'],
                ["style", "text-align", 'center'],
                ["style", "width", '148px'],
                ["style", "left", '2px'],
                ["style", "font-size", '20px']
            ],
            "${_accept_blue_payment}": [
                ["style", "top", '-12.19%'],
                ["style", "display", 'none'],
                ["style", "height", '145px'],
                ["style", "right", '17.22%'],
                ["style", "left", 'auto'],
                ["style", "width", '145px']
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
            "${_ROCON_BANK_DESC}": [
                ["style", "top", '-622px'],
                ["style", "text-align", 'left'],
                ["color", "color", 'rgba(160,160,160,1.00)'],
                ["style", "display", 'block'],
                ["style", "opacity", '1'],
                ["style", "left", '294px'],
                ["style", "width", '454px']
            ],
            "${_coffee_sel2}": [
                ["style", "top", '70.74%'],
                ["transform", "scaleY", '0.45'],
                ["transform", "scaleX", '0.45'],
                ["style", "opacity", '1'],
                ["style", "left", '24.53%']
            ],
            "${_Text}": [
                ["style", "top", '61.96%'],
                ["style", "left", '33px'],
                ["style", "text-align", 'center'],
                ["style", "font-size", '20px']
            ],
            "${_TextCopy2}": [
                ["style", "top", '55.07%'],
                ["style", "text-align", 'center'],
                ["style", "left", '4px'],
                ["style", "font-size", '20px']
            ],
            "${_espresso_conpanna2}": [
                ["style", "left", '14px'],
                ["style", "top", '0%']
            ],
            "${_cafemochaCopy2}": [
                ["style", "left", '0px'],
                ["style", "top", '0%']
            ],
            "${_s1p4}": [
                ["color", "background-color", 'rgba(67,222,254,1.00)'],
                ["style", "top", '290px'],
                ["style", "height", '22px'],
                ["subproperty", "filter.blur", '7.17px'],
                ["style", "display", 'none'],
                ["style", "opacity", '1'],
                ["style", "left", '59.8%'],
                ["style", "width", '21px']
            ],
            "${_Text6Copy2}": [
                ["style", "top", '-16.65%'],
                ["style", "display", 'none'],
                ["color", "color", 'rgba(255,255,255,1.00)'],
                ["style", "right", '17.08%'],
                ["style", "left", 'auto'],
                ["style", "font-size", '30px']
            ],
            "${_TextCopy14}": [
                ["style", "top", '62.77%'],
                ["style", "text-align", 'center'],
                ["style", "left", '22px'],
                ["style", "font-size", '20px']
            ],
            "${_s1p3}": [
                ["color", "background-color", 'rgba(67,222,254,1.00)'],
                ["style", "top", '290px'],
                ["style", "height", '22px'],
                ["subproperty", "filter.blur", '7.17px'],
                ["style", "display", 'none'],
                ["style", "opacity", '1'],
                ["style", "left", '53.13%'],
                ["style", "width", '21px']
            ],
            "${_espresso}": [
                ["style", "left", '0px'],
                ["style", "top", '0%']
            ],
            "${_s1p2Copy2}": [
                ["color", "background-color", 'rgba(67,222,254,1.00)'],
                ["style", "top", '582px'],
                ["style", "height", '22px'],
                ["style", "opacity", '1'],
                ["style", "display", 'none'],
                ["subproperty", "filter.blur", '7.17px'],
                ["style", "left", '53.19%'],
                ["style", "width", '21px']
            ],
            "${_copyright}": [
                ["style", "top", '98%'],
                ["style", "width", '100%'],
                ["color", "color", 'rgba(100,61,23,0.37)'],
                ["style", "height", '24px'],
                ["style", "left", '0.14%'],
                ["style", "font-size", '70%']
            ],
            "${_Text2Copy}": [
                ["style", "top", '875px'],
                ["style", "width", '99.05%'],
                ["style", "display", 'none'],
                ["style", "height", '6.08%'],
                ["color", "color", 'rgba(255,255,255,1.00)'],
                ["style", "font-weight", '700'],
                ["style", "left", '0.81%'],
                ["style", "font-size", '400%']
            ],
            "${_s1p4Copy}": [
                ["color", "background-color", 'rgba(67,222,254,1.00)'],
                ["style", "top", '465px'],
                ["style", "height", '22px'],
                ["style", "opacity", '1'],
                ["style", "display", 'none'],
                ["subproperty", "filter.blur", '7.17px'],
                ["style", "left", '78.33%'],
                ["style", "width", '21px']
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
                ["subproperty", "filter.blur", '7.17px'],
                ["style", "display", 'none'],
                ["style", "opacity", '1'],
                ["style", "left", '46.33%'],
                ["style", "width", '21px']
            ],
            "${_cafelatteCopy}": [
                ["style", "left", '0px'],
                ["style", "top", '0%']
            ],
            "${_YUJINMASTER}": [
                ["style", "top", '-505px'],
                ["style", "display", 'block'],
                ["style", "height", '145px'],
                ["style", "opacity", '0.3'],
                ["style", "left", '132px'],
                ["style", "width", '145px']
            ],
            "${_COFFEE_TITLE}": [
                ["style", "top", '53.38%'],
                ["style", "left", '21.6%'],
                ["style", "background-size", [400,'auto'], {valueTemplate:'@@0@@px @@1@@'} ],
                ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ],
                ["style", "opacity", '1']
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
            "${_coffee_sel6}": [
                ["style", "top", '70.74%'],
                ["transform", "scaleY", '0.45'],
                ["transform", "scaleX", '0.45'],
                ["style", "opacity", '1'],
                ["style", "left", '80.22%'],
                ["style", "display", 'block']
            ],
            "${_Text7Copy}": [
                ["style", "top", '-16.65%'],
                ["style", "display", 'none'],
                ["color", "color", 'rgba(255,255,255,1.00)'],
                ["style", "left", '17.64%'],
                ["style", "font-size", '30px']
            ],
            "${_cafelatteCopy4}": [
                ["style", "left", '0px'],
                ["style", "top", '0%']
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
            "${_coffee_sel0}": [
                ["style", "top", '70.74%'],
                ["transform", "scaleY", '0.45'],
                ["transform", "scaleX", '0.45'],
                ["style", "opacity", '1'],
                ["style", "left", '-28px']
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
            "${_TextCopy5}": [
                ["style", "top", '66.82%'],
                ["style", "text-align", 'center'],
                ["style", "height", '70px'],
                ["style", "width", '168px'],
                ["style", "left", '71px'],
                ["style", "font-size", '20px']
            ],
            "${_P1M2}": [
                ["style", "left", '25.14%']
            ],
            "${_accept}": [
                ["style", "top", '-601px'],
                ["style", "height", '63px'],
                ["style", "display", 'block'],
                ["style", "left", '43px'],
                ["style", "width", '63px']
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
            "${_P1M6}": [
                ["style", "top", '29.43%'],
                ["style", "left", '27.08%']
            ],
            "${_TextCopy17}": [
                ["style", "top", '118px'],
                ["style", "left", '22px'],
                ["style", "font-size", '20px']
            ],
            "${_back_blue}": [
                ["style", "top", '734px'],
                ["style", "width", '129px'],
                ["style", "height", '129px'],
                ["style", "display", 'none'],
                ["style", "opacity", '0'],
                ["style", "left", '14px'],
                ["subproperty", "filter.saturate", '0']
            ],
            "${_P2M2}": [
                ["style", "top", '8.42%'],
                ["style", "left", '132.52%']
            ],
            "${_P3M1}": [
                ["style", "top", '8.56%'],
                ["style", "left", '205.09%'],
                ["style", "display", 'block']
            ],
            "${_ROCON_BANK_CARD}": [
                ["style", "top", '-649px'],
                ["style", "display", 'block'],
                ["style", "height", '145px'],
                ["style", "opacity", '1'],
                ["style", "left", '130px'],
                ["style", "width", '145px']
            ],
            "${_Text4Copy2}": [
                ["style", "top", '705px'],
                ["style", "height", '56px'],
                ["style", "display", 'none'],
                ["style", "opacity", '0.2'],
                ["style", "left", '71px'],
                ["style", "width", '200px']
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
                ["style", "height", '22px'],
                ["style", "opacity", '1'],
                ["style", "display", 'none'],
                ["subproperty", "filter.blur", '7.17px'],
                ["style", "left", '78.33%'],
                ["style", "width", '21px']
            ],
            "${_deleteCopy2}": [
                ["style", "top", '-12.19%'],
                ["style", "display", 'none'],
                ["style", "height", '144px'],
                ["style", "left", '15.48%'],
                ["style", "width", '145px']
            ],
            "${_TextCopy13}": [
                ["style", "top", '62.77%'],
                ["style", "text-align", 'center'],
                ["style", "width", '160px'],
                ["style", "left", '-3px'],
                ["style", "font-size", '20px']
            ],
            "${_Text5Copy}": [
                ["style", "top", '-521px'],
                ["style", "width", '70.84%'],
                ["style", "display", 'none'],
                ["style", "height", '6.79%'],
                ["color", "color", 'rgba(255,255,255,1.00)'],
                ["style", "left", '14.03%'],
                ["style", "font-size", '40px']
            ],
            "${_P1M5}": [
                ["style", "top", '29.43%'],
                ["style", "left", '21px']
            ],
            "${_YUJINMASTER_DESC}": [
                ["style", "top", '-478px'],
                ["style", "text-align", 'left'],
                ["color", "color", 'rgba(160,160,160,1.00)'],
                ["style", "display", 'block'],
                ["style", "opacity", '0.5'],
                ["style", "left", '298px'],
                ["style", "width", '454px']
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
            "${_cafelatte}": [
                ["style", "left", '0px'],
                ["style", "top", '0%']
            ],
            "${_nfc_logo}": [
                ["style", "top", '164px'],
                ["style", "display", 'none'],
                ["style", "height", '55px'],
                ["style", "left", '137px'],
                ["style", "width", '200px']
            ],
            "${_SANDWITCH_TITLE}": [
                ["style", "top", '51.48%'],
                ["style", "left", '33.82%'],
                ["style", "background-size", [224,'auto'], {valueTemplate:'@@0@@px @@1@@'} ],
                ["style", "display", 'block'],
                ["style", "opacity", '0'],
                ["style", "background-position", [50,50], {valueTemplate:'@@0@@% @@1@@%'} ],
                ["style", "height", '10%']
            ],
            "${_s1p1Copy}": [
                ["color", "background-color", 'rgba(67,222,254,1.00)'],
                ["style", "top", '337px'],
                ["style", "height", '22px'],
                ["subproperty", "filter.blur", '7.17px'],
                ["style", "display", 'none'],
                ["style", "opacity", '1'],
                ["style", "left", '78.33%'],
                ["style", "width", '21px']
            ],
            "${_Rectangle2Copy2}": [
                ["color", "background-color", 'rgba(57,35,13,1.00)'],
                ["style", "opacity", '0.9'],
                ["style", "display", 'none'],
                ["color", "border-color", 'rgba(57,35,13,1.00)'],
                ["style", "left", '0%'],
                ["style", "top", '-794px']
            ],
            "${_s1p1Copy2}": [
                ["color", "background-color", 'rgba(67,222,254,1.00)'],
                ["style", "top", '582px'],
                ["style", "height", '22px'],
                ["subproperty", "filter.blur", '7.17px'],
                ["style", "display", 'none'],
                ["style", "opacity", '1'],
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
            "${_Kobuki_00}": [
                ["style", "top", '473px'],
                ["style", "display", 'none'],
                ["style", "height", '239px'],
                ["style", "opacity", '0.2'],
                ["style", "left", '63px'],
                ["style", "width", '195px']
            ],
            "${_P2M1}": [
                ["style", "top", '8.42%'],
                ["style", "left", '106.1%']
            ],
            "${_s1p1}": [
                ["color", "background-color", 'rgba(67,222,254,1.00)'],
                ["style", "top", '289px'],
                ["style", "height", '22px'],
                ["subproperty", "filter.blur", '7.17px'],
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
            "${_TextCopy6}": [
                ["style", "top", '65.69%'],
                ["style", "text-align", 'center'],
                ["style", "height", '70px'],
                ["style", "font-size", '20px'],
                ["style", "left", '42px'],
                ["style", "width", '226px']
            ],
            "${_s1p3Copy}": [
                ["color", "background-color", 'rgba(67,222,254,1.00)'],
                ["style", "top", '423px'],
                ["style", "height", '22px'],
                ["style", "opacity", '1'],
                ["style", "display", 'none'],
                ["subproperty", "filter.blur", '7.17px'],
                ["style", "left", '78.33%'],
                ["style", "width", '21px']
            ],
            "${_coffee_sel1}": [
                ["style", "top", '70.74%'],
                ["transform", "scaleY", '0.45'],
                ["transform", "scaleX", '0.45'],
                ["style", "opacity", '1'],
                ["style", "left", '10.64%']
            ],
            "${_Text4Copy}": [
                ["style", "top", '705px'],
                ["style", "height", '56px'],
                ["style", "right", '6.64%'],
                ["style", "bottom", 'auto'],
                ["style", "display", 'none'],
                ["style", "opacity", '0.2'],
                ["style", "left", 'auto'],
                ["style", "width", '200px']
            ],
            "${_P3M4}": [
                ["style", "top", '30.21%'],
                ["style", "left", '252%'],
                ["style", "display", 'block']
            ],
            "${_TextCopy15}": [
                ["style", "top", '118px'],
                ["style", "font-size", '20px'],
                ["style", "left", '22px'],
                ["style", "width", '132px']
            ],
            "${_P3M2}": [
                ["style", "top", '8.56%'],
                ["style", "left", '251.75%'],
                ["style", "display", 'block']
            ],
            "${_s1p3Copy2}": [
                ["color", "background-color", 'rgba(67,222,254,1.00)'],
                ["style", "top", '582px'],
                ["style", "height", '22px'],
                ["style", "opacity", '1'],
                ["style", "display", 'none'],
                ["subproperty", "filter.blur", '7.17px'],
                ["style", "left", '46.39%'],
                ["style", "width", '21px']
            ],
            "${_menu-category-sandwich-italbmt_copy}": [
                ["style", "top", '0%'],
                ["transform", "scaleX", '1'],
                ["transform", "scaleY", '1'],
                ["style", "left", '0px']
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
            "${_P1M7}": [
                ["style", "top", '29.43%'],
                ["style", "left", '51.25%']
            ],
            "${_menu-category-sandwich-buffchic_copy}": [
                ["style", "top", '0%'],
                ["transform", "scaleX", '1'],
                ["transform", "scaleY", '1'],
                ["style", "left", '0px']
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
            duration: 10500,
            autoPlay: true,
            timeline: [
                { id: "dg169", tween: [ "style", "${_P3M4}", "left", '151.25%', { fromValue: '252%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg170", tween: [ "style", "${_P3M4}", "left", '51.73%', { fromValue: '151.25%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg171", tween: [ "style", "${_P3M4}", "left", '51.73%', { fromValue: '51.73%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg173", tween: [ "style", "${_s1p2}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
                { id: "dg174", tween: [ "style", "${_s1p2}", "display", 'none', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg175", tween: [ "style", "${_s1p2}", "display", 'block', { fromValue: 'none'}], position: 7250, duration: 0 },
                { id: "dg33", tween: [ "style", "${__114_anwansoonfge}", "opacity", '1', { fromValue: '0.2'}], position: 7000, duration: 1000 },
                { id: "dg156", tween: [ "style", "${_accept_blue}", "opacity", '1', { fromValue: '1'}], position: 0, duration: 0 },
                { id: "dg157", tween: [ "style", "${_accept_blue}", "opacity", '0.5', { fromValue: '1'}], position: 2500, duration: 0 },
                { id: "dg158", tween: [ "style", "${_accept_blue}", "opacity", '0.5', { fromValue: '0.5'}], position: 3250, duration: 0 },
                { id: "dg47", tween: [ "style", "${_accept}", "display", 'none', { fromValue: 'block'}], position: 4250, duration: 0 },
                { id: "dg48", tween: [ "style", "${_accept}", "display", 'none', { fromValue: 'none'}], position: 5191, duration: 0 },
                { id: "dg67", tween: [ "style", "${_P3M1}", "left", '104.34%', { fromValue: '205.09%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg68", tween: [ "style", "${_P3M1}", "left", '4.82%', { fromValue: '104.34%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg69", tween: [ "style", "${_P3M1}", "left", '4.82%', { fromValue: '4.82%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg179", tween: [ "style", "${_s1p3Copy}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
                { id: "dg180", tween: [ "style", "${_s1p3Copy}", "display", 'none', { fromValue: 'none'}], position: 8000, duration: 0 },
                { id: "dg181", tween: [ "style", "${_s1p3Copy}", "display", 'block', { fromValue: 'none'}], position: 8500, duration: 0 },
                { id: "dg56", tween: [ "style", "${_ROCON_BANK_CARD}", "opacity", '0.3', { fromValue: '1'}], position: 4070, duration: 179, easing: "easeOutBounce" },
                { id: "dg123", tween: [ "style", "${_Rectangle}", "left", '-0.27%', { fromValue: '-0.27%'}], position: 7000, duration: 0 },
                { id: "dg26", tween: [ "style", "${_YUJINMASTER}", "opacity", '1', { fromValue: '0.3'}], position: 4070, duration: 179, easing: "easeOutBounce" },
                { id: "dg189", tween: [ "style", "${_Text6Copy2}", "top", '45.12%', { fromValue: '-16.65%'}], position: 3250, duration: 821, easing: "easeOutBounce" },
                { id: "dg74", tween: [ "style", "${_Text4Copy2}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg182", tween: [ "style", "${_s1p4}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
                { id: "dg183", tween: [ "style", "${_s1p4}", "display", 'none', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg184", tween: [ "style", "${_s1p4}", "display", 'block', { fromValue: 'none'}], position: 7750, duration: 0 },
                { id: "dg20", tween: [ "style", "${_ROCON_BANK_DESC}", "opacity", '0.5', { fromValue: '1'}], position: 4070, duration: 179, easing: "easeOutBounce" },
                { id: "dg28", tween: [ "style", "${_YUJINMASTER}", "display", 'none', { fromValue: 'block'}], position: 5191, duration: 0, easing: "easeOutBounce" },
                { id: "dg64", tween: [ "style", "${_P2M2}", "left", '28.24%', { fromValue: '132.52%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg65", tween: [ "style", "${_P2M2}", "left", '-71.28%', { fromValue: '28.24%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg66", tween: [ "style", "${_P2M2}", "left", '-71.28%', { fromValue: '-71.28%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "eid2481", tween: [ "style", "${_yujinrobot_ci_png_b_white}", "top", '74.75%', { fromValue: '74.75%'}], position: 7000, duration: 0 },
                { id: "dg29", tween: [ "style", "${_coffee_sel6}", "display", 'block', { fromValue: 'block'}], position: 0, duration: 0 },
                { id: "dg159", tween: [ "subproperty", "${_accept_blue}", "filter.saturate", '1', { fromValue: '1'}], position: 0, duration: 0 },
                { id: "dg160", tween: [ "subproperty", "${_accept_blue}", "filter.saturate", '0', { fromValue: '1'}], position: 2500, duration: 0 },
                { id: "eid2478", tween: [ "style", "${_yujinrobot_ci_png_b_white}", "width", '58.34%', { fromValue: '58.34%'}], position: 7000, duration: 0 },
                { id: "dg4", tween: [ "style", "${_P1M4}", "left", '-23.64%', { fromValue: '75.56%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg5", tween: [ "style", "${_P1M4}", "left", '-123.16%', { fromValue: '-23.64%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg6", tween: [ "style", "${_P1M4}", "left", '-123.16%', { fromValue: '-123.16%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg99", tween: [ "style", "${__410_anwansoon2}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "eid2477", tween: [ "style", "${_yujinrobot_ci_png_b_white}", "height", '15.7%', { fromValue: '15.7%'}], position: 7000, duration: 0 },
                { id: "dg57", tween: [ "style", "${_ROCON_BANK_CARD}", "left", '130px', { fromValue: '130px'}], position: 3250, duration: 0, easing: "easeOutBounce" },
                { id: "dg41", tween: [ "style", "${_P2M3}", "left", '53.19%', { fromValue: '157.08%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg42", tween: [ "style", "${_P2M3}", "left", '-46.33%', { fromValue: '53.19%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg43", tween: [ "style", "${_P2M3}", "left", '-46.33%', { fromValue: '-46.33%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg62", tween: [ "style", "${_back_blue}", "opacity", '1', { fromValue: '0'}], position: 0, duration: 1000 },
                { id: "dg52", tween: [ "style", "${_P1M6}", "left", '-72.09%', { fromValue: '27.08%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg53", tween: [ "style", "${_P1M6}", "left", '-171.61%', { fromValue: '-72.09%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg54", tween: [ "style", "${_P1M6}", "left", '-171.61%', { fromValue: '-171.61%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg87", tween: [ "style", "${_s1p1Copy}", "display", 'block', { fromValue: 'none'}], position: 8000, duration: 0 },
                { id: "dg166", tween: [ "style", "${_s1p3Copy2}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
                { id: "dg167", tween: [ "style", "${_s1p3Copy2}", "display", 'none', { fromValue: 'none'}], position: 9000, duration: 0 },
                { id: "dg168", tween: [ "style", "${_s1p3Copy2}", "display", 'block', { fromValue: 'none'}], position: 9500, duration: 0 },
                { id: "dg84", tween: [ "style", "${_YUJINMASTER_DESC}", "display", 'none', { fromValue: 'block'}], position: 5191, duration: 0 },
                { id: "dg147", tween: [ "style", "${_accept_blue_payment}", "display", 'block', { fromValue: 'none'}], position: 3250, duration: 0 },
                { id: "dg148", tween: [ "style", "${_accept_blue_payment}", "display", 'block', { fromValue: 'block'}], position: 3758, duration: 0 },
                { id: "dg149", tween: [ "style", "${_accept_blue_payment}", "display", 'none', { fromValue: 'block'}], position: 5191, duration: 0 },
                { id: "dg150", tween: [ "style", "${_accept_blue_payment}", "display", 'none', { fromValue: 'none'}], position: 8191, duration: 0 },
                { id: "eid2476", tween: [ "style", "${_yujinrobot_ci_png_b_white}", "display", 'none', { fromValue: 'block'}], position: 0, duration: 0 },
                { id: "eid2475", tween: [ "style", "${_yujinrobot_ci_png_b_white}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg162", tween: [ "style", "${_Text4Copy}", "right", '6.64%', { fromValue: '6.64%'}], position: 10000, duration: 0 },
                { id: "dg12", tween: [ "style", "${_Text5Copy2}", "top", '120px', { fromValue: '-697px'}], position: 3250, duration: 821, easing: "easeOutBounce" },
                { id: "dg37", tween: [ "subproperty", "${_fron_blue}", "filter.saturate", '0', { fromValue: '1'}], position: 1000, duration: 1000 },
                { id: "dg22", tween: [ "style", "${_P1M1}", "left", '-694px', { fromValue: '20px'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg23", tween: [ "style", "${_P1M1}", "left", '-1411px', { fromValue: '-694px'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg24", tween: [ "style", "${_P1M1}", "left", '-1411px', { fromValue: '-1411px'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg81", tween: [ "style", "${_s1p2Copy}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
                { id: "dg82", tween: [ "style", "${_s1p2Copy}", "display", 'none', { fromValue: 'none'}], position: 8000, duration: 0 },
                { id: "dg83", tween: [ "style", "${_s1p2Copy}", "display", 'block', { fromValue: 'none'}], position: 8250, duration: 0 },
                { id: "dg112", tween: [ "style", "${_Rectangle2Copy2}", "display", 'block', { fromValue: 'none'}], position: 3250, duration: 0 },
                { id: "dg113", tween: [ "style", "${_Rectangle2Copy2}", "display", 'block', { fromValue: 'block'}], position: 3758, duration: 0 },
                { id: "dg114", tween: [ "style", "${_Rectangle2Copy2}", "display", 'none', { fromValue: 'block'}], position: 5191, duration: 0 },
                { id: "dg115", tween: [ "style", "${_Rectangle2Copy2}", "display", 'none', { fromValue: 'none'}], position: 8191, duration: 0 },
                { id: "dg71", tween: [ "style", "${_s1p3}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
                { id: "dg72", tween: [ "style", "${_s1p3}", "display", 'none', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg73", tween: [ "style", "${_s1p3}", "display", 'block', { fromValue: 'none'}], position: 7500, duration: 0 },
                { id: "dg116", tween: [ "style", "${_Rectangle2Copy2}", "top", '79px', { fromValue: '-794px'}], position: 3250, duration: 821, easing: "easeOutBounce" },
                { id: "dg59", tween: [ "style", "${_back_blue}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
                { id: "dg60", tween: [ "style", "${_back_blue}", "display", 'block', { fromValue: 'none'}], position: 49, duration: 0 },
                { id: "dg61", tween: [ "style", "${_back_blue}", "display", 'none', { fromValue: 'block'}], position: 7000, duration: 0 },
                { id: "dg31", tween: [ "style", "${_Text4}", "opacity", '1', { fromValue: '0.2'}], position: 7000, duration: 1000 },
                { id: "dg172", tween: [ "style", "${_P3M4}", "display", 'none', { fromValue: 'block'}], position: 7000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg129", tween: [ "style", "${_s1p1}", "opacity", '1', { fromValue: '1'}], position: 7000, duration: 0 },
                { id: "dg36", tween: [ "style", "${_fron_blue}", "opacity", '0', { fromValue: '1'}], position: 1000, duration: 1000 },
                { id: "dg142", tween: [ "style", "${_deleteCopy2}", "top", '49.55%', { fromValue: '-12.19%'}], position: 3250, duration: 821, easing: "easeOutBounce" },
                { id: "dg134", tween: [ "style", "${_P1M3}", "left", '-47.82%', { fromValue: '51.39%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg135", tween: [ "style", "${_P1M3}", "left", '-147.34%', { fromValue: '-47.82%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg136", tween: [ "style", "${_P1M3}", "left", '-147.34%', { fromValue: '-147.34%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg25", tween: [ "style", "${_YUJINMASTER}", "top", '343px', { fromValue: '-505px'}], position: 3250, duration: 821, easing: "easeOutBounce" },
                { id: "dg176", tween: [ "style", "${_P1M7}", "left", '-47.92%', { fromValue: '51.25%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg177", tween: [ "style", "${_P1M7}", "left", '-147.44%', { fromValue: '-47.92%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg178", tween: [ "style", "${_P1M7}", "left", '-147.44%', { fromValue: '-147.44%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg117", tween: [ "style", "${_s1p1Copy2}", "display", 'block', { fromValue: 'none'}], position: 9000, duration: 0 },
                { id: "dg125", tween: [ "style", "${_P1M8}", "left", '-22.92%', { fromValue: '76.25%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg126", tween: [ "style", "${_P1M8}", "left", '-122.44%', { fromValue: '-22.92%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg127", tween: [ "style", "${_P1M8}", "left", '-122.44%', { fromValue: '-122.44%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg70", tween: [ "style", "${_P3M1}", "display", 'none', { fromValue: 'block'}], position: 7000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg130", tween: [ "style", "${_Kobuki_00}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg15", tween: [ "style", "${_acceptCopy}", "display", 'block', { fromValue: 'none'}], position: 4250, duration: 0 },
                { id: "dg16", tween: [ "style", "${_acceptCopy}", "display", 'none', { fromValue: 'block'}], position: 5191, duration: 0 },
                { id: "dg165", tween: [ "style", "${_Text4Copy}", "width", '200px', { fromValue: '200px'}], position: 10000, duration: 0 },
                { id: "dg27", tween: [ "style", "${_YUJINMASTER}", "left", '132px', { fromValue: '132px'}], position: 3250, duration: 0, easing: "easeOutBounce" },
                { id: "dg97", tween: [ "style", "${_Text3}", "left", '57px', { fromValue: '57px'}], position: 7000, duration: 0 },
                { id: "dg21", tween: [ "style", "${_ROCON_BANK_DESC}", "top", '225px', { fromValue: '-622px'}], position: 3250, duration: 821, easing: "easeOutBounce" },
                { id: "dg138", tween: [ "style", "${_Text7Copy2}", "display", 'block', { fromValue: 'none'}], position: 3250, duration: 0, easing: "easeOutBounce" },
                { id: "dg139", tween: [ "style", "${_Text7Copy2}", "display", 'block', { fromValue: 'block'}], position: 3758, duration: 0, easing: "easeOutBounce" },
                { id: "dg140", tween: [ "style", "${_Text7Copy2}", "display", 'none', { fromValue: 'block'}], position: 5191, duration: 0, easing: "easeOutBounce" },
                { id: "dg141", tween: [ "style", "${_Text7Copy2}", "display", 'none', { fromValue: 'none'}], position: 8191, duration: 0, easing: "easeOutBounce" },
                { id: "dg55", tween: [ "style", "${_ROCON_BANK_CARD}", "top", '198px', { fromValue: '-649px'}], position: 3250, duration: 821, easing: "easeOutBounce" },
                { id: "dg49", tween: [ "style", "${_accept}", "top", '247px', { fromValue: '-601px'}], position: 3250, duration: 821, easing: "easeOutBounce" },
                { id: "dg32", tween: [ "style", "${__114_anwansoonfge}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg19", tween: [ "style", "${_ROCON_BANK_DESC}", "display", 'none', { fromValue: 'block'}], position: 5191, duration: 0 },
                { id: "dg161", tween: [ "style", "${_Text4Copy}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg30", tween: [ "style", "${_Text4}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg78", tween: [ "style", "${_P1M5}", "left", '-693px', { fromValue: '21px'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg79", tween: [ "style", "${_P1M5}", "left", '-1410px', { fromValue: '-693px'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg80", tween: [ "style", "${_P1M5}", "left", '-1410px', { fromValue: '-1410px'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg18", tween: [ "style", "${_acceptCopy}", "top", '388px', { fromValue: '-601px'}], position: 4070, duration: 179, easing: "easeOutBounce" },
                { id: "dg131", tween: [ "style", "${_Kobuki_00}", "opacity", '0.2', { fromValue: '0.2'}], position: 7000, duration: 0 },
                { id: "dg132", tween: [ "style", "${_Kobuki_00}", "opacity", '1', { fromValue: '0.2'}], position: 9000, duration: 1000 },
                { id: "dg137", tween: [ "style", "${_Text7Copy2}", "top", '45.12%', { fromValue: '-16.65%'}], position: 3250, duration: 821, easing: "easeOutBounce" },
                { id: "dg143", tween: [ "style", "${_deleteCopy2}", "display", 'block', { fromValue: 'none'}], position: 3250, duration: 0, easing: "easeOutBounce" },
                { id: "dg144", tween: [ "style", "${_deleteCopy2}", "display", 'block', { fromValue: 'block'}], position: 3758, duration: 0, easing: "easeOutBounce" },
                { id: "dg145", tween: [ "style", "${_deleteCopy2}", "display", 'none', { fromValue: 'block'}], position: 5191, duration: 0, easing: "easeOutBounce" },
                { id: "dg146", tween: [ "style", "${_deleteCopy2}", "display", 'none', { fromValue: 'none'}], position: 8191, duration: 0, easing: "easeOutBounce" },
                { id: "dg17", tween: [ "style", "${_acceptCopy}", "left", '48px', { fromValue: '46px'}], position: 4070, duration: 179, easing: "easeOutBounce" },
                { id: "dg185", tween: [ "style", "${_Text6Copy2}", "display", 'block', { fromValue: 'none'}], position: 3250, duration: 0 },
                { id: "dg186", tween: [ "style", "${_Text6Copy2}", "display", 'block', { fromValue: 'block'}], position: 3758, duration: 0 },
                { id: "dg187", tween: [ "style", "${_Text6Copy2}", "display", 'none', { fromValue: 'block'}], position: 5191, duration: 0 },
                { id: "dg188", tween: [ "style", "${_Text6Copy2}", "display", 'none', { fromValue: 'none'}], position: 8191, duration: 0 },
                { id: "dg77", tween: [ "style", "${_Text4Copy2}", "width", '200px', { fromValue: '200px'}], position: 10000, duration: 0 },
                { id: "dg86", tween: [ "style", "${_YUJINMASTER_DESC}", "top", '370px', { fromValue: '-478px'}], position: 3250, duration: 821, easing: "easeOutBounce" },
                { id: "dg58", tween: [ "style", "${_ROCON_BANK_CARD}", "display", 'none', { fromValue: 'block'}], position: 5191, duration: 0, easing: "easeOutBounce" },
                { id: "dg88", tween: [ "style", "${_s1p1Copy}", "opacity", '1', { fromValue: '1'}], position: 8000, duration: 0 },
                { id: "dg1", tween: [ "style", "${_s1p4Copy2}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
                { id: "dg2", tween: [ "style", "${_s1p4Copy2}", "display", 'none', { fromValue: 'none'}], position: 9000, duration: 0 },
                { id: "dg3", tween: [ "style", "${_s1p4Copy2}", "display", 'block', { fromValue: 'none'}], position: 9750, duration: 0 },
                { id: "dg96", tween: [ "style", "${_Text3}", "top", '283px', { fromValue: '283px'}], position: 10500, duration: 0 },
                { id: "dg121", tween: [ "style", "${_Rectangle}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg98", tween: [ "style", "${_Text3}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg122", tween: [ "style", "${_Rectangle}", "opacity", '1', { fromValue: '0.9'}], position: 9950, duration: 50 },
                { id: "dg118", tween: [ "style", "${_s1p1Copy2}", "opacity", '1', { fromValue: '1'}], position: 9000, duration: 0 },
                { id: "eid2482", tween: [ "style", "${_yujinrobot_ci_png_b_white}", "left", '21.53%', { fromValue: '21.53%'}], position: 7000, duration: 0 },
                { id: "dg153", tween: [ "style", "${_P3M3}", "left", '102.92%', { fromValue: '203.67%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg154", tween: [ "style", "${_P3M3}", "left", '3.4%', { fromValue: '102.92%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg155", tween: [ "style", "${_P3M3}", "left", '3.4%', { fromValue: '3.4%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg109", tween: [ "style", "${_SANDWITCH_TITLE}", "display", 'none', { fromValue: 'block'}], position: 7000, duration: 0 },
                { id: "dg106", tween: [ "style", "${_s1p4Copy}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
                { id: "dg107", tween: [ "style", "${_s1p4Copy}", "display", 'none', { fromValue: 'none'}], position: 8000, duration: 0 },
                { id: "dg108", tween: [ "style", "${_s1p4Copy}", "display", 'block', { fromValue: 'none'}], position: 8750, duration: 0 },
                { id: "dg38", tween: [ "style", "${_P1M2}", "left", '-74.07%', { fromValue: '25.14%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg39", tween: [ "style", "${_P1M2}", "left", '-173.59%', { fromValue: '-74.07%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg40", tween: [ "style", "${_P1M2}", "left", '-173.59%', { fromValue: '-173.59%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg105", tween: [ "style", "${_nfc_logo}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg128", tween: [ "style", "${_s1p1}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg14", tween: [ "style", "${_Text5Copy2}", "width", '83.07%', { fromValue: '83.07%'}], position: 4070, duration: 0, easing: "easeOutBounce" },
                { id: "dg13", tween: [ "style", "${_Text5Copy2}", "left", '7.92%', { fromValue: '7.92%'}], position: 4070, duration: 0, easing: "easeOutBounce" },
                { id: "dg85", tween: [ "style", "${_YUJINMASTER_DESC}", "opacity", '1', { fromValue: '0.5'}], position: 4070, duration: 179, easing: "easeOutBounce" },
                { id: "dg120", tween: [ "style", "${_a4_nomal_png_a}", "opacity", '1', { fromValue: '0.2'}], position: 7000, duration: 1000 },
                { id: "dg34", tween: [ "style", "${_fron_blue}", "display", 'none', { fromValue: 'block'}], position: 2000, duration: 0 },
                { id: "dg35", tween: [ "style", "${_fron_blue}", "display", 'none', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg7", tween: [ "style", "${_Text2Copy}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg75", tween: [ "style", "${_Text4Copy2}", "opacity", '0.2', { fromValue: '0.2'}], position: 7000, duration: 0 },
                { id: "dg76", tween: [ "style", "${_Text4Copy2}", "opacity", '1', { fromValue: '0.2'}], position: 9000, duration: 1000 },
                { id: "dg124", tween: [ "style", "${_Rectangle}", "top", '796px', { fromValue: '796px'}], position: 7000, duration: 0 },
                { id: "dg102", tween: [ "style", "${_P2M1}", "left", '3.33%', { fromValue: '106.1%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg103", tween: [ "style", "${_P2M1}", "left", '-96.19%', { fromValue: '3.33%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg104", tween: [ "style", "${_P2M1}", "left", '-96.25%', { fromValue: '-96.25%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg92", tween: [ "style", "${_P3M2}", "left", '151%', { fromValue: '251.75%'}], position: 0, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg93", tween: [ "style", "${_P3M2}", "left", '51.48%', { fromValue: '151%'}], position: 1000, duration: 1000, easing: "easeInOutCubic" },
                { id: "dg94", tween: [ "style", "${_P3M2}", "left", '51.48%', { fromValue: '51.48%'}], position: 2000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg50", tween: [ "style", "${_COFFEE_TITLE}", "opacity", '0', { fromValue: '1'}], position: 1000, duration: 1000 },
                { id: "dg51", tween: [ "style", "${_COFFEE_TITLE}", "opacity", '0', { fromValue: '0'}], position: 2000, duration: 0 },
                { id: "dg151", tween: [ "style", "${_accept_blue_payment}", "top", '49.55%', { fromValue: '-12.19%'}], position: 3250, duration: 821, easing: "easeOutBounce" },
                { id: "dg100", tween: [ "style", "${__410_anwansoon2}", "opacity", '0.2', { fromValue: '0.2'}], position: 7000, duration: 0 },
                { id: "dg101", tween: [ "style", "${__410_anwansoon2}", "opacity", '1', { fromValue: '0.2'}], position: 8000, duration: 1000 },
                { id: "dg119", tween: [ "style", "${_a4_nomal_png_a}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg133", tween: [ "style", "${__03_pp_anwansoon}", "display", 'block', { fromValue: 'none'}], position: 7000, duration: 0 },
                { id: "dg63", tween: [ "subproperty", "${_back_blue}", "filter.saturate", '1', { fromValue: '0'}], position: 0, duration: 1000 },
                { id: "eid2473", tween: [ "style", "${_Text7Copy2}", "left", '18.19%', { fromValue: '18.19%'}], position: 3758, duration: 0 },
                { id: "dg95", tween: [ "style", "${_P3M2}", "display", 'none', { fromValue: 'block'}], position: 7000, duration: 0, easing: "easeInOutCubic" },
                { id: "dg163", tween: [ "style", "${_Text4Copy}", "opacity", '0.2', { fromValue: '0.2'}], position: 7000, duration: 0 },
                { id: "dg164", tween: [ "style", "${_Text4Copy}", "opacity", '1', { fromValue: '0.2'}], position: 8000, duration: 1000 },
                { id: "eid2474", tween: [ "style", "${_Text6Copy2}", "right", '17.08%', { fromValue: '17.08%'}], position: 3758, duration: 0 },
                { id: "dg152", tween: [ "style", "${_P3M3}", "display", 'none', { fromValue: 'block'}], position: 7000, duration: 0 },
                { id: "dg110", tween: [ "style", "${_SANDWITCH_TITLE}", "opacity", '1', { fromValue: '0'}], position: 1000, duration: 1000 },
                { id: "dg111", tween: [ "style", "${_SANDWITCH_TITLE}", "opacity", '1', { fromValue: '1'}], position: 2000, duration: 0 },
                { id: "dg89", tween: [ "style", "${_s1p2Copy2}", "display", 'none', { fromValue: 'none'}], position: 0, duration: 0 },
                { id: "dg90", tween: [ "style", "${_s1p2Copy2}", "display", 'none', { fromValue: 'none'}], position: 9000, duration: 0 },
                { id: "dg91", tween: [ "style", "${_s1p2Copy2}", "display", 'block', { fromValue: 'none'}], position: 9250, duration: 0 },
                { id: "dg8", tween: [ "style", "${_Text5Copy2}", "display", 'block', { fromValue: 'none'}], position: 3250, duration: 0 },
                { id: "dg9", tween: [ "style", "${_Text5Copy2}", "display", 'block', { fromValue: 'block'}], position: 3758, duration: 0 },
                { id: "dg10", tween: [ "style", "${_Text5Copy2}", "display", 'none', { fromValue: 'block'}], position: 5191, duration: 0 },
                { id: "dg11", tween: [ "style", "${_Text5Copy2}", "display", 'none', { fromValue: 'none'}], position: 8191, duration: 0 }            ]
        }
    }
}
};


Edge.registerCompositionDefn(compId, symbols, fonts, resources, opts);

/**
 * Adobe Edge DOM Ready Event Handler
 */
$(window).ready(function() {
     Edge.launchComposition(compId);
});
})(jQuery, AdobeEdge, "EDGE-1251484");
