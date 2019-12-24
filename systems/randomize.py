import random

# TODO randomize axiom
axiom = "w=F-+"
# TODO randomize rules
rules = [
    "F->F-+",
    "-->F",
    "+->-",
]
iterations = random.randint(2,10)
segment_length = lambda: random.randint(1,20)
alpha_zero = random.randint(0, 360)
angle = lambda: random.randint(45,60)
