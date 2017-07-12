import turtle
import tkinter as tk
from tkinter import IntVar, StringVar
import math

class turtleListCommands():

    def __init__(self):

        self.root = tk.Tk()

        self.canvas = tk.Canvas(self.root,width = 500, height = 500)
        self.canvas.grid(row = 0, column = 0,columnspan = 4)


        self.labelDistance = tk.Label(text = "Distance")
        self.labelDistance.grid(row = 1, column = 0)

        self.entryDistance = tk.Entry(self.root)
        self.entryDistance.grid(row = 2,column = 0)

        self.buttonDistance = tk.Button(self.root, text = "SPACE")
        self.buttonDistance.grid(row = 2, column = 1, sticky = "W")

        self.labelAngle = tk.Label(text = "Angle")
        self.labelAngle.grid(row = 3, column = 0)

        self.entryAngle = tk.Entry(self.root)
        self.entryAngle.grid(row = 4,column = 0)

        self.buttonAngle = tk.Button(self.root, text = "SHIFT")
        self.buttonAngle.grid(row = 4, column = 1, sticky = "W")

        #*************************************
        self.ButtonUp = tk.Button(self.root, text = "W")
        self.ButtonUp.grid(row=2, column=3)
        self.root.bind("<w>", self.move)

        self.ButtonDown = tk.Button(self.root, text = "S")
        self.ButtonDown.grid(row=4, column=3)
        self.root.bind("<s>", self.move)

        self.ButtonLeft = tk.Button(self.root, text = "A",command = self.move)
        self.ButtonLeft.grid(row=3, column=2, sticky = "E")
        self.root.bind("<a>",self.move)

        self.ButtonRight = tk.Button(self.root, text = "D",command = self.move)
        self.ButtonRight.grid(row=3, column=4,sticky = "W")
        self.root.bind("<d>", self.move)

        self.bob = turtle.RawTurtle(self.canvas)

        self.root.mainloop()


    def move(self,event):
        print("LEFT")

        if event.keysym == "a":
            self.bob.setheading(180)
        elif event.keysym == "d":
            self.bob.setheading(0)
        elif event.keysym == "w":
            self.bob.setheading(90)
        elif event.keysym == "s":
            self.bob.setheading(270)

        dist = self.entryDistance.get()

        try:
            dist = int(dist)
        except ValueError:
            dist = 10

        self.bob.forward(dist)

    def runMe(self):
        print("Running!")
        angle = int(self.entryAng.get())
        print(angle)




turtleListCommands()