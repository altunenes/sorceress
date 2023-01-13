let xIncrementSlider, amplitudeSlider, frequencySlider, gridThicknessSlider, speed = 3;
let speedUpButton, speedDownButton, bgColorPicker, gridColorPicker, sinColorPicker,cosColorPicker;
let cosineToggle = false;
let toggleButton;
let sliderContainer;
let buttonContainer;
let colorContainer;
let labelContainer;
function setup() {
  createCanvas(800, 800);
  sliderContainer = createDiv();
  buttonContainer = createDiv();
  colorContainer = createDiv();
  labelContainer = createDiv();
  xIncrementSlider = createSlider(1, 20, 4, 1);
  amplitudeSlider = createSlider(50, 150, 90, 1);
  frequencySlider = createSlider(1, 10, 1, 0.1);
  gridThicknessSlider = createSlider(1, 20, 7, 1);
  sliderContainer.child(xIncrementSlider);
  sliderContainer.child(amplitudeSlider);
  sliderContainer.child(frequencySlider);
  sliderContainer.child(gridThicknessSlider);
  sliderContainer.style("display: flex; flex-wrap:wrap; justify-content: space-between;");
  speedUpButton = createButton("Speed -");
  speedUpButton.mousePressed(increaseSpeed);
  speedDownButton = createButton("Speed +");
  speedDownButton.mousePressed(decreaseSpeed);
  buttonContainer.child(speedUpButton);
  buttonContainer.child(speedDownButton);
  buttonContainer.style("display: flex; justify-content: space-between;");
  bgColorPicker = createColorPicker("#FFFFFF");
  gridColorPicker = createColorPicker("#000000");
  sinColorPicker = createColorPicker("#FF0000");
  cosColorPicker = createColorPicker("#0000FF");
  colorContainer.child(bgColorPicker);
  colorContainer.child(gridColorPicker);
  colorContainer.child(sinColorPicker);
  colorContainer.child(cosColorPicker);
  colorContainer.style("display: flex; justify-content: space-between;");
  toggleButton = createButton("Toggle Cosine Wave");
  toggleButton.mousePressed(toggleCosineWave);
  buttonContainer.child(toggleButton);
  createLabel("X-Increment : ",xIncrementSlider);
  createLabel("Amplitude : ",amplitudeSlider);
  createLabel("Frequency : ",frequencySlider);
  createLabel("Grid Thickness : ",gridThicknessSlider);
  createLabel("Background Color : ",bgColorPicker);
  createLabel("Grid Color : ",gridColorPicker);
  createLabel("Sine Color : ",sinColorPicker);
  createLabel("Cosine Color : ",cosColorPicker);
}
function createLabel(label,element){
  let labelElement = createDiv(label);
  labelElement.child(element);
  labelContainer.child(labelElement);
}
function drawSineWave() {
  stroke(sinColorPicker.color());
  strokeWeight(2);
  noFill();
  beginShape();
  for (let x = 0; x <= width; x += xIncrementSlider.value()) {
    let y = amplitudeSlider.value() * sin(x / frequencySlider.value()) + height / 2;
    vertex(x, y);
  }
  endShape();
}
function drawCosineWave() {
  if (cosineToggle) {
    stroke(cosColorPicker.color());
    strokeWeight(2);
    noFill();
    beginShape();
    for (let x = 0; x <= width; x += xIncrementSlider.value()) {
      let y = amplitudeSlider.value() * cos(x / frequencySlider.value()) + height / 2;
      vertex(x, y);
    }
    endShape();
  }
}
function drawGrid() {
  stroke(gridColorPicker.color());
  strokeWeight(gridThicknessSlider.value());
  let t = frameCount / speed;
  for (let x = 0; x < 150; x += 12) {
    line(x + t % width, 0, x + t % width, height);
  }
}
function increaseSpeed() {
  speed += 1;
}
function decreaseSpeed() {
  speed -= 1;
}
function toggleCosineWave() {
  cosineToggle = !cosineToggle;
}
function draw() {
  background(bgColorPicker.color());
  drawSineWave();
  drawCosineWave();
  drawGrid();
}