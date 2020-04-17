int radius = 180;
int diameter = radius * 2;

float xFactor = 1;              // eCity horizontal-axis 1:1 compression
float yFactor = sqrt(3.0)/2;    // eCity vertical-axis compression
float zFactor = 0.5;            // eCity depth-axis 2:1 compression

void settings() {
  size(480, 480);
  noSmooth();

  println("xFactor: " + xFactor);
  println("yFactor: " + yFactor);
  println("zFactor: " + zFactor);
}

void setup() {
  translate(width/2,  width/2);
  noFill();
  strokeWeight(0.5);
  // rotate(PI/4); // optional rotation

  // draw vertical axis
  stroke(191, 0, 0);
  line(0, radius * yFactor, 0, -radius * yFactor);

  // draw slices
  stroke(0, 191, 0);
  drawSlice(0.0);
  drawSlice(0.2);
  drawSlice(0.4);
  drawSlice(0.6);
  drawSlice(0.8);

  // draw outline
  stroke(0, 0, 191);
  circle( 0,  0, diameter);
}

float calcArcChord(float arcSagitta) {
  float arcChord = sqrt(arcSagitta) * sqrt(2 * radius - arcSagitta) * 2;
  return arcChord;
}

void drawSlice(float apothemNormalized) {
  float apothem = radius * apothemNormalized;
  float sagitta = radius - apothem;
  float arcChord = calcArcChord(sagitta);

  ellipse(0, apothem * yFactor, arcChord, arcChord * zFactor);
  ellipse(0, -apothem * yFactor, arcChord, arcChord * zFactor);
}
