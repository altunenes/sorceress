  var rectangles = [];
  var speed2 = 1;


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
    redRectangle.style.width = '40px';
    redRectangle.style.height = '40px';
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
    blackLine.style.width = '23px';
    blackLine.style.height = window.innerHeight + 'px';
    blackLine.style.backgroundColor = 'black';
    blackLine.style.position = 'absolute';
    blackLine.style.left = i + 'px';
    blackLine.style.top = '0px';
    document.body.appendChild(blackLine);
    lines.push(blackLine);
  }

  setInterval(moveLines, 10);




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

  var slider3 = document.createElement('input');
  slider3.type = 'range';
  slider3.min = '0';
  slider3.max = '360';
  slider3.value = '0';
  slider3.style.position = 'absolute';
  slider3.style.top = '1%';
  slider3.style.right = '55%';
  slider3.style.transform = 'translate(-50%, -50%)';
  document.body.appendChild(slider3);
  slider3.addEventListener('change', function() {
    document.body.style.transform = 'rotate(' + slider3.value + 'deg)';
  });
  var slider2 = document.createElement('input');
  slider2.type = 'range';
  slider2.min = 1;
  slider2.max = 10;
  slider2.value = 0;
  slider2.style.position = 'absolute';
  slider2.style.top = '1%';
  slider2.style.right = '44%';
  slider2.style.transform = 'translate(-50%, -50%)';

  slider2.oninput = function() {
    speed2 = slider2.value;
  };
  document.body.appendChild(slider2);

var colorPicker = document.createElement('input');
colorPicker.type = 'color';
colorPicker.style.position = 'absolute';
colorPicker.style.top = '1%';
colorPicker.style.right = '35%';
colorPicker.style.transform = 'translate(-50%, -50%)';
document.body.appendChild(colorPicker);
colorPicker.addEventListener('change', function() {
  for (var i = 0; i < lines.length; i++) {
    lines[i].style.backgroundColor = colorPicker.value;
  }
});
var colorPicker2 = document.createElement('input');
colorPicker2.type = 'color';
colorPicker2.style.position = 'absolute';
colorPicker2.style.top = '1%';
colorPicker2.style.right = '25%';
colorPicker2.style.transform = 'translate(-50%, -50%)';
document.body.appendChild(colorPicker2);
colorPicker2.addEventListener('change', function() {
  for (var i = 0; i < rectangles.length; i++) {
    rectangles[i].style.backgroundColor = colorPicker2.value;
  }
});
