from tkinter import *

class View(Tk):

    def __init__(self):
        Tk.__init__(self)
        #self.callback = callback

        self.title("Calculator")
        self.geometry('460x300')
        self.enter = Entry(master=self)
        self.enter.grid(row = 0, column = 0, columnspan = 6, sticky = E+W)

        # buttons
        b_10 = Button(self, text= "%")
        b_10.grid(row = 1, column = 0, sticky = E+W)
        b_11 = Button(self, text = "CE")
        b_11.grid(row = 1, column = 1, sticky = E+W)
        b_12 = Button(self, text = "C")
        b_12.grid(row = 1, column = 2, sticky = E+W)
        b_13 = Button(self, text = "<x")
        b_13.grid(row = 1, column = 3, sticky = E+W)

        b_20 = Button(self, text = "1/X")
        b_20.grid(row = 2, column = 0, sticky = E+W)
        b_21 = Button(self, text = "x^2")
        b_21.grid(row = 2, column = 1, sticky = E+W)
        b_22 = Button(self, text = "sqrt")
        b_22.grid(row = 2, column = 2, sticky = E+W)
        b_23 = Button(self, text = "/")
        b_23.grid(row = 2, column = 3, sticky = E+W)

        b_30 = Button(self, text = "7")
        b_30.grid(row = 3, column = 0, sticky = E+W)
        b_31 = Button(self, text = "8")
        b_31.grid(row = 3, column = 1, sticky = E+W)
        b_32 = Button(self, text = "9")
        b_32.grid(row = 3, column = 2, sticky = E+W)
        b_33 = Button(self, text = "X")
        b_33.grid(row = 3, column = 3, sticky = E+W)

        b_40 = Button(self, text = "4")
        b_40.grid(row = 4, column = 0, sticky = E+W)
        b_41 = Button(self, text = "5")
        b_41.grid(row = 4, column = 1, sticky = E+W)
        b_42 = Button(self, text = "6")
        b_42.grid(row = 4, column = 2, sticky = E+W)
        b_43 = Button(self, text = "-")
        b_43.grid(row = 4, column = 3, sticky = E+W)

        b_50 = Button(self, text = "1")
        b_50.grid(row = 5, column = 0, sticky = E+W)
        b_51 = Button(self, text = "2")
        b_51.grid(row = 5, column = 1, sticky = E+W)
        b_52 = Button(self, text = "3")
        b_52.grid(row = 5, column = 2, sticky = E+W)
        b_53 = Button(self, text = "+")
        b_53.grid(row = 5, column = 3, sticky = E+W)

        b_60 = Button(self, text = "+/-")
        b_60.grid(row = 6, column = 0, sticky = E+W)
        b_61 = Button(self, text = "0")
        b_61.grid(row = 6, column = 1, sticky = E+W)
        b_62 = Button(self, text = ",")
        b_62.grid(row = 6, column = 2, sticky = E+W)
        b_63 = Button(self, text = "/")
        b_63.grid(row = 6, column = 3, sticky = E+W)

