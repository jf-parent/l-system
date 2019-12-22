import turtle

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

    r_turtle = set_turtle(alpha_zero)
    turtle_screen = turtle.Screen()
    turtle_screen.screensize(1500, 1500)
    draw_l_system(r_turtle, model[-1], segment_length, angle)
    turtle_screen.exitonclick()


def draw_l_system(turtle, SYSTEM_RULES, seg_length, angle):
    stack = []
    for command in SYSTEM_RULES:
        turtle.pd()
        if command in ["F", "G", "R", "L"]:
            turtle.forward(seg_length)
        elif command == "f":
            turtle.pu()
            turtle.forward(seg_length)
        elif command == "+":
            turtle.right(angle)
        elif command == "-":
            turtle.left(angle)
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
