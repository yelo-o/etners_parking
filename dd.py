import time
from datetime import datetime
import tkinter as Tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import openpyxl
import sys, os
import pyautogui as pg
#
def search_car():
    pass
def select_car():
    pass
def divMin10():
    pass
def divMin30():
    pass
def divHr1():
    pass
def enrollGrp():
    pass
#
root = ttk.Window()
style = ttk.Style('darkly')
frame1 = ttk.Frame(bootstyle="light")
frame1.pack(side="left",fill='both', expand=True)
frame2 = ttk.Frame(bootstyle="light")
frame2.pack(side="right",fill='both', expand=True)
frame3 = ttk.Frame(bootstyle="light")
frame3.pack(side="bottom",fill='none', expand=True)
root.iconbitmap("./favicon.ico")
root.title("주차 자동 등록")
root.geometry("300x900")

# 프레임 1
myLabel1 = Label(frame1, text = "아래에 차량번호를 입력해주세요!")
myLabel2 = Label(frame1, text = "주차 차량 리스트")
carNumEntry = Entry(frame1)
carList = Listbox(frame1)
btn_search = ttk.Button(frame1, text="검색(10초 정도 소요)", bootstyle = SUCCESS, command=search_car)
btn_select = ttk.Button(frame1, text="선택", bootstyle = SUCCESS, command=select_car)

myLabel1.pack(padx= 10, pady=0)
carNumEntry.pack(padx= 10, pady=5)
btn_search.pack(padx= 10, pady=5)
myLabel2.pack(padx= 10, pady=10)
carList.pack(padx= 10, pady=5)
btn_select.pack(padx= 10, pady=5)

# myLabel1.place(x=0,y=0)
# carNumEntry.place(x=0, y=10)
# btn_search.place(x=0, y=20)
# myLabel2.place(x=0, y=30)
# carList.place(x=0, y=100)
# btn_select.place(x=0, y=200)

# 프레임2
lblCar = Label(frame2, text = "차량번호")
btn0 = ttk.Button(frame2, text="10분 안에 나가요", bootstyle=DARK, command=divMin10)
btn1 = ttk.Button(frame2, text="30분 안에 나가요", bootstyle=DARK, command=divMin30)
btn2 = ttk.Button(frame2, text="1시간 안에 나가요", bootstyle=DARK, command=divHr1)

lblCar.pack(padx= 10, pady=40)
btn0.pack(padx= 10, pady=40)
btn1.pack(padx= 10, pady=40)
btn2.pack(padx= 10, pady=40)

# 프레임3 
btn3 = ttk.Button(frame3, text="단체 등록", bootstyle = WARNING, command=enrollGrp)
btn3.pack(padx= 10, pady=10)

root.mainloop()