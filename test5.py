import tkinter as tk
from tkinter import *

def check_data():
    if user_id.get() == "Passing" and password.get() == "story":
        newwin = Tk()
        tk.Label(newwin, text="Welcome to " + user_id.get()).grid(row = 0, column = 0, padx = 10, pady = 10)
        newwin.mainloop()
        print("Logged IN Successfully")
    else:
        print("Check your Username/Password")
window =Tk()
user_id, password = StringVar(), StringVar()

tk.Label(window, text = "Username : ").grid(row = 0, column = 0, padx = 10, pady = 10)
tk.Label(window, text = "Password : ").grid(row = 1, column = 0, padx = 10, pady = 10)
tk.Entry(window, textvariable=user_id).grid(row = 0, column = 1, padx = 10, pady = 10)
tk.Entry(window, textvariable=password, show = "*").grid(row = 1, column = 1, padx = 10, pady = 10)
tk.Button(window, text = "Login", command = check_data).grid(row = 2, column = 1, padx = 10, pady = 10)

window.mainloop()

# window = tkinter.Tk()

# window.title("Frame Change")
# window.geometry("600x600+200+200")

# frame1 = tkinter.Frame(window)
# frame2 = tkinter.Frame(window)
# frame3 = tkinter.Frame(window)

# frame1.grid(row=0, column=0, sticky="nsew")
# frame2.grid(row=0, column=0, sticky="nsew")
# frame3.grid(row=0, column=0, sticky="nsew")

# def openFrame(frame):
#     frame.tkraise()
    
# btnToFrame1 = tkinter.Button(frame3, text="Change to Frame1", padx=10, pady=10,command=lambda:[openFrame(frame1)])
# btnToFrame2 = tkinter.Button(frame1, text="Change to Frame2", padx=10, pady=10,command=lambda:[openFrame(frame2)])
# btnToFrame3 = tkinter.Button(frame2, text="Change to Frame3", padx=10, pady=10,command=lambda:[openFrame(frame3)])

# btnToFrame1.pack()
# btnToFrame2.pack()
# btnToFrame3.pack()

# openFrame(frame1)
# window.mainloop()
