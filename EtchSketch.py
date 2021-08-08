"""

This script creates a Turtle object that walks in the direction
you choose.

This script requires that 'turtle' be installed within the Python
environment you are running this script in.

"""

from turtle import Turtle, Screen
tim = Turtle()


def move_forward():

    tim.forward(distance=10)


def move_backward():

    tim.backward(distance=10)


def turn_clockwise():

    tim.right(angle=5)


def turn_counterclockwise():

    tim.left(angle=5)


screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key='s', fun=move_backward)
screen.onkeypress(key='d', fun=turn_clockwise)
screen.onkeypress(key='a', fun=turn_counterclockwise)
screen.onkey(key='c', fun=screen.reset)
screen.exitonclick()
