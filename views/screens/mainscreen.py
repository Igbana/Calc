from tkinter import Frame, Entry, Button
from tkinter.constants import DISABLED, FLAT, RIGHT
from views.props import fonts, dimensions, colors
from controller.controller import Controller

class MainScreen(Frame):
    def __init__(self, root):
        self.backend = Controller()
        super().__init__(root, padx=dimensions.framePadx, pady=dimensions.framePady)
        self.dspFrame = Frame(self)
        self.trgFrame = Frame(self, padx=dimensions.framePadx, pady=dimensions.framePady)
        self.mthFrame = Frame(self, padx=dimensions.framePadx, pady=dimensions.framePady)

        self.dspFrame.grid(row=0, columnspan=2)
        self.trgFrame.grid(row=1, column=0)
        self.mthFrame.grid(row=1, column=1)

        self.disp = Entry(
            self.dspFrame,
            borderwidth=dimensions.dispBrdWidth,
            border=dimensions.dispBrdWidth,
            width=dimensions.dispWidth,
            relief=FLAT,
            bg=colors.dispBg,
            justify=RIGHT,
            font=fonts.dispFont)

        self.disp.insert(0, "0")

        self.disp.grid(
            padx=dimensions.dispPadx,
            ipadx=dimensions.dispInnerPadx,
            pady=dimensions.dispPady,
            ipady=dimensions.dispInnerPady)


        self.mthBtnLst = [
            ['7','8','9','/'],
            ['4','5','6','x'],
            ['1','2','3','-'],
            ['.','0','' ,'+'],
            ['(',')','=','' ]]

        self.trgBtnLst = [
            [ 'C' ,'DEL', '←' ,'→'],
            ['nPr','nCr','PI' ,'^'],
            ['sin','cos','tan','%'],
            ['ln' ,'log', 'E' ,'!'],
            ['e^' ,'MOD','1/x','√']]

        self.opers = '+-x/'
        self.cmdBtns = {
            'C': lambda x='':self.backend.clearAll(self.disp),
            '←': lambda x='':self.backend.curLeft(self.disp),
            '→': lambda x='':self.backend.curRight(self.disp),
            'DEL': lambda x='':self.backend.delVal(self.disp),
            '=': lambda x='':self.backend.solve(self.disp)}
        
        for i in self.mthBtnLst:
            for j in i:
                if j == '+':
                    self.colspan = 1
                    self.rowspan = 2
                    self.btnWd = dimensions.dgtBtnwidth
                    self.btnHt = (dimensions.dgtBtnheight*2)+1
                    self.fg = colors.blue
                elif j == '0':
                    self.rowspan = 1
                    self.colspan = 2
                    self.btnWd = (dimensions.dgtBtnwidth*2)+2
                    self.btnHt = dimensions.dgtBtnheight
                else:
                    self.rowspan = 1
                    self.colspan = 1
                    self.btnWd = dimensions.dgtBtnwidth
                    self.btnHt = dimensions.dgtBtnheight
                if j in self.opers:
                    self.fg = colors.white
                    self.bg = colors.red
                else:
                    self.fg = colors.black
                    self.bg = colors.lightGrey
                if j == '':
                    pass
                else:
                    self.mthBtn = Button(
                        self.mthFrame,
                        text = j,
                        font=fonts.btnFont,
                        borderwidth=dimensions.btnBrdWidth,
                        height=self.btnHt, width=self.btnWd,
                        fg= self.fg,
                        bg= self.bg,
                        command=lambda x=j: self.backend.appendVal(self.disp, x)
                        )
                    self.mthBtn.grid(
                        row= self.mthBtnLst.index(i),
                        column=i.index(j),
                        rowspan=self.rowspan,
                        columnspan=self.colspan
                        )
                if j in self.cmdBtns:
                    print(self.cmdBtns[j])
                    self.mthBtn.config(command=self.cmdBtns[j], bg = colors.dispBg, fg = colors.white)


        for i in self.trgBtnLst:
            for j in i:
                self.btnWd = dimensions.dgtBtnwidth
                self.btnHt = dimensions.dgtBtnheight
                if j =='C':
                    self.bg = colors.pepper
                    self.fg = colors.white
                else:
                    self.bg = colors.darkGrey
                    self.fg = colors.white
                if j == '':
                    pass
                else:
                    self.trgBtn = Button(
                        self.trgFrame,
                        text = j,
                        font=fonts.btnFont,
                        borderwidth=dimensions.btnBrdWidth,
                        height=self.btnHt, width=self.btnWd,
                        fg= self.fg,
                        bg= self.bg,
                        command=lambda x=j: self.backend.appendVal(self.disp)
                        )
                    self.trgBtn.grid(
                        row= self.trgBtnLst.index(i),
                        column=i.index(j),
                        rowspan=self.rowspan,
                        columnspan=self.colspan
                        )
                if j in self.cmdBtns:
                    print(self.cmdBtns[j])
                    self.trgBtn.config(command=self.cmdBtns[j])