var ball3 = document.createElement('div');
ball3.style.position = 'absolute';
ball3.style.left = '20px';
ball3.style.top = '20px';
ball3.style.width = '20px';
ball3.style.height = '40px';
ball3.style.backgroundColor = 'purple';
document.body.appendChild(ball3);
var p = 0;
var direction = 1;
setInterval(function() {
  p += direction;
  ball3.style.left = p + 'px';
  if (p >= document.body.clientWidth - 50) {
    direction = -1;
  } else if (p <= 0) {
    direction = 1;
  }
}, 44);
var ball4 = document.createElement('div');
ball4.style.position = 'absolute';
ball4.style.left = '20px';
ball4.style.top = '170px';
ball4.style.width = '20px';
ball4.style.height = '20px';
ball4.style.backgroundColor = 'red';
document.body.appendChild(ball4);
var p = 0;
var direction = 1;
setInterval(function() {
  p += direction;
  ball4.style.left = p + 'px';
  if (p >= document.body.clientWidth - 50) {
    direction = -1;
  } else if (p <= 0) {
    direction = 1;
  }
}, 44);
for (var i = 0; i < document.body.clientWidth; i += 44) {
  var ball5 = document.createElement('div');
  ball5.style.position = 'absolute';
  ball5.style.left = i + 'px';
  ball5.style.top = '20px';
  ball5.style.width = '20px';
  ball5.style.height = '40px';
  ball5.style.backgroundColor = 'red';
  document.body.appendChild(ball5);
  var p = 0;
  var direction = 1;
  setInterval(function() {
    p += direction;
    ball5.style.left = p + 'px';
    if (p >= document.body.clientWidth - 50) {
      direction = -1;
    } else if (p <= 0) {
      direction = 1;
    }
  }, 555);
}
