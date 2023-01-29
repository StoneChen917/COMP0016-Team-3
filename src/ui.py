import os
os.chdir(".")
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
from Backend import readfile



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

        img = ImageTk.PhotoImage(Image.open("src/Assets/Images/IFRC-logo.png").resize((110, 110)))
        self.logo = Label(image=img) 
        self.logo.image = img 
        self.logo.place(x=0, y=0) 
 
        separator = ttk.Separator(self, orient='horizontal')
        separator.place(relx=0, y=75, relwidth=1, relheight=1)

        self.label = Label(self, text="File:", font=('Arial', 13))
        self.label.pack(pady=((screen_height-280)/2,0))
 
        self.select_button =Button(self, text="Choose File", fg="black", bg="#F5333F", font=('Arial', 11), command=self.click_select)
        self.select_button.pack(pady=10)

        #self.select_label_text = "No file selected"

       # self.select_label = Label(self, text=self.select_label_text, font=('Arial', 18))
        #self.select_label.pack(pady=(0,30))

        self.upload_button = Button(self, text="Upload", fg="black", bg="#F5333F", font=('Arial', 18), command=lambda: controller.show_frame(InfoPage))

    def click_select(self):
        f = filedialog.askopenfilename()
        try:
            self.file_text = readfile.ReadFile().exec(f)
            self.select_label.config(text=f, fg='black')
            self.upload_button.pack()
        except ValueError as e:
            self.select_label.config(text="File not supported, pdf only", fg='red')
            self.upload_button.pack_forget()

    def get_text(self):
        return self.file_text


class InfoPage(Frame):

    def __init__(self, parent, controller, mainpage):
        Frame.__init__(self, parent)

        self.mainpage = mainpage

        separator = ttk.Separator(self, orient='horizontal')
        separator.place(relx=0, y=75, relwidth=1, relheight=1)

        self.label = Label(self, text="", font="Arial")
        self.label.pack(pady=(120,0))

        self.update_button = Button(self, text="Update", fg="white", bg="#F5333F", font=('Arial', 18), command=self.update_text)
        self.update_button.pack()

        self.back_arrow_photo = ImageTk.PhotoImage(Image.open("src/Assets/Images/Arrow.png").resize((51, 45)))
        self.back_button = Button(self, image=self.back_arrow_photo, borderwidth=0, command=lambda: controller.show_frame(MainPage))
        self.back_button.place(x=0, y=76)

    def update_text(self):
        print(self.mainpage.get_text())
        self.label.config(text=self.mainpage.get_text(), fg='red')
        


app = UI()
app.protocol("WM_DELETE_WINDOW", app.on_closing)
app.mainloop()