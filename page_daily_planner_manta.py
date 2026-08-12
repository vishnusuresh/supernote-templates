from textwrap import dedent

import svg

from supernote_manta import MM, SCREEN_WIDTH, SCREEN_HEIGHT, border
from utils import generate_grid, generate_dot_grid


grid_size = 6.0 * MM
grid_width = int(SCREEN_WIDTH // grid_size)
grid_height = int(SCREEN_HEIGHT // grid_size)
offset_line = 4
dash_unit = grid_size / 18

top_corner = (
    (SCREEN_WIDTH - grid_width * grid_size) / 2,
    (SCREEN_HEIGHT - grid_height * grid_size) / 2,
)

text_spacing = 10 * grid_size / 7


canvas = svg.SVG(
    width=SCREEN_WIDTH,
    height=SCREEN_HEIGHT,
    elements=[
        # border(),
        # Bottom half grid
        generate_grid(
            top_corner[0],
            top_corner[1] + 4 * grid_size,
            grid_size,
            grid_width,
            grid_height - 4,
            enable_border=False,
            stroke="#888888",
            # stroke_dasharray=[0.375 * MM, 0.25 * MM, 0.375 * MM, 0 * MM],
            # stroke_dasharray=[0.5 * MM, 0.25 * MM, 0.5 * MM, 0 * MM],
            stroke_dasharray=[dash_unit * 2, dash_unit * 2, dash_unit * 2, 0],
        ),
        # Middle vertical grid
        generate_grid(
            top_corner[0] + 7 * grid_size,
            top_corner[1],
            grid_size,
            1,
            4,
            stroke_width=2,
            # stroke_dasharray=[0.375 * MM, 0.25 * MM, 0.375 * MM, 0 * MM],
            # stroke_dasharray=[0.5 * MM, 0.25 * MM, 0.5 * MM, 0 * MM],
            # stroke_dasharray=[dash_unit * 1, dash_unit * 1, dash_unit * 1, 0],
        ),
        # Top right area
        generate_grid(
            top_corner[0] + 8 * grid_size,
            top_corner[1],
            grid_size,
            grid_width - 8,
            4,
            enable_border=False,
            stroke="#888888",
            # stroke_dasharray=[0.375 * MM, 0.25 * MM, 0.375 * MM, 0 * MM],
            # stroke_dasharray=[0.5 * MM, 0.25 * MM, 0.5 * MM, 0 * MM],
            stroke_dasharray=[dash_unit * 2, dash_unit * 2, dash_unit * 2, 0],
        ),
        # Top left blank area
        svg.Path(
            stroke="#000000",
            fill="none",
            stroke_width=1,
            d=[
                svg.M(
                    x=top_corner[0],
                    y=top_corner[1] + 4 * grid_size,
                ),
                svg.h(grid_size * grid_width),
            ],
        ),
        svg.Text(
            font_size= 3 * MM,
            font_family="Monaco",
            fill= "#666666",
            dominant_baseline="middle",
            elements=[
                svg.TSpan(
                    text_anchor="middle",
                    x=top_corner[0] + (3.5 * grid_size),
                    y=top_corner[1] + (1 * grid_size),
                    text="DATE : __________________",
                )
                #for (i, day) in enumerate(6, 8, 10, 12, 14, 16, 18, 20)
                #for (i, time) in enumerate(("06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"))
                #for (i, time) in enumerate(("06:00", "08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"))
            ],
        ),
        # Offset Line
        svg.Path(
            stroke="#000000",
            fill="none",
            stroke_width=2,
            d=[
                svg.M(
                    x=top_corner[0] + offset_line * grid_size,
                    y=top_corner[1] + 4 * grid_size,
                ),
                svg.v(grid_size * grid_height),
            ],
        ),
        # Centre Line
        svg.Path(
            stroke="#000000",
            fill="none",
            stroke_width=2,
            d=[
                svg.M(
                    x=top_corner[0] + 4 * grid_size,
                    y=top_corner[1] + 18 * grid_size,
                ),
                svg.h(grid_size * grid_height),
            ],
        ),
        svg.Text(
            font_size= 3 * MM,
            font_family="Monaco",
            fill= "#CCCCCC",
            dominant_baseline="middle",
            elements=[
                svg.TSpan(
                    text_anchor="middle",
                    x=top_corner[0] + 2 * grid_size,
                    y=top_corner[1] + (7.75 * grid_size) + (i * grid_size * 4),
                    text=time,
                )
                for (i, time) in enumerate(("08:00", "10:00", "12:00", "14:00", "16:00", "18:00", "20:00"))
            ],
        ),
    ],
)

print(canvas)
