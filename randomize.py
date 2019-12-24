#!/usr/bin/env python

import random
from l_system import render_l_system

def main():
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
    print('rules=', rules)
    print('axiom=', axiom)
    print('iterations=', iterations)
    print('segment_length=', segment_length)
    print('alpha_zero=', alpha_zero)
    print('angle=', angle)
    render_l_system(rules, axiom, iterations, segment_length, alpha_zero, angle)


if __name__ == "__main__":
    main()
