from manim import *


ACCENT = BLUE
MUTED = GREY_A


def bullet_rows(items, font_size=30):
    rows = VGroup()
    for item in items:
        marker = Text("•", font_size=font_size, color=ACCENT)
        label = Text(item, font_size=font_size)
        row = VGroup(marker, label).arrange(RIGHT, buff=0.3)
        marker.set_y(label.get_center()[1])
        rows.add(row)
    rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35)
    return rows


def slide_title(text, center=False):
    title = Text(text, font_size=44, weight=BOLD)
    if center:
        title.move_to(ORIGIN)
    else:
        title.to_edge(UP, buff=0.9)
    return title
