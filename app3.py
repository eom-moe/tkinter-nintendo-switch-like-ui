import tkinter as tk
from widgetLibrary import FourButtonWidget

directionButtonTextList = ['←', '→', '↑', '↓']
actionButtonTextList = ['Y', 'A', 'X', 'B']

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('400x400+300+100')

    directionButtonWindow = tk.Toplevel()
    directionButtonWindow.geometry('200x100+100+500')
    FourButtonWidget(directionButtonWindow, directionButtonTextList)

    actionButtonWindow = tk.Toplevel()
    actionButtonWindow.geometry('200x100+700+500')
    FourButtonWidget(actionButtonWindow, actionButtonTextList)

    root.mainloop()

