int radius = 180;
int diameter = radius * 2;
float perspectiveCompression = 5.0 / 7.0; // eCity 2:1 compression

void settings() {
  size(480, 480);
  noSmooth();
}

void setup() {
  colorMode(RGB, 255, 255, 255, 100);
  strokeWeight(0.5);
  //scale(2);
  translate(width/2,  width/2);
  circle( 0,  0, diameter);
  //rotate(PI/2.84);
  noFill();
  
  // draw vertical axis
  float compressedAxis = radius * perspectiveCompression;
  line(0, compressedAxis, 0, -compressedAxis);
  
  stroke(color(0, 0, 255, 50));
  int w1 = 352;
  ellipse(0,  30, w1, w1/2);
  ellipse(0, -30, w1, w1/2);

  int w2 = 332;
  stroke(color(255, 0, 255, 50));
  ellipse(0,  60, w2, w2/2);
  ellipse(0, -60, w2, w2/2);

  int w3 = 294;
  stroke(color(255, 0, 0, 50));
  ellipse(0,  90, w3, w3/2);
  ellipse(0, -90, w3, w3/2);
  
  int w4 = 228;
  stroke(color(0, 128, 255, 50));
  ellipse(0,  120, w4, w4/2);
  ellipse(0, -120, w4, w4/2);
  
  int w5 = 128;
  stroke(color(0, 128, 255, 50));
  ellipse(0,  128, w5, w5/2);
  ellipse(0, -128, w5, w5/2);
  
  stroke(color(0, 255, 0, 50));
  ellipse(0, 0, 360, 180);
}
