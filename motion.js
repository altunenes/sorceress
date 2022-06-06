var rectangles = [];
var speed2 = 1;
var slider2 = document.createElement('input');
slider2.type = 'range';
slider2.min = 1;
slider2.max = 10;
slider2.value = 1;
slider2.oninput = function() {
  speed2 = slider2.value;
};
document.body.appendChild(slider2);
document.body.style.overflow = 'hidden';

function moveRectangles() {
  for (var i = 0; i < rectangles.length; i++) {
    rectangles[i].style.top = parseInt(rectangles[i].style.top) - speed2 + 'px';
    if (parseInt(rectangles[i].style.top) < -10) {
      rectangles[i].style.top = window.innerHeight + 'px';
    }
  }
}
for (var i = 0; i < 10; i++) {
  var redRectangle = document.createElement('div');
  redRectangle.style.width = '40px';
  redRectangle.style.height = '40px';
  redRectangle.style.backgroundColor = 'red';
  redRectangle.style.position = 'absolute';
  redRectangle.style.left = Math.random() * window.innerWidth + 'px';
  redRectangle.style.top = Math.random() * window.innerHeight + 'px';
  document.body.appendChild(redRectangle);
  rectangles.push(redRectangle);
}

setInterval(moveRectangles, 10);

var lines = [];
var speed = 1;


function moveLines() {
  for (var i = 0; i < lines.length; i++) {
    lines[i].style.left = parseInt(lines[i].style.left) + speed + 'px';
    if (parseInt(lines[i].style.left) > window.innerWidth) {
      lines[i].style.left = '0px';
    }
  }
}

for (var i = 0; i < window.innerWidth; i += 24) {
  var blackLine = document.createElement('div');
  blackLine.style.width = '23px';
  blackLine.style.height = window.innerHeight + 'px';
  blackLine.style.backgroundColor = 'black';
  blackLine.style.position = 'absolute';
  blackLine.style.left = i + 'px';
  blackLine.style.top = '0px';
  document.body.appendChild(blackLine);
  lines.push(blackLine);
}

setInterval(moveLines, 10);


var reds = [];
var speed4 = 1;


function movereds() {
  for (var i = 0; i < reds.length; i++) {
    reds[i].style.left = parseInt(reds[i].style.left) + speed4 + 'px';
    if (parseInt(reds[i].style.left) > window.innerWidth) {
      reds[i].style.left = '0px';
    }
  }
}

for (var i = 0; i < 10; i++) {
  var reds4 = document.createElement('div');
  reds4.style.width = '10px';
  reds4.style.height = '10px';
  reds4.style.backgroundColor = 'black';
  reds4.style.position = 'absolute';
  reds4.style.left = i * window.innerWidth + 'px';
  reds4.style.top = Math.random() * window.innerHeight + 'px';
  document.body.appendChild(reds4);
  reds.push(reds4);
}

setInterval(movereds, 10);


var slider4 = document.createElement('input');
slider4.type = 'range';
slider4.min = '0';
slider4.max = '25';
slider4.value = '0';
slider4.style.position = 'absolute';
slider4.style.top = '1%';
slider4.style.right = '65%';
slider4.style.transform = 'translate(-50%, -50%)';
document.body.appendChild(slider4);
slider4.addEventListener('change', function() {
  document.body.style.filter = 'blur(' + slider4.value + 'px)';
});

var slider3 = document.createElement('input');
slider3.type = 'range';
slider3.min = '0';
slider3.max = '360';
slider3.value = '0';
slider3.style.position = 'absolute';
slider3.style.top = '1%';
slider3.style.right = '55%';
slider3.style.transform = 'translate(-50%, -50%)';
document.body.appendChild(slider3);
slider3.addEventListener('change', function() {
  document.body.style.transform = 'rotate(' + slider3.value + 'deg)';
});
