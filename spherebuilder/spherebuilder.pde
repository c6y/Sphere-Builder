// Sphere dimensions
int radius = 180;
int diameter = radius * 2;
float sliceCountPerHalf = 6; // default is 6

// Camera rotations
float cameraPitch = 30; // eCity is 30°
float cameraRoll = 0; // no roll at 0

// float xFactor = 1; // eCity horizontal-axis compression is 1
float yFactor;     // Isometric vertical-axis compression
float zFactor;     // Isometric depth-axis compression

void settings() {
  size(400, 400);
  noSmooth();
}

void setup() {
  background(216, 216, 216);
  translate(width/2,  width/2);
  noFill();
  strokeWeight(0.5);
  rotate(radians(cameraRoll));

  calcIsometricYandZ();

  // draw vertical axis
  stroke(191, 0, 0);
  line(0, radius * yFactor, 0, -radius * yFactor);

  // draw slices
  stroke(0, 191, 0);
  float sliceHeight = 1/sliceCountPerHalf;
  for (int i = 0; i < sliceCountPerHalf; i = i+1) {
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
  float angleB = cameraPitch;
  float angleC = angleA - angleB;
  float sideA = 1;
  float sideB = sideA * sin(radians(angleC));
  float sideC = sideA * sin(radians(angleB));

  // Assign triangle values to scaling factors
  yFactor = sideB;
  zFactor = sideC;

  println("yFactor: " + yFactor + ", zFactor: " + zFactor);
}
