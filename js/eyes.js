document.addEventListener("DOMContentLoaded", function() {
    
    var img = document.createElement('img');


    img.src = 'https://raw.githubusercontent.com/altunenes/MathArt/main/avarage.jpg';
    
    
    
    img.style.width = '300px';
    img.style.height = '300px';
    img.style.position = 'absolute';
    img.style.left = '30%';
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
    button.style.top = '95%';
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
    input.style.left = '10%';
    input.style.top = '85%';
    input.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(input);
    
    input.addEventListener('change', function() {
      img.src = URL.createObjectURL(this.files[0]);
    });
    
    
    /*/var point = document.createElement('div');
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
    /*/
    
    
    
    
    /*/var text = document.createElement('div');
    text.innerHTML = 'restart the animation';
    text.style.fontWeight = 'bold';
    text.style.position = 'absolute';
    text.style.left = '10%';
    text.style.top = '5%';
    text.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(text);
    /*/
    
    /*/var text = document.createElement('div');
    text.innerHTML = 'upload an img';
    text.style.position = 'absolute';
    text.style.left = '85%';
    text.style.top = '5%';
    text.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(text);
    /*/
    
    var slider = document.createElement('input');
    slider.type = 'range';
    slider.min = '1';
    slider.max = '10';
    slider.value = '1';
    slider.style.position = 'absolute';
    slider.style.left = '5%';
    slider.style.top = '2%';
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
    colorpicker.style.left = '30%';
    colorpicker.style.top = '90%';
    colorpicker.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(colorpicker);
    colorpicker.addEventListener('input', function() {
      lineColor = this.value;
      for (var i = 0; i < lineCount; i++) {
        lines[i].style.backgroundColor = lineColor;
      }
    });
    var blurButton = document.createElement('button');
    blurButton.innerHTML = 'Blur';
    blurButton.style.position = 'absolute';
    blurButton.style.left = '3%';
    blurButton.style.top = '95%';
    blurButton.style.transform = 'translate(-50%, -50%)';
    blurButton.onclick = function() {
      if (blurButton.innerHTML == 'Blur') {
        blurButton.innerHTML = 'Blur more';
        document.body.style.filter = 'blur(5px)';
      } else if (blurButton.innerHTML == 'Blur more') {
        blurButton.innerHTML = 'Blur less';
        document.body.style.filter = 'blur(10px)';
      } else {
        blurButton.innerHTML = 'Blur';
        document.body.style.filter = 'blur(0px)';
      }
    };
    document.body.appendChild(blurButton);
    
    blurButton.style.fontFamily = 'sans-serif';
    blurButton.style.fontSize = '20px';
    blurButton.style.color = 'white';
    blurButton.style.backgroundColor = 'black';
    blurButton.style.border = 'none';
    blurButton.style.padding = '10px 20px';
    blurButton.style.borderRadius = '5px';

    /*/add stlye to other buttons restart, upload and speed/*/

    var restartButton = document.createElement('button');
    restartButton.innerHTML = 'Restart';
    restartButton.style.position = 'absolute';
    restartButton.style.left = '10%';
    restartButton.style.top = '95%';
    restartButton.style.transform = 'translate(-50%, -50%)';
    restartButton.onclick = function() {
      location.reload();
    }
    document.body.appendChild(restartButton);

    restartButton.style.fontFamily = 'sans-serif';
    restartButton.style.fontSize = '20px';
    restartButton.style.color = 'white';
    restartButton.style.backgroundColor = 'black';
    restartButton.style.border = 'none';
    restartButton.style.padding = '10px 20px';
    restartButton.style.borderRadius = '5px';



    var speedButton = document.createElement('button');
    speedButton.innerHTML = 'Speed: 0.1';
    speedButton.style.position = 'absolute';
    speedButton.style.left = '20%';
    speedButton.style.top = '95%';
    speedButton.style.transform = 'translate(-50%, -50%)';
    speedButton.onclick = function() {
      if (lineMove == 0.1) {
        lineMove = 0.2;
        speedButton.innerHTML = 'Speed: 0.2';
      } else if (lineMove == 0.2) {
        lineMove = 0.3;
        speedButton.innerHTML = 'Speed: 0.3';
      } else if (lineMove == 0.3) {
        lineMove = 0.4;
        speedButton.innerHTML = 'Speed: 0.4';
      } else {
        lineMove = 0.1;
        speedButton.innerHTML = 'Speed: 0.1';
      }
    }
    document.body.appendChild(speedButton);

    speedButton.style.fontFamily = 'sans-serif';
    speedButton.style.fontSize = '20px';
    speedButton.style.color = 'white';
    speedButton.style.backgroundColor = 'black';
    speedButton.style.border = 'none';
    speedButton.style.padding = '10px 20px';
    speedButton.style.borderRadius = '5px';


    
      
       
});