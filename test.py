import time
from datetime import datetime
from tkinter import *
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as pg
import openpyxl
import sys, os

# 가짜 버튼 입력 함수
def min120():
    print("2시간 버튼 클릭")
def min60():
    print("1시간 버튼 클릭")
def min30():
    print("30분 버튼 클릭")
    
# 함수 정의
def selection1():
    
# pyinstaller 셀레니움 저장용
if  getattr(sys, 'frozen', False): 
    chromedriver_path = os.path.join(sys._MEIPASS, "chromedriver.exe") # 실행 파일과 크롬드라이버가 같은 폴더에 있다는 뜻
    driver = webdriver.Chrome(chromedriver_path)
else:
    driver = webdriver.Chrome()
# tkinter 실행하여 어떤 모드로 실행할지 선택하는 버튼 할당
root = Tk()
root.title("nado")
root.geometry("640x480")
listbox = Listbox(root)
btn1 = Button(root, text="개별 선택", command = lambda :[selection1(), root.quit()])
btn2 = Button(root, text="단체 선택", command = lambda :[selection2(), root.quit()])
# 개별 입력
car_number = pg.prompt(text = "차량번호를 입력하세요", title='번호') # 차량 넘버 입력
reason = pg.prompt(text = "사유를 입력하세요", title='사유')# 주차 사유 입력
root = Tk()
root.title("nado")
root.geometry("640x480")
listbox = Listbox(root)

t_table = [0,110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800,830,860,890,920]
tdelta = 180
for i in range(1,28):
    if int(t_table[i-1]) < tdelta <= int(t_table[i]): # 110~920까지 차례로 대입
        std = int(t_table[i]-110)/60
        if int(t_table[i]) <= 110:
            min120()
        elif isinstance(int(t_table[i]-110)/60, int) == True:
            min120()
            for j in range(int(std)):
                min60()
        elif isinstance(int(t_table[i]-110)/60, int) == False:
            min120()
            min30()
            for j in range(int(std)):
                min60()
    else:
        pass
                