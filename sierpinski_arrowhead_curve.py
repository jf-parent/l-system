#!/usr/bin/env python

from l_system import render_l_system

def main():
    axiom = "w=F"
    rules = [
        "F->G+F+G",
        "G->F-G-F"
    ]
    iterations = 8
    segment_length = 5
    alpha_zero = 60
    angle = 60
    render_l_system(rules, axiom, iterations, segment_length, alpha_zero, angle)


if __name__ == "__main__":
    main()
