# TODO validate

import math

axiom = "w=X"
rules = [
    "F->FF",
    "X->F[+X]F[-X]+X",
]
iterations = 5
segment_length = 5
alpha_zero = 90
angle = math.pi/9
