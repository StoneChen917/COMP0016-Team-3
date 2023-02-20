from pathlib import Path
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
from Backend.Integration import readfile
from tkinterdnd2 import *
from Backend.Integration import new_integ



pinkish_red = "#F5333F"
darkish_blue = "#12284C"
light_greyish = "#EBEBEB"



class UI(Tk):
    
    def __init__(self, *args, **kwargs):
        
        TkinterDnD.Tk.__init__(self, *args, **kwargs)
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

    doctext = " "
    
    def __init__(self, parent, controller):
        Frame.__init__(self,parent)

        self.screen_width = self.winfo_screenwidth() 
        self.screen_height = self.winfo_screenheight() 

        self.file_text = ""

        self.topbanner = Label(self, width = self.screen_width, height = 4, bg = "white")
        self.topbanner.place(x=0, y=0)

        logo_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/logo.png")).resize((220, 66)))
        self.logo = Label(borderwidth=0, image=logo_image) 
        self.logo.image = logo_image
        self.logo.place(x=100, y=0) 

        self.midbannerone = Label(self, width = self.screen_width, height = 10, bg = "#12284C")
        self.midbannerone.place(x=0, y=66)

        self.maintext = Label(self, text="Data Extraction App", fg="white", bg=darkish_blue, font=('Verdana', 40, "bold"))
        self.maintext.place(x=(self.screen_width-self.maintext.winfo_reqwidth())/2, y=105)

        self.midbannertwo = Label(self, width = self.screen_width, height = 60, bg = "#EBEBEB")
        self.midbannertwo.place(x=0, y=66+self.midbannerone.winfo_reqheight())

        self.upload_box_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/upload_box.png")).resize((458, 324)))
        self.upload_box_uploaded_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/upload_box_uploaded.png")).resize((458, 324)))
        self.upload_box = Button(self, image=self.upload_box_image, borderwidth=0, command=self.click_select)
        self.upload_box.image = self.upload_box_image
        self.upload_box.place(x=(self.screen_width-458)/2, y=280)
        self.upload_box.drop_target_register(DND_FILES)
        self.upload_box.dnd_bind('<<Drop>>', self.drop_file)

        self.label = Label(self, text="", font=('Arial', 13))
        self.label.pack(pady=((self.screen_height-280)/2,0))

        self.select_label_text = ""

        self.select_label = Label(self, text=self.select_label_text, font=('Arial', 18))

        self.cancel_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/cancel_button.png")).resize((190, 60)))
        self.cancel_button = Button(self, image=self.cancel_image, borderwidth=0, command=self.click_cancel)
        self.cancel_button.image = self.cancel_image

        self.upload_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/upload_button.png")).resize((190, 60)))
        self.upload_button = Button(self, image=self.upload_image, borderwidth=0, command=lambda: controller.show_frame(InfoPage))
        self.upload_button.image = self.upload_image

    def click_select(self):
        f = filedialog.askopenfilename()
        try:
            self.file_text = readfile.ReadFile().exec(f)
            file_name = f[f.rfind("/")+1:]
            self.upload_box.configure(image=self.upload_box_uploaded_image)
            self.upload_box.image = self.upload_box_uploaded_image
            self.select_label.config(text=file_name, fg='black')

            self.select_label.place(x=(self.screen_width-self.select_label.winfo_reqwidth())/2, y=330)
            self.cancel_button.place(x=(self.screen_width-self.cancel_button.winfo_reqwidth())/2, y=400)
            self.upload_button.place(x=(self.screen_width-self.upload_button.winfo_reqwidth())/2, y=490)
        except ValueError as e:
            messagebox.showerror(title="Upload failed", message="File not supported, pdf only")
            self.upload_box.configure(image=self.upload_box_image)
            self.upload_box.image = self.upload_box_image

            self.select_label.place_forget()
            self.cancel_button.place_forget()
            self.upload_button.place_forget()

    def drop_file(self, event):
        f = event.data
        if event.data.endswith(".pdf"):
            self.file_text = readfile.ReadFile().exec(f)
            file_name = f[f.rfind("/")+1:]
            self.upload_box.configure(image=self.upload_box_uploaded_image)
            self.upload_box.image = self.upload_box_uploaded_image
            self.select_label.config(text=file_name, fg='black')

            self.select_label.place(x=(self.screen_width-self.select_label.winfo_reqwidth())/2, y=330)
            self.cancel_button.place(x=(self.screen_width-self.cancel_button.winfo_reqwidth())/2, y=400)
            self.upload_button.place(x=(self.screen_width-self.upload_button.winfo_reqwidth())/2, y=490)
        else:
            messagebox.showerror(title="Upload failed", message="File not supported, pdf only")
            self.upload_box.configure(image=self.upload_box_image)
            self.upload_box.image = self.upload_box_image

            self.select_label.place_forget()
            self.cancel_button.place_forget()
            self.upload_button.place_forget()

    def click_cancel(self):
        self.upload_box.configure(image=self.upload_box_image)
        self.upload_box.image = self.upload_box_image

        self.select_label.place_forget()
        self.cancel_button.place_forget()
        self.upload_button.place_forget()

# why all three functions
    def get_text(self):
        return self.file_text
    
    def get_text(self):
        global doctext
        doctext = self.file_text
        return self.file_text
    
    def return_doctext():
        return doctext



class InfoPage(Frame):
    
    def __init__(self, parent, controller, mainpage):
        Frame.__init__(self, parent)

        self.mainpage = mainpage

        self.screen_width = self.winfo_screenwidth() 
        self.screen_height = self.winfo_screenheight() 
        
        self.topbanner = Label(self, width = self.screen_width, height = 4, bg = "white")
        self.topbanner.place(x=0, y=0)

        self.label = Label(self, text="", font="Arial")
        self.label.pack(pady=(120,0))

        self.update_button = Button(self, text="Update", fg="white", bg="#F5333F", font=('Arial', 18), command=self.update_text)
        self.update_button.pack()

        self.back_arrow_photo = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/Arrow.png")).resize((50, 50)))
        self.back_button = Button(self, image=self.back_arrow_photo, borderwidth=0, command=lambda: controller.show_frame(MainPage))
        self.back_button.place(x=0, y=76)
                
        admin0 = Frontoback.get_admin0()
        output = "Admin 0: " + admin0
        self.label = Label(self, text= output, font="Arial")
        self.label.pack(pady= 7, padx= 5, side= TOP)
        
        admin1 = Frontoback.get_admin1()
        output = "Admin 1: " + admin1
        self.label = Label(self, text= output, font="Arial")
        self.label.pack(pady= 7, padx= 5, side= TOP)
        
        admin2 = Frontoback.get_admin2()
        output = "Admin 2: " + admin2
        self.label = Label(self, text= output, font="Arial")
        self.label.pack(pady= 7, padx= 5, side= TOP)
        
        start = Frontoback.get_start()
        output = "Start Date: " + start
        self.label = Label(self, text= output, font="Arial")
        self.label.pack(pady= 7, padx= 5, side= TOP)
        
        end = Frontoback.get_end()
        output = "End Date: " + end
        self.label = Label(self, text= output, font="Arial")
        self.label.pack(pady= 7, padx= 5, side= TOP)
        
        glide = Frontoback.get_glide()
        output = "Glide Number: " + glide
        self.label = Label(self, text= output, font="Arial")
        self.label.pack(pady= 7, padx= 5, side= TOP)
        
        operationbudget = Frontoback.get_operationbudget()
        output = "Operation Budget: " + operationbudget
        self.label = Label(self, text= output, font="Arial")
        self.label.pack(pady= 7, padx= 5, side= TOP)
        
        host = Frontoback.get_host()
        output = "Host National Society: " + host
        self.label = Label(self, text= output, font="Arial")
        self.label.pack(pady= 7, padx= 5, side= TOP)


    def update_text(self):
        self.label.config(text=self.mainpage.get_text(), fg='red')
        
                      
   
class Frontoback(Frame):
    global answers
    answers = []
    
    #def getText():
     #   doctext = MainPage.return_doctext()
      #  print(doctext)
            
    def Answers(admin0, admin1, admin2, start, end, glide, operationBudget, host):
        answers.append(admin0)
        answers.append(admin1)
        answers.append(admin2)
        answers.append(start)
        answers.append(end)
        answers.append(glide)
        answers.append(operationBudget)
        answers.append(host)
        
    def get_admin0():
        x = answers[0]
        return x
    
    def get_admin1():
        x = answers[1]
        return x
    
    def get_admin2():
        x = answers[2]
        return x
    
    def get_start():
        x = answers[3]
        return x
    
    def get_end():
        x = answers[4]
        return x
    
    def get_glide():
        x = answers[5]
        return x
    
    def get_operationbudget():
        x = answers[6]
        return x
    
    def get_host():
        x = answers[7]
        return x
    

    
app = UI()
app.state('zoomed')
app.protocol("WM_DELETE_WINDOW", app.on_closing)
app.mainloop()