from pathlib import Path
from tkinter import *
from PIL import Image, ImageTk



pinkish_red = "#F5333F"
darkish_blue = "#12284C"
light_greyish = "#EBEBEB"



class LoadPage(Frame):
    
    def __init__(self, parent, controller, fronttoback):
        Frame.__init__(self, parent)

        self.controller = controller
        self.fronttoback = fronttoback

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.topbanner = Label(self, width = self.screen_width, height = 100, bg = "black")
        self.topbanner.place(x = 0, y = 0)

        self.maintext = Label(self, text = "Extracting data, please wait...", fg = "white", bg = "black", font = ('Verdana', 40, "bold"))
        self.maintext.place(x = (self.screen_width-self.maintext.winfo_reqwidth())/2, y = (self.screen_height-self.maintext.winfo_reqheight())/2)