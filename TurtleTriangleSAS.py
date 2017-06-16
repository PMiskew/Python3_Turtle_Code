import turtle
import math

#Creates a turtle called bob
bob = turtle.Turtle()


a = 100
B = 60
c = 200

b = math.sqrt(a*a+c*c - 2*a*c*math.cos(math.radians(60)))

A = math.degrees(math.asin(math.sin(math.radians(B))*a/b))

C = 180 - A - B

bob.forward(a)
bob.right(180 - B)


bob.forward(c)
bob.right(180 - A)



bob.forward(b)
bob.right(180 - C)








turtle.done()