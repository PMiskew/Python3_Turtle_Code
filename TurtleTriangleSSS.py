import turtle
import math

bob = turtle.Turtle()


a = 100
b = 120
c = 200


A = math.degrees(math.acos((b*b + c*c - a*a)/(2*b*c)))

B = math.degrees(math.acos((a*a + c*c - b*b)/(2*a*c)))

C = 180 - A - B

print(A)
print(B)
print(C)

bob.forward(a)
bob.right(180 - B)

bob.forward(c)
bob.right(180 - A)

bob.forward(b)
bob.right(180 - C)

turtle.done()