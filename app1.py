import tkinter as tk
from widgetLibrary import FourButtonWidget

directionButtonTextList = ['←', '→', '↑', '↓']
actionButtonTextList = ['Y', 'A', 'X', 'B']

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x400')

    FourButtonWidget(root, directionButtonTextList, tk.LEFT)
    FourButtonWidget(root, actionButtonTextList, tk.RIGHT)

    root.mainloop()

