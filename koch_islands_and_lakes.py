#!/usr/bin/env python

from l_system import render_l_system

def main():
    rules = [
        "F->F+f-FF+F+FF+Ff+FF-f+FF-F-FF-Ff-FFF",
        "f->ffffff"
    ]
    axiom = "w=F+F+F+F"
    iterations = 2
    segment_length = 5
    alpha_zero = 90
    angle = 90
    render_l_system(rules, axiom, iterations, segment_length, alpha_zero, angle)


if __name__ == "__main__":
    main()
