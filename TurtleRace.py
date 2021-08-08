"""

This script creates multiple Turtle object that walks in
random forward movements to simulate a race.

This script requires that 'turtle' be installed within the Python
environment you are running this script in.

"""

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet.', prompt='Which turtle will win the race? Enter a color:')
colors = ['red', 'blue', 'yellow', 'orange', 'purple', 'green']

x_position = -230
y_position = -125
turtle_list = []

for _ in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[_])
    new_turtle.penup()
    new_turtle.goto(x=x_position, y=y_position)
    y_position += 25
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'You win! The winner was {winning_color}')
            else:
                print(f'You lose! The winner was {winning_color}.')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()