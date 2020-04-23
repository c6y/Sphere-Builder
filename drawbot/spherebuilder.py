# Sphere dimensions
RADIUS = 180
DIAMETER = RADIUS * 2

# Slices
SLICE_COUNT_PER_HALF = 9 # default is 9
SEGMENTATION_PERIMETER = True
# if true, slice into segments with same perimeter (default)
# if false, slice into segments with same height

# Camera rotations
CAMERA_PITCH = 30       # default is 30° (eCity)
CAMERA_ROLL = 0         # no roll at 0

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
  oval_height = arc_chord * z_factor
  oval_y_offset_plus = -oval_height / 2 + apothem * y_factor
  oval_y_offset_minus = -oval_height / 2 - apothem * y_factor

  oval(-arc_chord / 2, oval_y_offset_plus, arc_chord, oval_height)
  oval(-arc_chord / 2, oval_y_offset_minus, arc_chord, oval_height)

size(364, 364)

# background
# fill(0.12, 0.13, 0.15, 1)
# rect(0, 0, 364, 364)

y_factor = calc_triangle_side_B(1, 90, CAMERA_PITCH)
z_factor = calc_triangle_side_C(1, 90, CAMERA_PITCH)

with savedState():
    translate(width() / 2, height() / 2)
    rotate(CAMERA_ROLL, center=(0, 0))
    fill()
    strokeWidth(1)

    # draw y-axis
    stroke(0, 0, 1, 1)
    line((0, RADIUS * y_factor), (0, -RADIUS * y_factor))

    stroke(0, 0.75, 0, 1)

    if SEGMENTATION_PERIMETER:
        # slice in half
        drawSlice(0)
        # slice into segments with same perimeter
        for i in range(SLICE_COUNT_PER_HALF):
            angle = 90 / SLICE_COUNT_PER_HALF * i
            foo = calc_triangle_side_B(1, 90, angle)
            drawSlice(foo)
    else:
        # slice into segments with same height
        slice_height = 1 / SLICE_COUNT_PER_HALF
        for i in range(SLICE_COUNT_PER_HALF):
            drawSlice(slice_height * i)

    # draw outline
    stroke(1, 0, 0, 1)
    oval(-RADIUS, -RADIUS, DIAMETER, DIAMETER)

slice_count_total = SLICE_COUNT_PER_HALF * 2
filename = "sphere_%ss_%sp_%sr" % (slice_count_total, CAMERA_PITCH, CAMERA_ROLL)
extension = ".svg"
directory = "~/Desktop/"
path = directory + filename + extension
saveImage(path)
