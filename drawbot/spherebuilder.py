from math import sin, radians, sqrt

# Constants (Uppercase as per convention for constants)
RADIUS = 180
DIAMETER = RADIUS * 2
COLOR_BACK = (0, 0, 0.5, 1)
COLOR_CIRCLE_OUTLINE = (1, 1, 1, 1)
COLOR_CIRCLE_FILL = (1, 0, 1, 1)
COLOR_SLICES = (1, 1, 0, 1)
COLOR_AXIS = (1, 1, 0, 1)
SLICE_COUNT_PER_HALF = 3
SEGMENTATION_PERIMETER = True
CAMERA_PITCH = 30
CAMERA_ROLL = 45
STROKE_WEIGHT = 4
PADDING = STROKE_WEIGHT * 3
CANVAS_SIZE = 360 + PADDING

# Utility Functions
def calc_triangle_side_B(side_A, angle_A, angle_B):
    angle_C = angle_A - angle_B
    return side_A * sin(radians(angle_C))


def calc_triangle_side_C(side_A, angle_A, angle_B):
    return side_A * sin(radians(angle_B))


def calc_arc_chord(arc_sagitta):
    return sqrt(arc_sagitta) * sqrt(2 * RADIUS - arc_sagitta) * 2


def draw_slice(apothem_normalized, y_factor, z_factor):
    apothem = RADIUS * apothem_normalized
    sagitta = RADIUS - apothem
    arc_chord = calc_arc_chord(sagitta)
    oval_height = arc_chord * z_factor
    oval_y_offset_plus = -oval_height / 2 + apothem * y_factor
    oval_y_offset_minus = -oval_height / 2 - apothem * y_factor

    oval(-arc_chord / 2, oval_y_offset_plus, arc_chord, oval_height)
    oval(-arc_chord / 2, oval_y_offset_minus, arc_chord, oval_height)


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


# Main
def main():
    setup_canvas()
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
