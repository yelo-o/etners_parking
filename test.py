import time
from datetime import datetime
import tkinter as tk
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
from selenium.common.exceptions import NoSuchElementException

# 가짜 버튼 입력 함수
def min120():
    print("2시간 버튼 클릭")
def min60():
    print("1시간 버튼 클릭")
def min30():
    print("30분 버튼 클릭")
    
# 알고리즘 테스트
t_table = [0,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570,600,630,660,690,720,750,780,810,840,870,900,930]

# {}분후에 나가도록 설정
# td = 90
# tdelta = td + 30
# 60분
td = 110 # 현재시간 - 입차시간
st = input("몇 분 후에 나가실 건가요?")
tdelta = td + int(st)
tt = tdelta%60 # 시간과 분으로 변환
tx = int(tdelta/60)
print("현재 {}분 경과했고, {}분 후에 나갈 예정입니다.".format(td, int(st)))
print('{}분 후는 입차시간으로 부터 {}분인 {}시간 {}분 경과할 예정입니다.'.format(int(st), tdelta, tx, tt))
for j in range(1,28):
            # 0 < 110 <= 120
        if int(t_table[j-1]) < tdelta <= int(t_table[j]): # 110~920까지 차례로 대입
            std = int(t_table[j]-120)/60
            print("기준은 {}시간입니다.".format(std))
            if int(t_table[j]) <= 120:
                min120()
            elif int(t_table[j]-120)%60 == 0:
                min120()
                for k in range(int(std)):
                    min60()
            elif int(t_table[j]-120)%60 != 0:
                min120()
                min30()
                for k in range(int(std)):
                    min60()
        else:
            pass


# GUI 부분
root = ttk.Window()
root.iconbitmap("./favicon.ico")
root.title("주차 자동 정산")
frame1 = ttk.Frame(root, width=700, height=500, bootstyle = "default") # 1번 프레임 좌측에 배치
frame1.pack(fill=tk.X, expand=True)
frame2 = ttk.Frame(root, width=700, height=100)
frame2.pack(fill=tk.X, expand=True)

# 프레임 1의 첫번째 열
sep1 = ttk.Separator(frame1, bootstyle = "danger")
myLabel1 = Label(frame1, text = "아래에 차량번호를 입력해주세요!")
myLabel2 = Label(frame1, text = "주차 차량 리스트")
carNumEntry = ttk.Entry(frame1, bootstyle="default")
carList = Listbox(frame1)
btn_search = ttk.Button(frame1, text="검색(10초 정도 소요됩니다.)", bootstyle="warning" ,command=search_car)
btn_select = ttk.Button(frame1, text="선택", bootstyle="warning" ,command=select_car)

sep1.grid(row=0, column=0, sticky="ew",pady=5)
myLabel1.grid(row=1, column=0, sticky="nsew",padx=5, pady=5)
carNumEntry.grid(row=2, column=0, sticky="ns",padx=5, pady=5)
btn_search.grid(row=3, column=0, sticky="ns",padx=5, pady=5)
myLabel2.grid(row=4, column=0, sticky="nsew",padx=5, pady=5)
carList.grid(row=5, column=0, sticky="nsew",padx=5, pady=5)
btn_select.grid(row=6, column=0, sticky="ns",padx=5, pady=5)


# 프레임1의 두번째 열
sep2 = ttk.Separator(frame1, bootstyle = "danger")
lblCar = ttk.Label(frame1, text="                차량번호", bootstyle="inverse-dark")
btn0 = ttk.Button(frame1, text="10분 안에 나가요", bootstyle="primary" ,command=divMin10)
btn1 = ttk.Button(frame1, text="30분 안에 나가요", bootstyle="primary" ,command=divMin30)
btn2 = ttk.Button(frame1, text="1시간 안에 나가요", bootstyle="primary" ,command=divHr1)

sep2.grid(row=0, column=1, sticky="ew",pady=5)
lblCar.grid(row=2, column=1, sticky="nsew", padx=5, pady=5, ipadx=30, ipady=10)
btn0.grid(row=4, column=1, sticky="nsew", padx=5, pady=5)
btn1.grid(row=5, column=1, sticky="ew", padx=5, pady=5)
btn2.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)

# 프레임2
sep3 = ttk.Separator(frame2, bootstyle = "info")
sep3.pack(fill=ttk.X, pady=10)
btn3 = ttk.Button(frame2, text="단체 등록", bootstyle = SUCCESS, command=enrollGrp)
btn3.pack(padx=100,pady=20)

root.mainloop()