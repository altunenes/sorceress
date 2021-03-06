var circles = [];
var numCircles = 14;
var radius = 100;
var speed = 0.1;
var angle = 0;
var angleIncrement = 2 * Math.PI / numCircles;
for (var i = 0; i < numCircles; i++) {
  var circle = document.createElement('div');
  circle.style.width = circle.style.height = radius + 'px';
  circle.style.borderRadius = '100%';
  circle.style.position = 'absolute';
  circle.style.left = circle.style.top = '50%';
  circle.style.marginLeft = 100+ 'px';
  circle.style.marginTop = 150+ 'px';
  circle.style.backgroundColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
  document.body.appendChild(circle);
  circles.push(circle);
}
function animate() {
  angle += speed;
  for (var i = 0; i < numCircles; i++) {
    var circle = circles[i];
    var x = radius * Math.cos(angle + i * angleIncrement);
    var y = radius * Math.sin(angle + i * angleIncrement);
    circle.style.left = x + 'px';
    circle.style.top = y + 'px';
  }
  requestAnimationFrame(animate);
}
animate();

var circles2 = [];
var numCircles2 = 14;
var radius2 = 100;
var speed2 = 0.1;
var angle2 = 0;
var angleIncrement2 = 2 * Math.PI / numCircles2;
for (var i = 0; i < numCircles2; i++) {
  var circle2 = document.createElement('div');
  circle2.style.width = circle2.style.height = radius2 + 'px';
  circle2.style.borderRadius = '100%';
  circle2.style.position = 'absolute';
  circle2.style.left = circle2.style.top = '50%';
  circle2.style.marginLeft = 410+ 'px';
  circle2.style.marginTop = 150+ 'px';
  circle2.style.backgroundColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
  document.body.appendChild(circle2);
  circles2.push(circle2);
}

function animate2() {
  angle2 += speed2;
  for (var i = 0; i < numCircles2; i++) {
    var circle2 = circles2[i];
    var x2 = radius2 * Math.cos(angle2 + i * angleIncrement2);
    var y2 = radius2 * Math.sin(angle2 + i * angleIncrement2);
    circle2.style.left = x2 + 'px';
    circle2.style.top = y2 + 'px';
  }
  requestAnimationFrame(animate2);
}
animate2();

for (var i = 0; i < numCircles; i++) {
  var circle = circles[i];
  var circle2 = circles2[i];
  circle.style.backgroundColor = circle2.style.backgroundColor;
}

document.body.style.backgroundColor = 'gray';

var slider4 = document.createElement('input');
   slider4.type = 'range';
   slider4.min = '0';
   slider4.max = '25';
   slider4.value = '0';
   slider4.style.position = 'absolute';
   slider4.style.top = '5%';
   slider4.style.right = '75%';
   slider4.style.transform = 'translate(-50%, -50%)';
   document.body.appendChild(slider4);
   slider4.addEventListener('change', function() {
     document.body.style.filter = 'blur(' + slider4.value + 'px)';
   });

var colors = ['blue','gray','yellow','purple'];
var colorIndex = 0;
function animate3() {
  colorIndex = (colorIndex + 1) % colors.length;
  for (var i = 0; i < numCircles; i++) {
    var circle = circles[i];
    var circle2 = circles2[i];
    circle.style.backgroundColor = colors[colorIndex];
    circle2.style.backgroundColor = colors[colorIndex];
  }
  requestAnimationFrame(animate3);
}
animate3();



document.body.style.overflow = 'hidden';

var header = document.createElement('h1');
header.innerHTML = 'Circles are rotating left to right';
header.style.position = 'absolute';
header.style.top = '70%';
header.style.left = '50%';
header.style.transform = 'translate(-50%, -50%)';
document.body.appendChild(header);
header.style.fontSize = '15px';
header.style.color = '#' + Math.floor(Math.random() * 16777215).toString(16);
