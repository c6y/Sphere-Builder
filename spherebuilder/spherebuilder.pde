int radius = 180;
int diameter = radius * 2;
float numOfSlicesPerHalf = 6; // default is 6
float rotateByPI = 0; // no rotation at 0
float cameraAngle = 30; // eCity is 30°

float xFactor = 1; // eCity horizontal-axis 1:1 compression
float yFactor;     // eCity vertical-axis compression
float zFactor;     // eCity depth-axis 2:1 compression

void settings() {
  size(480, 480);
  noSmooth();
}

void setup() {
  calcIsometricYandZ();

  background(240);
  translate(width/2,  width/2);
  noFill();
  strokeWeight(0.5);
  rotate(rotateByPI * PI);

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

void calcIsometricYandZ() {
  // Calculate missing triangle values
  float angleA = 90;
  float angleB = cameraAngle;
  float angleC = angleA - angleB;
  float sideA = 1;
  float sideB = sideA * sin(radians(angleC));
  float sideC = sideA * sin(radians(angleB));

  // Assign triangle values to scaling factors
  yFactor = sideB;
  zFactor = sideC;

  println("yFactor: " + yFactor + ", zFactor: " + zFactor);
}
