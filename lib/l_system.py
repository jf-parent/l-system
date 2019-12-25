import turtle
from time import sleep

from . import logger

HOOKS = ['before_draw', 'before_render', 'after_render']


class LSystem(object):

    def __init__(self, rules, axiom, iterations, segment_length, alpha_zero, angle, title, debug=False, delay=0):

        # Make sure rules is a list
        if type(rules) is not list:
            self.rules = [rules]
        else:
            self.rules = rules

        self.axiom = axiom
        self.iterations = iterations
        self.segment_length = segment_length
        self.alpha_zero = alpha_zero
        self.angle = angle
        self.title = title
        self.debug = debug
        self.delay = delay
        self.system_rules = dict()

        self.configure_logger()

    def configure_logger(self):
        if self.debug:
            logger.setLevel('DEBUG')
        else:
            logger.setLevel('INFO')

    def register_hook(self, hook_type, hook_fn):
        if hook_type not in HOOKS:
            raise Exception(f'Wrong hook type: {hook_type}')

        setattr(self, hook_type, hook_fn)

    def call_hook(self, hook_type):
        try:
            return getattr(self, hook_type)(self)
        except AttributeError:
            pass
        except Exception as e:
            logger.error(f"Hook {hook_type} exception: {e}")

    def derivation(self, axiom, steps):
        derived = [axiom]
        for _ in range(steps):
            next_seq = derived[-1]
            next_axiom = [self.rule(char) for char in next_seq]
            derived.append(''.join(next_axiom))
        return derived

    def rule(self, sequence):
        if sequence in self.system_rules:
            return self.system_rules[sequence]
        return sequence

    def render(self):
        for rule in self.rules:
            key, value = rule.split("->")
            self.system_rules[key] = value

        # TODO support multi-models
        self.model = self.derivation(self.axiom, self.iterations)

        logger.debug(f"model={self.model}")
        logger.debug(f'rules={self.rules}')
        logger.debug(f'axiom={self.axiom}')
        logger.debug(f'iterations={self.iterations}')
        logger.debug(f'segment_length={self.segment_length}')
        logger.debug(f'alpha_zero={self.alpha_zero}')
        logger.debug(f'angle={self.angle}')

        self.setup_turtle()

        self.call_hook('before_render')

        if self.delay:
            self.wait()

        self.draw()

        logger.info('Drawing ended')

        self.call_hook('after_render')

        self.screen.exitonclick()

    def draw(self):
        stack = []
        for command in self.model[-1]:
            values = self.call_hook('before_draw')

            if type(values) is not dict:
                values = dict()

            _segment_length = values.get('segment_length', self.segment_length)
            _angle = values.get('angle', self.angle)

            self.turtle.pendown()

            if command in ["F", "G", "R", "L"]:
                self.turtle.forward(_segment_length)

            elif command == "f":
                self.turtle.penup()
                self.turtle.forward(_segment_length)

            elif command == "+":
                self.turtle.right(_angle)

            elif command == "-":
                self.turtle.left(_angle)

            elif command == "[":
                stack.append((self.turtle.position(), self.turtle.heading()))

            elif command == "]":
                self.turtle.penup()
                position, heading = stack.pop()
                self.turtle.goto(position)
                self.turtle.setheading(heading)

    def wait(self):
        self.screen.delay(self.delay*100)
        for _ in range(self.delay):
            self.turtle.home()

        self.screen.delay(0)

    def setup_turtle(self):
        """
        See documentation for other options: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
        """

        self.turtle = turtle.Turtle()

        sh = sw = 2000

        # Screen
        self.screen = self.turtle.getscreen()
        self.screen.bgcolor("black")
        self.screen.screensize(sw, sh)
        self.screen.title(self.title)

        # Turtle
        # self.turtle.setposition(0, 0)
        self.turtle.speed(0)
        self.turtle.setheading(self.alpha_zero)
        self.turtle.hideturtle()
        self.turtle.pencolor("white")

        return self.turtle
