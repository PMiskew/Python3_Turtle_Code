import turtle
import tkinter as tk
from tkinter import IntVar, StringVar
import math

class turtleScreen():

    def __init__(self):

        self.root = tk.Tk()

        self.canvas = tk.Canvas(self.root,width = 500, height = 500)
        self.canvas.grid(row = 0, column = 0,columnspan = 4)


        self.labelAng = tk.Label(text = "Angle")
        self.labelAng.grid(row = 1, column = 0)

        self.entryAng = tk.Entry(self.root)
        self.entryAng.grid(row = 2,column = 0)


        self.labelOpp = tk.Label(text = "Opposite")
        self.labelOpp.grid(row = 1, column = 1)

        self.entryOpp = tk.Entry(self.root)
        self.entryOpp.grid(row = 2,column = 1)


        self.labelAdj = tk.Label(text = "Adjacent")
        self.labelAdj.grid(row = 1, column = 2)

        self.entryAdj = tk.Entry(self.root)
        self.entryAdj.grid(row = 2,column = 2)
        self.entryAdj.config(state = "disabled")

        self.labelHyp = tk.Label(text = "Hyponenuse")
        self.labelHyp.grid(row = 1, column = 3)

        self.entryHyp = tk.Entry(self.root)
        self.entryHyp.grid(row = 2,column = 3)

        #*************************************

        self.v = tk.IntVar()
        self.v.set(1)
        self.trigFunctionS = tk.Radiobutton(self.root, text = "Sine", variable = self.v, value = 1, command = self.sel)
        self.trigFunctionS.grid(row = 1, column = 5,sticky = "W")


        self.trigFunctionC = tk.Radiobutton(self.root, text = "Cosine", variable = self.v, value = 2,command = self.sel)
        self.trigFunctionC.grid(row = 2, column = 5,sticky = "W")

        self.trigFunctionT = tk.Radiobutton(self.root, text = "Tan", variable = self.v, value = 3,command = self.sel)
        self.trigFunctionT.grid(row = 3, column = 5,sticky = "W")


        self.buttRunMe = tk.Button(self.root,text = "RUN ME", command = self.runMe)
        self.buttRunMe.grid(row = 3, column = 0, columnspan = 4,sticky = "NESW")





        self.bob = turtle.RawTurtle(self.canvas)

        self.root.mainloop()

    def sel(self):
        selection = "You selected the option " + str(self.v.get())

        selector = str(self.v.get())

        if selector == "1":
            self.entryAdj.config(state = "disabled")
            self.entryHyp.config(state = "disabled")
            self.entryOpp.config(state = "normal")
            self.entryAng.config(state = "normal")
        elif selector == "2":
            self.entryAdj.config(state="normal")
            self.entryHyp.config(state="normal")
            self.entryOpp.config(state="disabled")
            self.entryAng.config(state = "normal")
        elif selector == "3":
            self.entryAdj.config(state="normal")
            self.entryHyp.config(state="disabled")
            self.entryOpp.config(state="normal")
            self.entryAng.config(state = "normal")


    def runMe(self):
        print("Running!")
        angle = int(self.entryAng.get())
        print(angle)




'''        
def main():

    canvas = tk.Canvas(master=None,width=500,height=500)
    canvas.pack()
    t = turtle.RawTurtle(canvas)
    t.forward(50)

    canvas.mainloop()
'''
turtleScreen()