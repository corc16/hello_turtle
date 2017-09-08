import turtle
import random


COLORS = ["blue", "orange", "green", "red", "purple", "teal", "brown"]


canvas = turtle.Canvas()

gang = []
for x in range(16):
    gang.append(turtle.Turtle())
    gang[x].shape("turtle")
# change all the turtles' color
    gang[x].color(random.choice(COLORS))
# move all the turtles to a random spot
    gang[x].penup()
    gang[x].goto(random.randint(-250, 250), random.randint(-250, 250))



# EXTRA: make all of the turtles with an even index write a message


input("Press enter to quit")