from tkinter import *

class View(Tk):

    def __init__(self):
        Tk.__init__(self)
        #self.callback = callback

        self.title("Calculator")
        self.geometry('460x300')
        self.enter = Entry(master=self)
        self.enter.grid(row = 0, column = 0, rowspan = 4)

        # buttons
        # modulo
        b_01 = Button(self, text= "%")
        b_01.grid(row = 0, column = 1)
        b_11 = Button(self, text = "CE")
        b_11.grid(row = 1, column = 1)