document.body.style.backgroundColor = 'gray';

var dots = [];
for (var i = 0; i < 800; i++) {
var dot = document.createElement('div');
dot.style.width = '10px';
dot.style.height = '10px';
dot.style.backgroundColor = 'white';
dot.style.borderRadius = '50%';
dot.style.position = 'absolute';
dot.style.top = Math.random() * window.innerHeight + 'px';
dot.style.left = Math.random() * window.innerWidth + 'px';
document.body.appendChild(dot);
dots.push(dot);
}

var moveDots = function() {
for (var i = 0; i < dots.length; i++) {
  var dot = dots[i];
  var left = parseInt(dot.style.left);
  dot.style.left = (left + 1) + 'px';
  if (left > window.innerWidth) {
    dot.style.left = '0px';
  }
}
requestAnimationFrame(moveDots);
};
moveDots();

var speed = 15;
var moveDots = function() {
for (var i = 0; i < dots.length; i++) {
  var dot = dots[i];
  var left = parseInt(dot.style.left);
  dot.style.left = (left + speed) + 'px';
  if (left > window.innerWidth) {
    dot.style.left = '0px';
  }
}
requestAnimationFrame(moveDots);
};
moveDots();



var x = document.createElement('div');
x.innerHTML = 'X';
x.style.position = 'absolute';
x.style.top = '50%';
x.style.left = '50%';
x.style.transform = 'translate(-50%, -50%)';
x.style.fontSize = '40px';
x.style.color = '#fff';
document.body.appendChild(x);


var circle = document.createElement('div');
circle.style.position = 'absolute';
circle.style.top = '30%';
circle.style.left = '30%';
circle.style.transform = 'translate(-50%, -50%)';
circle.style.width = '50px';
circle.style.height = '50px';
circle.style.borderRadius = '50%';
circle.style.border = '2px solid #f00';
document.body.appendChild(circle);

document.body.style.overflow = 'hidden';

for (var i = 0; i < dots.length; i++) {
  var dot = dots[i];
  dot.style.width = '8px';
  dot.style.height = '8px';
}
