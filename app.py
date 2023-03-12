import tkinter
from tkinter import ttk
import callForUser

class MyApp:

    def __init__(self):
        self.root = tkinter.Tk()
        self.user = callForUser.User()

        self.globalFrame = ttk.Frame(self.root, padding=20)
        self.globalFrame.grid(row=0, column=0, sticky='nsew')

        self.root.grid_rowconfigure(0, minsize=200, weight=1)
        self.root.grid_columnconfigure(0, minsize=200, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.root.mainloop()

    def getNewUser(self):
        self.user = callForUser.User()

if __name__ == "__main__":
    app = MyApp()