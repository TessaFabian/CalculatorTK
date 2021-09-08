from tkinter import *

class View(Tk):

    def __init__(self, callback):
        Tk.__init__(self)
        self.callback = callback

        self.title("Calculator")
        self.label = Label(master=self, text="Calculator")
        self.label.place(x=20,y=20)