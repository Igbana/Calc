from views.screens.mainscreen import MainScreen
from views.props import dimensions
from tkinter import Tk

class MainApp(Tk):
    def __init__(self):
        super().__init__()
        self.geometry = dimensions.winGeometry
        MainScreen(self).pack()

MainApp().mainloop()