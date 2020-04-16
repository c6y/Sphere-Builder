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
  stroke(0, 191, 0);
  line(0, radius * yFactor, 0, -radius * yFactor);

  // draw sphere outline
  stroke(191, 0, 0);
  circle( 0,  0, diameter);

  // draw center circle
  stroke(0, 0, 191);
  ellipse(0, 0, 360, 180);
}
