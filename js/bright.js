document.addEventListener("DOMContentLoaded", function() {
    document.body.style.overflow = 'hidden';
    var canvas = document.createElement('canvas');
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
    document.body.appendChild(canvas);
    var ctx = canvas.getContext('2d');
    var x = canvas.width / 2;
    var y = canvas.height / 2;
    var radius = 150;
    var angle = 24;
    var speed = 25;
    var lineWidth = 1;
    var lineLength = 1;
    var startColor = [255, 255, 0]; // Yellow
    var lineColor = "rgb(" + startColor[0] + "," + startColor[1] + "," + startColor[2] + ")";
    var endColor = [0, 0, 0]; // Black
    // Set the duration of the color transition (in milliseconds)
    var duration = 2000; // 5 seconds
    // Set the interval for updating the color (in milliseconds)
    var interval = 100// 50 milliseconds
    // Calculate the number of intervals
    var steps = duration / interval;
    // Calculate the change in color at each interval
    var colorDelta = [(endColor[0] - startColor[0]) / steps,
                      (endColor[1] - startColor[1]) / steps,
                      (endColor[2] - startColor[2]) / steps];
    // Set the initial color to the starting color
    var currentColor = startColor;
    // Start the color transition
    var timer = setInterval(function() {
      // Update the current color
      currentColor = [currentColor[0] + colorDelta[0],
                      currentColor[1] + colorDelta[1],
                      currentColor[2] + colorDelta[2]];
      // Convert the color values to a CSS color string
      var colorString = "rgb(" + Math.round(currentColor[0]) + "," +
                                Math.round(currentColor[1]) + "," +
                                Math.round(currentColor[2]) + ")";
      // Update the line color
      lineColor = colorString;
    }, interval);
    function draw() {
      ctx.beginPath();
      ctx.arc(x, y, radius, 0, 2* Math.PI);
      ctx.strokeStyle = lineColor;
      ctx.lineWidth = lineWidth;
      ctx.stroke();
      ctx.closePath();
      radius += lineLength;
      angle += speed;
      lineWidth += 0.1;
      lineLength += 0.1;
      requestAnimationFrame(draw);
    }
    draw();
   
    var startColorPicker = document.createElement('input');
    startColorPicker.type = 'color';
    startColorPicker.value = '#ffff00';
    startColorPicker.addEventListener('change', function() {
      startColor = [parseInt(startColorPicker.value.substr(1, 2), 16),
                    parseInt(startColorPicker.value.substr(3, 2), 16),
                    parseInt(startColorPicker.value.substr(5, 2), 16)];
      lineColor = "rgb(" + startColor[0] + "," + startColor[1] + "," + startColor[2] + ")";
    });
    startColorPicker.style.position = 'absolute';
    startColorPicker.style.top = '0px';
    startColorPicker.style.left = '0px';
    document.body.appendChild(startColorPicker);
    var endColorPicker = document.createElement('input');
    endColorPicker.type = 'color';
    endColorPicker.value = '#000000';
    endColorPicker.addEventListener('change', function() {
      endColor = [parseInt(endColorPicker.value.substr(1, 2), 16),
                  parseInt(endColorPicker.value.substr(3, 2), 16),
                  parseInt(endColorPicker.value.substr(5, 2), 16)];
      colorDelta = [(endColor[0] - startColor[0]) / steps,
                    (endColor[1] - startColor[1]) / steps,
                    (endColor[2] - startColor[2]) / steps];
    });
    endColorPicker.style.position = 'absolute';
    endColorPicker.style.top = '0px';
    endColorPicker.style.left = '50px';
    document.body.appendChild(endColorPicker);
    var restartButton = document.createElement('button');
    restartButton.innerHTML = 'Restart';
    restartButton.addEventListener('click', function() {
      radius = 150;
      angle = 24;
      speed = 25;
      lineWidth = 1;
      lineLength = 1;
      currentColor = startColor;
      lineColor = "rgb(" + startColor[0] + "," + startColor[1] + "," + startColor[2] + ")";
    });
    restartButton.style.position = 'absolute';
    restartButton.style.top = '0px';
    restartButton.style.left = '100px';
    document.body.appendChild(restartButton);
    var clearButton = document.createElement('button');
    clearButton.innerHTML = 'Clear';
    clearButton.addEventListener('click', function() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
    });
    clearButton.style.position = 'absolute';
    clearButton.style.top = '0px';
    clearButton.style.left = '150px';
    document.body.appendChild(clearButton);
});
