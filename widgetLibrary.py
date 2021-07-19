import tkinter as tk

class FourButtonWidget(tk.Frame):
    def __init__(self, master, textList, frameSide = None):
        super().__init__(master)

        frame = tk.Frame(master, width = 150, height = 200)

        # frameに4つのボタンを配置
        tk.Button(frame, text = textList[0], width = 3).pack(side = tk.LEFT)
        tk.Button(frame, text = textList[1], width = 3).pack(side = tk.RIGHT)
        tk.Button(frame, text = textList[2], width = 3).pack(side = tk.TOP)
        tk.Button(frame, text = textList[3], width = 3).pack(side = tk.BOTTOM)

        frame.pack(side = frameSide, ipadx = 10, ipady = 10)

class EightButtonWidget(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # leftFrameにdirectionButtonを配置
        directionButtonTextList = ['←', '→', '↑', '↓']
        leftFrame = tk.Frame(master, width = 150, height = 50)
        directionButtonList = FourButtonWidget(leftFrame, directionButtonTextList)

        # rightFrameにdirectionButtonを配置
        actionButtonTextList = ['Y', 'A', 'X', 'B']
        rightFrame = tk.Frame(master, width = 150, height = 50)
        actionButtonList = FourButtonWidget(rightFrame, actionButtonTextList)
        leftFrame.pack(side = tk.LEFT)
        rightFrame.pack(side = tk.RIGHT)

