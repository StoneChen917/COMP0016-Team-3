import os
os.chdir(".")
from tkinter import *
from tkinter import messagebox, filedialog
from Backend import readfile



class UI(Tk):

    def __init__(self, *args, **kwargs):
        
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (MainPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

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

        self.label = Label(self, text = "Upload the file by clicking the button below", font = ('Arial', 18))
        self.label.pack(pady = 60)

        self.select_button = Button(self, text = "Select", font = ('Arial', 18), command = self.click_select)
        self.select_button.pack(pady = 40)

        self.upload_button = Button(self, text = "Upload", font = ('Arial', 18), command = self.click_upload)
        self.upload_button.pack(pady = 20)

        self.check_state = IntVar()

        self.check = Checkbutton(self, text = "Show", font = ('Arial', 18), variable = self.check_state)
        self.check.pack(pady = 20)

    def click_select(self):
        f = filedialog.askopenfilename()
        readfile.ReadFile().exec(f)

    def click_upload(self):
        if self.check_state.get() == 1:
            messagebox.showinfo(title = "Error", message = "No file has been uploaded")


class PageOne(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page One!!!", font="Arial")
        label.pack(pady=10)

        button1 = Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        label = Label(self, text="Page Two!!!", font="Arial")
        label.pack(pady=10)

        button1 = Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()
        


app = UI()
app.protocol("WM_DELETE_WINDOW", app.on_closing)
app.mainloop()