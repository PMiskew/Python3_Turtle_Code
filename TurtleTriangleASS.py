import turtle
import math

bob = turtle.Turtle()
# The angle, side, side triangle (ASS) is the socially akward triangle.
# This is because given an angle side side there could be 0, 1 or two possible triangles.


A = 120
c = 40
a = 50

#Calculate C

C = math.degrees(math.asin((math.sin(math.radians(A))*c/a)))
#C = 180 - C

B = 180 - A - C

print(B)
print(C)


b = math.sqrt(a**2+c**2-2*a*c*math.cos(math.radians(B)))

bob.left(A)
bob.forward(c)

bob.left(180 + B)
bob.forward(a)

bob.setheading(180)
bob.forward(b)

turtle.done()