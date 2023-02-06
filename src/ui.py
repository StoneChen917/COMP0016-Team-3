import os
os.chdir(".")
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
from Backend import readfile



pinkish_red = "#F5333F"
darkish_blue = "#12284C"



class UI(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        mainpage = MainPage(container, self)
        self.frames[MainPage] = mainpage
        mainpage.grid(row=0, column=0, sticky="nsew")

        infopage = InfoPage(container, self, mainpage)
        self.frames[InfoPage] = infopage
        infopage.grid(row=0, column=0, sticky="nsew")


        self.show_frame(MainPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def on_closing(self):
        if messagebox.askyesno(title = "Quit?", message = "Do you really want to quit?"):
            self.destroy()

        
class MainPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        screen_width = self.winfo_screenwidth() 
        screen_height = self.winfo_screenheight() 

        self.file_text = ""

        self.topbanner = Label(self, width = screen_width, height = 4, bg = "white")
        self.topbanner.place(x=0, y=0)

        img = ImageTk.PhotoImage(Image.open("Assets/Images/logo.png").resize((220, 66)))
        self.logo = Label(borderwidth=0, image=img) 
        self.logo.image = img 
        self.logo.place(x=100, y=0) 

        self.midbannerone = Label(self, width = screen_width, height = 10, bg = "#12284C")
        self.midbannerone.place(x=0, y=66)

        self.maintext = Label(self, text="Data Extraction App", fg="white", bg=darkish_blue, font=('Verdana', 40, "bold"))
        print(screen_width, " ", self.maintext.winfo_width())
        self.maintext.place(x=(screen_width-self.maintext.winfo_reqwidth())/2, y=105)
 
        # separator = ttk.Separator(self, orient='horizontal')
        # separator.place(relx=0, y=75, relwidth=1, relheight=1)

        self.midbannertwo = Label(self, width = screen_width, height = 60, bg = "#EBEBEB")
        self.midbannertwo.place(x=0, y=66+self.midbannerone.winfo_reqheight())

        self.label = Label(self, text="", font=('Arial', 13))
        self.label.pack(pady=((screen_height-280)/2,0))
 
        self.select_button_border = Frame(self, highlightbackground = darkish_blue, 
                        highlightthickness = 2, bd=0)
        self.select_button =Button(self.select_button_border, text="Choose File", fg=darkish_blue, 
                        bg="#EBEBEB", font=('Verdaba', 15), borderwidth=0, command=self.click_select)
        self.select_button.pack(padx=20, pady=4)
        self.select_button_border.pack()

        self.select_label_text = "No file selected"

        self.select_label = Label(self, text=self.select_label_text, font=('Arial', 18))
        self.select_label.pack(pady=30)

        self.upload_button_border = Frame(self, highlightbackground = darkish_blue, 
                        highlightthickness = 2, bd=0)
        self.upload_button = Button(self.upload_button_border, text="Upload", fg=darkish_blue, 
                        bg="#EBEBEB", font=('Verdana', 15), borderwidth=0, command=lambda: controller.show_frame(InfoPage))

    def click_select(self):
        f = filedialog.askopenfilename()
        try:
            self.file_text = readfile.ReadFile().exec(f)
            self.select_label.config(text=f, fg='black')
            self.upload_button.pack(padx=37, pady=2)
            self.upload_button_border.pack()
        except ValueError as e:
            self.select_label.config(text="File not supported, pdf only", fg='red')
            self.upload_button.pack_forget()
            self.upload_button_border.pack_forget()

    def get_text(self):
        return self.file_text


class InfoPage(Frame):

    def __init__(self, parent, controller, mainpage):
        Frame.__init__(self, parent)

        self.mainpage = mainpage

        self.label = Label(self, text="", font="Arial")
        self.label.pack(pady=(120,0))

        self.update_button = Button(self, text="Update", fg="white", bg="#F5333F", font=('Arial', 18), command=self.update_text)
        self.update_button.pack()

        self.back_arrow_photo = ImageTk.PhotoImage(Image.open("Assets/Images/Arrow.png").resize((51, 45)))
        self.back_button = Button(self, image=self.back_arrow_photo, borderwidth=0, command=lambda: controller.show_frame(MainPage))
        self.back_button.place(x=0, y=76)

    def update_text(self):
        self.label.config(text=self.mainpage.get_text(), fg='red')
        


app = UI()
app.protocol("WM_DELETE_WINDOW", app.on_closing)
app.mainloop()