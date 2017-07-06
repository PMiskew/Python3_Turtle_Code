import turtle
from turtle import *
import math

tur = turtle.Turtle()
screen = Screen()

def turnLeft():
    print("LEFT")
    tur.left(10)

def turnRight():
    print("RIGHT")
    tur.right(10)

def forward():
    print("FORWARD")
    tur.forward(10)

screen.onkey(turnLeft, "Left")
screen.onkey(turnRight, "Right")
screen.onkey(forward,"Up")
screen.listen()
turtle.done()