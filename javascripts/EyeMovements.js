var img = document.createElement('img');
	

	

	img.src = 'https://raw.githubusercontent.com/altunenes/MathArt/main/avarage.jpg';
	

	

	

	img.style.width = '300px';
	img.style.height = '300px';
	img.style.position = 'absolute';
	img.style.left = '20%';
	img.style.top = '40%';
	img.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(img);
	

	

	

	for (var i = 0; i < 18; i++) {
	  var line = document.createElement('div');
	  line.style.width = '6px';
	  line.style.height = '340px';
	  line.style.backgroundColor = 'black';
	  line.style.position = 'absolute';
	  line.style.left = '300px';
	  line.style.top = '80px';
	  line.style.transform = 'translate(' + (i * 10) + 'px, 0px)';
	  document.body.appendChild(line);
	}
	

	

	var lines = document.querySelectorAll('div');
	var lineWidth = lines[0].offsetWidth;
	var lineHeight = lines[0].offsetHeight;
	var lineCount = lines.length;
	var lineMove = 0.1;
	var lineMoveCount = 0;
	var lineMoveInterval = setInterval(function() {
	  for (var i = 0; i < lineCount; i++) {
	    lines[i].style.left = (lineMoveCount + i * lineMove) + 'px';
	  }
	  lineMoveCount += lineMove;
	  if (lineMoveCount > document.body.offsetWidth) {
	    clearInterval(lineMoveInterval);
	  }
	}, 10);
	

	var button = document.createElement('button');
	button.innerHTML = 'Restart';
	button.style.position = 'absolute';
	button.style.left = '10%';
	button.style.top = '10%';
	button.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(button);
	

	button.addEventListener('click', function() {
	  clearInterval(lineMoveInterval);
	  lineMoveCount = 0;
	  lineMoveInterval = setInterval(function() {
	    for (var i = 0; i < lineCount; i++) {
	      lines[i].style.left = (lineMoveCount + i * lineMove) + 'px';
	    }
	    lineMoveCount += lineMove;
	    if (lineMoveCount > document.body.offsetWidth) {
	      clearInterval(lineMoveInterval);
	    }
	  }, 10);
	});
	

	var input = document.createElement('input');
	input.type = 'file';
	input.style.position = 'absolute';
	input.style.left = '92%';
	input.style.top = '10%';
	input.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(input);
	

	input.addEventListener('change', function() {
	  img.src = URL.createObjectURL(this.files[0]);
	});
	

	

	var point = document.createElement('div');
	point.style.width = '10px';
	point.style.height = '10px';
	point.style.backgroundColor = 'red';
	point.style.position = 'absolute';
	point.style.left = '20%';
	point.style.top = '40%';
	point.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(point);
	

	var text = document.createElement('div');
	text.innerHTML = 'Look at the red dot or an eye';
	text.style.position = 'absolute';
	text.style.left = '20%';
	text.style.top = '10%';
	text.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(text);
	

	

	

	

	var text = document.createElement('div');
	text.innerHTML = 'restart the animation';
	text.style.fontWeight = 'bold';
	text.style.position = 'absolute';
	text.style.left = '10%';
	text.style.top = '5%';
	text.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(text);
	

	

	var text = document.createElement('div');
	text.innerHTML = 'upload an img';
	text.style.position = 'absolute';
	text.style.left = '85%';
	text.style.top = '5%';
	text.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(text);
	

	var text = document.createElement('div');
	text.innerHTML = 'thickness';
	text.style.position = 'absolute';
	text.style.left = '38%';
	text.style.top = '7%';
	text.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(text);
	

	

	var text = document.createElement('div');
	text.innerHTML = 'line colors';
	text.style.position = 'absolute';
	text.style.left = '60%';
	text.style.top = '5%';
	text.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(text);
	

	

	

	var text = document.createElement('div');
	text.innerHTML = 'Blur (recommended) ';
	text.style.position = 'absolute';
	text.style.fontWeight = 'bold';
	text.style.left = '75%';
	text.style.top = '7%';
	text.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(text);
	

	

	var button = document.createElement('button');
	button.innerHTML = 'Speed: 0.1';
	button.style.position = 'absolute';
	button.style.left = '50%';
	button.style.top = '10%';
	button.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(button);
	button.addEventListener('click', function() {
	  if (lineMove == 0.1) {
	    lineMove = 0.2;
	    button.innerHTML = 'Speed: 0.2';
	  } else if (lineMove == 0.2) {
	    lineMove = 0.3;
	    button.innerHTML = 'Speed: 0.3';
	  } else if (lineMove == 0.3) {
	    lineMove = 0.4;
	    button.innerHTML = 'Speed: 0.4';
	  } else {
	    lineMove = 0.1;
	    button.innerHTML = 'Speed: 0.1';
	  }
	});
	

	

	

	var slider = document.createElement('input');
	slider.type = 'range';
	slider.min = '1';
	slider.max = '10';
	slider.value = '1';
	slider.style.position = 'absolute';
	slider.style.left = '40%';
	slider.style.top = '10%';
	slider.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(slider);
	slider.addEventListener('input', function() {
	  lineWidth = this.value;
	  for (var i = 0; i < lineCount; i++) {
	    lines[i].style.width = lineWidth + 'px';
	  }
	});
	var colorpicker = document.createElement('input');
	colorpicker.type = 'color';
	colorpicker.style.position = 'absolute';
	colorpicker.style.left = '60%';
	colorpicker.style.top = '10%';
	colorpicker.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(colorpicker);
	colorpicker.addEventListener('input', function() {
	  lineColor = this.value;
	  for (var i = 0; i < lineCount; i++) {
	    lines[i].style.backgroundColor = lineColor;
	  }
	});
	var slider4 = document.createElement('input');
	slider4.type = 'range';
	slider4.min = '0';
	slider4.max = '25';
	slider4.value = '0';
	slider4.style.position = 'absolute';
	slider4.style.top = '10%';
	slider4.style.right = '15%';
	slider4.style.transform = 'translate(-50%, -50%)';
	document.body.appendChild(slider4);
	slider4.addEventListener('change', function() {
	  document.body.style.filter = 'blur(' + slider4.value + 'px)';

});

var button = document.querySelectorAll('button');
var text = document.querySelectorAll('div');
var input = document.querySelectorAll('input');
for (var i = 0; i < button.length; i++) {
  button[i].style.backgroundColor = '#4CAF50';
  button[i].style.border = 'none';
  button[i].style.color = 'white';
  button[i].style.padding = '15px 28px';
  button[i].style.textAlign = 'center';
  button[i].style.textDecoration = 'none';
  button[i].style.display = 'inline-block';
  button[i].style.fontSize = '16px';
  button[i].style.margin = '1px 2px';
  button[i].style.cursor = 'pointer';
}
for (var i = 0; i < text.length; i++) {
  text[i].style.fontFamily = 'Arial';
  text[i].style.fontSize = '10px';
  text[i].style.color = 'black';
}
for (var i = 0; i < input.length; i++) {
  input[i].style.fontFamily = 'Arial';
  input[i].style.fontSize = '10px';
  input[i].style.color = 'black';
}
