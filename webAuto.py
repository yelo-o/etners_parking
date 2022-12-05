import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 자동화 브라우저 구동
browser = webdriver.Chrome()
browser.maximize_window() # 창 확대
browser.get("http://uspace.awp1.co.kr/login")

# id, pw 저장 <= 추후에 입력한 값으로 받아서 하는것으로 진행 예정
# 로그인
real_id = "2b-704"
real_pw = "20200801"
abc = '64조3973'

input_id = browser.find_element(By.XPATH,'//*[@id="userId"]')
input_pw = browser.find_element(By.XPATH,'//*[@id="loginForm"]/li[3]/input')
input_id.send_keys(real_id)
input_pw.send_keys(real_pw)
close_btn= browser.find_element(By.XPATH,'//*[@id="modal-window"]/div/div/div[3]/a[2]')
login_btn= browser.find_element(By.CLASS_NAME,'login_area_btn')
close_btn.click()
login_btn.click()

# # 메인 페이지 진입
time.sleep(3)
# 차량 검색
input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
input_car_number.send_keys(abc)
# search_btn = browser.find_element(By.CLASS_NAME, 'btnS1_1 btn')
search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
search_btn.click()

# 버튼 및 비고 설정
btn_2hr = browser.find_element(By.XPATH,'//*[@id="2"]')
btn_1hr = browser.find_element(By.XPATH,'//*[@id="3"]')
btn_30min = browser.find_element(By.XPATH, '//*[@id="4"]')
memo = browser.find_element(By.XPATH, '//*[@id="memo"]')

# 할인 등록 전, 이미 등록되어 있는지 사전 확인

# 셀레니움 꺼지지 않도록 유지
time.sleep(10)