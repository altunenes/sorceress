document.addEventListener("DOMContentLoaded", function() {

    var dust = document.createElement('div');
    dust.id = 'dust';
    document.body.appendChild(dust);
    var slider = document.createElement('input');
    slider.type = 'range';
    slider.min = 0;
    slider.max = 300;
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
    var dust = document.getElementById('dust');
    var dots = dust.getElementsByClassName('dot');
    var animation12 = setInterval(function() {
    for (var i = 0; i < dots.length; i++) {
    dots[i].style.top = parseInt(dots[i].style.top) - 1 + '%';
    if (parseInt(dots[i].style.top) < -10) {
    dots[i].style.top = '100%';
    }
    }
    }, 10);
    
    
    document.body.appendChild(slider);
    var slider2 = document.createElement('input');
    slider2.type = 'range';
    slider2.min = 0;
    slider2.max = 30;
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
    circle1.style.width = '14px';
    circle1.style.height = '14px';
    circle1.style.backgroundColor = 'blue';
    circle1.style.borderRadius = '50%';
    circle1.style.position = 'absolute';
    circle1.style.left = '10%';
    circle1.style.top = '50%';
    document.body.appendChild(circle1);
    var circle2 = document.createElement('div');
    circle2.style.width = '32px';
    circle2.style.height = '32px';
    circle2.style.backgroundColor = 'blue';
    circle2.style.borderRadius = '50%';
    circle2.style.position = 'absolute';
    circle2.style.left = '80%';
    circle2.style.top = '50%';
    document.body.appendChild(circle2);
    
    
    var changeDirectionButton = document.createElement('button');
    changeDirectionButton.innerHTML = 'bg direction';
    changeDirectionButton.style.position = 'absolute';
    changeDirectionButton.style.left = '5%';
    changeDirectionButton.style.top = '85%';
    changeDirectionButton.style.transform = 'translate(-50%, -50%)';
    changeDirectionButton.onclick = function() {
      if (changeDirectionButton.innerHTML == 'bg direction') {
        changeDirectionButton.innerHTML = 'direction1';
        clearInterval(animation12);
        animation12 = setInterval(function() {
          for (var i = 0; i < dots.length; i++) {
            dots[i].style.top = parseInt(dots[i].style.top) - 1 + '%';
            if (parseInt(dots[i].style.top) < -10) {
              dots[i].style.top = '100%';
            }
          }
        }, 10);
      } else if (changeDirectionButton.innerHTML == 'direction1') {
        changeDirectionButton.innerHTML = 'direction2';
        clearInterval(animation12);
        animation12 = setInterval(function() {
          for (var i = 0; i < dots.length; i++) {
            dots[i].style.top = parseInt(dots[i].style.top) - 1 + '%';
            dots[i].style.left = parseInt(dots[i].style.left) - 1 + '%';
            if (parseInt(dots[i].style.top) < -10) {
              dots[i].style.top = '100%';
            }
            if (parseInt(dots[i].style.left) < -10) {
              dots[i].style.left = '100%';
            }
          }
        }, 10);
      } else {
        changeDirectionButton.innerHTML = 'bg direction';
        clearInterval(animation12);
        animation12 = setInterval(function() {
          for (var i = 0; i < dots.length; i++) {
            dots[i].style.top = parseInt(dots[i].style.top) - 1 + '%';
            if (parseInt(dots[i].style.top) < -10) {
              dots[i].style.top = '100%';
            }
          }
        }, 10);
      }
    };
    document.body.appendChild(changeDirectionButton);
    
    
    var angle = 180;
    var radius = 290;
    var centerX = window.innerWidth / 2;
    var centerY = window.innerHeight / 2;
    var circle1X = centerX + radius * Math.cos(angle);
    var circle1Y = centerY + radius * Math.sin(angle);
    var circle2X = centerX + radius * Math.cos(angle + Math.PI);
    var circle2Y = centerY + radius * Math.sin(angle + Math.PI);
    var animation = setInterval(function() {
      angle += 0.01;
      circle1X = centerX + radius * Math.cos(angle);
      circle1Y = centerY + radius * Math.sin(angle);
      circle2X = centerX + radius * Math.cos(angle + Math.PI);
      circle2Y = centerY + radius * Math.sin(angle + Math.PI);
      circle1.style.left = circle1X + 'px';
      circle1.style.top = circle1Y + 'px';
      circle2.style.left = circle2X + 'px';
      circle2.style.top = circle2Y + 'px';
      circle1.style.width = (24 + Math.sin(angle) * 15) + 'px';
      circle1.style.height = (24 + Math.sin(angle) * 15) + 'px';
      circle2.style.width = (24 - Math.sin(angle) * 15) + 'px';
      circle2.style.height = (24 - Math.sin(angle) * 15) + 'px';
    }, 10);
    
    var speedSlider = document.createElement('input');
    speedSlider.type = 'range';
    speedSlider.min = 0;
    speedSlider.max = 100;
    speedSlider.value = 50;
    speedSlider.oninput = function() {
      clearInterval(animation);
      animation = setInterval(function() {
        angle += 0.01 * speedSlider.value / 50;
        circle1X = centerX + radius * Math.cos(angle);
        circle1Y = centerY + radius * Math.sin(angle);
        circle2X = centerX + radius * Math.cos(angle + Math.PI);
        circle2Y = centerY + radius * Math.sin(angle + Math.PI);
        circle1.style.left = circle1X + 'px';
        circle1.style.top = circle1Y + 'px';
        circle2.style.left = circle2X + 'px';
        circle2.style.top = circle2Y + 'px';
        circle1.style.width = (24 + Math.sin(angle) * 15) + 'px';
        circle1.style.height = (24 + Math.sin(angle) * 15) + 'px';
        circle2.style.width = (24 - Math.sin(angle) * 15) + 'px';
        circle2.style.height = (24 - Math.sin(angle) * 15) + 'px';
      }, 10);
    };
    document.body.appendChild(speedSlider);
    
    var speedSliderText = document.createElement('div');
    speedSliderText.innerHTML = 'speed';
    speedSliderText.style.position = 'absolute';
    speedSliderText.style.left = '80%';
    speedSliderText.style.top = '4%';
    speedSliderText.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(speedSliderText);
    
    speedSlider.style.position = 'absolute';
    speedSlider.style.left = '80%';
    speedSlider.style.top = '10%';
    speedSlider.style.transform = 'translate(-50%, -50%)';
    
    document.body.style.backgroundColor = 'gray';
    
    speedSliderText.style.fontFamily = 'sans-serif';
    speedSliderText.style.fontSize = '20px';
    speedSliderText.style.color = 'white';
    
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
    
    var github = document.createElement('a');
    github.href = 'https://github.com/altunenes/';
    github.target = '_blank';
    github.style.position = 'absolute';
    github.style.right = '5%';
    github.style.bottom = '5%';
    github.style.transform = 'translate(50%, 50%)';
    github.style.width = '50px';
    github.style.height = '50px';
    github.style.backgroundImage = 'url(https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)';
    github.style.backgroundSize = 'contain';
    github.style.backgroundRepeat = 'no-repeat';
    github.style.backgroundPosition = 'center';
    document.body.appendChild(github);
    
    github.style.borderRadius = '50%';
    github.style.boxShadow = '0 0 10px rgba(0, 0, 0, 0.5)';
    
    var circle1ColorPicker = document.createElement('input');
    circle1ColorPicker.type = 'color';
    circle1ColorPicker.value = '#0000ff';
    circle1ColorPicker.oninput = function() {
      circle1.style.backgroundColor = circle1ColorPicker.value;
    };
    document.body.appendChild(circle1ColorPicker);
    var circle1ColorPickerText = document.createElement('div');
    circle1ColorPickerText.innerHTML = 'C1color';
    circle1ColorPickerText.style.position = 'absolute';
    
    
    circle1ColorPickerText.style.left = '15%';
    circle1ColorPickerText.style.top = '91%';
    circle1ColorPickerText.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(circle1ColorPickerText);
    circle1ColorPicker.style.position = 'absolute';
    circle1ColorPicker.style.left = '15%';
    circle1ColorPicker.style.top = '95%';
    circle1ColorPicker.style.transform = 'translate(-50%, -50%)';
    
    var circle2ColorPicker = document.createElement('input');
    circle2ColorPicker.type = 'color';
    circle2ColorPicker.value = '#0000ff';
    circle2ColorPicker.oninput = function() {
      circle2.style.backgroundColor = circle2ColorPicker.value;
    };
    document.body.appendChild(circle2ColorPicker);
    var circle2ColorPickerText = document.createElement('div');
    circle2ColorPickerText.innerHTML = 'C2color';
    circle2ColorPickerText.style.position = 'absolute';
    circle2ColorPickerText.style.left = '80%';
    circle2ColorPickerText.style.top = '92%';
    circle2ColorPickerText.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(circle2ColorPickerText);
    circle2ColorPicker.style.position = 'absolute';
    circle2ColorPicker.style.left = '80%';
    circle2ColorPicker.style.top = '95%';
    circle2ColorPicker.style.transform = 'translate(-50%, -50%)';
    
    var dustColorPicker = document.createElement('input');
    dustColorPicker.type = 'color';
    dustColorPicker.value = '#000000';
    dustColorPicker.oninput = function() {
      for (var i = 0; i < dots.length; i++) {
        dots[i].style.backgroundColor = dustColorPicker.value;
      }
    };
    document.body.appendChild(dustColorPicker);
    var dustColorPickerText = document.createElement('div');
    dustColorPickerText.innerHTML = 'Dust color';
    dustColorPickerText.style.position = 'absolute';
    dustColorPickerText.style.left = '95%';
    dustColorPickerText.style.top = '4%';
    dustColorPickerText.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(dustColorPickerText);
    dustColorPicker.style.position = 'absolute';
    dustColorPicker.style.left = '95%';
    dustColorPicker.style.top = '10%';
    dustColorPicker.style.transform = 'translate(-50%, -50%)';
    
    var bgColorPicker = document.createElement('input');
    bgColorPicker.type = 'color';
    bgColorPicker.value = '#808080';
    bgColorPicker.oninput = function() {
      document.body.style.backgroundColor = bgColorPicker.value;
    };
    document.body.appendChild(bgColorPicker);
    
    
    changeDirectionButton.style.fontFamily = 'sans-serif';
    changeDirectionButton.style.fontSize = '10px';
    changeDirectionButton.style.color = 'white';
    changeDirectionButton.style.backgroundColor = 'black';
    changeDirectionButton.style.border = 'none';
    changeDirectionButton.style.padding = '10px 20px';
    changeDirectionButton.style.borderRadius = '5px';
    
    circle1ColorPickerText.style.fontFamily = 'sans-serif';
    circle1ColorPickerText.style.fontSize = '10px';
    circle1ColorPickerText.style.color = 'white';
    
    
    
    circle2ColorPickerText.style.fontFamily = 'sans-serif';
    circle2ColorPickerText.style.fontSize = '10px';
    circle2ColorPickerText.style.color = 'white';
    
    dustColorPickerText.style.fontFamily = 'sans-serif';
    dustColorPickerText.style.fontSize = '10px';
    dustColorPickerText.style.color = 'white';
    
    var bgAnimationText = document.createElement('div');
    bgAnimationText.innerHTML = 'add dusts';
    bgAnimationText.style.position = 'absolute';
    bgAnimationText.style.left = '5%';
    bgAnimationText.style.top = '8%';
    bgAnimationText.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(bgAnimationText);
    bgAnimationText.style.fontFamily = 'sans-serif';
    bgAnimationText.style.fontSize = '8px';
    bgAnimationText.style.color = 'white';
    
    var dustSizeText = document.createElement('div');
    dustSizeText.innerHTML = 'dust size';
    dustSizeText.style.position = 'absolute';
    dustSizeText.style.left = '20%';
    dustSizeText.style.top = '8%';
    dustSizeText.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(dustSizeText);
    dustSizeText.style.fontFamily = 'sans-serif';
    dustSizeText.style.fontSize = '8px';
    dustSizeText.style.color = 'white';
    
    var changeCircleDirectionButton = document.createElement('button');
    changeCircleDirectionButton.innerHTML = 'circle direction';
    changeCircleDirectionButton.style.position = 'absolute';
    changeCircleDirectionButton.style.left = '92%';
    changeCircleDirectionButton.style.top = '85%';
    changeCircleDirectionButton.style.transform = 'translate(-50%, -50%)';
    changeCircleDirectionButton.onclick = function() {
      if (changeCircleDirectionButton.innerHTML == 'clockwise') {
        changeCircleDirectionButton.innerHTML = 'counterclockwise';
        clearInterval(animation);
        animation = setInterval(function() {
          angle -= 0.01 * speedSlider.value / 50;
          circle1X = centerX + radius * Math.cos(angle);
          circle1Y = centerY + radius * Math.sin(angle);
          circle2X = centerX + radius * Math.cos(angle + Math.PI);
          circle2Y = centerY + radius * Math.sin(angle + Math.PI);
          circle1.style.left = circle1X + 'px';
          circle1.style.top = circle1Y + 'px';
          circle2.style.left = circle2X + 'px';
          circle2.style.top = circle2Y + 'px';
          circle1.style.width = (14 + Math.sin(angle) * 10) + 'px';
          circle1.style.height = (14 + Math.sin(angle) * 10) + 'px';
          circle2.style.width = (32 - Math.sin(angle) * 10) + 'px';
          circle2.style.height = (32 - Math.sin(angle) * 10) + 'px';
        }, 10);
      } else {
        changeCircleDirectionButton.innerHTML = 'clockwise';
        clearInterval(animation);
        animation = setInterval(function() {
          angle += 0.01 * speedSlider.value / 50;
          circle1X = centerX + radius * Math.cos(angle);
          circle1Y = centerY + radius * Math.sin(angle);
          circle2X = centerX + radius * Math.cos(angle + Math.PI);
          circle2Y = centerY + radius * Math.sin(angle + Math.PI);
          circle1.style.left = circle1X + 'px';
          circle1.style.top = circle1Y + 'px';
          circle2.style.left = circle2X + 'px';
          circle2.style.top = circle2Y + 'px';
          circle1.style.width = (14 + Math.sin(angle) * 10) + 'px';
          circle1.style.height = (14 + Math.sin(angle) * 10) + 'px';
          circle2.style.width = (32 - Math.sin(angle) * 10) + 'px';
          circle2.style.height = (32 - Math.sin(angle) * 10) + 'px';
        }, 10);
      }
    };
    document.body.appendChild(changeCircleDirectionButton);
    changeCircleDirectionButton.style.fontFamily = 'sans-serif';
    changeCircleDirectionButton.style.fontSize = '10px';
    changeCircleDirectionButton.style.color = 'white';
    changeCircleDirectionButton.style.backgroundColor = 'black';
    changeCircleDirectionButton.style.border = 'none';
    changeCircleDirectionButton.style.padding = '10px 20px';
    changeCircleDirectionButton.style.borderRadius = '5px';
    });
