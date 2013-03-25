/*
   See License file
 */

_DEBUG_ = false;
(function (root, factory) {
    if(typeof define === 'function' && define.amd) {
        define([], factory);
    }
    else {
        root.VirtualJoystick = factory();
    }
}(this, function() {
var VirtualJoystick = function(opts)
{
  opts               = opts              || {};
  this._container    = opts.container    || document.body;
  this._mouseSupport = 'mouseSupport' in opts? opts.mouseSupport  : false;
  this._range        = opts.range        || 60;
  this.processMessage = opts.processMessage || function(x,y) {};

  this._container.style.cursor = 'pointer';
  this._container.style.position = "relative";
  
  this._pressed = false;
  this._baseX = 0;
  this._baseY = 0;
  this._stickX = 0;
  this._stickY = 0;

  __bind = function(fn, me){ return function(){ return fn.apply(me, arguments); }; };

  this._$onTouchStart = __bind(this._onTouchStart, this);
  this._$onTouchEnd   = __bind(this._onTouchEnd  , this);
  this._$onTouchMove  = __bind(this._onTouchMove , this);
  this._container.addEventListener('touchstart' , this._$onTouchStart, false);
  this._container.addEventListener('touchend'   , this._$onTouchEnd  , false);
  this._container.addEventListener('touchmove'  , this._$onTouchMove , false);
  if (this._mouseSupport) {
    this._$onMouseDown = __bind(this._onMouseDown, this);
    this._$onMouseUp   = __bind(this._onMouseUp  , this);
    this._$onMouseMove = __bind(this._onMouseMove, this);
    this._$onMouseOut  = __bind(this._onMouseOut , this);
    this._container.addEventListener('mousedown', this._$onMouseDown, false);
    this._container.addEventListener('mouseup'  , this._$onMouseUp  , false);
    this._container.addEventListener('mousemove', this._$onMouseMove, false);
    this._container.addEventListener('mouseout' , this._$onMouseOut , false);
  }

  this._ctx = this._container.getContext('2d');

  this._clear();
  this._drawText();

  // This is a bit tricky: the method registered with setInterval cannot properly reference
  // the current object with "this", so we save this global reference to it as a workaround
  _self_ = this;
}

VirtualJoystick.prototype.destroy = function()
{
  this._container.removeEventListener('touchstart' , this._$onTouchStart, false);
  this._container.removeEventListener('touchend'   , this._$onTouchEnd  , false);
  this._container.removeEventListener('touchmove'  , this._$onTouchMove , false);
  if (this._mouseSupport) {
    this._container.removeEventListener('mouseup'  , this._$onMouseUp   , false);
    this._container.removeEventListener('mousedown', this._$onMouseDown , false);
    this._container.removeEventListener('mousemove', this._$onMouseMove , false);
    this._container.removeEventListener('mouseout' , this._$onMouseOut  , false);
  }
}

/**
 * @returns {Boolean} true if touchscreen is currently available, false otherwise
*/
VirtualJoystick.touchScreenAvailable = function()
{
  return 'createTouch' in document ? true : false;
}

//////////////////////////////////////////////////////////////////////////////////
//                    //
//////////////////////////////////////////////////////////////////////////////////

VirtualJoystick.prototype.deltaX = function(){ return this._stickX - this._baseX;  }
VirtualJoystick.prototype.deltaY = function(){ return this._stickY - this._baseY;  }

VirtualJoystick.prototype.up = function() {
  if (this._pressed === false)  return false;
  var deltaX = this.deltaX();
  var deltaY = this.deltaY();
  if (deltaY >= 0)  return false;
  if (Math.abs(deltaY) < this._range && Math.abs(deltaY) < Math.abs(deltaX)) {
    return false;
  }
  return true;
}
VirtualJoystick.prototype.down = function() {
  if (this._pressed === false)  return false;
  var deltaX = this.deltaX();
  var deltaY = this.deltaY();
  if (deltaY <= 0)  return false;
  if (Math.abs(deltaY) < this._range && Math.abs(deltaY) < Math.abs(deltaX)) {
    return false;
  }
  return true;  
}
VirtualJoystick.prototype.right = function() {
  if (this._pressed === false)  return false;
  var deltaX = this.deltaX();
  var deltaY = this.deltaY();
  if (deltaX <= 0)  return false;
  if (Math.abs(deltaX) < this._range && Math.abs(deltaY) > Math.abs(deltaX)) {
    return false;
  }
  return true;  
}
VirtualJoystick.prototype.left = function() {
  if (this._pressed === false)  return false;
  var deltaX = this.deltaX();
  var deltaY = this.deltaY();
  if (deltaX >= 0)  return false;
  if (Math.abs(deltaX) < this._range && Math.abs(deltaY) > Math.abs(deltaX)) {
    return false;
  }
  return true;  
}

//////////////////////////////////////////////////////////////////////////////////
//                    //
//////////////////////////////////////////////////////////////////////////////////

VirtualJoystick.prototype._sendMessage = function()
{
  // Send a message with the joystick deltas
  //console.log("here");
  //gapi.hangout.data.sendMessage('deltaX: ' + _self_.deltaX() + ' deltaY: ' + _self_.deltaY());

  _self_.processMessage(_self_.deltaX(),_self_.deltaY());

//  _self_._ctx.fillStyle = '#FFF';
//  _self_._ctx.font = "16px Arial";
//  _self_._ctx.fillText('Virtual joystick: '
//  + '  dx:' + _self_.deltaX()
//  + '  dy:' + _self_.deltaY()
//  + (_self_.right() ? ' right' : '')
//  + (_self_.up()    ? ' up'    : '')
//  + (_self_.left()  ? ' left'  : '')
//  + (_self_.down()  ? ' down'  : ''),
//  15, 30);
}

VirtualJoystick.prototype._onUp = function()
{
  if (_DEBUG_)
    console.log('RELEASED');

  this._pressed = false; 
  
  this._baseX  = this._baseY  = 0;
  this._stickX = this._stickY = 0;

  this._clear();
  this._drawText();

  this._container.style.cursor = 'pointer';

  // Send update to shared state
  //gapi.hangout.data.submitDelta( {'deltaX':'0', 'deltaY':'0'} );

  // Force last 0-0 message and stop sending messages
  this._sendMessage();
  
  clearInterval(this._msg_timer);
}

VirtualJoystick.prototype._onDown = function(x, y)
{
  if (_DEBUG_)
    console.log('PRESSED   x = ' + x +'  y = ' + y + '   dX: 0  dY" 0');

  this._pressed = true; 
  this._baseX   = x;
  this._baseY   = y;
  this._stickX  = x;
  this._stickY  = y;

  this._clear();
  this._drawBase(this._baseX, this._baseY);
  this._drawStick(this._stickX, this._stickY);
  this._drawText(true);

  this._container.style.cursor = 'move';

  // Send update to shared state
  //gapi.hangout.data.submitDelta( {'deltaX':'0', 'deltaY':'0'} );

  // Start sending joystick deltas messages every 100 milliseconds
  this._msg_timer = setInterval(VirtualJoystick.prototype._sendMessage, 100);
}

VirtualJoystick.prototype._onMove = function(x, y)
{
  if (_DEBUG_)
    console.log('MOVED   x = ' + x +'  y = ' + y + '   dX: ' + this.deltaX() + '  dY: ' + this.deltaY());

  if (this._pressed === true) {
    this._stickX = x;
    this._stickY = y;

    this._clear();
    this._drawBase(this._baseX, this._baseY);
    this._drawStick(this._stickX, this._stickY);
    this._drawText(true);

    this._container.style.cursor = 'move';

    // Send update to shared state
    //gapi.hangout.data.submitDelta( {'deltaX': '' + this.deltaX(), 'deltaY': '' + this.deltaY()} );
  }
}


//////////////////////////////////////////////////////////////////////////////////
//               bind touch events (and mouse events for debug)                 //
//////////////////////////////////////////////////////////////////////////////////

VirtualJoystick.prototype._canvasCoords = function(x,y)
{
  var totalOffsetX = 0;
  var totalOffsetY = 0;
  var currentElement = this._container;
  
  do {
    totalOffsetX += currentElement.offsetLeft;
    totalOffsetY += currentElement.offsetTop;
  }
  while(currentElement = currentElement.offsetParent)

  return {x:x - totalOffsetX, y:y - totalOffsetY};
}

VirtualJoystick.prototype._onMouseUp = function(event)
{
  return this._onUp();
}

VirtualJoystick.prototype._onMouseDown = function(event)
{
  event.preventDefault();

  var coords = this._canvasCoords(event.clientX,event.clientY);
  return this._onDown(coords.x, coords.y);
}

VirtualJoystick.prototype._onMouseMove = function(event)
{
  event.preventDefault();

  var coords = this._canvasCoords(event.clientX,event.clientY);
  return this._onMove(coords.x, coords.y);
}

VirtualJoystick.prototype._onMouseOut = function(event)
{
  event.preventDefault();

  if (this._pressed === true)
    return this._onUp();
}

VirtualJoystick.prototype._onTouchStart = function(event)
{
  if (event.touches.length != 1)  return;

  event.preventDefault();
  var x = event.touches[ 0 ].pageX;
  var y = event.touches[ 0 ].pageY;

  var coords = this._canvasCoords(x,y);

  return this._onDown(coords.x,coords.y);
}

VirtualJoystick.prototype._onTouchEnd = function(event)
{
//??????
// no preventDefault to get click event on ios
event.preventDefault();

  return this._onUp();
}

VirtualJoystick.prototype._onTouchMove = function(event)
{
  if (event.touches.length != 1)  return;

  event.preventDefault();

  var x = event.touches[ 0 ].pageX;
  var y = event.touches[ 0 ].pageY;
  var coords = this._canvasCoords(x,y);
  return this._onMove(coords.x,coords.y);
}


//////////////////////////////////////////////////////////////////////////////////
//    build default stickEl and baseEl        //
//////////////////////////////////////////////////////////////////////////////////

VirtualJoystick.prototype._clear = function()
{
  this._ctx.fillStyle = '#BBB';
  this._ctx.fillRect(0, 0, this._container.width, this._container.height);
}

VirtualJoystick.prototype._drawBase = function(x, y)
{
  this._ctx.beginPath(); 
  this._ctx.strokeStyle = "cyan"; 
  this._ctx.lineWidth = 6; 
  this._ctx.arc(x, y, 40, 0, Math.PI*2, true); 
  this._ctx.stroke();  

  this._ctx.beginPath(); 
  this._ctx.strokeStyle = "cyan"; 
  this._ctx.lineWidth = 2; 
  this._ctx.arc(x, y, 60, 0, Math.PI*2, true); 
  this._ctx.stroke();
}


VirtualJoystick.prototype._drawStick = function(x, y)
{
  this._ctx.beginPath(); 
  this._ctx.strokeStyle = "cyan"; 
  this._ctx.lineWidth = 6; 
  this._ctx.arc(x, y, 40, 0, Math.PI*2, true); 
  this._ctx.stroke();
}

VirtualJoystick.prototype._drawButton = function(x, y)
{
  this._ctx.beginPath(); 
  this._ctx.strokeStyle = "red"; 
  this._ctx.lineWidth = 6; 
  this._ctx.arc(x, y, 40, 0, Math.PI*2, true); 
  this._ctx.stroke();
}

VirtualJoystick.prototype._drawText = function(output)
{
  var text = 'Virtual joystick';
  text += output ?
         ': dx:' + this.deltaX()
       + '  dy:' + this.deltaY()
       + (this.right() ? ' right' : '')
       + (this.up()    ? ' up'    : '')
       + (this.left()  ? ' left'  : '')
       + (this.down()  ? ' down'  : ''):'';

  this._ctx.fillStyle = '#FFF';
  this._ctx.font = "15px Arial";
  this._ctx.fillText(text, 10, 25);
}

return VirtualJoystick;
}));
