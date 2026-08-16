from textwrap import dedent

import svg

from supernote_manta import MM, SCREEN_WIDTH, SCREEN_HEIGHT, border
from utils import generate_grid, generate_dot_grid


grid_size = 3.5 * MM
grid_width = int(SCREEN_WIDTH // grid_size)
grid_height = int(SCREEN_HEIGHT // grid_size)
dash_unit = grid_size / 18

top_corner = (
    (SCREEN_WIDTH - grid_width * grid_size) / 2,
    (SCREEN_HEIGHT - grid_height * grid_size) / 2,
)



canvas = svg.SVG(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT,
    elements=[
        # Grid
        generate_grid(
            top_corner[0],
            top_corner[1],
            grid_size,
            grid_width,
            grid_height,
            enable_border=True,
            stroke="#AAAAAA",
            stroke_dasharray=[dash_unit * 2, dash_unit * 2, dash_unit * 2, 0],
        ),
        # Four line partitions
        *[
                svg.Path(
                    stroke="#888888",
                    fill="none",
                    stroke_width=2,
                    d=[
                        svg.M(
                            x=top_corner[0] + (2 * grid_size),
                            y=top_corner[1] + (4 * grid_size) + (i * grid_size * 5) + (j * grid_size),
                        ),
                        # Draw across until about few grid_size from edge of Screen
                        svg.h(SCREEN_WIDTH - (grid_size * 4)),
                    ],
                )
            # Two loops for number of lines in a bunch, and how many bunches
            for j in range(0,4)
                for i in range(0,11)
        ],
        # Vertical Section Lines
        *[
            svg.Path(
                stroke="#888888",
                fill="none",
                stroke_width=2,
                d=[
                    svg.M(
                        x=top_corner[0] + (6 * grid_size) + (i * grid_size * 7),
                        y=top_corner[1] + 4 * grid_size,
                    ),
                # Draw down until about few grid_size from edge of Screen
                svg.v(SCREEN_HEIGHT - (grid_size * 8)),
                ],
            )
            for i in range(0,6)
        ],
    ],
)

print(canvas)
