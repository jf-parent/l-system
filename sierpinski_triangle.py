#!/usr/bin/env python

from l_system import render_l_system

def main():
    axiom = "w=F+G+G"
    rules = [
        "F->F+G-F-G+F",
        "G->GG"
    ]
    iterations = 8
    segment_length = 5
    alpha_zero = 120
    angle = 120
    render_l_system(rules, axiom, iterations, segment_length, alpha_zero, angle)


if __name__ == "__main__":
    main()
