var canvas = document.createElement('canvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;
document.body.appendChild(canvas);
var ctx = canvas.getContext('2d');
ctx.fillStyle = 'black';
for (var i = 0; i < window.innerWidth; i += 10) {
  ctx.fillRect(i, 0, 5, window.innerHeight);
}


var rect = document.createElement('div');
rect.style.position = 'absolute';
rect.style.left = '150px';
rect.style.top = '150px';
rect.style.width = '22px';
rect.style.height = '65px';
rect.style.backgroundColor = 'yellow';
document.body.appendChild(rect);

var rect = document.createElement('div');
rect.style.position = 'absolute';
rect.style.left = '150px';
rect.style.top = '250px';
rect.style.width = '22px';
rect.style.height = '65px';
rect.style.backgroundColor = 'blue';
document.body.appendChild(rect);

var rect = document.createElement('div');
rect.style.position = 'absolute';
rect.style.left = '250px';
rect.style.top = '250px';
rect.style.width = '22px';
rect.style.height = '65px';
rect.style.backgroundColor = 'blue';
document.body.appendChild(rect);

var rect = document.createElement('div');
rect.style.position = 'absolute';
rect.style.left = '250px';
rect.style.top = '150px';
rect.style.width = '22';
rect.style.height = '65px';
rect.style.backgroundColor = 'yellow';
document.body.appendChild(rect);


var rect = document.createElement('div');
rect.style.position = 'absolute';
rect.style.left = '205px';
rect.style.top = '230px';
rect.style.width = '8';
rect.style.height = '8px';
rect.style.backgroundColor = 'red';
document.body.appendChild(rect);

var rects = document.querySelectorAll('div');
var direction = 1;
var speed = 1;
function animate() {
  for (var i = 0; i < rects.length; i++) {
    var rect = rects[i];
    rect.style.left = (parseInt(rect.style.left) + speed * direction) + 'px';
    if (parseInt(rect.style.left) >= window.innerWidth - 15) {
      direction = -1;
    }
    if (parseInt(rect.style.left) <= 0) {
      direction = 1;
    }
  }
  requestAnimationFrame(animate);
}
animate();
