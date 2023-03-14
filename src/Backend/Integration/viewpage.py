import magic
from pathlib import Path
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from readfile import ReadFile
import tkinter.scrolledtext as scrolledtext



pinkish_red = "#F5333F"
darkish_blue = "#12284C"
light_greyish = "#EBEBEB"



class ViewPage(Frame):
    
    def __init__(self, parent, controller, fronttoback, infopage):
        Frame.__init__(self, parent)

        self.controller = controller
        self.fronttoback = fronttoback
        self.infopage = infopage

        self.screen_width = self.winfo_screenwidth() 
        self.screen_height = self.winfo_screenheight() 

        self.files = []
        self.file_num = 0
        self.file_max = 0
        
        self.topbanner = Label(self, width = self.screen_width, height = 4, bg = "white")
        self.topbanner.place(x = 0, y = 0)

        logo_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/logo.png")).resize((220, 66)))
        self.logo = Label(self, borderwidth = 0, image = logo_image) 
        self.logo.image = logo_image
        self.logo.place(x = 100, y = 0) 

        self.midbanner = Label(self, width = self.screen_width, height = 100, bg = "#EBEBEB")
        self.midbanner.place(x = 0, y = 66)

        self.home_photo = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/home.png")).resize((50, 50)))
        self.home_button = Button(self, image = self.home_photo, bg = "white", borderwidth = 0, command = self.back_main)
        self.home_button.place(x = 9, y = 8)

        self.file_name_text = Label(self, text = "", fg = darkish_blue, bg = light_greyish, font = ('Verdana', 15, "bold"))
        self.file_name_text.place(x = (self.screen_width-self.file_name_text.winfo_reqwidth())/2, y = 66)

        self.back_arrow_photo = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/back_arrow.png")).resize((50, 70)))
        self.back_arrow_button = Button(self, image = self.back_arrow_photo, bg = light_greyish, borderwidth = 0, command = self.click_back_arrow)
        self.back_arrow_button.place(x = (self.screen_width-800)/2-50, y = 100+215)

        self.forward_arrow_photo = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/forward_arrow.png")).resize((50, 70)))
        self.forward_arrow_button = Button(self, image = self.forward_arrow_photo, bg = light_greyish, borderwidth = 0, command = self.click_forward_arrow)
        self.forward_arrow_button.place(x = (self.screen_width-800)/2+800, y = 100+215)

        self.pdf_text = Text(self, bg="white", highlightthickness=1, foreground="black",
                    insertbackground="black", wrap="word")
        self.text_scroll = Scrollbar(self, orient=VERTICAL)
        self.text_scroll.config(command=self.pdf_text.yview)
        self.pdf_text["yscrollcommand"] = self.text_scroll.set
        self.pdf_text.place(x = (self.screen_width-800)/2, y = 100, width = 800, height = 500)
        self.text_scroll.place(x = (self.screen_width-800)/2+800-10, y = 100, width = 10, height = 500)

        self.file_num_text = Label(self, text = "", fg = darkish_blue, bg = light_greyish, font = ('Verdana', 15, "bold"))

        self.extract_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/extract_button.png")).resize((262, 82)))
        self.extract_button = Button(self, image = self.extract_image, borderwidth = 0, command = self.click_extract)
        self.extract_button.image = self.extract_image
        self.extract_button.place(x = (self.screen_width-self.extract_button.winfo_reqwidth())/2, y = 638)

    def back_main(self):
        self.file_num = 0
        self.controller.show_frame("MainPage")
    
    def click_extract(self):
        self.update_info_page()
        self.controller.show_frame("LoadPage")

    def update_info_page(self):
        self.fronttoback.extract_answers()
        self.infopage.update_text()

    def set_files(self, files):
        self.files = files
        self.file_max = len(files)-1
        self.update_pdf(self.files[self.file_num])

    def click_back_arrow(self):
        if self.file_num > 0:
            self.file_num -= 1
            self.update_pdf(self.files[self.file_num])
        else:
            messagebox.showinfo(title = "First file reached", message = "This is the first of all the files you uploaded")

    def click_forward_arrow(self):
        if self.file_num < self.file_max:
            self.file_num += 1
            self.update_pdf(self.files[self.file_num])
        else:
            messagebox.showinfo(title = "Last file reached", message = "This is the last of all the files you uploaded")

    def update_pdf(self, filename):
        self.file_name_text.config(text = filename)
        self.file_name_text.place_forget()
        self.file_name_text.place(x = (self.screen_width-self.file_name_text.winfo_reqwidth())/2, y = 66)
        self.file_num_text.config(text = str(self.file_num+1)+" / "+str(self.file_max+1))
        self.file_num_text.place_forget
        self.file_num_text.place(x = (self.screen_width-self.file_num_text.winfo_reqwidth())/2, y = 603)
        pgone, rest = ReadFile().read_file(filename)
        self.pdf_text.config(state=NORMAL)
        self.pdf_text.delete('1.0', END)
        self.pdf_text.insert(INSERT, pgone+rest)
        self.pdf_text.config(state=DISABLED)