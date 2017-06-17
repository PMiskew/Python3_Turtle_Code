import turtle
import math


bob = turtle.Turtle()

A = 70
c = 100
B = 60

C = 180 - A - B

a = math.sin(math.radians(A))*c/math.sin(math.radians(C))
b = math.sin(math.radians(B))*c/math.sin(math.radians(C))

print(A)
print(B)
print(C)
print(a)
print(b)
print(c)

bob.forward(a)
bob.right(180 - B)

bob.forward(c)
bob.right(180 - A)

bob.forward(b)
bob.right(180 - C)






turtle.done()