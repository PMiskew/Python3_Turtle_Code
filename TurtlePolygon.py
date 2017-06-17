import turtle
import math

bob = turtle.Turtle()


n = 80
side = 3


angle = (180 * (n-2))/n


print(angle)


for i in range(0,n,1):

    bob.right(180 - angle)
    bob.forward(side)

turtle.done()


