#!/usr/bin/env python

from l_system import render_l_system


def main():
    rule = "F->F-F+F+FF-F-F+F"
    axiom = "w=F-F-F-F"
    iterations = 2
    segment_length = 5
    alpha_zero = 90
    angle = 90
    render_l_system(rule, axiom, iterations, segment_length, alpha_zero, angle)


if __name__ == "__main__":
    main()
