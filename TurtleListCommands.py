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
        self.ButtonUp.grid(row=1, column=1)


        self.ButtonUp = tk.Button(self.root, text = "W")
        self.ButtonUp.grid(row=1, column=1)



        self.bob = turtle.RawTurtle(self.canvas)

        self.root.mainloop()

    def runMe(self):
        print("Running!")
        angle = int(self.entryAng.get())
        print(angle)




turtleListCommands()