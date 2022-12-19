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
from selenium.common.exceptions import NoSuchElementException

# 기본 변수 설정
t_table = [0,110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800,830,860,890,920]
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
        car_info = lblCar.configure(text="선택하신 차량번호는 {}".format(car_number))
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
    tdelta = otime - itime
    memo = browser.find_element(By.XPATH, '//*[@id="memo"]')
    print(tdelta, reason, memo)
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
def divMin30():
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
    tdelta = otime - itime + 30
    memo = browser.find_element(By.XPATH, '//*[@id="memo"]')
    print(tdelta, reason, memo)
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
def divHr1():
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
    tdelta = otime - itime + 50
    memo = browser.find_element(By.XPATH, '//*[@id="memo"]')
    print(tdelta, reason, memo)
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
# GUI
root = Tk()
root.iconbitmap("./favicon.ico")
root.title("주차 자동 등록")
root.geometry("300x700")
frame1 = tkinter.Frame(root, relief="solid") # 1번 프레임 좌측에 배치
frame1.pack(side="top", fill="x", expand=True)
# frame1.place(x=0,y=0)
frame2 = tkinter.Frame(root, relief="solid") # 2번 프레임 우측에 배치
frame2.pack(side="bottom", fill="y", expand=True)
# frame2.place(x=120,y=0)
# frame3 = tkinter.Frame(root, relief="solid") # 2번 프레임 우측에 배치
# frame3.pack(side="bottom", fill="both", expand=True)

# 프레임 1
myLabel1 = Label(frame1, text = "아래에 차량번호를 입력해주세요!")
myLabel2 = Label(frame1, text = "주차 차량 리스트")
carNumEntry = Entry(frame1)
carList = Listbox(frame1)
btn_search = Button(frame1, text="검색(10초 정도 소요됩니다.)", command=search_car)
btn_select = Button(frame1, text="선택", command=select_car)

myLabel1.pack(padx= 10, pady=5)
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
btn0 = Button(frame2, text="10분 안에 나가요", command=divMin10)
btn1 = Button(frame2, text="30분 안에 나가요", command=divMin30)
btn2 = Button(frame2, text="1시간 안에 나가요", command=divHr1)

lblCar.pack(padx= 10, pady=20)
btn0.pack(padx= 10, pady=20)
btn1.pack(padx= 10, pady=20)
btn2.pack(padx= 10, pady=20)

# 프레임3 
btn3 = Button(frame2, text="단체 등록", bg = "green", command=enrollGrp)
btn3.pack(padx= 10, pady=10)

root.mainloop()
print("함수 외부에서 차량 번호는 : [{}]".format(car_number))