import random

axiom = "w=F-+"
rules = [
    "F->F-+",
    "-->F",
    "+->-",
]
iterations = 2
segment_length = 10
alpha_zero = 0
angle = 90


def before_draw(l_system):
    return dict(
        segment_length=random.randint(1, 10),
        angle=random.randint(0, 90)
    )
