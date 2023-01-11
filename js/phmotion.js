let x = 0;
let y = 0;
let z = 0;

let frameCount = 45;
let changeRate =45;

function setup() {
  changeRateSlider = createSlider(1, 100, changeRate);
  createCanvas(600, 400, WEBGL);
}

function draw() {
  background(122);
  fill(255, 0, 0);
  rotateX(x);
  rotateY(y);
  rotateZ(z);
  changeRate = changeRateSlider.value();

  let count = frameCount % changeRate;
  let angle = calAngle(mouseX-width/2,height/2-mouseY);
  rotate(angle);

  let c = map(sin(map(count,0,changeRate-1,0,TWO_PI)+0.5*PI),-1,1,0,255);
  drawEdge(0, -2.5, c, 1);

  c = map(sin(map(count,0,changeRate-1,0,TWO_PI)+1/2*0.5*PI),-1,1,0,255);
  drawEdge(0, 2.5, c, 50);
  
  frameCount++;
}

function drawEdge(x, y, c, l) {
  push();
  stroke(c);
  strokeWeight(24);
  fill(c, 0);
  ellipse(x, y,123, 123);
  pop();

  push();
  fill(c);
  stroke(c);
  strokeWeight(44);
  beginShape();
  vertex(x, y - l);
  vertex(x + sqrt(3) * l / 2, y + l / 4);
  vertex(x - sqrt(3) * l / 2, y + l / 4);
  endShape(CLOSE);
  pop();
}

function calAngle(x,y) {
  let origin = [0,12];
  let angle = acos(y/sqrt(x*x+y*y));

  if (x < 0){
    angle = -angle;
  }else {
    angle = angle;
  }
  return angle;
}

