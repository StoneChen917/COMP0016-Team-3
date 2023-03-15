import magic
from pathlib import Path
from tkinter import *
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
from tkinterdnd2 import *
import os



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

        self.box_y = 250

        self.listbox = Listbox(self, selectmode = MULTIPLE)
        self.listbox_scroll = Scrollbar(self, orient=VERTICAL)
        self.listbox.drop_target_register(DND_FILES)
        self.listbox.dnd_bind('<<Drop>>', self.drop_file)
        self.listbox.configure(yscrollcommand=self.listbox_scroll.set)
        self.listbox_scroll.config(command=self.listbox.yview)
        self.listbox.place(x = (self.screen_width-800)/2, y = self.box_y, width = 500, height = 500)
        self.listbox_scroll.place(x = (self.screen_width-800)/2+500-10, y = self.box_y, width = 10, height = 500)

        self.button_box = Frame(self, highlightbackground = darkish_blue, highlightthickness=2, width = 300, height = 500)
        self.button_box.place(x = (self.screen_width-800)/2+500, y = self.box_y)

        self.upload_file_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/upload_file_button.png")).resize((266, 86)))
        self.upload_file_button = Button(self, image = self.upload_file_image, borderwidth = 0, command = self.click_upload_file)
        self.upload_file_button.image = self.upload_file_image
        self.upload_file_button.place(x = (self.screen_width-800)/2+517, y = self.box_y+11)

        self.upload_folder_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/upload_folder_button.png")).resize((266, 86)))
        self.upload_folder_button = Button(self, image = self.upload_folder_image, borderwidth = 0, command = self.click_upload_folder)
        self.upload_folder_button.image = self.upload_folder_image
        self.upload_folder_button.place(x = (self.screen_width-800)/2+517, y = self.box_y+109)

        self.remove_s_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/remove_s_button.png")).resize((266, 86)))
        self.remove_s_button = Button(self, image = self.remove_s_image, borderwidth = 0, command = self.click_remove_selected)
        self.remove_s_button.image = self.remove_s_image
        self.remove_s_button.place(x = (self.screen_width-800)/2+517, y = self.box_y+207)

        self.remove_a_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/remove_a_button.png")).resize((266, 86)))
        self.remove_a_button = Button(self, image = self.remove_a_image, borderwidth = 0, command = self.click_remove_all)
        self.remove_a_button.image = self.remove_a_image
        self.remove_a_button.place(x = (self.screen_width-800)/2+517, y = self.box_y+305)

        self.preview_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/preview_button.png")).resize((266, 86)))
        self.preview_button = Button(self, image = self.preview_image, borderwidth = 0, command = self.click_preview)
        self.preview_button.image = self.preview_image
        self.preview_button.place(x = (self.screen_width-800)/2+517, y = self.box_y+403)

    def click_info(self):
        messagebox.showinfo(title = "Info", 
                                message = """1.Upload your file by drag and drop, or select from folders. (pdf only)\n2.Check if the informations are correct and push it to the database.""")

    def get_files_in_folder(self, mypath):
        files = [mypath+"/"+f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
        for f in files:
            if "PDF document" in magic.from_file(f):
                self.listbox.insert(END, f)

    def click_upload_folder(self):
        mypath = filedialog.askdirectory()
        self.get_files_in_folder(mypath)

    def click_upload_file(self):
        f = filedialog.askopenfilename()
        if "PDF document" in magic.from_file(f):
            self.listbox.insert(END, f)
        else:
            self.upload_failure()

    def click_remove_selected(self):
        if messagebox.askyesno(title = "Remove selected files?", message = "Do you really want to remove the selected files?"):
            selected_checkboxs = self.listbox.curselection()
            for selected_checkbox in selected_checkboxs[::-1]:
                self.listbox.delete(selected_checkbox)

    def click_remove_all(self):
        if messagebox.askyesno(title = "Remove all files?", message = "Do you really want to remove all the files?"):
            self.listbox.delete(0, END)

    def click_preview(self):
        if self.listbox.size() > 0:
            self.viewpage.set_files(self.listbox.get(0 , END))
            self.fronttoback.set_files(self.listbox.get(0 , END))
            self.controller.show_frame("ViewPage")
        else:
            messagebox.showinfo(title = "No file uploaded", message = "Please upload one or more files before you proceed")

    def upload_failure(self):
        messagebox.showerror(title = "Upload failed", message = "File not supported, pdf only")

    def split_file_names(self, string):
        files = []
        while string:
            i = 0
            file_end = 0
            last_reached = False
            keepgoing = True
            if string[0] != "{":
                while keepgoing:
                    if i == len(string)-1:
                        file_end = i
                        last_reached = True
                        keepgoing = False
                    elif string[i] == " ":
                        file_end = i
                        keepgoing = False
                    else:
                        i += 1
                if last_reached:
                    files.append(string[0:])
                    string = ""
                else:
                    files.append(string[:file_end])
                    string = string[file_end+1:]
            else:
                while keepgoing:
                    if string[i] == "}" and i == len(string)-1:
                        file_end = i
                        last_reached = True
                        keepgoing = False
                    elif string[i] == "}" and string[i+1] == " ":
                        file_end = i
                        keepgoing = False
                    else:
                        i += 1
                if last_reached:
                    files.append(string[1:-1])
                    string = ""
                else:
                    files.append(string[1:file_end])
                    string = string[file_end+2:]

        return files

    def drop_file(self, event):
        items = self.split_file_names(event.data)
        for i in items:
            if os.path.isdir(i):
                self.get_files_in_folder(i)
            elif "PDF document" in magic.from_file(i):
                self.listbox.insert(END, i)