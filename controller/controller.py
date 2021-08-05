from tkinter.constants import END


class Controller:
    def __init__(self):
        pass
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
        self.widget.insert(len(self.widget.get())-1, END)
        self.checkEmpty()
    def solve(self, widget):
        self.widget = widget
        self.ques = self.widget.get()
        self.ques = self.ques.replace('x', '*')
        self.ques = self.ques.replace('^', '**')
        self.ques = self.ques.replace('MOD', '%')
        try:
            self.answer = eval(self.ques)
            self.widget.delete(0,END)
            self.widget.insert(0, self.answer)
        except:
            print("BREAK")

    def checkEmpty(self, widget):
        self.widget = widget
        if self.widget.get() == '':
            self.disp.insert(0, "0")
