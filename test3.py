import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# 가짜 버튼 입력 함수
def min120():
    print("2시간 버튼 클릭")

def min60():
    print("1시간 버튼 클릭")

def min30():
    print("30분 버튼 클릭")
    

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
t_table = [0,110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800,830,860,890,920]
car_num = '구냥'
reason = '테스트'
input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
input_car_number.clear()
input_car_number.send_keys(car_num)
search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
search_btn.click()
time.sleep(2)

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