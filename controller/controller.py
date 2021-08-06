from tkinter.constants import END, INSERT


class Controller:
    def __init__(self):
        self.swaps = {'x':'*', '^':'**', 'MOD':'%', '√':'**0.5', }

    def appendVal(self, widget, val):
        self.val = val
        self.widget = widget
        if self.widget.get() == '0' and self.val != '.':
            self.widget.delete(0, END)
            self.widget.insert(0,self.val)
        else:
            self.widget.insert(len(self.widget.get()), self.val)

    def delVal(self, widget):
        self.widget = widget
        self.widget.delete(len(self.widget.get())-1, END)
        self.checkEmpty(self.widget)

    def clearAll(self, widget):
        self.widget = widget
        self.widget.delete(0, END)
        self.checkEmpty(self.widget)

    def curLeft(self, widget):
        self.widget = widget
        if self.widget.index(INSERT) < 0:
            self.widget.icursor(self.widget.index(INSERT)+1)

    def curRight(self, widget):
        self.widget = widget
        if self.widget.index(INSERT) > 0:
            self.widget.icursor(self.widget.index(INSERT)-1)

    def solve(self, widget):
        self.widget = widget
        self.ques = self.widget.get()
        for i in self.swaps:
            self.ques = self.ques.replace(i, self.swaps[i])
        try:
            self.answer = eval(self.ques)
            self.widget.delete(0,END)
            self.widget.insert(0, self.answer)
        except:
            print("BREAK")

    def checkEmpty(self, widget):
        self.widget = widget
        if self.widget.get() == '':
            self.widget.insert(0, "0")
