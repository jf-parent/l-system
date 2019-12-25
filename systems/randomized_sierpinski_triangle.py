import random

from lib import color

axiom = "w=F+G+G"
rules = [
    "F->F+G-F-G+F",
    "G->GG"
]
iterations = 6
segment_length = 5
alpha_zero = 120
angle = 120


def before_render(l_system):
    l_system.screen.colormode(255)
    l_system.turtle.penup()
    l_system.turtle.setposition(-100, 100)


def before_draw(l_system):
    l_system.turtle.pencolor(color.get_random_color())
    return dict(
        segment_length=random.randint(10, 11)
    )
