import time
from datetime import datetime
from tkinter import *
from tkinter import filedialog
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import openpyxl

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "C:/Users/flyordig/Desktop/mgpy/etners_parking",title = "엑셀 파일을 골라주세요.",filetypes = (("excel files","*.xlsx"),("all files","*.*")))
print (root.filename)
ssfile = root.filename
root.withdraw()
# 가짜 버튼 입력 함수
def min120():
    print(car_num)
    print(reason)
    print("2시간 버튼 클릭")
def min60():
    print("1시간 버튼 클릭")
def min30():
    print("30분 버튼 클릭")

# 셀레니움 실행
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"]) # 쓸모없는 로그 삭제
browser = webdriver.Chrome(options=options)
browser.get("http://uspace.awp1.co.kr/login")
# 비밀번호는 보안을 위해 로컬 파일에 저장합니다. (pw.txt 파일 참조)
f = open("pw.txt", 'r')
uspaces = f.readlines() # 유스페이스 주차장 관리자 아이디와 비밀번호 List에 저장
uspaces = [uspace.rstrip('\n') for uspace in uspaces]
f.close()
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
# filename = 'parking_data.xlsx' # 열고 싶은 파일 이름 저장

book = openpyxl.load_workbook(ssfile) # 엑셀 파일 열기
ws = book.active # 시트 활성화
row_max = ws.max_row # row_max = 엑셀 파일 내 행숫자를 읽음 ※ 주의 0부터 읽는거 아님 1부터 읽음
data = [] # 빈 리스트 생성
btn = [120,60,30]
memo = browser.find_element(By.XPATH, '//*[@id="memo"]')
t_table = [0,110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800,830,860,890,920]
sheet = book.worksheets[0]
for i in range(row_max-1):
    for row in ws.rows:
        data.append([row[i].value, row[i+1].value])
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
            print("std의 값은", std)
            print("int(std)의 값은", int(std))
            print("stupid의 값은", stupid)
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