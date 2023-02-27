import magic
from pathlib import Path
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from tkinterdnd2 import *



pinkish_red = "#F5333F"
darkish_blue = "#12284C"
light_greyish = "#EBEBEB"



class MainPage(Frame):

    doctext = " "
    
    def __init__(self, parent, controller, fronttoback, viewpage):
        Frame.__init__(self,parent)

        self.files = []

        self.controller = controller
        self.fronttoback = fronttoback
        self.viewpage = viewpage

        self.screen_width = self.winfo_screenwidth() 
        self.screen_height = self.winfo_screenheight()

        self.topbanner = Label(self, width = self.screen_width, height = 4, bg = "white")
        self.topbanner.place(x = 0, y = 0)

        logo_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/logo.png")).resize((220, 66)))
        self.logo = Label(self, borderwidth = 0, image = logo_image) 
        self.logo.image = logo_image
        self.logo.place(x = 100, y = 0) 

        self.info_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/info.png")).resize((60, 60)))
        self.info_button = Button(self, image = self.info_image, borderwidth = 0, bg = "white", command = self.click_info)
        self.info_button.image = self.info_image
        self.info_button.place(x = self.screen_width-63, y = 3)
        self.logo.place(x = 100, y = 0) 

        self.midbannerone = Label(self, width = self.screen_width, height = 10, bg = "#12284C")
        self.midbannerone.place(x = 0, y = 66)

        self.maintext = Label(self, text = "Data Extraction App", fg = "white", bg = darkish_blue, font = ('Verdana', 40, "bold"))
        self.maintext.place(x = (self.screen_width-self.maintext.winfo_reqwidth())/2, y = 105)

        self.midbannertwo = Label(self, width = self.screen_width, height = 60, bg = "#EBEBEB")
        self.midbannertwo.place(x = 0, y = 66+self.midbannerone.winfo_reqheight())

        # self.upload_box_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/upload_box.png")).resize((458, 324)))
        # self.upload_box_uploaded_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/upload_box_uploaded.png")).resize((458, 324)))
        # self.upload_box = Button(self, image = self.upload_box_image, borderwidth = 0, command = self.click_select)
        # self.upload_box.image = self.upload_box_image
        # self.upload_box.place(x = (self.screen_width-458)/2, y = 280)
        # self.upload_box.drop_target_register(DND_FILES)
        # self.upload_box.dnd_bind('<<Drop>>', self.drop_file)

        self.lb = Listbox(self, selectmode=SINGLE)
        self.lb_scroll = Scrollbar(self, orient=VERTICAL)
        self.lb.drop_target_register(DND_FILES)
        self.lb.dnd_bind('<<Drop>>', self.drop_file)
        self.lb.configure(yscrollcommand=self.lb_scroll.set)
        self.lb_scroll.config(command=self.lb.yview)
        self.lb.place(x = (self.screen_width-800)/2, y = 280, width = 500, height = 500)
        self.lb_scroll.place(x = (self.screen_width-800)/2+500-10, y = 280, width = 10, height = 500)

        self.label = Label(self, text = "", font = ('Arial', 13))
        self.label.pack(pady = ((self.screen_height-280)/2,0))

        self.select_label_text = ""

        self.select_label = Label(self, text = self.select_label_text, font = ('Arial', 18))

        self.remove_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/remove_button.png")).resize((262, 82)))
        self.remove_button = Button(self, image = self.remove_image, borderwidth = 0, command = self.click_cancel)
        self.remove_button.image = self.remove_image

        self.preview_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/preview_button.png")).resize((262, 82)))
        self.preview_button = Button(self, image = self.preview_image, borderwidth = 0, command = self.click_preview)
        self.preview_button.image = self.preview_image

    def click_info(self):
        messagebox.showinfo(title = "Info", 
                                message = """1.Upload your file by drag and drop, or select from folders. (pdf only)\n2.Check if the informations are correct and push it to the database.""")

    def click_preview(self):
        self.controller.show_frame("ViewPage")

    def upload_success(self, f):
        file_name = f[f.rfind("/")+1:]
        self.fronttoback.set_file_name(f)
        self.viewpage.update_pdf(f)
        self.upload_box.configure(image = self.upload_box_uploaded_image)
        self.upload_box.image = self.upload_box_uploaded_image
        self.select_label.config(text = file_name, fg = 'black')

        self.select_label.place(x = (self.screen_width-self.select_label.winfo_reqwidth())/2, y = 330)
        self.remove_button.place(x = (self.screen_width-self.remove_button.winfo_reqwidth())/2, y = 390)
        self.preview_button.place(x = (self.screen_width-self.preview_button.winfo_reqwidth())/2, y = 490)

    def upload_failure(self):
        messagebox.showerror(title = "Upload failed", message = "File not supported, pdf only")
        self.upload_box.configure(image = self.upload_box_image)
        self.upload_box.image = self.upload_box_image

        self.select_label.place_forget()
        self.remove_button.place_forget()
        self.preview_button.place_forget()

    def click_select(self):
        f = filedialog.askopenfilename()
        if "PDF document" in magic.from_file(f):
            self.upload_success(f)
        else:
            self.upload_failure(f)

    def drop_file(self, event):
        for e in event.data:
            print(e)
        f = event.data
        if "PDF document" in magic.from_file(f):
            self.upload_success(f)
        else:
            self.upload_failure(f)

    def click_cancel(self):
        self.upload_box.configure(image = self.upload_box_image)
        self.upload_box.image = self.upload_box_image

        self.select_label.place_forget()
        self.remove_button.place_forget()
        self.preview_button.place_forget()