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
# 글로벌 변수 설정
t_table = [0,110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800,830,860,890,920]
# 개인/단체 선택
class SelectEvent:
    def __init__(self):
        window = Tk()
        window.title("ETNERS")
        window.geometry("640x400+100+100")
        window.resizable(False, False)
        frame1 = tkinter.Frame(window) # 1번 프레임 좌측에 배치
        frame1.pack(side="left", fill="both", expand=True)
        frame2 = tkinter.Frame(window) # 2번 프레임 우측에 배치
        frame2.pack(side="right", fill="both", expand=True)
        
        btnDiv = Button(frame1, text = "1명 등록", bg = "green", command = self.processinDiv)
        btnGrp = Button(frame2, text = "단체 등록", bg = "yellow", command = self.processGrp)
        self.myLabel1 = Label( text = "아래에 차량번호를 입력해주세요!")
        self.myLabel2 = Label( text = "주차 차량 리스트")
        self.carNumEntry = Entry()
        self.carList = Listbox()
        self.btn_search = Button( text="검색", \
            command=self.search_car)
        self.btn_select = Button( text="선택", \
            command=self.select_car)
        btnDiv.pack()
        btnGrp.pack()
        window.mainloop()
        
    def processinDiv(self):
        indiv()
    def processGrp(self):
        grp()
    
# 개별 등록
class indiv:
    def __init__(self):
        def min120():
            print("2시간 추가용")
        def min60():
            print("1시간 추가용")
        def min30():
            print("30분 추가용")
        global car_number, reason
        car_number = pg.prompt(text = "차량번호를 입력하세요", title='번호') # 차량 넘버 입력
        reason = pg.prompt(text = "사유를 입력하세요", title='사유')# 주차 사유 입력
        print(car_number, reason)
        window = Tk()
        btn1 = Button(window, text = "10분 안에 나가요", bg = "white", command = self.min10)
        btn2 = Button(window, text = "30분 안에 나가요", bg = "yellow", command = self.min30)
        btn3 = Button(window, text = "1시간 안에 나가요", bg = "green", command = self.hr1)
        
        btn1.pack()
        btn2.pack()
        btn3.pack()
        window.mainloop()
    def select_car(self):
        self.car_number = str(self.carList.get(self.carList.curselection()))
        return self.car_number
        
    def min10(self):
        indiv10()
    def min30(self):
        indiv30()
    def hr1(self):
        indiv60()
        
# 10분 내에 출차
class indiv10:
    def __init__(self):
        def min120():
            btn_2hr = browser.find_element(By.XPATH,'//*[@id="1"]')
            btn_2hr.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
        def min60():
            memo.send_keys(reason)
            time.sleep(1)
            btn_1hr = browser.find_element(By.XPATH,'//*[@id="3"]')
            btn_1hr.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
        def min30():
            memo.send_keys(reason)
            time.sleep(1)
            btn_30min = browser.find_element(By.XPATH, '//*[@id="2"]')
            btn_30min.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
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
        # 차량 번호 입력
        input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
        input_car_number.send_keys(car_number)
        search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
        search_btn.click()
        time.sleep(2)
        # 시간 계산
        time_parking = browser.find_element(By.XPATH,'//*[@id="entryDate"]').text
        time_in = time_parking[11:]
        now = datetime.now()
        time_out = str(now.time())[0:8]
        itime = int(time_in[0:2])*60 + int(time_in[3:5])
        otime = int(time_out[0:2])*60 + int(time_out[3:5])
        tdelta = otime - itime
        memo = browser.find_element(By.XPATH, '//*[@id="memo"]')
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
# 30분 내 출차
class indiv30:
    def __init__(self):
        def min120():
            btn_2hr = browser.find_element(By.XPATH,'//*[@id="1"]')
            btn_2hr.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
        def min60():
            memo.send_keys(reason)
            time.sleep(1)
            btn_1hr = browser.find_element(By.XPATH,'//*[@id="3"]')
            btn_1hr.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
        def min30():
            memo.send_keys(reason)
            time.sleep(1)
            btn_30min = browser.find_element(By.XPATH, '//*[@id="2"]')
            btn_30min.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
# 1시간 내 출차
class indiv60:
    def __init__(self):
        def min120():
            btn_2hr = browser.find_element(By.XPATH,'//*[@id="1"]')
            btn_2hr.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
        def min60():
            memo.send_keys(reason)
            time.sleep(1)
            btn_1hr = browser.find_element(By.XPATH,'//*[@id="3"]')
            btn_1hr.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
        def min30():
            memo.send_keys(reason)
            time.sleep(1)
            btn_30min = browser.find_element(By.XPATH, '//*[@id="2"]')
            btn_30min.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
# 단체 등록
class grp:
    def __init__(self):
        def min120():
            btn_2hr = browser.find_element(By.XPATH,'//*[@id="1"]')
            btn_2hr.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
        def min60():
            memo.send_keys(reason)
            time.sleep(1)
            btn_1hr = browser.find_element(By.XPATH,'//*[@id="3"]')
            btn_1hr.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
        def min30():
            memo.send_keys(reason)
            time.sleep(1)
            btn_30min = browser.find_element(By.XPATH, '//*[@id="2"]')
            btn_30min.click()
            time.sleep(2)
            btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
            btn_ok.click()
            time.sleep(2)
        root = Tk()
        root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/flyordig/Desktop/mgpy/etners_parking",title = "주차 데이터가 있는 엑셀 파일을 골라주세요.",filetypes = (("excel files","*.xlsx"),("all files","*.*")))
        ssfile = root.filename
        root.withdraw()
        # 셀레니움 실행
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
        # data 받아서 차량번호(car_num) 주차사유(reason) 얻기
        book = openpyxl.load_workbook(ssfile) # 엑셀 파일 열기
        ws = book.active # 시트 활성화
        data = [] # 빈 리스트 생성
        # btn = [120,60,30]
        memo = browser.find_element(By.XPATH, '//*[@id="memo"]')
        t_table = [0,110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800,830,860,890,920]
        sheet = book.worksheets[0]
        for row in ws.rows:
            data.append([row[0].value,row[1].value])
        for i in range(len(data)):
            car_num = data[i][0]
            reason = data[i][1]
            input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
            input_car_number.clear()
            input_car_number.send_keys(car_num)
            search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
            search_btn.click()
            time.sleep(2)
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

SelectEvent() # __init__ 메소드를 호출하는 오브젝트 생성