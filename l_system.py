import turtle
from time import sleep

SYSTEM_RULES = {}


def derivation(axiom, steps):
    derived = [axiom]  # seed
    for _ in range(steps):
        next_seq = derived[-1]
        next_axiom = [rule(char) for char in next_seq]
        derived.append(''.join(next_axiom))
    return derived


def rule(sequence):
    if sequence in SYSTEM_RULES:
        return SYSTEM_RULES[sequence]
    return sequence


def render_l_system(rules, axiom, iterations, segment_length, alpha_zero, angle):
    if type(rules) is not list:
        rules = [rules]

    for rule in rules:
        key, value = rule.split("->")
        SYSTEM_RULES[key] = value

    model = derivation(axiom, iterations)
    print(model)

    r_turtle = set_turtle(alpha_zero)
    turtle_screen = turtle.Screen()
    turtle_screen.screensize(1500, 1500)
    sleep(5)
    draw_l_system(r_turtle, model[-1], segment_length, angle)
    turtle_screen.exitonclick()


def draw_l_system(turtle, SYSTEM_RULES, seg_length, angle):

    stack = []
    for command in SYSTEM_RULES:
        if type(seg_length) == int:
            _seg_length = seg_length
        else:
            _seg_length = seg_length()

        if type(angle) == int:
            _angle = angle
        else:
            _angle = angle()

        turtle.pd()
        if command in ["F", "G", "R", "L"]:
            turtle.forward(_seg_length)
        elif command == "f":
            turtle.pu()
            turtle.forward(_seg_length)
        elif command == "+":
            turtle.right(_angle)
        elif command == "-":
            turtle.left(_angle)
        elif command == "[":
            stack.append((turtle.position(), turtle.heading()))
        elif command == "]":
            turtle.pu()
            position, heading = stack.pop()
            turtle.goto(position)
            turtle.setheading(heading)


def set_turtle(alpha_zero):
    r_turtle = turtle.Turtle()
    r_turtle.screen.title("L-System Derivation")
    r_turtle.speed(0)
    r_turtle.setheading(alpha_zero)
    return r_turtle
