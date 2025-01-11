from math import sin, radians, sqrt

# Constants for sphere dimensions
RADIUS = 180  # Radius of the sphere (default is 180 for full size)
DIAMETER = RADIUS * 2  # Diameter of the sphere

COLOR_BACK = (0.12, 0.13, 0.15, 1)
COLOR_CIRCLE_OUTLINE = (1.0, 0.1, 0.1, 1)
COLOR_SLICES = (0.1, 1.0, 0.1, 1)
COLOR_AXIS = (0.2, 0.2, 1.0, 1)

# Slice configuration
SLICE_COUNT_PER_HALF = 5  # Number of slices per hemisphere
SEGMENTATION_PERIMETER = True  # True for equal perimeter slices, False for equal height

# Camera configuration
CAMERA_PITCH = 30  # Vertical camera pitch (default is 30°)
CAMERA_ROLL = 45   # Camera roll; 0° for no roll

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
STROKE_WEIGHT = 2
CANVAS_SIZE = 360 + (STROKE_WEIGHT * 5)  # Canvas dimensions (adjust as needed)
size(CANVAS_SIZE, CANVAS_SIZE)
fill(*COLOR_BACK)  # Background color
rect(0, 0, width(), height())  # Fill the background

# Precompute y-factor and z-factor
y_factor = calc_triangle_side_B(1, 90, CAMERA_PITCH)
z_factor = calc_triangle_side_C(1, 90, CAMERA_PITCH)

# Drawing the sphere
with savedState():
    translate(width() / 2, height() / 2)  # Center the drawing
    rotate(CAMERA_ROLL, center=(0, 0))  # Apply camera roll
    fill(None)  # No fill for slices
    strokeWidth(STROKE_WEIGHT)

    # Draw the y-axis
    stroke(*COLOR_AXIS)  # Blue for y-axis
    lineCap("round")  # Set the line cap to rounded ends
    line((0, RADIUS * y_factor), (0, -RADIUS * y_factor))
    

    # Draw slices
    stroke(*COLOR_SLICES)  # Green for slices
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
    stroke(*COLOR_CIRCLE_OUTLINE)  # Red for outline
    oval(-RADIUS, -RADIUS, DIAMETER, DIAMETER)

# File output
slice_count_total = SLICE_COUNT_PER_HALF * 2
filename = f"sphere_{slice_count_total}s_{CAMERA_PITCH}p_{CAMERA_ROLL}r.svg"
directory = "~/Desktop/SphereBuilder/"
path = directory + filename
saveImage(path, antiAliasing=True)