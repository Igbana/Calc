from tkinter.constants import END


class Controller:
    def __init__(self, widget):
        self.widget = widget
        self.checkEmpty()
    def appendVal(self, val):
        self.val = val
        self.widget.insert(len(self.widget.get()), self.val)
        self.checkEmpty()
    def delVal(self):
        self.widget.insert(len(self.widget.get())-1, END)
        self.checkEmpty()
    def solve(self, cleanString):
        pass
    def checkEmpty(self):
        if self.widget.get() == '':
            self.disp.insert(0, "0")
