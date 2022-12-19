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
from selenium.common.exceptions import NoSuchElementException

t_table = [0,110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800,830,860,890,920]
car_number = "167머5834"
def min120():
    print("2시간 버튼 클릭")
def min60():
    print("1시간 버튼 클릭")
def min30():
    print("30분 버튼 클릭")
def login():
    global browser
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 쓸모없는 로그 삭제
    browser = webdriver.Chrome(options=options)
    browser.maximize_window() # 창 확대
    browser.get("http://uspace.awp1.co.kr/login")
    # 유스페이스 주차관리 아이디/비번
    uspaces = ['2b-704','20200801'] # 유스페이스 주차장 관리자 아이디와 비밀번호 List에 저장
    # 상기 정보를 이용하여 로그인
    input_id = browser.find_element(By.XPATH,'//*[@id="userId"]')
    input_pw = browser.find_element(By.XPATH,'//*[@id="loginForm"]/li[3]/input')
    input_id.send_keys(uspaces[0])
    input_pw.send_keys(uspaces[1])
    close_btn= browser.find_element(By.XPATH,'//*[@id="modal-window"]/div/div/div[3]/a[2]')
    login_btn= browser.find_element(By.CLASS_NAME,'login_area_btn')
    close_btn.click()
    login_btn.click()
    time.sleep(2)
def check():
    while True:
        try:
            browser.find_element(By.XPATH,'//*[@id="gridDtl"]/div[2]/table/tbody/tr[2]/td[5]/input')
            pg.alert("해당 차량은 이미 등록되어있습니다.")
            # return False
            exit()
        except NoSuchElementException:
            pass
            return False

# 웹 자동화 로직 수행
reason = pg.prompt(text = "사유를 입력하세요", title='사유' )# 주차 사유 입력
login()
input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
input_car_number.send_keys(car_number)
search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
search_btn.click()
time.sleep(2)
# 예외처리
# alEn = browser.find_element(By.XPATH,'//*[@id="gridDtl"]/div[2]/table/tbody/tr[2]/td[5]/input').isDisplayed()
  
check()
# 시간 계산
time_parking = browser.find_element(By.XPATH,'//*[@id="entryDate"]').text
time_in = time_parking[11:]
now = datetime.now()
time_out = str(now.time())[0:8]
itime = int(time_in[0:2])*60 + int(time_in[3:5])
otime = int(time_out[0:2])*60 + int(time_out[3:5])
tdelta = otime - itime
memo = browser.find_element(By.XPATH, '//*[@id="memo"]')
print(tdelta, reason)
for j in range(1,28):
    if int(t_table[j-1]) < tdelta <= int(t_table[j]): # 110~920까지 차례로 대입
        std = int(t_table[j]-110)/60
        stupid = int(t_table[j]-110)%60
        if int(t_table[j]) <= 110:
            min120()
        elif int(t_table[j]-110)%60 == 0:
            min120()
            for k in range(int(std)):
                min60()
        elif int(t_table[j]-110)%60 != 0:
            min120()
            min30()
            for k in range(int(std)):
                min60()
    else:
        pass