        document.addEventListener("DOMContentLoaded", function() {

document.body.style.backgroundColor = 'black';

var rect1 = document.createElement('div');
rect1.style.width = '100px';
rect1.style.height = '100px';
rect1.style.backgroundColor = 'black';
rect1.style.border = '1px solid gray';
document.body.appendChild(rect1);

var rect2 = document.createElement('div');
rect2.style.width = '100px';
rect2.style.height = '100px';
rect2.style.backgroundColor = 'black';
rect2.style.border = '1px solid gray';
document.body.appendChild(rect2);

rect1.style.float = 'left';
rect2.style.float = 'right';

rect1.style.width = '300px';
rect1.style.height= '350px';

rect2.style.width = '300px';
rect2.style.height= '350px';

for (var i = 0; i < 100; i++) {
  var dot = document.createElement('div');
  dot.style.width = '10px';
  dot.style.height = '10px';
  dot.style.backgroundColor = 'blue';
  dot.style.borderRadius = '50%';
  dot.style.float = 'left';
  rect1.appendChild(dot);
}

for (var i = 0; i < 100; i++) {
  var dot = document.createElement('div');
  dot.style.width = '10px';
  dot.style.height = '10px';
  dot.style.backgroundColor = 'blue';
  dot.style.borderRadius = '50%';
  dot.style.float = 'left';
  rect2.appendChild(dot);
}

var rect1Dots = rect1.childNodes;
var rect2Dots = rect2.childNodes;

function moveDots(dots) {
  for (var i = 0; i < dots.length; i++) {
    var dot = dots[i];
    var x = Math.floor(Math.random() * 50);
    var y = Math.floor(Math.random() * 50);
    dot.style.marginLeft = x + 'px';
    dot.style.marginTop = y + 'px';
  }
}


setInterval(function() {
  moveDots(rect1Dots);
  moveDots(rect2Dots);
}, 150);
rect1.style.width = '40%';
rect1.style.height = '100%';
rect2.style.width = '40%';
rect2.style.height = '100%';


document.body.style.overflow = 'hidden';
var circle = document.createElement('div');
circle.style.width = '25px';
circle.style.height = '25px';
circle.style.backgroundColor = 'yellow';
circle.style.borderRadius = '50%';
circle.style.position = 'absolute';
circle.style.top = '50%';
circle.style.left = '90%';
circle.style.marginTop = '-50px';
circle.style.marginLeft = '-50px';
document.body.appendChild(circle);
var cross1 = document.createElement('div');
cross1.style.width = '10px';
cross1.style.height = '10px';
cross1.style.backgroundColor = 'white';
cross1.style.position = 'absolute';
cross1.style.top = '50%';
cross1.style.left = '80%';
cross1.style.marginTop = '-50px';
cross1.style.marginLeft = '-50px';
document.body.appendChild(cross1);
var cross2 = document.createElement('div');
cross2.style.width = '10px';
cross2.style.height = '10px';
cross2.style.backgroundColor = 'white';
cross2.style.position = 'absolute';
cross2.style.top = '50%';
cross2.style.left = '40%';
cross2.style.marginTop = '-50px';
cross2.style.marginLeft = '-290px';
document.body.appendChild(cross2);
cross1.style.transform = 'rotate(45deg)';
cross2.style.transform = 'rotate(45deg)';
var slider = document.createElement('input');
slider.type = 'range';
slider.min = '10';
slider.max = '50';
slider.value = '10';
slider.style.position = 'absolute';
slider.style.left = '50%';
slider.style.top = '10%';
document.body.appendChild(slider);
slider.oninput = function() {
  for (var i = 0; i < rect1Dots.length; i++) {
    var dot = rect1Dots[i];
    dot.style.width = slider.value + 'px';
    dot.style.height = slider.value + 'px';
  }
  for (var i = 0; i < rect2Dots.length; i++) {
    var dot = rect2Dots[i];
    dot.style.width = slider.value + 'px';
    dot.style.height = slider.value + 'px';
  }
};






circle.addEventListener('mousedown', function(e) {
  var startX = e.clientX;
  var startY = e.clientY;
  var startLeft = parseInt(circle.style.left);
  var startTop = parseInt(circle.style.top);
  document.addEventListener('mousemove', onMouseMove);
  document.addEventListener('mouseup', onMouseUp);
  function onMouseMove(e) {
    var newLeft = startLeft + e.clientX - startX;
    var newTop = startTop + e.clientY - startY;
    circle.style.left = newLeft + 'px';
    circle.style.top = newTop + 'px';
  }
  function onMouseUp() {
    document.removeEventListener('mousemove', onMouseMove);
    document.removeEventListener('mouseup', onMouseUp);
  }
});
var decreaseButton = document.createElement('button');
decreaseButton.innerHTML = '-';
decreaseButton.style.position = 'fixed';
decreaseButton.style.top = '90px';
decreaseButton.style.left = '0px';
decreaseButton.style.width = '50px';
decreaseButton.style.height = '50px';
decreaseButton.style.fontSize = '30px';
decreaseButton.style.backgroundColor = 'white';
decreaseButton.style.border = 'none';
decreaseButton.style.borderRadius = '50%';
decreaseButton.style.color = 'black';
decreaseButton.style.cursor = 'pointer';
document.body.appendChild(decreaseButton);
var increaseButton = document.createElement('button');
increaseButton.innerHTML = '+';
increaseButton.style.position = 'fixed';
increaseButton.style.top = '90px';
increaseButton.style.right = '0px';
increaseButton.style.width = '50px';
increaseButton.style.height = '50px';
increaseButton.style.fontSize = '30px';
increaseButton.style.backgroundColor = 'white';
increaseButton.style.border = 'none';
increaseButton.style.borderRadius = '50%';
increaseButton.style.color = 'black';
increaseButton.style.cursor = 'pointer';
document.body.appendChild(increaseButton);
var speed = 50;
var intervalId;
function startAnimation() {
  intervalId = setInterval(function() {
    moveDots(rect1Dots);
    moveDots(rect2Dots);
  }, speed);
}
function stopAnimation() {
  clearInterval(intervalId);
}
startAnimation();
decreaseButton.onclick = function() {
  stopAnimation();
  speed += 150;
  startAnimation();
};
increaseButton.onclick = function() {
  stopAnimation();
  speed -= 150;
  startAnimation();
};

var hideButton = document.createElement('button');
hideButton.innerHTML = 'Hide/Show';
hideButton.style.position = 'fixed';
hideButton.style.top = '90%';
hideButton.style.left = '30%';
hideButton.style.width = '170px';
hideButton.style.height = '50px';
hideButton.style.fontSize = '30px';
hideButton.style.backgroundColor = 'white';
hideButton.style.border = 'none';
hideButton.style.borderRadius = '50%';
hideButton.style.color = 'black';
hideButton.style.cursor = 'pointer';
document.body.appendChild(hideButton);
hideButton.onclick = function() {
  if (rect1.style.display === 'none') {
    rect1.style.display = 'block';
    rect2.style.display = 'block';
  } else {
    rect1.style.display = 'none';
    rect2.style.display = 'none';
  }
};
hideButton.style.left = 'calc(50% - 50px)';
decreaseButton.style.backgroundColor = '#ff0000';
increaseButton.style.backgroundColor = '#00ff00';
hideButton.style.backgroundColor = '#0000ff';

var addCircleButton = document.createElement('button');
addCircleButton.innerHTML = 'Add Circle';
addCircleButton.style.position = 'fixed';
addCircleButton.style.top = '90%';
addCircleButton.style.left = 'calc(30% - 100px)';
addCircleButton.style.width = '200px';
addCircleButton.style.height = '50px';
addCircleButton.style.fontSize = '30px';
addCircleButton.style.backgroundColor = 'white';
addCircleButton.style.border = 'none';
addCircleButton.style.borderRadius = '50%';
addCircleButton.style.color = 'black';
addCircleButton.style.cursor = 'pointer';
document.body.appendChild(addCircleButton);
addCircleButton.onclick = function() {
  var circle = document.createElement('div');
  circle.style.width = '25px';
  circle.style.height = '25px';
  circle.style.backgroundColor = 'yellow';
  circle.style.borderRadius = '50%';
  circle.style.position = 'absolute';
  circle.style.top = '50%';
  circle.style.left = '50%';
  circle.style.marginLeft = '-25px';
  circle.style.marginTop = '-25px';
  circle.style.cursor = 'pointer';
  document.body.appendChild(circle);
  circle.onmousedown = function(e) {
    var initialX = e.clientX;
    var initialY = e.clientY;
    var initialLeft = parseInt(circle.style.left);
    var initialTop = parseInt(circle.style.top);
    document.onmousemove = function(e) {
      var newX = e.clientX;
      var newY = e.clientY;
      var deltaX = newX - initialX;
      var deltaY = newY - initialY;
      circle.style.left = initialLeft + deltaX + 'px';
      circle.style.top = initialTop + deltaY + 'px';
    };
    document.onmouseup = function() {
      document.onmousemove = null;
      document.onmouseup = null;
    };
  };
};
var slider2 = document.createElement('input');
slider2.type = 'range';
slider2.min = '1';
slider2.max = '100';
slider2.value = '1';
slider2.style.position = 'absolute';
slider2.style.top = '0';
slider2.style.left = '40%';
document.body.appendChild(slider2);
slider2.oninput = function() {
  circle.style.width = slider2.value + 'px';
  circle.style.height = slider2.value + 'px';
  circle.style.marginTop = -slider2.value / 2 + 'px';
  circle.style.marginLeft = -slider2.value / 2 + 'px';
};
document.body.style.overflow = 'hidden';

var plus = document.createElement('div');
plus.style.width = '50px';
plus.style.height = '50px';
plus.style.backgroundColor = 'red';
plus.style.borderRadius = '50%';
plus.style.position = 'absolute';
plus.style.top = '50%';
plus.style.left = '50%';
plus.style.marginLeft = '-25px';
plus.style.marginTop = '-25px';
plus.style.cursor = 'pointer';
plus.style.display = 'flex';
plus.style.justifyContent = 'center';
plus.style.alignItems = 'center';
plus.style.fontSize = '30px';
plus.style.color = 'white';
plus.innerHTML = '+';
document.body.appendChild(plus);

    var github = document.createElement('a');
    github.href = 'https://github.com/altunenes';
    github.innerHTML = 'GitHub';
    github.style.position = 'fixed';
    github.style.bottom = '0';
    github.style.right = '0';
    github.style.padding = '10px';
    github.style.backgroundColor = '#333';
    github.style.color = '#fff';
    document.body.appendChild(github);
    var twitter = document.createElement('a');
    twitter.href = 'https://twitter.com/emportent';
    twitter.innerHTML = 'Twitter';
    twitter.style.position = 'fixed';
    twitter.style.bottom = '0';
    twitter.style.right = '100px';
    twitter.style.padding = '10px';
    twitter.style.backgroundColor = '#333';
    twitter.style.color = '#fff';
    document.body.appendChild(twitter);
    document.body.style.overflow = 'hidden';
    
    github.innerHTML = '<i class="fa fa-github"></i>';
    twitter.innerHTML = '<i class="fa fa-twitter"></i>';
    var fontAwesome = document.createElement('link');
    fontAwesome.rel = 'stylesheet';
    fontAwesome.href = 'https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css';
    document.head.appendChild(fontAwesome);

    plus.onmousedown = function(e) {
      var initialX = e.clientX;
      var initialY = e.clientY;
      var initialLeft = parseInt(plus.style.left);
      var initialTop = parseInt(plus.style.top);
      document.onmousemove = function(e) {
        var newX = e.clientX;
        var newY = e.clientY;
        var deltaX = newX - initialX;
        var deltaY = newY - initialY;
        plus.style.left = initialLeft + deltaX + 'px';
        plus.style.top = initialTop + deltaY + 'px';
      };
      document.onmouseup = function() {
        document.onmousemove = null;
        document.onmouseup = null;
      };
    };

    var blurButton = document.createElement('button');
    blurButton.innerHTML = 'Blur';
    blurButton.style.position = 'absolute';
    blurButton.style.left = '3%';
    blurButton.style.top = '95%';
    blurButton.style.transform = 'translate(-50%, -50%)';
    blurButton.onclick = function() {
      if (blurButton.innerHTML == 'Blur') {
        blurButton.innerHTML = 'Blur more';
        document.body.style.filter = 'blur(5px)';
      } else if (blurButton.innerHTML == 'Blur more') {
        blurButton.innerHTML = 'Blur less';
        document.body.style.filter = 'blur(10px)';
      } else {
        blurButton.innerHTML = 'Blur';
        document.body.style.filter = 'blur(0px)';
      }
    };
    document.body.appendChild(blurButton);
    
    blurButton.style.fontFamily = 'sans-serif';
    blurButton.style.fontSize = '20px';
    blurButton.style.color = 'white';
    blurButton.style.backgroundColor = 'gray';
    blurButton.style.border = 'none';
    blurButton.style.padding = '10px 20px';
    blurButton.style.borderRadius = '5px';
    });
