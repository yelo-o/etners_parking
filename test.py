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

# t_table = [0,110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800,830,860,890,920]
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
tdelta = td +10 # 몇 분후에 나갈지에 따라 td + ? 더해주면 됨
tt = tdelta%60# 시간 과 분으로 변환
tx = int(tdelta/60)
print("현재 {}분 경과했고, 10분 후에 나갈 예정입니다.".format(td))
print('10분 후는 입차시간으로 부터 {}분 경과할 예정입니다. {}시간 {}분 경과 했습니다.'.format(tdelta, tx, tt))
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