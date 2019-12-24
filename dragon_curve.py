#!/usr/bin/env python

from l_system import render_l_system

# TODO debug
def main():
    axiom = "w=FX"
    rules = [
        "X->X+YF+",
        "Y->−FX−Y"
    ]
    iterations = 10
    segment_length = 5
    alpha_zero = 90
    angle = 90
    render_l_system(rules, axiom, iterations, segment_length, alpha_zero, angle)


if __name__ == "__main__":
    main()
