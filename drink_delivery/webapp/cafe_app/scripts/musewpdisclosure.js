/*
 ADOBE CONFIDENTIAL
 ___________________

 Copyright 2012 Adobe Systems Incorporated
 All Rights Reserved.

 NOTICE:  All information contained herein is, and remains
 the property of Adobe Systems Incorporated and its suppliers,
 if any.  The intellectual and technical concepts contained
 herein are proprietary to Adobe Systems Incorporated and its
 suppliers and may be covered by U.S. and Foreign Patents,
 patents in process, and are protected by trade secret or copyright law.
 Dissemination of this information or reproduction of this material
 is strictly forbidden unless prior written permission is obtained
 from Adobe Systems Incorporated.
*/
(function(b,c,a){a.Plugins.TabbedPanelsPlugin={defaultOptions:{widgetClassName:"TabbedPanelsWidget",tabClassName:"TabbedPanelsTab",tabHoverClassName:"TabbedPanelsTabHover",tabDownClassName:"TabbedPanelsTabDown",tabActiveClassName:"TabbedPanelsTabSelected",panelClassName:"TabbedPanelsContent",panelActiveClassName:"TabbedPanelsContentVisible",defaultIndex:0,canCloseAll:!1},initialize:function(a,g){var f=this;b.extend(g,b.extend({},f.defaultOptions,g));c.Widget.Disclosure.DisplayPropertyTransitionPlugin.initialize(a,
g);a.bind("attach-behavior",function(){f._attachBehavior(a)})},_attachBehavior:function(a){var b=a.tabs?a.tabs.$element:null;if(b&&(b.first().addClass("TabbedPanelsTabFirst"),b.last().addClass("TabbedPanelsTabLast"),a.options.event!=="click"))b.on(a.options.event,function(){a.tabs.selectTab(this)})}};a.Plugins.AccordionPlugin={defaultOptions:{widgetClassName:"AccordionWidget",tabClassName:"AccordionPanelTab",tabHoverClassName:"AccordionPanelTabHover",tabDownClassName:"AccordionPanelTabDown",tabActiveClassName:"AccordionPanelTabOpen",
panelClassName:"AccordionPanelContent",panelActiveClassName:"AccordionPanelContentActive",defaultIndex:0,canCloseAll:!1,transitionDirection:"vertical"},initialize:function(a,g){var f=this;b.extend(g,b.extend({},f.defaultOptions,g));g.toggleStateEnabled=g.canCloseAll;c.Widget.Disclosure.AccordionTransitionPlugin.initialize(a,g);a.bind("transform-markup",function(){f._transformMarkup(a)});a.bind("attach-behavior",function(){f._attachBehavior(a)})},_transformMarkup:function(a){var b=a.$element[0];c.scopedFind(b,
".AccordionPanelContent",a.options.widgetClassName,b).removeClass("AccordionPanelContent colelem").wrap('<div class="AccordionPanelContent colelem"><div class="AccordionPanelContentClip"></div></div>').closest(".AccordionPanelContent").css({width:"100%",position:"relative"})},_attachBehavior:function(a){var b=a.$element[0],a=a.options,f=0,h=a.transitionDirection==="vertical",j=h?"offsetWidth":"offsetHeight",i=h?"width":"height";c.scopedFind(b,".AccordionPanel",a.widgetClassName,b).each(function(){f=
f<this[j]?this[j]:f}).each(function(){f>this[j]&&(this.style[i]=f+"px")})}};c.Widget.TabbedPanels.prototype.defaultPlugins=[a.Plugins.TabbedPanelsPlugin];c.Widget.Accordion.prototype.defaultPlugins=[a.Plugins.AccordionPlugin]})(jQuery,WebPro,Muse,window);
