import tkinter
from tkinter import *

import pandas as pd
from PIL import ImageTk, Image
import pymysql
import os
import smtplib
import ssl
from email.message import EmailMessage
import random
import pickle
import time
import re
from threading import Timer


class LoginPage:
    def __init__(self, window):
        self.username_var = tkinter.StringVar()
        self.password_var = tkinter.StringVar()
        self.email_var = tkinter.StringVar()
        self.code_var = tkinter.StringVar()
        self.search_var = tkinter.StringVar()
        self.flag = 0
        self.flag1 = 0
        self.flag2 = 0
        self.flag3 = 0

        self.window = window
        self.window.geometry('1366x768')
        self.window.resizable(0, 0)
        self.window.state('iconic')
        self.window.title('Login Page')
        self.search=""

        def Signup_Submit():
            self.connection = pymysql.connect(host="sql12.freemysqlhosting.net", user="sql12530135", password="cc9s3YUrLR",
                                         database="sql12530135")
            self.cursor = self.connection.cursor()
            username = self.username_var.get()
            password = self.password_var.get()
            email = self.email_var.get()

            self.sql = "INSERT into USERS (user_name, password, email) VALUES (%s, %s, %s)"
            self.val = (username, password, email)

            self.username_var.set("")
            self.password_var.set("")
            self.email_var.set("")

            email_sender = 'workqp@gmail.com'
            email_password = os.environ.get('workqp_password')
            email_receiver = email

            subject = 'Email verification code'
            self.code = str(random.randint(100000, 999999))
            #print(self.code)
            body = """
            You've applied to register an account
            Verification Code:"""+self.code

            em = EmailMessage()
            em['From'] = email_sender
            em['To'] = email_receiver
            em['Subject'] = subject
            em.set_content(body)

            context = ssl.create_default_context()
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                smtp.login(email_sender, email_password)
                smtp.sendmail(email_sender, email_receiver, em.as_string())
            self.window.title('Sign Up Page')
            self.lgn_frame.destroy()
            Code_Entry()

        def Code_Entry():

            #   Login Frame
            self.lgn_frame = Frame(self.window, bg='#040405', width='950', height=600)
            self.lgn_frame.place(x=210, y=70)

            self.txt = 'Email Verification'
            self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'),
                                 bg='#040405', fg='white')
            self.heading.place(x=80, y=40, width=300, height=30)

            #   Left Side Image
            self.side_image = Image.open('images\\vector.png')
            photo = ImageTk.PhotoImage(self.side_image)
            self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
            self.side_image_label.image = photo
            self.side_image_label.place(x=5, y=100)

            #   Sign up Image
            self.sign_up_image = Image.open('images\\hyy.png')
            photo = ImageTk.PhotoImage(self.sign_up_image)
            self.sign_up_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
            self.sign_up_image_label.image = photo
            self.sign_up_image_label.place(x=620, y=80)

            self.sign_up_label = Label(self.lgn_frame, text='Enter Verification Code', bg='#040405', fg='white',
                                       font=('yu gothic ui', 17, 'bold'))
            self.sign_up_label.place(x=550, y=200)

            #   Email Verification
            self.code_entry = Entry(self.lgn_frame, textvariable=self.code_var, highlightthickness=0, relief=FLAT,
                                     bg="#040405", fg="#6b6a69", font=("yu gothic ui ", 19, "bold"))
            self.code_entry.place(x=610, y=274, width=300)

            self.code_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
            self.code_line.place(x=550, y=308)

            #   Submit Button
            self.signup_button = Image.open('images\\btn1.png')
            photo = ImageTk.PhotoImage(self.signup_button)
            self.signup_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
            self.signup_button_label.image = photo
            self.signup_button_label.place(x=550, y=400)
            self.signup = Button(self.signup_button_label, command=Code_Submit, text='Submit', relief=FLAT,
                                 font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff', cursor='hand2',
                                 activebackground='#3047ff', fg='white')
            self.signup.place(x=20, y=10)

        def Code_Submit():
            self.code_num = int(self.code_var.get())
            print(self.code_num)
            if int(self.code) != self.code_num:
                self.wrong = Label(self.lgn_frame, text='Wrong Verification Code', font=("yu gothic ui", 12, "bold"),
                                        relief=FLAT, borderwidth=0, background="#040405", fg='red')
                self.wrong.place(x=600, y=500)
                Code_Entry()

            else:
                self.window.title('Sign Up Page')
                self.lgn_frame.destroy()

                #   Login Frame
                self.lgn_frame = Frame(self.window, bg='#040405', width='950', height=600)
                self.lgn_frame.place(x=210, y=70)

                self.txt = 'Email Verification'
                self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'),
                                     bg='#040405', fg='white')
                self.heading.place(x=80, y=30, width=300, height=30)

                #   Left Side Image
                self.side_image = Image.open('images\\vector.png')
                photo = ImageTk.PhotoImage(self.side_image)
                self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
                self.side_image_label.image = photo
                self.side_image_label.place(x=5, y=100)

                self.sign_up_label = Label(self.lgn_frame, text='Email Verified', bg='#040405', fg='white',
                                           font=('yu gothic ui', 18, 'bold'))
                self.sign_up_label.place(x=630, y=180)
                self.flag1 = 1
                self.cursor.execute(self.sql, self.val)
                self.connection.commit()
                self.connection.close()

                #   Login Transfer
                self.login_transfer = Button(self.lgn_frame, text="Login Again", command=Login(),
                                            font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                            activebackground="#040405"
                                            , borderwidth=0, background="#040405", cursor="hand2")
                self.login_tranfer.place(x=630, y=510)

        def Login_Submit():
            username = self.username_var.get()
            password = self.password_var.get()

            self.connection = pymysql.connect(host="sql12.freemysqlhosting.net", user="sql12530135",
                                              password="cc9s3YUrLR",
                                              database="sql12530135")
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT * FROM USERS WHERE user_name=%s", username)
            myresult = self.cursor.fetchall()
            if myresult == ():
                self.wrong_label = Label(self.lgn_frame, text='Invalid Username', bg='#040405',
                                            font=('yu gothic ui', 13, 'bold'), fg='red')
                self.wrong_label.place(x=680, y=341)
                self.username_var.set("")
                self.password_var.set("")
                return()
            if password != myresult[0][2]:
                self.wrong_label = Label(self.lgn_frame, text='Invalid Password', bg='#040405',
                                         font=('yu gothic ui', 13, 'bold'), fg='red')
                self.wrong_label.place(x=680, y=422)
                self.username_var.set("")
                self.password_var.set("")
                return()

            self.connection.close()
            Home()

        def Signup():
            self.window.title('Signup Page')
            self.lgn_frame.destroy()

            #   Login Frame
            self.lgn_frame = Frame(self.window, bg='#040405', width='950', height=600)
            self.lgn_frame.place(x=210, y=70)

            self.txt = 'WELCOME'
            self.heading = Label(self.lgn_frame, text=self.txt, font=('yu gothic ui', 25, 'bold'),
                                 bg='#040405', fg='white')
            self.heading.place(x=80, y=30, width=300, height=30)

            #   Left Side Image
            self.side_image = Image.open('images\\vector.png')
            photo = ImageTk.PhotoImage(self.side_image)
            self.side_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
            self.side_image_label.image = photo
            self.side_image_label.place(x=5, y=100)

            #   Sign up Image
            self.sign_up_image = Image.open('images\\hyy.png')
            photo = ImageTk.PhotoImage(self.sign_up_image)
            self.sign_up_image_label = Label(self.lgn_frame, image=photo, bg='#040405')
            self.sign_up_image_label.image = photo
            self.sign_up_image_label.place(x=620, y=80)

            self.sign_up_label = Label(self.lgn_frame, text='Sign Up', bg='#040405', fg='white',
                                       font=('yu gothic ui', 17, 'bold'))
            self.sign_up_label.place(x=650, y=180)

            #   Email
            self.email_label = Label(self.lgn_frame, text="Email", bg="#040405", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
            self.email_label.place(x=550, y=220)

            self.email_entry = Entry(self.lgn_frame, textvariable=self.email_var, highlightthickness=0, relief=FLAT, bg="#040405",
                                        fg="#6b6a69", font=("yu gothic ui ", 12, "bold"))
            self.email_entry.place(x=580, y=254, width=270)

            self.email_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
            self.email_line.place(x=550, y=278)

            #   Email Icon
            self.email_icon = Image.open('images\\email.png')
            photo = ImageTk.PhotoImage(self.email_icon)
            self.email_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
            self.email_icon_label.image = photo
            self.email_icon_label.place(x=550, y=250)

            #   Username
            self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
            self.username_label.place(x=550, y=300)

            self.username_entry = Entry(self.lgn_frame, textvariable=self.username_var, highlightthickness=0, relief=FLAT, bg="#040405",
                                        fg="#6b6a69", font=("yu gothic ui ", 12, "bold"))
            self.username_entry.place(x=580, y=335, width=270)

            self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
            self.username_line.place(x=550, y=359)

            #   Username Icon
            self.username_icon = Image.open('images\\username_icon.png')
            photo = ImageTk.PhotoImage(self.username_icon)
            self.username_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
            self.username_icon_label.image = photo
            self.username_icon_label.place(x=550, y=332)

            #   Password
            self.password_label = Label(self.lgn_frame, text='Password', bg='#040405',
                                        font=('yu gothic ui', 13, 'bold'), fg='#4f4e4d')
            self.password_label.place(x=550, y=380)

            self.password_entry = Entry(self.lgn_frame, textvariable=self.password_var, highlightthickness=0, relief=FLAT, bg='#040405',
                                        fg='#6b6a69', font=('yu gothic ui', 12, 'bold'))
            self.password_entry.place(x=580, y=416, width=244)

            self.password_line = Canvas(self.lgn_frame, width=300, height=2, bg='#bdb9b1', highlightthickness=0)
            self.password_line.place(x=550, y=440)

            #   Password Icon
            self.password_icon = Image.open('images\\password_icon.png')
            photo = ImageTk.PhotoImage(self.username_icon)
            self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
            self.password_icon_label.image = photo
            self.password_icon_label.place(x=550, y=414)

            #   Sign up Button
            self.signup_button = Image.open('images\\btn1.png')
            photo = ImageTk.PhotoImage(self.signup_button)
            self.signup_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
            self.signup_button_label.image = photo
            self.signup_button_label.place(x=550, y=460)
            self.signup = Button(self.signup_button_label, command=Signup_Submit, text='SIGN UP', relief=FLAT,
                                 font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff', cursor='hand2',
                                 activebackground='#3047ff', fg='white')
            self.signup.place(x=20, y=10)

            #   Show/Hide Password
            self.show_image = ImageTk.PhotoImage \
                (file='images\\show.png')

            self.hide_image = ImageTk.PhotoImage \
                (file='images\\hide.png')

            self.y_val=420
            self.hide()
            self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                      activebackground="white"
                                      , borderwidth=0, background="white", cursor="hand2")
            self.show_button.place(x=860, y=420)

        def Login():
            if self.flag1 == 1:
                self.lgn_frame.destroy()
            #   Background Image
            self.bg_frame = Image.open('images\\background1.png')
            photo = ImageTk.PhotoImage(self.bg_frame)
            self.bg_panel = Label(self.window, image=photo)
            self.bg_panel.image = photo
            self.bg_panel.pack(fill='both', expand='yes')

            #   Login Frame
            self.lgn_frame = Frame(self.window, bg='#040405', width='950', height=600)
            self.lgn_frame.place(x=210,y=70)

            self.txt = 'WELCOME'
            self.heading = Label(self.lgn_frame, text = self.txt, font = ('yu gothic ui', 25, 'bold'),
                                 bg = '#040405', fg='white')
            self.heading.place(x=80, y=30, width=300, height=30)

            #   Left Side Image
            self.side_image = Image.open('images\\vector.png')
            photo = ImageTk.PhotoImage(self.side_image)
            self.side_image_label = Label(self.lgn_frame, image=photo, bg = '#040405')
            self.side_image_label.image = photo
            self.side_image_label.place(x=5, y=100)

            #   Sign in Image
            self.sign_in_image = Image.open('images\\hyy.png')
            photo = ImageTk.PhotoImage(self.sign_in_image)
            self.sign_in_image_label = Label(self.lgn_frame, image=photo, bg = '#040405')
            self.sign_in_image_label.image = photo
            self.sign_in_image_label.place(x=620, y=130)

            self.sign_in_label = Label(self.lgn_frame, text = 'Sign In', bg = '#040405', fg = 'white',
                                       font = ('yu gothic ui', 17, 'bold'))
            self.sign_in_label.place(x=650, y=240)

            #   Username
            self.username_label = Label(self.lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                        font=("yu gothic ui", 13, "bold"))
            self.username_label.place(x=550, y=280)

            self.username_entry = Entry(self.lgn_frame, highlightthickness=0, textvariable=self.username_var,
                                        relief=FLAT, bg="#040405", fg="#6b6a69", font=("yu gothic ui ", 12, "bold"))
            self.username_entry.place(x=580, y=315, width=270)

            self.username_line = Canvas(self.lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
            self.username_line.place(x=550, y=339)

            #   Username Icon
            self.username_icon = Image.open('images\\username_icon.png')
            photo = ImageTk.PhotoImage(self.username_icon)
            self.username_icon_label = Label(self.lgn_frame, image=photo, bg = '#040405')
            self.username_icon_label.image = photo
            self.username_icon_label.place(x=550, y=312)

            #   Password
            self.password_label = Label(self.lgn_frame, text='Password', bg='#040405',
                                        font=('yu gothic ui', 13, 'bold'), fg='#4f4e4d')
            self.password_label.place(x=550, y=360)

            self.password_entry = Entry(self.lgn_frame, highlightthickness=0, textvariable=self.password_var,
                                        relief=FLAT, bg='#040405', fg='#6b6a69', font=('yu gothic ui', 12, 'bold'))
            self.password_entry.place(x=580, y=396, width=244)

            self.password_line = Canvas(self.lgn_frame, width=300, height=2, bg='#bdb9b1', highlightthickness=0)
            self.password_line.place(x=550, y=420)

            #   Password Icon
            self.password_icon = Image.open('images\\password_icon.png')
            photo = ImageTk.PhotoImage(self.username_icon)
            self.password_icon_label = Label(self.lgn_frame, image=photo, bg='#040405')
            self.password_icon_label.image = photo
            self.password_icon_label.place(x=550, y=394)

            #   Login Button
            self.lgn_button = Image.open('images\\btn1.png')
            photo = ImageTk.PhotoImage(self.lgn_button)
            self.lgn_button_label = Label(self.lgn_frame, image=photo, bg='#040405')
            self.lgn_button_label.image = photo
            self.lgn_button_label.place(x=550, y=450)
            self.login = Button(self.lgn_button_label, command=Login_Submit, text='LOGIN', relief=FLAT,
                                font=("yu gothic ui", 13, "bold"), width=25, bd=0, bg='#3047ff', cursor='hand2',
                                activebackground='#3047ff', fg='white')
            self.login.place(x=20, y=10)

            #   Forgot Password
            self.forgot_button = Button(self.lgn_frame, text="Forgot Password ?",
                                        font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                        activebackground="#040405"
                                        , borderwidth=0, background="#040405", cursor="hand2")
            self.forgot_button.place(x=630, y=510)

            #   Sign Up
            self.sign_label = Label(self.lgn_frame, text='No account yet?', font=("yu gothic ui", 11, "bold"),
                                    relief=FLAT, borderwidth=0, background="#040405", fg='white')
            self.sign_label.place(x=550, y=560)

            self.signup_img = ImageTk.PhotoImage(file='images\\register.png')
            self.signup_button_label = Button(self.lgn_frame, image=self.signup_img, command=Signup, bg='#98a65d', cursor="hand2",
                                              borderwidth=0, background="#040405", activebackground="#040405")
            self.signup_button_label.place(x=670, y=555, width=111, height=35)

            #   Show/Hide Password
            self.show_image = ImageTk.PhotoImage \
                (file='images\\show.png')

            self.hide_image = ImageTk.PhotoImage \
                (file='images\\hide.png')

            self.y_val=400
            self.hide()
            self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                      activebackground="white", borderwidth=0, background="white", cursor="hand2")
            self.show_button.place(x=860, y=400)

        def Search():
            self.mainframe.destroy()
            self.mainframe = Frame(self.window, bg="#040405", width='1100', height='550')
            self.mainframe.place(x=140, y=180)

            self.heading = Label(self.mainframe, text='Search', font=('yu gothic ui', 23, 'bold'),
                                 bg='#040405', fg='white')
            self.heading.place(x=200, y=30)

            self.search_entry = Entry(self.mainframe, highlightthickness=0, textvariable=self.search_var,
                                      bg='#040405', fg='#6b6a69', font=('yu gothic ui', 15, 'bold'))
            self.search_entry.place(x=120, y=120, width=400)

            #   Search Button
            #self.search_button_label = Label(self.mainframe, text="Search", bg='blue')
            #self.search_button_label.place(x=549, y=120)
            self.search = Button(self.mainframe, text="Search", font=('yu gothic ui', 15, 'bold'),
                                 command=Search_Submit,
                                 width=16, bd=0, bg='blue', cursor='hand2', activebackground='#3047ff')
            self.search.place(x=549, y=120)

            self.sugg_frame = Frame(self.mainframe, width=400, height=30, bg="#040405")
            self.sugg_frame.place(x=120, y=170)

            def suggestion():
                #self.entry = str(self.search_var.get())
                while(True):
                    df = pd.read_csv('data//books.csv',
                                     usecols=['title', 'authors', 'average_rating', 'isbn13', '  num_pages',
                                              'publication_date', 'publisher'])
                    if(self.entry == str(self.search_var.get)):
                        continue
                    self.entry = str(self.search_var.get())
                    for book_name in df['title']:
                        if(self.entry.lower() in (book_name.lower())):
                            self.text = book_name.lower()
                            break
                    self.sugg_frame.destroy()
                    self.sugg_frame = Frame(self.mainframe, width = 400, height = 30, bg="#040405")
                    self.sugg_frame.place(x=120,y=170)
                    self.sugg = Label(self.sugg_frame, text=self.text, bg="#040405", fg="white", relief=FLAT,
                                      font=('yu gothic ui', 13, 'bold'))
                    self.sugg.place(x=0, y=0)

                    time.sleep(1)

            self.entry = str(self.search_var.get())
            t = Timer(2.0, suggestion)
            t.start()

        def Search_Submit():
            #self.flag3 = 1
            self.sugg_frame.destroy()
            #self.search_results_frame.destroy()

            self.search_results_frame = Frame(self.mainframe, width=700, height=500, bg='#040405')
            self.search_results_frame.place(x=120, y=180)
            #if(self.flag2 == 0):
            self.entry = str(self.search_var.get())
            search1 = ()
            df = pd.read_csv('data//books.csv',
                             usecols=['title', 'authors', 'average_rating', 'isbn13', '  num_pages', 'publication_date',
                                      'publisher'])
            #with open("data//dictionary", "rb") as fp:
            #    dict = pickle.load(fp)
            '''if self.search in dict:
                search1 = dict[self.search][0] + "|" + dict[self.search][1] + "|" + dict[self.search][2] + "|" + dict[self.search][3] + "|" + dict[self.search][4] + "|" + dict[self.search][5] + "|" + dict[self.search][6] + "|" + dict[self.search][7] + "|" + dict[self.search][8] + "|" + dict[self.search][9]
                result=df.loc[df['title'].str.contains(self.search + "|" + search1, case=False)]
                print(result)
                return
            else:
                for words in dict.keys():
                    for word in dict[words]:
                        if word == self.search:
                            self.search = words
                            self.flag2 = 1
                            Search_Submit()

                return'''
            Print = []
            for title in df['title']:
                if self.entry in title.lower():
                    Print.append(str(title))
            length = len(self.entry)
            nline = ""
            for i in range(length):
                count=0
                nw=""
                if self.entry[i]==self.entry[i-1]:
                    continue
                for letter in self.entry:
                    count = count + 1
                    if count == i:
                        continue
                    if letter == ' ':
                        nline += nw
                        nw = ""
                        continue
                    nw = nw + letter
                nline += nw
            for title in df['title']:
                if nline in title.lower():
                    Print.append(title)

            for i in range(length):
                nw=""
                for j in range(length):
                    if i==j:
                        nw+=self.entry[j]
                    nw += self.entry[j]
                for title in df['title']:
                    if nw in title.lower():
                        Print.append(str(title))

            vowels = ['a', 'e', 'i', 'o', 'u']
            for let in vowels:
                for i in range(length):
                    nw=""
                    for j in range(length):
                        if i==j:
                            nw+=let
                        nw+=self.entry[j]
                    for title in df['title']:
                        if nw in title.lower():
                            Print.append(str(title))



            y = 20
            for var in Print:
                if y>270:
                    break
                self.label = Label(self.search_results_frame, text=var, font=('yu gothic ui', 15, 'bold'),
                                 bg='#040405', fg='white')
                y = y + 50
                self.label.place(x=10, y=y)
            for var in Print:
                print(Print)

        def Home():
            self.lgn_frame.destroy()
            self.frame = Frame(self.window, bg='#040405', width='1100', height='70')
            self.frame.place(x=140, y=70)

            self.home = Button(self.frame, text='Home', bg='#040405', font=('yu gothic ui', 18, 'bold'), fg='white', width=5, height=1, relief="flat")
            self.home.place(x=30, y=3)

            self.search = Button(self.frame, text='Search', bg='#040405', font=('yu gothic ui', 18, 'bold'), fg='white',
                               width=7, height=1, relief="flat", command=Search)
            self.search.place(x=130, y=3)

            self.contact = Button(self.frame, text='Contact', bg='#040405',
                                  font=('yu gothic ui', 18, 'bold'), fg='white', width=8, height=1, relief="flat")
            self.contact.place(x=240, y=3)

            self.logout = Button(self.frame, text='Log Out', bg='#040405', font=('yu gothic ui', 18, 'bold'),
                                  fg='white', command=Logout,
                                  width=10, height=1, relief="flat")
            self.logout.place(x=940, y=3)

            self.mainframe = Frame(self.window, bg="#040405", width='1100', height='550')
            self.mainframe.place(x=140, y=180)

        def Logout():
            self.frame.destroy()
            self.mainframe.destroy()
            Login()

        if self.flag == 0:
            self.flag = 1
            Login()

    def show(self):
        self.hide_button = Button(self.lgn_frame, image=self.hide_image, command=self.hide, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.hide_button.place(x=860, y=self.y_val)
        self.password_entry.config(show='')

    def hide(self):
        self.show_button = Button(self.lgn_frame, image=self.show_image, command=self.show, relief=FLAT,
                                  activebackground="white", borderwidth=0, background="white", cursor="hand2")
        self.show_button.place(x=860, y=self.y_val)
        self.password_entry.config(show='*')


def login():
    window = Tk()
    LoginPage(window)
    window.mainloop()


if __name__ == '__main__':
    login()