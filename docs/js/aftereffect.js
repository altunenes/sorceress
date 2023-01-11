let squares = [];
let current = 0;
let strokeSlider;
let bgColorPicker;
let color1, color2, color3, color4, color5, color6, color7, color8;
let movingSquareColorPicker;
let pattern = 0;


function setup() {
  frameRate(8); //speed
  createCanvas(900,900);
  strokeSlider = createSlider(1, 40, 4, 1);
  strokeSlider.position(20, 600);
  strokeSlider.style('width', '80px');
  bgColorPicker = createColorPicker("#000000"); // default background color is black
  movingSquareColorPicker = createColorPicker('white');
  movingSquareColorPicker.position(120, 600);
  patternButton = createButton("Change pattern");
  patternButton.position(width/2, height - 30);
  patternButton.mousePressed(changePattern);
  bgColorPicker.position(20, 550);
    for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
      squares.push([i, j]);
    }
  }

  color1 = createColorPicker('#0000ff'); 
  color2 = createColorPicker('#ff0000'); 
  color3 = createColorPicker('#00ff00'); 
  color4 = createColorPicker('#F74201'); 
  color5 = createColorPicker('#00c0ff'); 
  color6 = createColorPicker('#ffff00'); 
  color7 = createColorPicker('#ff00cb'); 
  color8 = createColorPicker('#7d0129'); 

  let container = createDiv("");
  container.id("colors-container");
  container.position(20, 700);


  color1.parent(container);
  color2.parent(container);
  color3.parent(container);
  color4.parent(container);
  color5.parent(container);
  color6.parent(container);
  color7.parent(container);
  color8.parent(container);
  color1.position(20, 35);
  color2.position(90, 35);
  color3.position(160, 35);
  color4.position(20,85);
  color5.position(90, 85);
  color6.position(160, 85);
  color7.position(20, 135);
  color8.position(90, 135);
}
function changePattern() {
  pattern++;
  pattern %= 4; // change this to the total number of patterns
}
let counter = 0;

function draw() {
  background(bgColorPicker.color()); // set the background color
  var xPos = 0;
  drawSquares(xPos, color1.color(), 0, 0, 0);
  xPos += (3*50 + 25); 
  drawSquares(xPos, color2.color(), 0, 0, 0);
  xPos += (3*50 + 25);
  drawSquares(xPos, color3.color(), 0, 0, 0);
  xPos = 0;
  drawSquares(xPos, color4.color(), 0, 0, 180);
  yPos=0
  drawSquares(xPos, color5.color(), 0, 0, 360);
  xPos += (3*50 + 200)
  drawSquares(xPos, color6.color(), 0, 0, 180);
  drawSquares(xPos, color7.color(), 0, 0, 360);
  xPos += (3*50 - 320)
  drawSquares(xPos, color8.color(), 0, 0, 360);
  counter++;
  
  stroke(1); 
  strokeWeight(strokeSlider.value());
  textSize(45);
  fill("white");
  text("X",250,280);
}

function drawSquares(xPos, r,g,b, yPos) {
  let color = movingSquareColorPicker.color();
  
   if (pattern == 0) {
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if ((i*j) % 5 === 1) {
        fill(255);
    } else {
        fill(r, g, b);
    }
    rect((i * 50) + (i * 10) + xPos, (j * 50) + (j * 10) + yPos, 50, 50);
    if (i == (counter % 3) && j == (counter % 4)) {
      fill(color);
      rect((i * 50) + (i * 10) + xPos, (j * 50) + (j * 10) + yPos, 50, 50);
    }
  }
}  } else if (pattern == 1) {
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
if ((i+j) % (1*3) == counter % (1*3)) {
        fill(255);
    } else {
        fill(r, g, b);
    }
    rect((i * 50) + (i * 10) + xPos, (j * 50) + (j * 10) + yPos, 50, 50);
if ((i+j) % (2*12) == counter % (3*3)) {
      fill(255);
      rect((i * 50) + (i * 10) + xPos, (j * 50) + (j * 10) + yPos, 50, 50);
    }
  }
}
  
  } else if (pattern == 2) {
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if ((i*j) % 4 === 1) {
        fill(255);
    } else {
        fill(r, g, b);
    }
    rect((i * 50) + (i * 10) + xPos, (j * 50) + (j * 10) + yPos, 50, 50);
if ((i+j) % (5*2) == counter % (2*3)) {
      fill(255);
      rect((i * 50) + (i * 10) + xPos, (j * 50) + (j * 10) + yPos, 50, 50);
    }
  }
} 
  
  
  
    } else {
for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if ((i + j) % 4 === 0) {
        fill(255);
    } else {
        fill(r, g, b);
    }
    rect((i * 50) + (i * 10) + xPos, (j * 50) + (j * 10) + yPos, 50, 50);
if ((i+j) % (1*1) == counter % (2*1)) {
  fill(color);
  rect((i * 50) + (i * 10) + xPos, (j * 50) + (j * 10) + yPos, 50, 50);
}
  }
}   }

  
  

}
