import magic
from pathlib import Path
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
from tkinterdnd2 import *
from mainpage import MainPage
from infopage import InfoPage
from viewpage import ViewPage
from loadpage import LoadPage
from fronttoback import Frontoback
#from new_integ import main



pinkish_red = "#F5333F"
darkish_blue = "#12284C"
light_greyish = "#EBEBEB"



class UI(Tk):
    
    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        self.timer = False

        fronttoback = Frontoback()

        infopage = InfoPage(container, self, fronttoback)
        self.frames[InfoPage] = infopage
        infopage.grid(row = 0, column = 0, sticky = "nsew")

        loadpage = LoadPage(container, self, fronttoback)
        self.frames[LoadPage] = loadpage
        loadpage.grid(row = 0, column = 0, sticky = "nsew")

        viewpage = ViewPage(container, self, fronttoback, infopage)
        self.frames[ViewPage] = viewpage
        viewpage.grid(row = 0, column = 0, sticky = "nsew")

        mainpage = MainPage(container, self, fronttoback, viewpage)
        self.frames[MainPage] = mainpage
        mainpage.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame("MainPage")

    def show_frame(self, cont):

        if cont == "MainPage":
            page = MainPage
        elif cont == "InfoPage":
            page = InfoPage
            self.timer = False
        elif cont == "ViewPage":
            page = ViewPage
        else:
            page = LoadPage
            self.timer = True
        frame = self.frames[page]
        frame.tkraise()

    def check_time(self):
        if self.timer:
            self.after(3000, self.show_frame("InfoPage"))
        self.after(3000, self.check_time)

    def on_closing(self):
        if messagebox.askyesno(title = "Quit?", message = "Do you really want to quit?"):
            self.destroy()
        
                      
    
app = UI()
app.state('zoomed')
app.protocol("WM_DELETE_WINDOW", app.on_closing)
app.check_time()
app.mainloop()