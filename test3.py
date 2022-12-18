import time
from datetime import datetime
import tkinter
from tkinter import *
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import openpyxl
import sys, os
import pyautogui as pg

class button:
    def __init__(self):
        # 가짜 버튼 입력 함수
        def min120():
            print("2시간 버튼 클릭")

        def min60():
            print("1시간 버튼 클릭")

        def min30():
            print("30분 버튼 클릭")

root = Tk()
root.title("티킨터 테스트")
# root.geometry('400x400')
class Window:
    def __init__(self, master):
        myFrame = Frame(master) # Frame(root) 대신에 Frame(master)
        myFrame.pack()
        self.myLabel1 = Label(master, text='차량번호 전부 알아요!')
        self.myLabel2 = Label(master, text='차량번호 일부만 알아요ㅠㅠ')
        self.myLabel1.pack(pady=20)
        self.myLabel2.pack(pady=20)

        self.myButton = Button(master, text = "Click Me!", command = self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("첫번째 버튼")
class autoEnroll:
    def __init__(self, car_number, reason):
        self.car_number = car_number
        self.reason = reason
    
class Elder2:
    def __init__(self, master):
        myFrame = Frame(master) # Frame(root) 대신에 Frame(master)
        myFrame.pack()

        self.myButton = Button(master, text = "Click Me!", command = self.clicker)
        self.myButton.pack(pady=20)

    def clicker(self):
        print("두번째 버튼")

e = Window(root)
e = Window(root)
# ee = Elder2(root)
root.mainloop()

        # lbl1 = Label(window, text='차량번호 전부 알아요!').grid(row=0, column=1, padx=10, pady=10)
        # lbl2 = Label(window, text='차량번호 일부만 알아요ㅠㅠ').grid(row=0, column=1, padx=10, pady=10)
        # tkinter.Label(window, text='차량번호 전부 알아요!').grid(row=0, column=1, padx=10, pady=10)
        # tkinter.Label(window, text='차량번호 일부만 알아요ㅠㅠ').grid(row=0, column=1, padx=10, pady=10)