let xSlider;
let tSlider;
let strokeWeightSlider;
let amplitudeSlider;


function setup() {
  // create the canvas and the sliders
  createCanvas(800, 600);
  xSlider = createSlider(1, 80, 20, 1);
  xSlider.position(10, 10);
  xSlider.style('width', '200px');
  
  tSlider = createSlider(1, 70, 15, 1);
  tSlider.position(10, 30);
  tSlider.style('width', '200px');

  strokeWeightSlider = createSlider(1, 40, 20, 1);
  strokeWeightSlider.position(10, 50);
  strokeWeightSlider.style('width', '200px');

  amplitudeSlider = createSlider(1, 125, 75, 1);
  amplitudeSlider.position(10, 70);
  amplitudeSlider.style('width', '200px');

  // create labels for the sliders
  xLabel = createSpan('X Spacing');
  xLabel.position(230, 15);
  xLabel.style('color', 'yellow');

  tLabel = createSpan('T Speed');
  tLabel.position(230, 35);
  tLabel.style('color', 'yellow');

  strokeWeightLabel = createSpan('Radius');
  strokeWeightLabel.position(230, 55);
  strokeWeightLabel.style('color', 'yellow');

  amplitudeLabel = createSpan('Amplitude');
  amplitudeLabel.position(230, 75);
  amplitudeLabel.style('color', 'yellow');
}

function drawGrid() {
  // set the stroke weight and color
  strokeWeight(strokeWeightSlider.value());
  stroke(255);
  
  let t = frameCount / tSlider.value();
  for (let x = 0; x < width; x += xSlider.value()) {
    let y = height / 2 + amplitudeSlider.value() * sin(x / 30 + t);
    point(x, y);
  }
}


function draw() {
  background(0);
  drawGrid();
}