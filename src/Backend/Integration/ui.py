import magic
from pathlib import Path
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
from tkinterdnd2 import *
from readfile import ReadFile
from new_integ import main



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

        fronttoback = Frontoback()

        infopage = InfoPage(container, self, fronttoback)
        self.frames[InfoPage] = infopage
        infopage.grid(row=0, column=0, sticky="nsew")

        mainpage = MainPage(container, self, fronttoback, infopage)
        self.frames[MainPage] = mainpage
        mainpage.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def on_closing(self):
        if messagebox.askyesno(title = "Quit?", message = "Do you really want to quit?"):
            self.destroy()



class MainPage(Frame):

    doctext = " "
    
    def __init__(self, parent, controller, fronttoback, infopage):
        Frame.__init__(self,parent)

        self.controller = controller

        self.fronttoback = fronttoback
        self.infopage = infopage

        self.screen_width = self.winfo_screenwidth() 
        self.screen_height = self.winfo_screenheight()

        self.topbanner = Label(self, width = self.screen_width, height = 4, bg = "white")
        self.topbanner.place(x=0, y=0)

        logo_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/logo.png")).resize((220, 66)))
        self.logo = Label(borderwidth=0, image=logo_image) 
        self.logo.image = logo_image
        self.logo.place(x=100, y=0) 

        self.info_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/info.png")).resize((60, 60)))
        self.info_button = Button(self, image = self.info_image, borderwidth = 0, bg = "white", command = self.click_info)
        self.info_button.image = self.info_image
        self.info_button.place(x = self.screen_width-63, y = 3)
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
        self.upload_button = Button(self, image=self.upload_image, borderwidth=0, command=self.click_upload)
        self.upload_button.image = self.upload_image

    def click_upload(self):
        self.update_info_page()
        self.controller.show_frame(InfoPage)

    def click_info(self):
        messagebox.showinfo(title = "Info", 
                                message = "1.Upload your file by drag and drop, or select from folders. (pdf only)\n2.Check if the informations are correct and push it to the database.")

    def update_info_page(self):
        self.fronttoback.extract_answers()
        self.infopage.update()

    def upload_success(self, f):
        file_name = f[f.rfind("/")+1:]
        self.fronttoback.set_file_name(f)
        self.upload_box.configure(image = self.upload_box_uploaded_image)
        self.upload_box.image = self.upload_box_uploaded_image
        self.select_label.config(text = file_name, fg = 'black')

        self.select_label.place(x = (self.screen_width-self.select_label.winfo_reqwidth())/2, y = 330)
        self.cancel_button.place(x = (self.screen_width-self.cancel_button.winfo_reqwidth())/2, y = 400)
        self.upload_button.place(x = (self.screen_width-self.upload_button.winfo_reqwidth())/2, y = 490)

    def upload_failure(self):
        messagebox.showerror(title = "Upload failed", message = "File not supported, pdf only")
        self.upload_box.configure(image = self.upload_box_image)
        self.upload_box.image = self.upload_box_image

        self.select_label.place_forget()
        self.cancel_button.place_forget()
        self.upload_button.place_forget()

    def click_select(self):
        f = filedialog.askopenfilename()
        if "PDF document" in magic.from_file(f):
            self.upload_success(f)
        else:
            self.upload_failure(f)

    def drop_file(self, event):
        f = event.data
        if "PDF document" in magic.from_file(f):
            self.upload_success(f)
        else:
            self.upload_failure(f)

    def click_cancel(self):
        self.upload_box.configure(image=self.upload_box_image)
        self.upload_box.image = self.upload_box_image

        self.select_label.place_forget()
        self.cancel_button.place_forget()
        self.upload_button.place_forget()



class InfoPage(Frame):
    
    def __init__(self, parent, controller, fronttoback):
        Frame.__init__(self, parent)

        self.fronttoback = fronttoback

        self.screen_width = self.winfo_screenwidth() 
        self.screen_height = self.winfo_screenheight() 
        
        self.topbanner = Label(self, width = self.screen_width, height = 4, bg = "white")
        self.topbanner.place(x=0, y=0)

        self.label = Label(self, text="", font="Arial")
        self.label.pack(pady=(120,0))

        self.back_arrow_photo = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/Arrow.png")).resize((50, 50)))
        self.back_button = Button(self, image=self.back_arrow_photo, borderwidth=0, command=lambda: controller.show_frame(MainPage))
        self.back_button.place(x=0, y=76)

        grid_x = (self.screen_width-910)/2
        grid_y = 150
        label_width = 310
        label_height = 31
        text_width = 600
        
        self.admin0_label = Label(self, text = "Admin 0", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.admin0_label.place(x = grid_x, y = grid_y, width = label_width, height = label_height)
        self.admin0_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.admin0_text.place(x = grid_x+label_width, y = grid_y, width = text_width, height = label_height)

        self.ISO_label = Label(self, text = "ISO Code", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.ISO_label.place(x = grid_x, y = grid_y+label_height, width = label_width, height = label_height)
        self.ISO_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.ISO_text.place(x = grid_x+label_width, y = grid_y+label_height, width = text_width, height = label_height)

        self.admin1_label = Label(self, text = "Admin 1", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.admin1_label.place(x = grid_x, y = grid_y+label_height*2, width = label_width, height = label_height)
        self.admin1_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.admin1_text.place(x = grid_x+label_width, y = grid_y+label_height*2, width = text_width, height = label_height)

        self.admin2_label = Label(self, text = "Admin 2", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.admin2_label.place(x = grid_x, y = grid_y+label_height*3, width = label_width, height = label_height)
        self.admin2_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.admin2_text.place(x = grid_x+label_width, y = grid_y+label_height*3, width = text_width, height = label_height)

        self.operation_number_label = Label(self, text = "Operation number", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.operation_number_label.place(x = grid_x, y = grid_y+label_height*4, width = label_width, height = label_height)
        self.operation_number_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.operation_number_text.place(x = grid_x+label_width, y = grid_y+label_height*4, width = text_width, height = label_height)

        self.operation_start_date_label = Label(self, text = "Operation start date", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.operation_start_date_label.place(x = grid_x, y = grid_y+label_height*5, width = label_width, height = label_height)
        self.operation_start_date_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.operation_start_date_text.place(x = grid_x+label_width, y = grid_y+label_height*5, width = text_width, height = label_height)

        self.operation_end_date_label = Label(self, text = "Operation End Date", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.operation_end_date_label.place(x = grid_x, y = grid_y+label_height*6, width = label_width, height = label_height)
        self.operation_end_date_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.operation_end_date_text.place(x = grid_x+label_width, y = grid_y+label_height*6, width = text_width, height = label_height)
       
        self.glide_number_label = Label(self, text = "Glide Number", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.glide_number_label.place(x = grid_x, y = grid_y+label_height*7, width = label_width, height = label_height)
        self.glide_number_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.glide_number_text.place(x = grid_x+label_width, y = grid_y+label_height*7, width = text_width, height = label_height)
       
        self.affected_label = Label(self, text = "Number pf people affected", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.affected_label.place(x = grid_x, y = grid_y+label_height*8, width = label_width, height = label_height)
        self.affected_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.affected_text.place(x = grid_x+label_width, y = grid_y+label_height*8, width = text_width, height = label_height)
       
        self.assisted_label = Label(self, text = "Number of people assisted", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.assisted_label.place(x = grid_x, y = grid_y+label_height*9, width = label_width, height = label_height)
        self.assisted_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.assisted_text.place(x = grid_x+label_width, y = grid_y+label_height*9, width = text_width, height = label_height)
       
        self.operation_budget_label = Label(self, text = "Operation Budget", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.operation_budget_label.place(x = grid_x, y = grid_y+label_height*10, width = label_width, height = label_height)
        self.operation_budget_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.operation_budget_text.place(x = grid_x+label_width, y = grid_y+label_height*10, width = text_width, height = label_height)
       
        self.host_national_society_label = Label(self, text = "Host National Society", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.host_national_society_label.place(x = grid_x, y = grid_y+label_height*11, width = label_width, height = label_height)
        self.host_national_society_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.host_national_society_text.place(x = grid_x+label_width, y = grid_y+label_height*11, width = text_width, height = label_height)
       
        self.push_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/push_button.png")).resize((190, 60)))
        self.push_button = Button(self, image = self.push_image, borderwidth = 0, command = self.click_push)
        self.push_button.image = self.push_image
        self.push_button.place(x = (self.screen_width-self.push_button.winfo_reqwidth())/2, y = 600)

    def update(self):
        # admin 0
        self.admin0_text.delete('1.0', END)
        self.admin0_text.insert(INSERT, self.fronttoback.get_glide())
        # ISO
        self.ISO_text.delete('1.0', END)
        self.ISO_text.insert(INSERT, self.fronttoback.get_ISO())
        # Admin 1
        self.admin1_text.delete('1.0', END)
        self.admin1_text.insert(INSERT, self.fronttoback.get_admin1())
        # Admin 2
        self.admin2_text.delete('1.0', END)
        self.admin2_text.insert(INSERT, self.fronttoback.get_admin2())
        # number
        self.operation_number_text.delete('1.0', END)
        self.operation_number_text.insert(INSERT, self.fronttoback.get_operation_number())
        # start
        self.operation_start_date_text.delete('1.0', END)
        self.operation_start_date_text.insert(INSERT, self.fronttoback.get_start())
        # end
        self.operation_end_date_text.delete('1.0', END)
        self.operation_end_date_text.insert(INSERT, self.fronttoback.get_end())
        # glide
        self.glide_number_text.delete('1.0', END)
        self.glide_number_text.insert(INSERT, self.fronttoback.get_glide())
        # affected
        self.affected_text.delete('1.0', END)
        self.affected_text.insert(INSERT, self.fronttoback.get_affected())
        # assisted
        self.assisted_text.delete('1.0', END)
        self.assisted_text.insert(INSERT, self.fronttoback.get_assisted())
        # budget
        self.operation_budget_text.delete('1.0', END)
        self.operation_budget_text.insert(INSERT, self.fronttoback.get_operation_budget())
        # host
        self.host_national_society_text.delete('1.0', END)
        self.host_national_society_text.insert(INSERT, self.fronttoback.get_host())


    def click_push(self):
        None
        
                      
   
class Frontoback():
    
    def __init__(self):
        self.file_name = ""
        self.answers = {}

    def extract_answers(self):
        integ = main(self.file_name)
        answers = integ.final_extract
        self.answers = answers
    
    def set_file_name(self, name):
        self.file_name = name
            
    # def append_answers(self, admin0, admin1, admin2, start, end, glide, operationBudget, host):
    #     self.answers.append(admin0)
    #     self.answers.append(admin1)
    #     self.answers.append(admin2)
    #     self.answers.append(start)
    #     self.answers.append(end)
    #     self.answers.append(glide)
    #     self.answers.append(operationBudget)
    #     self.answers.append(host)
        
    def get_admin0(self):
        x = self.answers["Country"]
        return x

    def get_ISO(self):
        x = self.answers["ISO"]
        return x
    
    def get_admin1(self):
        x = self.answers[["Admin1"]]
        return x
    
    def get_admin2(self):
        x = self.answers["Admin2"]
        return x
    
    def get_start(self):
        x = self.answers["Start"]
        return x
    
    def get_end(self):
        x = self.answers["End"]
        return x
    
    def get_glide(self):
        x = self.answers["Glide"]
        return x
    
    def get_operation_number(self):
        x = self.answers["OpBud"]
        return x

    def get_operation_budget(self):
        x = self.answers["OpBud"]
        return x
    
    def get_host(self):
        x = self.answers["Host"]
        return x
    
    def get_affected(self):
        x = self.answers["Affected"]
        return x

    def get_assisted(self):
        x = self.answers["Assisted"]
        return x  
    
app = UI()
app.state('zoomed')
app.protocol("WM_DELETE_WINDOW", app.on_closing)
app.mainloop()