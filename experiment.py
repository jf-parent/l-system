#!/usr/bin/env python

import random
from l_system import render_l_system

def main():
    rules = [
        "F->F-+FF",
        "-->F",
        "+->-",
    ]
    axiom = "w=F-+"
    iterations = 2
    segment_length = 5
    alpha_zero = 90
    angle = lambda: random.randint(45,60)
    render_l_system(rules, axiom, iterations, segment_length, alpha_zero, angle)


if __name__ == "__main__":
    main()
