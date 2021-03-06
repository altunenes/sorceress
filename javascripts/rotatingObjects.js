/* DO NOT LOOK TOO MUCH! */

var canvas = document.createElement('canvas');
	canvas.width = window.innerWidth;
	canvas.height = window.innerHeight;
	document.body.appendChild(canvas);
	var ctx = canvas.getContext('2d');
	var centerX = canvas.width / 2;
	var centerY = canvas.height / 2;
	var radius = canvas.width / 2;
	var angle = 0;
	var lineWidth = 6;
	var lineColor = 'blue';
	var lineLength = 100;
	var lineCount = 45;
	var lineSpacing = lineLength / lineCount;
	var lineAngle = Math.PI * 2 / lineCount;
	function draw() {
	  ctx.clearRect(0, 0, canvas.width, canvas.height);
	  ctx.strokeStyle = lineColor;
	  ctx.lineWidth = lineWidth;
	  for (var i = 0; i < lineCount; i++) {
	    ctx.beginPath();
	    ctx.moveTo(centerX, centerY);
	    ctx.lineTo(centerX + Math.cos(angle + i * lineAngle) * radius, centerY + Math.sin(angle + i * lineAngle) * radius);
	    ctx.stroke();
	  }
	  angle += 0.01;
	}
	setInterval(draw, 10);
	var slider = document.createElement('input');
	slider.type = 'range';
	slider.min = 1;
	slider.max = 100;
	slider.value = lineCount;
	slider.onchange = function() {
	  lineCount = parseInt(this.value);
	  draw();
	};
	document.body.appendChild(slider);
	var colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black'];
	var colorIndex = 0;
	function changeColor() {
	  lineColor = colors[colorIndex];
	  colorIndex = (colorIndex + 1) % colors.length;
	}
	setInterval(changeColor, 1000);

var stopButton = document.createElement('button');
stopButton.innerHTML = 'Stop';
document.body.appendChild(stopButton);
stopButton.onclick = function() {
  clearInterval(draw);
};

stopButton.onclick = function() {
  while (document.body.firstChild) {
    document.body.removeChild(document.body.firstChild);
  }
  var img = document.createElement('img');
  img.src = 'https://raw.githubusercontent.com/altunenes/sorceress/main/assets/addd.png';
img.style.position = 'absolute';
img.style.left = '50%';
img.style.top = '50%';
img.style.transform = 'translate(-50%, -50%)';
  document.body.appendChild(img);
};

document.body.style.backgroundColor = 'White';

var colorPicker = document.createElement('input');
colorPicker.type = 'color';
document.body.appendChild(colorPicker);
colorPicker.onchange = function() {
  document.body.style.backgroundColor = this.value;
};

var rect = document.createElement('div');
rect.style.position = 'absolute';
rect.style.left = '51%';
rect.style.top = '53%';
rect.style.width = '10px';
rect.style.height = '10px';
rect.style.backgroundColor = 'red';
document.body.appendChild(rect);

rect.onclick = function() {
  stopButton.click();
};
