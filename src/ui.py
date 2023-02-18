from pathlib import Path
from tkinter import *
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
from Backend.Integration import readfile
from tkinterdnd2 import *



pinkish_red = "#F5333F"
darkish_blue = "#12284C"
light_greyish = "#EBEBEB"



class UI(Tk):

    def __init__(self, *args, **kwargs):
        
        TkinterDnD.Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        infopage = InfoPage(container, self)
        self.frames[InfoPage] = infopage
        infopage.grid(row = 0, column = 0, sticky = "nsew")

        mainpage = MainPage(container, self, infopage)
        self.frames[MainPage] = mainpage
        mainpage.grid(row = 0, column = 0, sticky = "nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

    def on_closing(self):
        if messagebox.askyesno(title = "Quit?", message = "Do you really want to quit?"):
            self.destroy()


class MainPage(Frame):
    
    def __init__(self, parent, controller, infopage):
        Frame.__init__(self,parent)

        self.infopage = infopage

        self.screen_width = self.winfo_screenwidth() 
        self.screen_height = self.winfo_screenheight() 

        self.file_text = ""

        self.topbanner = Label(self, width = self.screen_width, height = 4, bg = "white")
        self.topbanner.place(x = 0, y = 0)

        logo_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/logo.png")).resize((220, 66)))
        self.logo = Label(borderwidth = 0, image = logo_image) 
        self.logo.image = logo_image
        self.logo.place(x = 100, y = 0) 

        self.info_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/info.png")).resize((60, 60)))
        self.info_button = Button(self, image = self.info_image, borderwidth = 0, bg = "white", command = self.click_info)
        self.info_button.image = self.info_image
        self.info_button.place(x = self.screen_width-63, y = 3)

        self.midbannerone = Label(self, width = self.screen_width, height = 10, bg = darkish_blue)
        self.midbannerone.place(x = 0, y = 66)

        self.maintext = Label(self, text = "Data Extraction App", fg = "white", bg = darkish_blue, font = ('Verdana', 40, "bold"))
        self.maintext.place(x = (self.screen_width-self.maintext.winfo_reqwidth())/2, y = 105)

        self.midbannertwo = Label(self, width = self.screen_width, height = 60, bg = light_greyish)
        self.midbannertwo.place(x = 0, y = 66+self.midbannerone.winfo_reqheight())

        self.upload_box_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/upload_box.png")).resize((458, 324)))
        self.upload_box_uploaded_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/upload_box_uploaded.png")).resize((458, 324)))
        self.upload_box = Button(self, image = self.upload_box_image, borderwidth = 0, command = self.click_select)
        self.upload_box.image = self.upload_box_image
        self.upload_box.place(x = (self.screen_width-458)/2, y = 280)
        self.upload_box.drop_target_register(DND_FILES)
        self.upload_box.dnd_bind('<<Drop>>', self.drop_file)

        self.select_label_text = ""

        self.select_label = Label(self, text = self.select_label_text, font = ('Arial', 18))

        self.cancel_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/cancel_button.png")).resize((190, 60)))
        self.cancel_button = Button(self, image = self.cancel_image, borderwidth = 0, command = self.click_cancel)
        self.cancel_button.image = self.cancel_image

        self.upload_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/upload_button.png")).resize((190, 60)))
        self.upload_button = Button(self, image = self.upload_image, borderwidth = 0, command = lambda: controller.show_frame(InfoPage))
        self.upload_button.image = self.upload_image

    def click_info(self):
        messagebox.showinfo(title = "Info", 
            message = "1.Upload your file by drag and drop, or select from folders. (pdf only)\n2.Check if the informations are correct and push it to the database.")

    def upload_success(self, f):
        self.file_text = readfile.ReadFile().exec(f)
        file_name = f[f.rfind("/")+1:]
        self.upload_box.configure(image = self.upload_box_uploaded_image)
        self.upload_box.image = self.upload_box_uploaded_image
        self.select_label.config(text = file_name, fg = 'black')

        self.select_label.place(x = (self.screen_width-self.select_label.winfo_reqwidth())/2, y = 330)
        self.cancel_button.place(x = (self.screen_width-self.cancel_button.winfo_reqwidth())/2, y = 400)
        self.upload_button.place(x = (self.screen_width-self.upload_button.winfo_reqwidth())/2, y = 490)

        self.infopage.update_file_text(self.file_text)

    def upload_failure(self):
        messagebox.showerror(title = "Upload failed", message = "File not supported, pdf only")
        self.upload_box.configure(image = self.upload_box_image)
        self.upload_box.image = self.upload_box_image

        self.select_label.place_forget()
        self.cancel_button.place_forget()
        self.upload_button.place_forget()

    def click_select(self):
        f = filedialog.askopenfilename()
        
        try:
            self.upload_success(f)
        except ValueError as e:
            self.upload_failure()

    def drop_file(self, event):
        f = event.data
        if event.data.endswith(".pdf"):
            self.upload_success(f)
        else:
            self.upload_failure()

    def click_cancel(self):
        self.upload_box.configure(image = self.upload_box_image)
        self.upload_box.image = self.upload_box_image

        self.select_label.place_forget()
        self.cancel_button.place_forget()
        self.upload_button.place_forget()

    def get_text(self):
        return self.file_text

class InfoPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.file_text = ""

        self.screen_width = self.winfo_screenwidth() 
        self.screen_height = self.winfo_screenheight() 
        
        self.topbanner = Label(self, width = self.screen_width, height = 4, bg = "white")
        self.topbanner.place(x = 0, y = 0)

        grid_x = (self.screen_width-910)/2
        grid_y = 150
        label_width = 310
        label_height = 31
        text_width = 600

        self.operation_number_label = Label(self, text = "Operation number", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, 
                                                relief = "solid", anchor = "w")
        self.operation_number_label.place(x = grid_x, y = grid_y, width = label_width, height = label_height)
        self.operation_number_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.operation_number_text.place(x = grid_x+label_width, y = grid_y, width = text_width, height = label_height)

        self.glide_number_label = Label(self, text = "Glide number", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, 
                                                relief = "solid", anchor = "w")
        self.glide_number_label.place(x = grid_x, y = grid_y+label_height, width = label_width, height = label_height)
        self.glide_number_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = light_greyish)
        self.glide_number_text.place(x = grid_x+label_width, y = grid_y+label_height, width = text_width, height = label_height)

        self.host_national_society_label = Label(self, text = "Host national society", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, 
                                                relief = "solid", anchor = "w")
        self.host_national_society_label.place(x = grid_x, y = grid_y+label_height*2, width = label_width, height = label_height)
        self.host_national_society_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.host_national_society_text.place(x = grid_x+label_width, y = grid_y+label_height*2, width = text_width, height = label_height)

        self.operation_budget_label = Label(self, text = "Operation budget", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, 
                                                relief = "solid", anchor = "w")
        self.operation_budget_label.place(x = grid_x, y = grid_y+label_height*3, width = label_width, height = label_height)
        self.operation_budget_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = light_greyish)
        self.operation_budget_text.place(x = grid_x+label_width, y = grid_y+label_height*3, width = text_width, height = label_height)

        self.operation_start_date_label = Label(self, text = "Operation start date", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, 
                                                relief = "solid", anchor = "w")
        self.operation_start_date_label.place(x = grid_x, y = grid_y+label_height*4, width = label_width, height = label_height)
        self.operation_start_date_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.operation_start_date_text.place(x = grid_x+label_width, y = grid_y+label_height*4, width = text_width, height = label_height)

        self.operation_end_date_label = Label(self, text = "Operation end date", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, 
                                                relief = "solid", anchor = "w")
        self.operation_end_date_label.place(x = grid_x, y = grid_y+label_height*5, width = label_width, height = label_height)
        self.operation_end_date_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = light_greyish)
        self.operation_end_date_text.place(x = grid_x+label_width, y = grid_y+label_height*5, width = text_width, height = label_height)

        self.number_of_people_affected_label = Label(self, text = "Number of people affected", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, 
                                                relief = "solid", anchor = "w")
        self.number_of_people_affected_label.place(x = grid_x, y = grid_y+label_height*6, width = label_width, height = label_height)
        self.number_of_people_affected_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.number_of_people_affected_text.place(x = grid_x+label_width, y = grid_y+label_height*6, width = text_width, height = label_height)
        
        self.number_of_people_assisted_label = Label(self, text = "Number of people assisted", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, 
                                                relief = "solid", anchor = "w")
        self.number_of_people_assisted_label.place(x = grid_x, y = grid_y+label_height*7, width = label_width, height = label_height)
        self.number_of_people_assisted_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = light_greyish)
        self.number_of_people_assisted_text.place(x = grid_x+label_width, y = grid_y+label_height*7, width = text_width, height = label_height)

        self.label = Label(self, text = "", fg = "black", font = "Arial")

        self.push_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/push_button.png")).resize((190, 60)))
        self.push_button = Button(self, image = self.push_image, borderwidth = 0, command = self.click_push)
        self.push_button.image = self.push_image
        self.push_button.place(x = (self.screen_width-self.push_button.winfo_reqwidth())/2, y = 430)

        self.back_arrow_photo = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/Arrow.png")).resize((50, 50)))
        self.back_button = Button(self, image = self.back_arrow_photo, borderwidth = 0, command = lambda: controller.show_frame(MainPage))
        self.back_button.place(x = 0, y = 76)
        
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
              
   
class Frontoback(Frame):
    global answers
    answers = []
            
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