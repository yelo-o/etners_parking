from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 함수 설정


# 자동화 브라우저 구동
browser = webdriver.Chrome()
browser.maximize_window() # 창 확대
browser.get("http://uspace.awp1.co.kr/login")

# 비밀번호는 보안을 위해 로컬 파일에 저장합니다. (pw.txt 파일 참조)
f = open("pw.txt", 'r')
uspaces = f.readlines() # 유스페이스 주차장 관리자 아이디와 비밀번호 List에 저장
uspaces = [uspace.rstrip('\n') for uspace in uspaces]
f.close()

# id, pw 저장 <= 추후에 입력한 값으로 받아서 하는것으로 진행 예정
abc = '10'

input_id = browser.find_element(By.XPATH,'//*[@id="userId"]')
input_pw = browser.find_element(By.XPATH,'//*[@id="loginForm"]/li[3]/input')
input_id.send_keys(uspaces[0])
input_pw.send_keys(uspaces[1])
close_btn= browser.find_element(By.XPATH,'//*[@id="modal-window"]/div/div/div[3]/a[2]')
login_btn= browser.find_element(By.CLASS_NAME,'login_area_btn')
close_btn.click()
login_btn.click()

# 메인 페이지 진입
time.sleep(5)
# 차량 검색
input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
input_car_number.send_keys(abc)
search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
search_btn.click()
time.sleep(5)

# 입력한 번호가 포함되는 차량 리스트 불러오기
list_car = browser.find_elements(By.XPATH,'//*[@id="gridMst"]/div[2]/table/tbody')
print(list_car)
sim_list=[]
for car in list_car:
    for c in car.text.split('\n'):
        # print(c.split()[1])
        a = c.split()[1]
        sim_list.append(a)
print(sim_list)

# 버튼 및 비고 설정
# 오후 5시 이전의 XPATH
btn_2hr = browser.find_element(By.XPATH,'//*[@id="1"]')
btn_30min = browser.find_element(By.XPATH, '//*[@id="2"]')
btn_1hr = browser.find_element(By.XPATH,'//*[@id="3"]')
memo = browser.find_element(By.XPATH, '//*[@id="memo"]')

# 시간 차이 계산
time_parking = browser.find_element(By.XPATH,'//*[@id="entryDate"]').text
time_in = time_parking[11:]
now = datetime.now()
time_now = str(now.time())[0:8]
FMT = '%H:%M:%S'
tdelta = datetime.strptime(time_now, FMT) - datetime.strptime(time_in, FMT)
time_interval2 = str(tdelta)
time_interval3 = int(time_interval2)

# # 오후 5시 이후의 XPATH
# btn_2hr = browser.find_element(By.XPATH,'//*[@id="2"]') # 오후 5시 이후의 xpath
# btn_30min = browser.find_element(By.XPATH, '//*[@id="4"]') #
# btn_1hr = browser.find_element(By.XPATH,'//*[@id="3"]') #

# 할인 등록 전, 이미 등록되어 있는지 사전 확인

# 셀레니움 꺼지지 않도록 유지
time.sleep(10)