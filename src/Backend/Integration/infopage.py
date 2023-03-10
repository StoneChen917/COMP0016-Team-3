from pathlib import Path
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinterdnd2 import *
import pythontopostgres



pinkish_red = "#F5333F"
darkish_blue = "#12284C"
light_greyish = "#EBEBEB"



class InfoPage(Frame):
    
    def __init__(self, parent, controller, fronttoback):
        Frame.__init__(self, parent)

        self.controller = controller
        self.fronttoback = fronttoback

        self.screen_width = self.winfo_screenwidth() 
        self.screen_height = self.winfo_screenheight()

        self.file_name_text = ""
        self.file_num = 0
        self.file_max = 0
        self.answers = []
        
        self.topbanner = Label(self, width = self.screen_width, height = 4, bg = "white")
        self.topbanner.place(x = 0, y = 0)

        logo_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/logo.png")).resize((220, 66)))
        self.logo = Label(self, borderwidth = 0, image = logo_image) 
        self.logo.image = logo_image
        self.logo.place(x = 100, y = 0) 

        self.midbanner = Label(self, width = self.screen_width, height = 60, bg = "#EBEBEB")
        self.midbanner.place(x = 0, y = 66)

        self.home_photo = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/home.png")).resize((50, 50)))
        self.home_button = Button(self, image = self.home_photo, bg = "white", borderwidth = 0, command = self.back_main)
        self.home_button.place(x = 9, y = 8)

        grid_x = (self.screen_width-910)/2
        grid_y = 100
        label_width = 310
        label_height = 31
        text_width = 600

        self.file_name_text = Label(self, text = "", fg = darkish_blue, bg = light_greyish, font = ('Verdana', 15, "bold"))
        self.file_name_text.place(x = (self.screen_width-self.file_name_text.winfo_reqwidth())/2, y = 66)

        self.info_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/info.png")).resize((23, 23)))
        
        self.admin0_label = Label(self, text = "Admin 0", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.admin0_label.place(x = grid_x, y = grid_y, width = label_width, height = label_height)
        self.admin0_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.admin0_text.place(x = grid_x+label_width, y = grid_y, width = text_width, height = label_height)
        self.admin0_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_admin0_info)
        self.admin0_info.image = self.info_image
        self.admin0_info.place(x = grid_x+label_width-27, y = grid_y+4)

        self.iso_label = Label(self, text = "ISO Code", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.iso_label.place(x = grid_x, y = grid_y+label_height, width = label_width, height = label_height)
        self.iso_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.iso_text.place(x = grid_x+label_width, y = grid_y+label_height, width = text_width, height = label_height)
        self.iso_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_iso_info)
        self.iso_info.image = self.info_image
        self.iso_info.place(x = grid_x+label_width-27, y = grid_y+label_height+4)

        self.admin1_label = Label(self, text = "Admin 1", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.admin1_label.place(x = grid_x, y = grid_y+label_height*2, width = label_width, height = label_height)
        self.admin1_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.admin1_text.place(x = grid_x+label_width, y = grid_y+label_height*2, width = text_width, height = label_height)
        self.admin1_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_admin1_info)
        self.admin1_info.image = self.info_image
        self.admin1_info.place(x = grid_x+label_width-27, y = grid_y+label_height*2+4)

        self.admin2_label = Label(self, text = "Admin 2", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.admin2_label.place(x = grid_x, y = grid_y+label_height*3, width = label_width, height = label_height)
        self.admin2_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.admin2_text.place(x = grid_x+label_width, y = grid_y+label_height*3, width = text_width, height = label_height)
        self.admin2_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_admin2_info)
        self.admin2_info.image = self.info_image
        self.admin2_info.place(x = grid_x+label_width-27, y = grid_y+label_height*3+4)

        self.operation_number_label = Label(self, text = "Operation number", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.operation_number_label.place(x = grid_x, y = grid_y+label_height*4, width = label_width, height = label_height)
        self.operation_number_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.operation_number_text.place(x = grid_x+label_width, y = grid_y+label_height*4, width = text_width, height = label_height)
        self.operation_number_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_op_num_info)
        self.operation_number_info.image = self.info_image
        self.operation_number_info.place(x = grid_x+label_width-27, y = grid_y+label_height*4+4)

        self.operation_start_date_label = Label(self, text = "Operation start date", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.operation_start_date_label.place(x = grid_x, y = grid_y+label_height*5, width = label_width, height = label_height)
        self.operation_start_date_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.operation_start_date_text.place(x = grid_x+label_width, y = grid_y+label_height*5, width = text_width, height = label_height)
        self.op_start_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_op_start_info)
        self.op_start_info.image = self.info_image
        self.op_start_info.place(x = grid_x+label_width-27, y = grid_y+label_height*5+4)

        self.operation_end_date_label = Label(self, text = "Operation End Date", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.operation_end_date_label.place(x = grid_x, y = grid_y+label_height*6, width = label_width, height = label_height)
        self.operation_end_date_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.operation_end_date_text.place(x = grid_x+label_width, y = grid_y+label_height*6, width = text_width, height = label_height)
        self.op_end_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_op_end_info)
        self.op_end_info.image = self.info_image
        self.op_end_info.place(x = grid_x+label_width-27, y = grid_y+label_height*6+4)
       
        self.glide_number_label = Label(self, text = "Glide Number", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.glide_number_label.place(x = grid_x, y = grid_y+label_height*7, width = label_width, height = label_height)
        self.glide_number_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.glide_number_text.place(x = grid_x+label_width, y = grid_y+label_height*7, width = text_width, height = label_height)
        self.glide_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_glide_info)
        self.glide_info.image = self.info_image
        self.glide_info.place(x = grid_x+label_width-27, y = grid_y+label_height*7+4)
       
        self.affected_label = Label(self, text = "Number pf people affected", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.affected_label.place(x = grid_x, y = grid_y+label_height*8, width = label_width, height = label_height)
        self.affected_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.affected_text.place(x = grid_x+label_width, y = grid_y+label_height*8, width = text_width, height = label_height)
        self.affected_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_affected_info)
        self.affected_info.image = self.info_image
        self.affected_info.place(x = grid_x+label_width-27, y = grid_y+label_height*8+4)
       
        self.assisted_label = Label(self, text = "Number of people assisted", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.assisted_label.place(x = grid_x, y = grid_y+label_height*9, width = label_width, height = label_height)
        self.assisted_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.assisted_text.place(x = grid_x+label_width, y = grid_y+label_height*9, width = text_width, height = label_height)
        self.assisted_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_assisted_info)
        self.assisted_info.image = self.info_image
        self.assisted_info.place(x = grid_x+label_width-27, y = grid_y+label_height*9+4)
       
        self.operation_budget_label = Label(self, text = "Operation Budget", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.operation_budget_label.place(x = grid_x, y = grid_y+label_height*10, width = label_width, height = label_height)
        self.operation_budget_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.operation_budget_text.place(x = grid_x+label_width, y = grid_y+label_height*10, width = text_width, height = label_height)
        self.op_bud_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_op_bud_info)
        self.op_bud_info.image = self.info_image
        self.op_bud_info.place(x = grid_x+label_width-27, y = grid_y+label_height*10+4)
       
        self.host_national_society_label = Label(self, text = "Host National Society", font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue,
                                                relief = "solid", anchor = "w")
        self.host_national_society_label.place(x = grid_x, y = grid_y+label_height*11, width = label_width, height = label_height)
        self.host_national_society_text = Text(self, font = ('Verdana', 15), borderwidth = 2, fg = darkish_blue, bg = "white")
        self.host_national_society_text.place(x = grid_x+label_width, y = grid_y+label_height*11, width = text_width, height = label_height)
        self.host_info = Button(self, image = self.info_image, borderwidth = 0, bg = light_greyish, command = self.click_host_info)
        self.host_info.image = self.info_image
        self.host_info.place(x = grid_x+label_width-27, y = grid_y+label_height*11+4)

        self.back_arrow_photo = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/back_arrow.png")).resize((50, 70)))
        self.back_arrow_button = Button(self, image = self.back_arrow_photo, bg = light_greyish, borderwidth = 0, command = self.click_back_arrow)
        self.back_arrow_button.place(x = grid_x-52, y = grid_y+(label_height*12-50)/2+3)

        self.forward_arrow_photo = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/forward_arrow.png")).resize((50, 70)))
        self.forward_arrow_button = Button(self, image = self.forward_arrow_photo, bg = light_greyish, borderwidth = 0, command = self.click_forward_arrow)
        self.forward_arrow_button.place(x = grid_x+912, y = grid_y+(label_height*12-50)/2+3)
       
        self.save_image = ImageTk.PhotoImage(Image.open(Path("src/Assets/Images/save_button.png")).resize((262, 82)))
        self.save_button = Button(self, image = self.save_image, borderwidth = 0, command = self.click_push)
        self.save_button.image = self.save_image
        self.save_button.place(x = (self.screen_width-self.save_button.winfo_reqwidth())/2, y = 600)

    def click_admin0_info(self):
        messagebox.showinfo(title = "Info", message = "Admin 0 code")

    def click_iso_info(self):
        messagebox.showinfo(title = "Info", message = "The iso country codes are internationally recognized codes that designate every country and most of the dependent areas a two-letter combination or a three-letter combination. E.g. Chad is TCD")

    def click_admin1_info(self):
        messagebox.showinfo(title = "Info", message = "Admin 1 code")

    def click_admin2_info(self):
        messagebox.showinfo(title = "Info", message = "Admin 2 code")

    def click_op_num_info(self):
        messagebox.showinfo(title = "Info", message = "The unique operation number. E.g. MDRJM004")

    def click_op_start_info(self):
        messagebox.showinfo(title = "Info", message = "The start date of the operation")

    def click_op_end_info(self):
        messagebox.showinfo(title = "Info", message = "The end date of the operation")

    def click_glide_info(self):
        messagebox.showinfo(title = "Info", message = "The components of a GLIDE number consist of two letters to identify the disaster type (e.g. EQ - earthquake); the year of the disaster; a six-digit, sequential disaster number; and the three-letter iso code for country of occurrence.")

    def click_affected_info(self):
        messagebox.showinfo(title = "Info", message = "Number of people affected by the disaster")

    def click_assisted_info(self):
        messagebox.showinfo(title = "Info", message = "Number of people assisted in this disaster")

    def click_op_bud_info(self):
        messagebox.showinfo(title = "Info", message = "Budget for this operation")

    def click_host_info(self):
        messagebox.showinfo(title = "Info", message = "National Societies are the backbone of the International Red Cross and Red Crescent Movement. Each one is made up of an unparalleled network of community-based volunteers and staff who provide a wide variety of services.")

    def back_main(self):
        if messagebox.askyesno(title = "Back to main page?", message = "Changes will be lost"):
            self.controller.show_frame("MainPage")

    def set_answers(self):
        self.file_max = self.fronttoback.get_max()
        self.update_text(0)

    def update_text(self, i):
        # admin 0
        self.admin0_text.delete('1.0', END)
        self.admin0_text.insert(INSERT, self.fronttoback.get_glide(i))
        # iso
        self.iso_text.delete('1.0', END)
        self.iso_text.insert(INSERT, self.fronttoback.get_iso(i))
        # Admin 1
        self.admin1_text.delete('1.0', END)
        self.admin1_text.insert(INSERT, self.fronttoback.get_admin1(i))
        # Admin 2
        self.admin2_text.delete('1.0', END)
        self.admin2_text.insert(INSERT, self.fronttoback.get_admin2(i))
        # number
        self.operation_number_text.delete('1.0', END)
        self.operation_number_text.insert(INSERT, self.fronttoback.get_operation_number(i))
        # start
        self.operation_start_date_text.delete('1.0', END)
        self.operation_start_date_text.insert(INSERT, self.fronttoback.get_start(i))
        # end
        self.operation_end_date_text.delete('1.0', END)
        self.operation_end_date_text.insert(INSERT, self.fronttoback.get_end(i))
        # glide
        self.glide_number_text.delete('1.0', END)
        self.glide_number_text.insert(INSERT, self.fronttoback.get_glide(i))
        # affected
        self.affected_text.delete('1.0', END)
        self.affected_text.insert(INSERT, self.fronttoback.get_affected(i))
        # assisted
        self.assisted_text.delete('1.0', END)
        self.assisted_text.insert(INSERT, self.fronttoback.get_assisted(i))
        # budget
        self.operation_budget_text.delete('1.0', END)
        self.operation_budget_text.insert(INSERT, self.fronttoback.get_operation_budget(i))
        # host
        self.host_national_society_text.delete('1.0', END)
        self.host_national_society_text.insert(INSERT, self.fronttoback.get_host(i))

    def click_back_arrow(self):
        if self.file_num > 0:
            self.file_num -= 1
            self.update_text(self.file_num)
        else:
            messagebox.showinfo(title = "First file reached", message = "This is the first of all the files you uploaded")

    def click_forward_arrow(self):
        if self.file_num < self.file_max:
            self.file_num += 1
            self.update_text(self.file_num)
        else:
            messagebox.showinfo(title = "Last file reached", message = "This is the last of all the files you uploaded")

    def click_push(self):
        for i in self.answers:
            pythontopostgres.save_to_table(i["OpNum"], i["Country"], i["Admin1"], i["Admin2"], i["iso"], i["Glide"], 
                                           i["Host"], i["OpBud"], i["Start"], i["End"], i["Affected"], i["Assisted"])