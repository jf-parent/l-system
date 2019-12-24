#!/usr/bin/env python

from l_system import render_l_system

def main():
    axiom = "w=X"
    rules = [
        "X->F+[[X]-X]-F[-FX]+X",
        "F->FF"
    ]
    iterations = 6
    segment_length = 5
    alpha_zero = 90
    angle = 25
    render_l_system(rules, axiom, iterations, segment_length, alpha_zero, angle)


if __name__ == "__main__":
    main()
