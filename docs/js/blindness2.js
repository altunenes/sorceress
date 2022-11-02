document.addEventListener("DOMContentLoaded", function() {

    document.body.style.overflow = 'hidden';
    
    var rect = document.createElement('div');
    rect.style.position = 'absolute';
    rect.style.left = '40%';
    rect.style.top = '10%';
    rect.style.width = '350px';
    rect.style.height = '350px';
    rect.style.backgroundColor = 'black';
    rect.style.border = 'white';
    document.body.appendChild(rect);
    
    
    var freq = 10;
    for (var i = 0; i < freq; i++) {
      for (var j = 0; j < freq; j++) {
        var plus = document.createElement('div');
        plus.style.position = 'absolute';
        plus.style.left = (i * rect.offsetWidth / freq) + 'px';
        plus.style.top = (j * rect.offsetHeight / freq) + 'px';
        plus.style.width = (rect.offsetWidth / freq) + 'px';
        plus.style.height = (rect.offsetHeight / freq) + 'px';
        plus.style.backgroundColor = 'black';
        plus.style.border = 'black';
        plus.style.fontSize = '35px';
        plus.innerHTML = '+';
        rect.appendChild(plus);
      }
    }
    
    
    
    
    var blue = document.getElementsByTagName('div');
    for (var i = 0; i < blue.length; i++) {
      blue[i].style.color = 'blue';
    }
    
    var slider = document.createElement('input');
    slider.type = 'range';
    slider.min = '1';
    slider.max = '100';
    slider.value = '1';
    slider.style.position = 'absolute';
    slider.style.left = '10%';
    slider.style.top = '25%';
    slider.style.width = '250px';
    slider.style.height = '50px';
    slider.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(slider);
    
    var angle = 0;
    var speed = 0.1;
    var animate = setInterval(function() {
      angle += speed;
      rect.style.transform = 'rotate(' + angle + 'deg)';
      speed = slider.value / 50;
    }, 10);
    
    var bold = document.getElementsByTagName('div');
    for (var i = 0; i < bold.length; i++) {
      bold[i].style.fontWeight = 'bold';
    }
    
    document.body.style.backgroundColor = 'black';
    
    var circle = document.createElement('div');
    circle.style.position = 'absolute';
    circle.style.left = '50%';
    circle.style.top = '50%';
    circle.style.width = '10px';
    circle.style.height = '10px';
    circle.style.backgroundColor = 'red';
    circle.style.borderRadius = '50%';
    circle.style.transform = 'translate(-50%, -50%)';
    rect.appendChild(circle);
    
    
    
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
        blurButton.style.backgroundColor = 'gray';
        blurButton.style.border = 'none';
        blurButton.style.padding = '10px 20px';
        blurButton.style.borderRadius = '5px';
    
    var addCircleButton = document.createElement('button');
    addCircleButton.innerHTML = 'Add Circle';
    document.body.appendChild(addCircleButton);
    var slider2 = document.createElement('input');
    slider2.type = 'range';
    slider2.min = 0;
    slider2.max = 100;
    slider2.value = 50;
    document.body.appendChild(slider2);
    var circles = [];
    addCircleButton.addEventListener('click', function() {
      var circle = document.createElement('div');
      circle.style.width = '10px';
      circle.style.height = '10px';
      circle.style.borderRadius = '50%';
      circle.style.backgroundColor = 'yellow';
      circle.style.position = 'absolute';
      circle.style.left = Math.random() * (window.innerWidth - 50) + 'px';
      circle.style.top = Math.random() * (window.innerHeight - 50) + 'px';
      document.body.appendChild(circle);
      circles.push(circle);
    });
    slider2.addEventListener('input', function() {
      for (var i = 0; i < circles.length; i++) {
        circles[i].style.width = slider2.value + 'px';
        circles[i].style.height = slider2.value + 'px';
      }
    });
    /* make the button looks fancy */
    addCircleButton.style.backgroundColor = '#4CAF50';
    addCircleButton.style.border = 'none';
    addCircleButton.style.color = 'white';
    addCircleButton.style.padding = '15px 32px';
    addCircleButton.style.textAlign = 'center';
    addCircleButton.style.textDecoration = 'none';
    addCircleButton.style.display = 'inline-block';
    addCircleButton.style.fontSize = '16px';
    addCircleButton.style.margin = '4px 2px';
    addCircleButton.style.cursor = 'pointer';
    
    
    var isMouseDown = false;
    var currentCircle;
    document.body.addEventListener('mousedown', function(event) {
      for (var i = 0; i < circles.length; i++) {
        if (event.target === circles[i]) {
          isMouseDown = true;
          currentCircle = circles[i];
          break;
        }
      }
    });
    document.body.addEventListener('mousemove', function(event) {
      if (isMouseDown) {
        currentCircle.style.left = event.clientX - parseInt(currentCircle.style.width) / 2 + 'px';
        currentCircle.style.top = event.clientY - parseInt(currentCircle.style.height) / 2 + 'px';
      }
    });
    document.body.addEventListener('mouseup', function(event) {
      isMouseDown = false;
    });
    
    var color = 'red';
    var changeColor = setInterval(function() {
      if (color == 'red') {
        color = 'green';
      } else {
        color = 'red';
      }
      circle.style.backgroundColor = color;
    }, 100);
    var colorPicker = document.createElement('input');
    colorPicker.type = 'color';
    colorPicker.style.position = 'absolute';
    colorPicker.style.left = '50%';
    colorPicker.style.top = '0%';
    colorPicker.style.width = '50px';
    colorPicker.style.height = '50px';
    colorPicker.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(colorPicker);
    var plus = document.getElementsByTagName('div');
    for (var i = 0; i < plus.length; i++) {
      plus[i].style.color = colorPicker.value;
    }
    colorPicker.addEventListener('change', function() {
      var plus = document.getElementsByTagName('div');
      for (var i = 0; i < plus.length; i++) {
        plus[i].style.color = colorPicker.value;
      }
    });
    colorPicker.value = '#0000ff';
    var plus = document.getElementsByTagName('div');
    for (var i = 0; i < plus.length; i++) {
      plus[i].style.color = '#0000ff';
    }
    colorPicker.style.top = '90%';
    
    var colorPicker2 = document.createElement('input');
    colorPicker2.type = 'color';
    colorPicker2.style.position = 'absolute';
    colorPicker2.style.left = '40%';
    colorPicker2.style.top = '90%';
    colorPicker2.style.width = '50px';
    colorPicker2.style.height = '50px';
    colorPicker2.style.transform = 'translate(-50%, -50%)';
    document.body.appendChild(colorPicker2);
    
    
    colorPicker2.addEventListener('change', function() {
      document.body.style.backgroundColor = colorPicker2.value;
      rect.style.backgroundColor = colorPicker2.value;
      var plus = document.getElementsByTagName('div');
      for (var i = 0; i < plus.length; i++) {
        plus[i].style.border = colorPicker2.value;
        plus[i].style.backgroundColor = colorPicker2.value;
      }
    });
    
    var github = document.createElement('a');
    github.href = 'https://github.com/altunenes';
    github.innerHTML = 'GitHub';
    github.style.position = 'fixed';
    github.style.bottom = '0';
    github.style.right = '0';
    github.style.padding = '10px';
    github.style.backgroundColor = '#333';
    github.style.color = '#fff';
    document.body.appendChild(github);
    var twitter = document.createElement('a');
    twitter.href = 'https://twitter.com/emportent';
    twitter.innerHTML = 'Twitter';
    twitter.style.position = 'fixed';
    twitter.style.bottom = '0';
    twitter.style.right = '100px';
    twitter.style.padding = '10px';
    twitter.style.backgroundColor = '#333';
    twitter.style.color = '#fff';
    document.body.appendChild(twitter);
    document.body.style.overflow = 'hidden';
    
    github.innerHTML = '<i class="fa fa-github"></i>';
    twitter.innerHTML = '<i class="fa fa-twitter"></i>';
    var fontAwesome = document.createElement('link');
    fontAwesome.rel = 'stylesheet';
    fontAwesome.href = 'https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css';
    document.head.appendChild(fontAwesome);
    
    });
    