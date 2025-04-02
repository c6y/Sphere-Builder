from math import sin, radians, sqrt

# Constants
RADIUS = 30 * 1.05128205  # Radius of the sphere
DIAMETER = RADIUS * 2
COLOR_BACK = (0, 0, 0.5, 1)
COLOR_CIRCLE_OUTLINE = (1, 1, 1, 1)
COLOR_CIRCLE_FILL = (0, 0, 0, 0)
COLOR_SLICES = (1, 1, 0, 1)
COLOR_AXIS = (1, 0, 0, 1)
SLICE_COUNT_PER_HALF = 2
SEGMENTATION_PERIMETER = True
# ECITY! pitch = 30, roll is 90 + 26.565
CAMERA_PITCH = 30  # in degrees
CAMERA_ROLL =  90 + 26.565  # in degrees
STROKE_WEIGHT = 1
PADDING = STROKE_WEIGHT * 5
CANVAS_SIZE = 60 + PADDING

# Utility Functions
def sin_deg(angle):
    """Return the sine of an angle in degrees."""
    return sin(radians(angle))

def calc_triangle_side_B(side_A, angle_A, angle_B):
    """Calculate side B given side_A and two angles (in degrees)."""
    return side_A * sin_deg(angle_A - angle_B)

def calc_triangle_side_C(side_A, angle_A, angle_B):
    """Calculate side C given side_A and an angle (in degrees)."""
    return side_A * sin_deg(angle_B)

def calc_arc_chord(arc_sagitta):
    """
    Calculate the chord length of an arc given its sagitta.
    Combines square roots for slight performance improvement.
    """
    return 2 * sqrt(arc_sagitta * (2 * RADIUS - arc_sagitta))

def draw_slice(apothem_normalized, y_factor, z_factor):
    """
    Draw a single slice using the normalized apothem and perspective factors.
    """
    apothem = RADIUS * apothem_normalized
    sagitta = RADIUS - apothem
    arc_chord = calc_arc_chord(sagitta)
    oval_height = arc_chord * z_factor
    # Calculate y-offsets for the upper and lower slices
    offset = oval_height / 2
    oval_y_plus = -offset + apothem * y_factor
    oval_y_minus = -offset - apothem * y_factor

    # Draw upper and lower slices
    oval(-arc_chord / 2, oval_y_plus, arc_chord, oval_height)
    oval(-arc_chord / 2, oval_y_minus, arc_chord, oval_height)

# Drawing Functions
def setup_canvas():
    size(CANVAS_SIZE, CANVAS_SIZE)
    fill(*COLOR_BACK)
    rect(0, 0, width(), height())

def draw_background():
    fill(*COLOR_CIRCLE_FILL)
    oval(-RADIUS, -RADIUS, DIAMETER, DIAMETER)

def draw_axes(y_factor):
    stroke(*COLOR_AXIS)
    lineCap("round")
    line((0, RADIUS * y_factor), (0, -RADIUS * y_factor))

def draw_slices(y_factor, z_factor):
    stroke(*COLOR_SLICES)
    fill(None)
    if SEGMENTATION_PERIMETER:
        # Divide 90° into equal parts for each slice in the hemisphere
        for i in range(SLICE_COUNT_PER_HALF):
            angle = 90 / SLICE_COUNT_PER_HALF * (i + 1)
            apothem_normalized = calc_triangle_side_B(1, 90, angle)
            draw_slice(apothem_normalized, y_factor, z_factor)
    else:
        slice_height = 1 / SLICE_COUNT_PER_HALF
        for i in range(SLICE_COUNT_PER_HALF):
            draw_slice(slice_height * i, y_factor, z_factor)

def draw_outline():
    stroke(*COLOR_CIRCLE_OUTLINE)
    fill(None)
    oval(-RADIUS, -RADIUS, DIAMETER, DIAMETER)

def save_output():
    slice_count_total = SLICE_COUNT_PER_HALF * 2
    filename = f"sphere_{slice_count_total}s_{CAMERA_PITCH}p_{CAMERA_ROLL}r.svg"
    directory = "~/Desktop/SphereBuilder/"
    path = directory + filename
    saveImage(path, antiAliasing=True)

def main():
    setup_canvas()
    # Calculate perspective factors using the helper for sine in degrees
    y_factor = calc_triangle_side_B(1, 90, CAMERA_PITCH)
    z_factor = calc_triangle_side_C(1, 90, CAMERA_PITCH)

    with savedState():
        strokeWidth(STROKE_WEIGHT)
        translate(width() / 2, height() / 2)
        rotate(CAMERA_ROLL)
        draw_background()
        draw_axes(y_factor)
        draw_slices(y_factor, z_factor)
        draw_outline()
    save_output()

# Run the program
main()