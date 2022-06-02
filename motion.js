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
  redRectangle.style.width = '30px';
  redRectangle.style.height = '30px';
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
  blackLine.style.width = '5px';
  blackLine.style.height = window.innerHeight + 'px';
  blackLine.style.backgroundColor = 'black';
  blackLine.style.position = 'absolute';
  blackLine.style.left = i + 'px';
  blackLine.style.top = '0px';
  document.body.appendChild(blackLine);
  lines.push(blackLine);
}

setInterval(moveLines, 10);

document.body.style.backgroundColor = '#00FFFF';

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
