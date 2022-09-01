var canvas = document.createElement('canvas');
   canvas.width = window.innerWidth;
   canvas.height = window.innerHeight;
   document.body.appendChild(canvas);
   var ctx = canvas.getContext('2d');
   ctx.fillStyle = 'black';
   for (var i = 0; i < window.innerWidth; i += 10) {
     ctx.fillRect(i, 0, 5, window.innerHeight);
   }



var button = document.createElement('button');
button.innerHTML = 'Hide Lines';
button.style.position = 'absolute';
button.style.top = '30';
button.style.left = '75px';
document.body.appendChild(button);
var lines = document.querySelectorAll('canvas');
function toggleLines() {
  for (var i = 0; i < lines.length; i++) {
    var line = lines[i];
    if (line.style.display === 'none') {
      line.style.display = 'block';
      button.innerHTML = 'Hide Lines';
    } else {
      line.style.display = 'none';
      button.innerHTML = 'Show Lines';
    }
  }
}
button.addEventListener('click', toggleLines);



button.style.position = 'absolute';

button.style.transform = 'translate(50%, -50%)';
button.style.fontSize = '20px';
button.style.fontWeight = 'bold';
button.style.backgroundColor = '#ff0000';
button.style.color = '#ffffff';
button.style.padding = '10px';
button.style.border = 'none';
button.style.borderRadius = '5px';
button.style.cursor = 'pointer';
   var rect = document.createElement('div');
   rect.style.position = 'absolute';
   rect.style.left = '150px';
   rect.style.top = '150px';
   rect.style.width = '22px';
   rect.style.height = '65px';
   rect.style.backgroundColor = 'yellow';
   document.body.appendChild(rect);


   var rect = document.createElement('div');
   rect.style.position = 'absolute';
   rect.style.left = '150px';
   rect.style.top = '250px';
   rect.style.width = '22px';
   rect.style.height = '65px';
   rect.style.backgroundColor = 'blue';
   document.body.appendChild(rect);


   var rect = document.createElement('div');
   rect.style.position = 'absolute';
   rect.style.left = '250px';
   rect.style.top = '250px';
   rect.style.width = '22px';
   rect.style.height = '65px';
   rect.style.backgroundColor = 'blue';
   document.body.appendChild(rect);


   var rect = document.createElement('div');
   rect.style.position = 'absolute';
   rect.style.left = '250px';
   rect.style.top = '150px';
   rect.style.width = '22';
   rect.style.height = '65px';
   rect.style.backgroundColor = 'yellow';
   document.body.appendChild(rect);

   document.getElementById("viewport").setAttribute("content",
   "initial-scale=0.5; maximum-scale=1.0; user-scalable=0;");

   document.body.style.overflow = 'hidden';

   var rect = document.createElement('div');
   rect.style.position = 'absolute';
   rect.style.left = '205px';
   rect.style.top = '230px';
   rect.style.width = '8';
   rect.style.height = '8px';
   rect.style.backgroundColor = 'red';
   document.body.appendChild(rect);


   var rects = document.querySelectorAll('div');
   var direction = 0.5;
   var speed = 0.5;
   function animate() {
     for (var i = 0; i < rects.length; i++) {
       var rect = rects[i];
       rect.style.left = (parseFloat(rect.style.left) + speed * direction) + 'px';
       if (parseFloat(rect.style.left) >= window.innerWidth - 15) {
         direction = -1;
       }
       if (parseFloat(rect.style.left) <= 0) {
         direction = 1;
       }
     }
     requestAnimationFrame(animate);
   }
   animate();

var slider = document.createElement('input');
slider.type = 'range';
slider.min = 0;
slider.max = 2;
slider.step = 0.01;
slider.value = 0.5;

document.body.appendChild(slider);

function updateSpeed() {
  speed = slider.value;
}
slider.addEventListener('input', updateSpeed);

var colorPicker = document.createElement('input');
colorPicker.type = 'color';
colorPicker.value = '#0000ff';
document.body.appendChild(colorPicker);

function updateColor() {
  for (var i = 0; i < rects.length; i++) {
    var rect = rects[i];
    rect.style.backgroundColor = colorPicker.value;
  }
}
var text = document.createElement('div');
text.innerHTML = 'Blur';
text.style.position = 'absolute';
text.style.fontWeight = 'bold';
text.style.right = '75%';
text.style.top = '107%';
text.style.transform = 'translate(-50%, -50%)';
document.body.appendChild(text);

colorPicker.addEventListener('input', updateColor);
var slider4 = document.createElement('input');
slider4.type = 'range';
slider4.min = '0';
slider4.max = '25';
slider4.value = '0';
slider4.style.position = 'absolute';
slider4.style.top = '90%';
slider4.style.right = '65%';
slider4.style.transform = 'translate(-50%, -50%)';
document.body.appendChild(slider4);
slider4.addEventListener('change', function() {
  document.body.style.filter = 'blur(' + slider4.value + 'px)';
});
