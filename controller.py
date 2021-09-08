from model import *
from view import *

class Controller(object):
    def __init__(self):
        self.view = View(self.calc)
        self.view.mainloop()

    def calc(self):
        pass

c = Controller()