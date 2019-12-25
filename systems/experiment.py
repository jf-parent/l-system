import random

rules = [
    "F->F-+FF",
    "-->F",
    "+->-",
]
axiom = "w=F-+"
iterations = 2
segment_length = 5
alpha_zero = 90
angle = lambda: random.randint(45, 60)
