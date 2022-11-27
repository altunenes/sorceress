document.addEventListener("DOMContentLoaded", function() {

    var canvas = document.createElement('canvas');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    document.body.appendChild(canvas);
    var ctx = canvas.getContext('2d');
    var stripes = [];
    var stripeWidth = 4;
    var stripeHeight = canvas.height;
    var stripeCount = canvas.width / stripeWidth;
    for (var i = 0; i < stripeCount; i++) {
      stripes.push(Math.random() < 0.5 ? '#000' : '#fff');
    }
    var lineWidth = 14;
    var lineHeight = canvas.height;
    var lineX = canvas.width / 2;
    var lineY = canvas.height / 2;
    var lineAngle = 0;
    var lineSpeed = 0.01;
    var lineColor = '#888';
    var line = {
      x: lineX,
      y: lineY,
      width: lineWidth,
      height: lineHeight,
      angle: lineAngle,
      speed: lineSpeed,
      color: lineColor
    };
    function draw() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (var i = 0; i < stripeCount; i++) {
        ctx.fillStyle = stripes[i];
        ctx.fillRect(i * stripeWidth, 0, stripeWidth, stripeHeight);
      }
      ctx.save();
      ctx.translate(line.x, line.y);
      ctx.rotate(line.angle);
      ctx.fillStyle = line.color;
      ctx.fillRect(-line.width / 2, -line.height / 2, line.width, line.height);
      ctx.restore();
      line.angle += line.speed;
      requestAnimationFrame(draw);
    }
    draw();
    
    var slider = document.createElement('input');
    slider.type = 'range';
    slider.min = 0;
    slider.max = canvas.height;
    slider.value = line.height;
    slider.oninput = function() {
      line.height = slider.value;
    };
    document.body.appendChild(slider);
    
    var removeBg = document.createElement('button');
    removeBg.innerHTML = 'remove bg';
    removeBg.onclick = function() {
      stripes = [];
    };
    document.body.appendChild(removeBg);
    
    removeBg.onclick = function() {
      if (stripes.length === 0) {
        for (var i = 0; i < stripeCount; i++) {
          stripes.push(Math.random() < 0.5 ? '#000' : '#fff');
        }
        removeBg.innerHTML = 'remove bg';
      } else {
        stripes = [];
        removeBg.innerHTML = 'show bg';
      }
    };
    
    var speedUp = document.createElement('button');
    speedUp.innerHTML = '+';
    speedUp.onclick = function() {
      line.speed *= 1.1;
    };
    document.body.appendChild(speedUp);
    var speedDown = document.createElement('button');
    speedDown.innerHTML = '-';
    speedDown.onclick = function() {
      line.speed /= 1.1;
    };
    document.body.appendChild(speedDown);
    
    speedUp.style.fontSize = '20px';
    speedDown.style.fontSize = '20px';
    
    removeBg.style.fontSize = '20px';
    
    speedUp.style.backgroundColor = '#f00';
    speedDown.style.backgroundColor = '#f00';
    removeBg.style.backgroundColor = '#f00';
    
    speedUp.style.position = 'absolute';
    speedUp.style.top = '0';
    speedUp.style.left= '0';
    speedDown.style.position = 'absolute';
    speedDown.style.top = '0';
    speedDown.style.left= '30px';
    removeBg.style.position = 'absolute';
    removeBg.style.top = '0';
    removeBg.style.left= '60px';
    
    slider.style.position = 'absolute';
    slider.style.top = '0';
    slider.style.left= '30%';
    
    var colorPicker = document.createElement('input');
    colorPicker.type = 'color';
    colorPicker.value = line.color;
    colorPicker.oninput = function() {
      line.color = colorPicker.value;
    };
    document.body.appendChild(colorPicker);
    
    var menuBar = document.createElement('div');
    menuBar.style.position = 'absolute';
    menuBar.style.top = '0';
    menuBar.style.left = '0';
    menuBar.style.width = '100%';
    menuBar.style.height = '30px';
    menuBar.style.backgroundColor = '#eee';
    menuBar.appendChild(speedUp);
    menuBar.appendChild(speedDown);
    menuBar.appendChild(removeBg);
    menuBar.appendChild(slider);
    menuBar.appendChild(colorPicker);
    document.body.appendChild(menuBar);
    
    colorPicker.style.position = 'absolute';
    colorPicker.style.top = '0';
    colorPicker.style.left= '200px';
    var circle = document.createElement('div');
    circle.style.position = 'absolute';
    circle.style.top = '50%';
    circle.style.left = '50%';
    circle.style.width = '10px';
    circle.style.height = '10px';
    circle.style.borderRadius = '50%';
    circle.style.backgroundColor = '#f00';
    document.body.appendChild(circle);
    document.body.style.overflow = 'hidden';
    
    var github = document.createElement('a');
github.href = 'https://github.com/altunenes';
github.innerHTML = '<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30" height="30">';
github.style.position = 'absolute';
github.style.top = '0';
github.style.right = '0';
document.body.appendChild(github);
/* animation of the bg stripes uncomment to see. It doesnt effect the illusion at least on my screen.
var stripeChangeSpeed = 0.1;
function changeStripes() {
  for (var i = 0; i < stripeCount; i++) {
    if (Math.random() < stripeChangeSpeed) {
      stripes[i] = Math.random() < 0.5 ? '#000' : '#fff';
    }
  }
  requestAnimationFrame(changeStripes);
}
changeStripes();
var animateBg = document.createElement('button');
animateBg.innerHTML = 'animate bg';
animateBg.onclick = function() {
  if (stripeChangeSpeed > 0) {
    stripeChangeSpeed = 0;
    animateBg.innerHTML = 'animate bg';
  } else {
    stripeChangeSpeed = 0.1;
    animateBg.innerHTML = 'stop bg';
  }
};
document.body.appendChild(animateBg);
*/
    });
    