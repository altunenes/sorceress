document.addEventListener("DOMContentLoaded", function() {
    
    var plus = document.createElement('div');
    plus.innerHTML = '+';
    plus.style.color = 'red';
    plus.style.fontSize = '40px';
    plus.style.position = 'absolute';
    plus.style.top = '50%';
    plus.style.left = '50%';
    plus.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(plus);
    
    var circles = [];
    var radius = 140;
    var center = {x: window.innerWidth / 2, y: window.innerHeight/2};
    var angle = 0;
    var step = Math.PI / 9;
    for (var i = 0; i < 18; i++) {
      var circle = document.createElement('div');
      circle.style.backgroundColor = 'purple';
      circle.style.borderRadius = '70%';
      circle.style.position = 'absolute';
      circle.style.top = center.y + radius * Math.sin(angle) + 'px';
      circle.style.left = center.x + radius * Math.cos(angle) + 'px';
      circle.style.transform = 'translate(-50%, -50%)';
      circle.style.width = circle.style.height = '20px';
      circle.style.transition = 'transform 1s';
      document.body.appendChild(circle);
      circles.push(circle);
      angle += step;
    }
    
    document.body.style.backgroundColor = 'gray';
    
    var colorPicker = document.createElement('input');
    colorPicker.type = 'color';
    colorPicker.style.position = 'absolute';
    colorPicker.style.top = '5%';
    colorPicker.style.left = '5%';
    colorPicker.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(colorPicker);
    colorPicker.addEventListener('change', function() {
      document.body.style.backgroundColor = colorPicker.value;
    });
    
    var colorPicker2 = document.createElement('input');
    colorPicker2.type = 'color';
    colorPicker2.style.position = 'absolute';
    colorPicker2.style.top = '5%';
    colorPicker2.style.right = '5%';
    colorPicker2.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(colorPicker2);
    colorPicker2.addEventListener('change', function() {
      for (var i = 0; i < circles.length; i++) {
        circles[i].style.backgroundColor = colorPicker2.value;
      }
    });
    
    var i = 1;
    var interval = setInterval(function() {
      circles[i].style.backgroundColor = colorPicker2.value;
      i = (i + 1) % circles.length;
    circles[i].style.backgroundColor = document.body.style.backgroundColor;
    
    
    }, 45);
    
    var sentence = document.createElement('div');
    sentence.innerHTML = 'circle color';
    sentence.style.position = 'absolute';
    sentence.style.top = '15%';
    sentence.style.right = '2%';
    sentence.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(sentence);
    
    var sentence2 = document.createElement('div');
    sentence2.innerHTML = 'bg color';
    sentence2.style.position = 'absolute';
    sentence2.style.top = '15%';
    sentence2.style.left = '5%';
    sentence2.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(sentence2);
    
    var slider = document.createElement('input');
    slider.type = 'range';
    slider.min = '1';
    slider.max = '400';
    slider.value = '45';
    slider.style.position = 'absolute';
    slider.style.top = '5%';
    slider.style.left = '25%';
    slider.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(slider);
    slider.addEventListener('change', function() {
      clearInterval(interval);
      interval = setInterval(function() {
        circles[i].style.backgroundColor = colorPicker2.value;
        i = (i + 1) % circles.length;
        circles[i].style.backgroundColor = document.body.style.backgroundColor;
      }, slider.value);
    });
    
    var sentence3 = document.createElement('div');
    sentence3.innerHTML = 'animation speed';
    sentence3.style.position = 'absolute';
    sentence3.style.top = '10%';
    sentence3.style.left = '25%';
    sentence3.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(sentence3);
    
    var slider2 = document.createElement('input');
    slider2.type = 'range';
    slider2.min = '1';
    slider2.max = '200';
    slider2.value = '25';
    slider2.style.position = 'absolute';
    slider2.style.top = '5%';
    slider2.style.right = '15%';
    slider2.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(slider2);
    slider2.addEventListener('change', function() {
      radius = slider2.value;
      center = {x: window.innerWidth / 2, y: window.innerHeight/2};
      angle = 0;
      step = Math.PI / 9;
      for (var i = 0; i < 18; i++) {
        circles[i].style.top = center.y + radius * Math.sin(angle) + 'px';
        circles[i].style.left = center.x + radius * Math.cos(angle) + 'px';
        angle += step;
      }
    });
    
    var sentence4 = document.createElement('div');
    sentence4.innerHTML = 'distance';
    sentence4.style.position = 'absolute';
    sentence4.style.top = '10%';
    sentence4.style.right = '25%';
    sentence4.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(sentence4);
    
    var slider3 = document.createElement('input');
    slider3.type = 'range';
    slider3.min = '1';
    slider3.max = '200';
    slider3.value = '25';
    slider3.style.position = 'absolute';
    slider3.style.top = '5%';
    slider3.style.right = '41%';
    slider3.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(slider3);
    slider3.addEventListener('change', function() {
      for (var i = 0; i < circles.length; i++) {
        circles[i].style.width = circles[i].style.height = slider3.value + 'px';
      }
    });
    
    var sentence5 = document.createElement('div');
    sentence5.innerHTML = 'radius';
    sentence5.style.position = 'absolute';
    sentence5.style.top = '10%';
    sentence5.style.right = '55%';
    sentence5.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(sentence5);
    
    var slider4 = document.createElement('input');
    slider4.type = 'range';
    slider4.min = '0';
    slider4.max = '25';
    slider4.value = '0';
    slider4.style.position = 'absolute';
    slider4.style.top = '25%';
    slider4.style.right = '75%';
    slider4.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(slider4);
    slider4.addEventListener('change', function() {
      document.body.style.filter = 'blur(' + slider4.value + 'px)';
    });
    
    var sentence6 = document.createElement('div');
    sentence6.innerHTML = 'blur';
    sentence6.style.position = 'absolute';
    sentence6.style.top = '32%';
    sentence6.style.right = '88%';
    sentence6.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(sentence6);
                
    document.body.style.overflow = 'hidden';
    
    document.body.style.fontFamily = 'Helvetica, Arial, sans-serif';            
    });