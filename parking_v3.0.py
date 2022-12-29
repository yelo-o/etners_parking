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

# 기본 변수 설정 (분)
t_table = [0,120,150,180,210,240,270,300,330,360,390,420,450,480,510,540,570,600,630,660,690,720,750,780,810,840,870,900,930]
# 진짜 버튼 입력 함수
def min120():
    btn_2hr = browser.find_element(By.XPATH,'//*[@id="1"]')
    btn_2hr.click()
    time.sleep(2)
    btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
    btn_ok.click()
    time.sleep(2)
def min60():
    memo = browser.find_element(By.XPATH, '//*[@id="memo"]')
    memo.send_keys(reason)
    time.sleep(1)
    btn_1hr = browser.find_element(By.XPATH,'//*[@id="3"]')
    btn_1hr.click()
    time.sleep(2)
    btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
    btn_ok.click()
    time.sleep(2)
def min30():
    memo = browser.find_element(By.XPATH, '//*[@id="memo"]')
    memo.send_keys(reason)
    time.sleep(1)
    btn_30min = browser.find_element(By.XPATH, '//*[@id="2"]')
    btn_30min.click()
    time.sleep(2)
    btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
    btn_ok.click()
    time.sleep(2)

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
            # browser.quit()
            exit()
        except NoSuchElementException:
            pass
            return False

def search_car():
    carList.delete(0, END)
    car_number = carNumEntry.get()
    options = webdriver.ChromeOptions()
    options.add_argument("headless") # 창 숨기는 옵션 추가
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
    time.sleep(1)
    input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
    input_car_number.send_keys(car_number)
    search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
    search_btn.click()
    time.sleep(1)
    list_car = browser.find_elements(By.XPATH,'//*[@id="gridMst"]/div[2]/table/tbody')
    sim_list=[]
    for car in list_car:
        for c in car.text.split('\n'):
            a = c.split()[1]
            sim_list.append(a)
            carList.insert(END, a)
    browser.quit() # 브라우저 닫기
def select_car():
        global car_number
        car_number = str(carList.get(carList.curselection()))
        car_info = lblCar.configure(text="선택한 차량번호 : {}".format(car_number))
        print("버튼 함수 안에서 차량 번호는 : [{}]".format(car_number))
        return car_number
def divMin10():
    global reason
    reason = pg.prompt(text = "사유를 입력하세요", title='사유' )# 주차 사유 입력
    login()
    input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
    input_car_number.send_keys(car_number)
    search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
    search_btn.click()
    time.sleep(2)
    # 이미 등록이 되어있는지 확인
    check()
    # 시간 계산
    time_parking = browser.find_element(By.XPATH,'//*[@id="entryDate"]').text
    time_in = time_parking[11:]
    now = datetime.now()
    time_out = str(now.time())[0:8]
    itime = int(time_in[0:2])*60 + int(time_in[3:5])
    otime = int(time_out[0:2])*60 + int(time_out[3:5])
    tt = 10
    tx = otime - itime
    tdelta = tx + tt
    memo = browser.find_element(By.XPATH, '//*[@id="memo"]')
    print("현재 {}분 경과했고, {}분 후에 나갈 예정입니다.".format(tx, tt))
    print("{}분 후는 입차시간으로부터 {}분인 {}시간 {}분 경과할 예정입니다.".format(tt,tdelta, int(tdelta/60),tdelta%60))
    for j in range(1,28):
        if int(t_table[j-1]) < tdelta <= int(t_table[j]): # 110~920까지 차례로 대입
            std = int(t_table[j]-120)/60
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
    pg.alert("주차 등록이 완료되었습니다.")
def divOther():
    global tz, reason
    tz = int(timeEntry.get())
    print(tz, type(tz))
    reason = pg.prompt(text = "사유를 입력하세요", title='사유' )# 주차 사유 입력
    login()
    input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
    input_car_number.send_keys(car_number)
    search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
    search_btn.click()
    time.sleep(2)
    # 이미 등록이 되어있는지 확인
    check()
    # 시간 계산
    time_parking = browser.find_element(By.XPATH,'//*[@id="entryDate"]').text
    time_in = time_parking[11:]
    now = datetime.now()
    time_out = str(now.time())[0:8]
    itime = int(time_in[0:2])*60 + int(time_in[3:5])
    otime = int(time_out[0:2])*60 + int(time_out[3:5])
    tx = otime - itime
    tdelta = tx + tz
    memo = browser.find_element(By.XPATH, '//*[@id="memo"]')
    print("현재 {}분 경과했고, {}분 후에 나갈 예정입니다.".format(tx, tz))
    print("{}분 후는 입차시간으로부터 {}분인 {}시간 {}분 경과할 예정입니다.".format(tz,tdelta, int(tdelta/60),tdelta%60))
    for j in range(1,28):
        if int(t_table[j-1]) < tdelta <= int(t_table[j]): # 110~920까지 차례로 대입
            std = int(t_table[j]-120)/60
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
    pg.alert("주차 등록이 완료되었습니다.")

def enrollGrp():
    root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/flyordig/Desktop/mgpy/etners_parking",title = "주차 데이터가 있는 엑셀 파일을 골라주세요.",filetypes = (("excel files","*.xlsx"),("all files","*.*")))
    ssfile = root.filename
    root.withdraw()
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 쓸모없는 로그 삭제
    global browser
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
    book = openpyxl.load_workbook(ssfile) # 엑셀 파일 열기
    ws = book.active # 시트 활성화
    data = [] # 빈 리스트 생성
    sheet = book.worksheets[0]
    for row in ws.rows:
        data.append([row[0].value,row[1].value])
    for i in range(len(data)):
        car_num = data[i][0]
        global reason
        reason = data[i][1]
        input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
        input_car_number.clear()
        input_car_number.send_keys(car_num)
        search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
        search_btn.click()
        time.sleep(2)
        # # 이미 등록이 되어있는지 확인 <----------- 추후 확인 필요
        check()
        # 시간 계산
        time_parking = browser.find_element(By.XPATH,'//*[@id="entryDate"]').text
        time_in = time_parking[11:]
        now = datetime.now()
        time_out = str(now.time())[0:8]
        itime = int(time_in[0:2])*60 + int(time_in[3:5])
        otime = int(time_out[0:2])*60 + int(time_out[3:5])
        tdelta = otime - itime
        print(tdelta)
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
textEX = tk.StringVar()
textEX.set("60")
sep2 = ttk.Separator(frame1, bootstyle = "danger")
lblCar = ttk.Label(frame1, text="                차량번호", bootstyle="inverse-dark")
btn0 = ttk.Button(frame1, text="10분 안에 나가요", bootstyle="primary" ,command=divMin10)
lblTime = ttk.Label(frame1, text="또는 몇 분 후에 나가실지 \n아래에 숫자 기입 후 클릭해주세요.", bootstyle="primary")
timeEntry = ttk.Entry(frame1, textvariable = textEX, bootstyle="default")
btn1 = ttk.Button(frame1, text="분 후에 나가요", bootstyle="primary" ,command=divOther)

sep2.grid(row=0, column=1, sticky="ew",pady=5)
lblCar.grid(row=2, column=1, sticky="nsew", padx=5, pady=5, ipadx=30, ipady=10)
btn0.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
lblTime.grid(row=5, column=1, sticky="nsew", ipadx=5, ipady=5)
timeEntry.grid(row=6, column=1, sticky="nsew", padx=5, pady=5)
btn1.grid(row=7, column=1, sticky="ew", padx=5, pady=5)

# 프레임2
sep3 = ttk.Separator(frame2, bootstyle = "info")
sep3.pack(fill=ttk.X, pady=10)
btn3 = ttk.Button(frame2, text="단체 등록", bootstyle = SUCCESS, command=enrollGrp)
btn3.pack(padx=100,pady=20)

root.mainloop()