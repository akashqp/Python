from tkinter import *
from PIL import ImageTk, Image

class LoginForm:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1920x1080')
        self.window.state('iconic')
        self.window.resizable(0,0)

        #   Background Image
        self.bg_frame = Image.open('/home/akash/Programs/Python/PBL/Final/images/background.jpg')
        photo = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=photo)
        self.bg_panel.image = photo
        self.bg_panel.pack(fill='none', expand='yes')

        #   Login Frame
        self.lgn_frame = Frame(self.window, bg='#040405', width='950', height=600)
        self.lgn_frame.place(x=200,y=70,anchor=CENTER)



def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()

if __name__ == '__main__':
    page()