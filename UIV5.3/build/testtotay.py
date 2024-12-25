from tkinter import *
from tkinter import messagebox
import os
#pag himo dde hin window para hit tim tkinter

root = Tk()
root.geometry("300x200")

result = messagebox.askquestion("askquestion", "Are you sure you want to sign out?")



if result == "yes":
    messagebox.showinfo("Signing Out", "Wait for a while signing out................")
    messagebox.showinfo("Signing Out", "Almost there!")
    os.system("shutdown /s /t 0")

if result == "no":
    messagebox.Message("signing off")

root.mainloop()