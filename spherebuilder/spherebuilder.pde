int radius = 180;
int diameter = radius * 2;
float numOfSlicesPerHalf = 6;
float rotateByPI = 0;

float angleA = 60;
float angleB = 90;
float angleC = 30; // AngleB minus Angle A
float aSide;
float bSide;
float cSide = 1;

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
  bSide = cSide * sin(radians(angleA));
  println("bSide: " + bSide);

  aSide = cSide * sin(radians(angleC));
  println("aSide: " + aSide);

  background(240);
  translate(width/2,  width/2);
  noFill();
  strokeWeight(0.5);
  rotate(rotateByPI);

  // draw vertical axis
  stroke(191, 0, 0);
  line(0, radius * yFactor, 0, -radius * yFactor);

  // draw slices
  stroke(0, 191, 0);
  float sliceHeight = 1/numOfSlicesPerHalf;
  for (int i = 0; i < numOfSlicesPerHalf; i = i+1) {
    drawSlice(sliceHeight * i);
  }

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
