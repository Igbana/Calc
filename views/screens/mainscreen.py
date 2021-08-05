from tkinter import Frame, Entry, Button
from ..props import fonts, dimensions, colors

class MainScreen(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.dspFrame = Frame(self)
        self.trgFrame = Frame(self)
        self.mthFrame = Frame(self)

        self.dspFrame.grid(row=0, columnspan=2)
        self.trgFrame.grid(row=1, column=0)
        self.mthFrame.grid(row=1, column=1)

        self.mthBtnLst = [
            ['7','8','9','/'],
            ['4','5','6','x'],
            ['1','2','3','-'],
            ['.','0','' ,'+'],
            ['(',')','=','' ]
        ]

        self.trgBtnLst = [
            [ 'C' ,'DEL',''   ,'' ],
            ['nPr','nCr','PI' ,'^'],
            ['sin','cos','tan','%'],
            ['ln' ,'log', 'E' ,'!'],
            ['e^' ,'MOD','1/x','√']
        ]

        self.opers = '+-x/'

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
                    self.fg = colors.darkGrey
                if j == '':
                    pass
                else:
                    Button(
                        self,
                        text = j,
                        font=fonts.btnFont,
                        borderwidth=dimensions.btnBrdWidth,
                        height=self.btnHt, width=self.btnWd,
                        fg= self.fg,
                        bg= self.bg
                        ).grid(
                            row= self.mthBtnLst.index(i),
                            column=i.index(j),
                            rowspan=self.rowspan,
                            columnspan=self.colspan
                            )