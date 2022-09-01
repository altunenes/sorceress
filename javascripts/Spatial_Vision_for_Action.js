var dust = document.createElement('div');
dust.id = 'dust';
document.body.appendChild(dust);
var slider = document.createElement('input');
slider.type = 'range';
slider.min = 0;
slider.max = 1000;
slider.value = 300;
slider.oninput = function() {
  dust.innerHTML = '';
  for (var i = 0; i < slider.value; i++) {
    var dot = document.createElement('div');
    dot.className = 'dot';
    dot.style.left = Math.random() * 100 + '%';
    dot.style.top = Math.random() * 100 + '%';
    dot.style.width = slider2.value + 'px';
    dot.style.height = slider2.value + 'px';
    dot.style.backgroundColor = 'black';
    dot.style.borderRadius = '50%';
    dot.style.position = 'absolute';
    dust.appendChild(dot);
  }
};
document.body.appendChild(slider);
var slider2 = document.createElement('input');
slider2.type = 'range';
slider2.min = 0;
slider2.max = 100;
slider2.value = 10;
slider2.oninput = function() {
  dust.innerHTML = '';
  for (var i = 0; i < slider.value; i++) {
    var dot = document.createElement('div');
    dot.className = 'dot';
    dot.style.left = Math.random() * 100 + '%';
    dot.style.top = Math.random() * 100 + '%';
    dot.style.width = slider2.value + 'px';
    dot.style.height = slider2.value + 'px';
    dot.style.backgroundColor = 'black';
    dot.style.borderRadius = '50%';
    dot.style.position = 'absolute';
    dust.appendChild(dot);
  }
};
document.body.appendChild(slider2);

document.body.style.overflow = 'hidden';

var line = document.createElement('div');
line.style.width = '1px';
line.style.height = '100%';
line.style.backgroundColor = 'red';
line.style.position = 'absolute';
line.style.left = '50%';
document.body.appendChild(line);

var circle1 = document.createElement('div');
circle1.style.width = '10px';
circle1.style.height = '10px';
circle1.style.backgroundColor = 'blue';
circle1.style.borderRadius = '50%';
circle1.style.position = 'absolute';
circle1.style.left = '10%';
circle1.style.top = '50%';
document.body.appendChild(circle1);
var circle2 = document.createElement('div');
circle2.style.width = '10px';
circle2.style.height = '10px';
circle2.style.backgroundColor = 'blue';
circle2.style.borderRadius = '50%';
circle2.style.position = 'absolute';
circle2.style.left = '80%';
circle2.style.top = '50%';
document.body.appendChild(circle2);

var slider3 = document.createElement('input');
slider3.type = 'range';
slider3.min = 0;
slider3.max = 10;
slider3.value = 10;
slider3.oninput = function() {
  var angle = 0;
  var angle2 = 500;
  var radius = 200;
  var radius2 = 200;
  var centerX = window.innerWidth / 2;
  var centerY = window.innerHeight / 2;
  var centerX2 = window.innerWidth / 2;
  var centerY2 = window.innerHeight / 2;
  var speed = slider3.value;
  var speed2 = slider3.value;
  var x = centerX + Math.cos(angle) * radius;
  var y = centerY + Math.sin(angle) * radius;
  var x2 = centerX2 + Math.cos(angle2) * radius2;
  var y2 = centerY2 + Math.sin(angle2) * radius2;
  var animate = function() {
    angle += speed / 100;
    angle2 += speed2 / 100;
    x = centerX + Math.cos(angle) * radius;
    y = centerY + Math.sin(angle) * radius;
    x2 = centerX2 + Math.cos(angle2) * radius2;
    y2 = centerY2 + Math.sin(angle2) * radius2;
    circle1.style.left = x+ 'px';
    circle1.style.top = y+ 'px';
    circle2.style.left = x2+ 'px';
    circle2.style.top = y2+ 'px';
    requestAnimationFrame(animate);
  };
  animate();
};
document.body.appendChild(slider3);

var dust = document.getElementById('dust');
var dots = dust.getElementsByClassName('dot');
var animation = setInterval(function() {
  for (var i = 0; i < dots.length; i++) {
    dots[i].style.top = parseInt(dots[i].style.top) - 1 + '%';
    if (parseInt(dots[i].style.top) < -10) {
      dots[i].style.top = '100%';
    }
  }
}, 10);
var slider5 = document.createElement('input');
slider5.type = 'range';
slider5.min = 0;
slider5.max = 400;
slider5.value = 66;
slider5.oninput = function() {
  clearInterval(animation5);
  animation5 = setInterval(function() {
    for (var i = 0; i < dots.length; i++) {
      dots[i].style.top = parseInt(dots[i].style.top) - 1 + '%';
      if (parseInt(dots[i].style.top) < -10) {
        dots[i].style.top = '100%';
      }
    }
  }, slider5.value);
};
document.body.appendChild(slider5);

var slider4 = document.createElement('input');
slider4.type = 'range';
slider4.min = 0;
slider4.max = 100;
slider4.value = 10;
slider4.oninput = function() {
  var angle = 0;
  var angle2 = 500;
  var radius = 200;
  var radius2 = 200;
  var centerX = window.innerWidth / 2;
  var centerY = window.innerHeight / 2;
  var centerX2 = window.innerWidth / 2;
  var centerY2 = window.innerHeight / 2;
  var speed = slider3.value;
  var speed2 = slider3.value;
  var x = centerX + Math.cos(angle) * radius;
  var y = centerY + Math.sin(angle) * radius;
  var x2 = centerX2 + Math.cos(angle2) * radius2;
  var y2 = centerY2 + Math.sin(angle2) * radius2;
  var animate = function() {
    angle += speed / 100;
    angle2 += speed2 / 100;
    x = centerX + Math.cos(angle) * radius;
    y = centerY + Math.sin(angle) * radius;
    x2 = centerX2 + Math.cos(angle2) * radius2;
    y2 = centerY2 + Math.sin(angle2) * radius2;
    circle1.style.left = x+ 'px';
    circle1.style.top = y+ 'px';
    circle2.style.left = x2+ 'px';
    circle2.style.top = y2+ 'px';
    circle1.style.width = Math.abs(Math.sin(angle)) * slider4.value + 'px';
    circle1.style.height = Math.abs(Math.sin(angle)) * slider4.value + 'px';
    circle2.style.width = Math.abs(Math.sin(angle2)) * slider4.value + 'px';
    circle2.style.height = Math.abs(Math.sin(angle2)) * slider4.value + 'px';
    requestAnimationFrame(animate);
  };
  animate();
};

document.body.appendChild(slider4);

document.body.style.backgroundColor = 'gray';
