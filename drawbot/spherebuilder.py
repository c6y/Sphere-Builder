from math import sin, radians, sqrt

# Constants for sphere dimensions
RADIUS = 180  # Radius of the sphere (180 is full size)
DIAMETER = RADIUS * 2  # Diameter of the sphere

# Slice configuration
SLICE_COUNT_PER_HALF = 3  # Default is 9
SEGMENTATION_PERIMETER = True
# If True, slices will have equal perimeter; otherwise, slices will have equal height

# Camera configuration
CAMERA_PITCH = 30  # Default is 30° (eCity)
CAMERA_ROLL = 35   # Camera roll; no roll at 0°

# Utility functions
def calc_triangle_side_B(side_A, angle_A, angle_B):
    """Calculate the length of side B in a triangle."""
    angle_C = angle_A - angle_B
    return side_A * sin(radians(angle_C))

def calc_triangle_side_C(side_A, angle_A, angle_B):
    """Calculate the length of side C in a triangle."""
    return side_A * sin(radians(angle_B))

def calc_arc_chord(arc_sagitta):
    """Calculate the chord length of an arc given its sagitta."""
    return sqrt(arc_sagitta) * sqrt(2 * RADIUS - arc_sagitta) * 2

def draw_slice(apothem_normalized, y_factor, z_factor):
    """Draw a slice of the sphere."""
    apothem = RADIUS * apothem_normalized
    sagitta = RADIUS - apothem
    arc_chord = calc_arc_chord(sagitta)
    oval_height = arc_chord * z_factor
    oval_y_offset_plus = -oval_height / 2 + apothem * y_factor
    oval_y_offset_minus = -oval_height / 2 - apothem * y_factor

    # Draw upper and lower ovals
    oval(-arc_chord / 2, oval_y_offset_plus, arc_chord, oval_height)
    oval(-arc_chord / 2, oval_y_offset_minus, arc_chord, oval_height)

# Canvas setup
size(364, 364)
fill(0.12, 0.13, 0.15, 1)  # Background color
rect(0, 0, width(), height())  # Background rectangle

# Precompute factors
y_factor = calc_triangle_side_B(1, 90, CAMERA_PITCH)
z_factor = calc_triangle_side_C(1, 90, CAMERA_PITCH)

# Drawing the sphere
with savedState():
    translate(width() / 2, height() / 2)
    rotate(CAMERA_ROLL, center=(0, 0))
    fill(None)  # No fill for slices
    strokeWidth(1)

    # Draw the y-axis
    stroke(0, 0, 1, 1)  # Blue for y-axis
    line((0, RADIUS * y_factor), (0, -RADIUS * y_factor))

    # Draw slices
    stroke(0, 0.75, 0, 1)  # Green for slices
    if SEGMENTATION_PERIMETER:
        # Slice into segments with equal perimeter
        for i in range(SLICE_COUNT_PER_HALF):
            angle = 90 / SLICE_COUNT_PER_HALF * (i + 1)
            apothem_normalized = calc_triangle_side_B(1, 90, angle)
            draw_slice(apothem_normalized, y_factor, z_factor)
    else:
        # Slice into segments with equal height
        slice_height = 1 / SLICE_COUNT_PER_HALF
        for i in range(SLICE_COUNT_PER_HALF):
            draw_slice(slice_height * i, y_factor, z_factor)

    # Draw sphere outline
    stroke(1, 0, 0, 1)  # Red for outline
    oval(-RADIUS, -RADIUS, DIAMETER, DIAMETER)

# File output
slice_count_total = SLICE_COUNT_PER_HALF * 2
filename = f"sphere_{slice_count_total}s_{CAMERA_PITCH}p_{CAMERA_ROLL}r.svg"
directory = "~/Desktop/SphereBuilder/"
path = directory + filename
saveImage(path, antiAliasing=True)