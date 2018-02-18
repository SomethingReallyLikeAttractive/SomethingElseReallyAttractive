import tkinter as tk

class Display:
    masterWindow = None
    displayer = None

    def __init__(self):
        self.masterWindow = tk.Tk()
        self.displayer = tk.Label(self.masterWindow, text = "")
        self.displayer.pack()

    def updateText(self, stringUpdate):
        self.displayer.config(text = stringUpdate)
        self.masterWindow.mainloop()

test = Display()