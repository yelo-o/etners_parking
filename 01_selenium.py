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

# 티킨터
root = Tk()
root.title("티킨터 테스트")



class GUI:
    def __init__(self, master):
        self.myLabel1 = Label(master, text = "아래에 차량번호를 입력해주세요!")
        self.myLabel2 = Label(master, text = "주차 차량 리스트")
        self.carNumEntry = Entry(master)
        self.carList = Listbox(master)
        self.btn_search = Button(master, text="검색", \
            command=self.search_car)
        self.btn_select = Button(master, text="선택", \
            command=self.select_car)

        self.myLabel1.pack(padx= 10, pady=5)
        self.carNumEntry.pack(padx= 10, pady=5)
        self.btn_search.pack(padx= 10, pady=5)
        self.myLabel2.pack(padx= 10, pady=10)
        self.carList.pack(padx= 10, pady=5)
        self.btn_select.pack(padx= 10, pady=5)

    def min120():
        print("2시간 버튼 클릭")
    def min60():
        print("1시간 버튼 클릭")
    def min30():
        print("30분 버튼 클릭")

    def search_car(self): 
        self.car_number = self.carNumEntry.get()
        options = webdriver.ChromeOptions()
        # options.add_argument("headless") # 창 숨기는 옵션 추가
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        browser = webdriver.Chrome(options=options)
        browser.get("http://uspace.awp1.co.kr/login")
        uspaces = ['2b-704','20200801']
        input_id = browser.find_element(By.XPATH,'//*[@id="userId"]')
        input_pw = browser.find_element(By.XPATH,'//*[@id="loginForm"]/li[3]/input')
        input_id.send_keys(uspaces[0])
        input_pw.send_keys(uspaces[1])
        close_btn= browser.find_element(By.XPATH,'//*[@id="modal-window"]/div/div/div[3]/a[2]')
        login_btn= browser.find_element(By.CLASS_NAME,'login_area_btn')
        close_btn.click()
        login_btn.click()
        time.sleep(2)
        input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
        input_car_number.send_keys(self.car_number)
        search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
        search_btn.click()
        time.sleep(2)
        list_car = browser.find_elements(By.XPATH,'//*[@id="gridMst"]/div[2]/table/tbody')
        sim_list=[]
        for car in list_car:
            for c in car.text.split('\n'):
                a = c.split()[1]
                sim_list.append(a)
                self.carList.insert(END, a)
        browser.quit() # 브라우저 닫기

    def select_car(self):
        self.car_number = str(self.carList.get(self.carList.curselection()))
        return self.car_number

class AutoWeb(GUI):
    def __init__(self):
        GUI.__init__(self, root)
        self.car_number = car_number
        print(self.car_number)
GUI(root)
# GetNumberAll()
root.mainloop()

print(car_number)