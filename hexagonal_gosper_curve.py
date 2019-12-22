#!/usr/bin/env python

from l_system import render_l_system

def main():
    rules = [
        "L->L+R++R-L--LL-R+",
        "R->-L+RR++R+L--L-R"
    ]
    axiom = "w=L"
    iterations = 4
    segment_length = 5
    alpha_zero = 60
    angle = 60
    render_l_system(rules, axiom, iterations, segment_length, alpha_zero, angle)


if __name__ == "__main__":
    main()
