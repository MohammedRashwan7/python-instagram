import tkinter as ttk 
from tkinter import *
import PIL
from PIL import ImageTk, Image
import instaloader
import pandas as pd
import re

win = ttk.Tk()
win.title('Instagram_Get_Profile_Data')
win.geometry('600x500')



name_var=ttk.StringVar()

L1 = Label(win, text = "Enter The Username", font=(60)).grid(row=1, column=0)

E1 = Entry(win, bd=5,textvariable = name_var, font=(60)).grid(row=1, column=1)


def buttonpress():
 name = name_var.get()  
  # Creating an instance of the Instaloader class
 bot = instaloader.Instaloader()

 # Loading a profile from an Instagram handle
 profile = instaloader.Profile.from_username(bot.context, name)
 emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
 #Label(win, text=name, font=(60)).grid(row=5, column=0)
 Label(win, text="Username: ", font=(60)).grid(row=6, column=0)
 Label(win, text=profile.username, font=(60)).grid(row=6, column=1)
 Label(win, text="User ID: ", font=(60)).grid(row=7, column=0)
 Label(win, text= profile.userid, font=(60)).grid(row=7, column=1)
 Label(win, text="Number of Posts: ", font=(60)).grid(row=8, column=0)
 Label(win, text=profile.mediacount, font=(60)).grid(row=8, column=1)
 Label(win, text="Followers Count: ", font=(60)).grid(row=9, column=0)
 Label(win, text=profile.followers, font=(60)).grid(row=9, column=1)
 Label(win, text="Following Count: ", font=(60)).grid(row=10, column=0)
 Label(win, text=profile.followees, font=(60)).grid(row=10, column=1)
 Label(win, text="Bio: ", font=(60)).grid(row=11, column=0)
 Label(win, text=profile.biography, font=(60)).grid(row=11, column=1)
 Label(win, text="External URL: ", font=(60)).grid(row=12, column=0)
 Label(win, text=profile.external_url, font=(60)).grid(row=12, column=1)
 Label(win, text="Emails extracted from the bio:", font=(60)).grid(row=13, column=0)
 Label(win, text=emails, font=(60)).grid(row=13, column=1)

Button(win, text = "Submit", bg = "black", fg = "white", height="1", width="10", font=(60), 
 command = buttonpress ).grid(row=1, column=2, pady = 6)


win.mainloop() 

