import turtle
import math

bob = turtle.Turtle()




r = 100
n = 64
angle = (180 * (n-2))/n
offset = angle #Must store this to alight all other shapes
print(angle)
side = 2*(r*math.cos(math.radians(angle/2)))
print(side)

for i in range(0,n,1):

    bob.right(180 - angle)
    bob.forward(side)


bob.setheading(0)

while n > 4:
    r = 100
    n = n//2

    angle = (180 * (n-2))/n
    print(angle)

    side = 2*(r*math.cos(math.radians(angle/2)))
    print(side)

    bob.left((offset-angle)/2)
    for i in range(0,n,1):

        bob.right(180 - angle)
        bob.forward(side)

    bob.setheading(0)

'''
r = 100
n = 4
angle = (180 * (n-2))/n
print(angle)
side = 2*(r*math.cos(math.radians(angle/2)))
print(side)

bob.left(67.5/2)
for i in range(0,n,1):

    bob.right(180 - angle)
    bob.forward(side)

bob.setheading(0)
'''


turtle.done()