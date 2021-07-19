import tkinter as tk
from widgetLibrary import EightButtonWidget

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('800x400')

    EightButtonWidget(root)

    root.mainloop()

