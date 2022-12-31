// create a canvas to draw on
function setup() {
  createCanvas(400, 400);
}

// define the sine wave pattern
function drawSineWave(amplitude, frequency) {
  stroke(255, 0, 0);
  strokeWeight(2); // use the value of the lineThickness parameter to set the strokeWeight of the sine lines
  noFill(0);

  beginShape();
  for (let x = 0; x <= width; x += 2) {
    let y = amplitude * sin(x / frequency) + height / 2;
    vertex(x, y);
  }
  endShape();
}
// define the moving grid
function drawGrid(lineThickness, speed) {
  stroke(0);
  strokeWeight(lineThickness);
  let t = frameCount / speed;
  for (let x = 0; x < 150; x += 12) {
    line(x + t, 0, x + t, height);
  }
}

// draw the animation
function draw() {
  background(255, 255, 255); // set the background color to white
  drawSineWave(90,1); // use a value of 100 for the amplitude and 10 for the frequency
  drawGrid(9.5,3); // use a value of 7 for the line thickness and 2 for the speed
}

