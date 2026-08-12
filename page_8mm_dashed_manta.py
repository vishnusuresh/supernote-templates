from textwrap import dedent

import svg

from supernote_manta import MM, SCREEN_WIDTH, SCREEN_HEIGHT, border
from utils import generate_grid, generate_dot_grid


grid_size = 8.0 * MM
grid_width = int(SCREEN_WIDTH // grid_size) + 1
grid_height = int(SCREEN_HEIGHT // grid_size) + 1
offset_line = 4
dash_unit = grid_size / 18

top_corner = (
    (SCREEN_WIDTH - grid_width * 8.0 * MM) / 2,
    (SCREEN_HEIGHT - grid_height * 8.0 * MM) / 2,
)


canvas = svg.SVG(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT,
    elements=[
        # border(),
        generate_grid(
            top_corner[0],
            top_corner[1],
            grid_size,
            grid_width,
            grid_height,
            stroke="#888888",
            stroke_dasharray=[dash_unit * 2, dash_unit * 2, dash_unit * 2, 0],
        ),
    ],
)

print(canvas)
