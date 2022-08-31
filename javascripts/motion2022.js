/*it's not finished yet, feel free to contribute */

var dust = document.createElement('div');
dust.id = 'dust';
document.body.appendChild(dust);
var slider = document.createElement('input');
slider.type = 'range';
slider.min = 0;
slider.max = 1000;
slider.value = 100;
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
slider5.max = 100;
slider5.value = 10;
slider5.oninput = function() {
  clearInterval(animation);
  animation = setInterval(function() {
    for (var i = 0; i < dots.length; i++) {
      dots[i].style.top = parseInt(dots[i].style.top) - 1 + '%';
      if (parseInt(dots[i].style.top) < -10) {
        dots[i].style.top = '100%';
      }
    }
  }, slider5.value);
};
document.body.appendChild(slider5);

var circle1 = document.createElement('div');
circle1.className = 'circle';
circle1.style.width = '100px';
circle1.style.height = '100px';
circle1.style.backgroundColor = 'black';
circle1.style.borderRadius = '50%';
circle1.style.position = 'absolute';
circle1.style.left = '50%';
circle1.style.top = '50%';
circle1.style.marginLeft = '-50px';
circle1.style.marginTop = '-50px';
document.body.appendChild(circle1);
var circle2 = document.createElement('div');
circle2.className = 'circle';
circle2.style.width = '100px';
circle2.style.height = '100px';
circle2.style.backgroundColor = 'black';
circle2.style.borderRadius = '50%';
circle2.style.position = 'absolute';
circle2.style.left = '50%';
circle2.style.top = '50%';
circle2.style.marginLeft = '-50px';
circle2.style.marginTop = '-50px';
document.body.appendChild(circle2);
var angle = 0;
var animation2 = setInterval(function() {
  angle += 0.1;
  circle1.style.left = 50 + Math.sin(angle) * 50 + '%';
  circle1.style.top = 50 + Math.cos(angle) * 50 + '%';
  circle2.style.left = 50 + Math.sin(angle + Math.PI) * 50 + '%';
  circle2.style.top = 50 + Math.cos(angle + Math.PI) * 50 + '%';
}, 50);

var animation3 = setInterval(function() {
  circle1.style.width = 100 + Math.sin(angle) * 50 + 'px';
  circle1.style.height = 100 + Math.sin(angle) * 50 + 'px';
  circle1.style.marginLeft = -50 - Math.sin(angle) * 50 + 'px';
  circle1.style.marginTop = -50 - Math.sin(angle) * 50 + 'px';
  circle2.style.width = 100 + Math.sin(angle) * 50 + 'px';
  circle2.style.height = 100 + Math.sin(angle) * 50 + 'px';
  circle2.style.marginLeft = -50 - Math.sin(angle) * 50 + 'px';
  circle2.style.marginTop = -50 - Math.sin(angle) * 50 + 'px';
}, 10);

document.body.style.backgroundColor = 'gray';
