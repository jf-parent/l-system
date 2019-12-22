#!/usr/bin/env python

from l_system import render_l_system

def main():
    rules = [
        "X->F-[[X]+X]+F[+FX]-X",
        "F->FF"
    ]
    axiom = "w=X"
    iterations = 5
    segment_length = 5
    alpha_zero = 90
    angle = 22.5
    render_l_system(rules, axiom, iterations, segment_length, alpha_zero, angle)


if __name__ == "__main__":
    main()
