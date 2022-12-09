from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as pg

# 계정 정보
f = open("pw.txt", 'r')
uspaces = f.readlines() # 유스페이스 주차장 관리자 아이디와 비밀번호 List에 저장
uspaces = [uspace.rstrip('\n') for uspace in uspaces]
f.close()

browser = webdriver.Chrome()
browser.maximize_window() # 창 확대
browser.get("http://uspace.awp1.co.kr/login")
# 아이디/ 비밀번호 입력
input_id = browser.find_element(By.XPATH,'//*[@id="userId"]')
input_pw = browser.find_element(By.XPATH,'//*[@id="loginForm"]/li[3]/input')
input_id.send_keys(uspaces[0])
input_pw.send_keys(uspaces[1])
close_btn= browser.find_element(By.XPATH,'//*[@id="modal-window"]/div/div/div[3]/a[2]')
login_btn= browser.find_element(By.CLASS_NAME,'login_area_btn')
close_btn.click()
login_btn.click()
time.sleep(3)
input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
# entry3 = input("차량번호를 입력하세요")
entry3 = pg.prompt(text = "차량번호를 입력하세요", title='번호')
reason = pg.prompt(text = "사유를 입력하세요", title='사유')
input_car_number.send_keys(entry3)
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
btn = [120,60,30]

# 오후 5시 30분 이전의 XPATH
btn_2hr = browser.find_element(By.XPATH,'//*[@id="1"]')
btn_1hr = browser.find_element(By.XPATH,'//*[@id="3"]')
btn_30min = browser.find_element(By.XPATH, '//*[@id="2"]')
memo = browser.find_element(By.XPATH, '//*[@id="memo"]')

t_table = [110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800]
if tdelta < int(t_table[0]): # 110
    print(btn[0])
    memo.send_keys(reason)
    btn_2hr.click()
elif tdelta < int(t_table[1]): # 140 < 120+30
    print(btn[0])
    btn_2hr.click()
    time.sleep(1)
    print(btn[2])
    memo.send_keys(reason)
    btn_30min.click()
elif tdelta < int(t_table[2]): # 170 < 120+60
    print(btn[0])
    btn_2hr.click()
    print(btn[1])
    time.sleep(1)
    memo.send_keys(reason)
    
elif tdelta < int(t_table[3]): # 200 < 120+60+30
    print(btn[0])
    print(btn[1])
    print(btn[2])
elif tdelta < int(t_table[4]): # 230 < 120+60+60
    print(btn[0])
    print(btn[1])
    print(btn[1])
    print("200~230 사이")
elif tdelta < int(t_table[5]): # 260 <120+60+60+30
    print(btn[0])
    print(btn[1])
    print(btn[1])
    print(btn[2])
    print("230~260 사이")
elif tdelta < int(t_table[6]): # 290 < 120+60+60+60
    print(btn[0])
    print(btn[1])
    print(btn[1])
    print(btn[1])
    print("260~290 사이")
elif tdelta < int(t_table[7]): # 320 <120+60+60+60+30
    print(btn[0])
    print(btn[1])
    print(btn[1])
    print(btn[1])
    print(btn[2])
else:
    print("주차 시간이 많이 경과되었습니다. 주차 시간을 확인해주세요")