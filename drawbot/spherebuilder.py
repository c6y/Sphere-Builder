# Sphere dimensions
RADIUS = 180
DIAMETER = RADIUS * 2

# Camera rotations
CAMERA_PITCH = 30   # eCity is 30°
CAMERA_ROLL = 0     # no roll at 0

def calc_triangle_side_B(side_A, angle_A, angle_B):
    angle_C = angle_A - angle_B
    side_B = side_A * sin(radians(angle_C))
    return side_B

def calc_triangle_side_C(side_A, angle_A, angle_B):
    side_C = side_A * sin(radians(angle_B))
    return side_C

def calc_arc_chord(arcSagitta):
  arc_chord = sqrt(arcSagitta) * sqrt(2 * RADIUS - arcSagitta) * 2
  return arc_chord

def drawSlice(apothem_normalized):
  apothem = RADIUS * apothem_normalized
  sagitta = RADIUS - apothem
  arc_chord = calc_arc_chord(sagitta)
  print(z_factor)
  oval_height = arc_chord * z_factor
  oval_y_offset_plus = -oval_height/2 + apothem * y_factor
  oval_y_offset_minus = -oval_height/2 - apothem * y_factor

  oval(-arc_chord/2, oval_y_offset_plus, arc_chord, oval_height)
  oval(-arc_chord/2, oval_y_offset_minus, arc_chord, oval_height)

size(400, 400)
y_factor = calc_triangle_side_B(1, 90, CAMERA_PITCH)
z_factor = calc_triangle_side_C(1, 90, CAMERA_PITCH)

with savedState():
    translate(width()/2, height()/2)
    fill()
    strokeWidth(1)

    # draw y-axis
    stroke(0, 0, 1, 1)
    line((0, RADIUS * y_factor), (0, -RADIUS * y_factor))

    stroke(0, 0.75, 0, 1)

    sliceHeight1 = 0
    drawSlice(sliceHeight1)

    sliceHeight2 = 0.5
    drawSlice(sliceHeight2)

    sliceHeight3 = 0.9
    drawSlice(sliceHeight3)

    # draw outline
    stroke(1, 0, 0, 1)
    oval(-RADIUS, -RADIUS, DIAMETER, DIAMETER)

saveImage("~/Desktop/firstImage.pdf")