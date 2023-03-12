import tkinter
from tkinter import ttk
import callForUser
from PIL import ImageTk, Image


class MyApp:

    def __init__(self):
        #create the window
        self.root = tkinter.Tk()
        self.root.geometry("720x480")
        self.user = callForUser.User()
        self.picture = self.getPic()
        self.globalFrame = ttk.Frame(self.root)

        #create the canvas for the profile picture
        self.cnvs = tkinter.Canvas(self.root, width=128, height=128, bg='ivory')
        self.cnvs.pack()
        self.image_container = self.cnvs.create_image(0, 0, anchor="nw", image=self.picture)

        # info from the user
        self.nameLabel = ttk.Label(text=self.getName())
        self.nameLabel.pack()

        self.addressLabel = ttk.Label(text=self.getAddress())
        self.addressLabel.pack()

        #button fror generating an other user
        self.newUserButton = ttk.Button(self.root, text='get new user', command=lambda:self.getNewUser())
        self.newUserButton.pack()

        #mainloop
        self.root.mainloop()

    def getNewUser(self):
        self.user = callForUser.User()
        self.picture = self.getPic()
        self.cnvs.itemconfig(self.image_container, image=self.picture)
        self.nameLabel["text"] = self.getName()
        self.addressLabel["text"] = self.getAddress()

    def getPic(self):
        self.user.getUserPicture()
        return ImageTk.PhotoImage(Image.open("img.jpg"))

    def getName(self):
        return "name: "+self.user.getUserFirstName()+" "+self.user.getUserLastName()

    def getAddress(self):
        return "Address: " + str(self.user.getUserStreetNumber()) + " " + self.user.getUserStreetName()+", "+self.user.getUserCity()


if __name__ == "__main__":
    app = MyApp()
