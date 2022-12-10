import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup


f = open("pw.txt", 'r')
uspaces = f.readlines() # 유스페이스 주차장 관리자 아이디와 비밀번호 List에 저장
uspaces = [uspace.rstrip('\n') for uspace in uspaces]
f.close()
browser = webdriver.Chrome()
browser.maximize_window() # 창 확대
browser.get("http://uspace.awp1.co.kr/login")

input_id = browser.find_element(By.XPATH,'//*[@id="userId"]')
input_pw = browser.find_element(By.XPATH,'//*[@id="loginForm"]/li[3]/input')
input_id.send_keys(uspaces[0])
input_pw.send_keys(uspaces[1])
close_btn= browser.find_element(By.XPATH,'//*[@id="modal-window"]/div/div/div[3]/a[2]')
login_btn= browser.find_element(By.CLASS_NAME,'login_area_btn')
close_btn.click()
login_btn.click()
time.sleep(2)
abc = '85'
input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
input_car_number.send_keys(abc)
search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
search_btn.click()

# 세션정보 저장
s = requests.Session()
headers = { "user-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
s.headers.update(headers)

for cookie in browser.get_cookies():
    c = {cookie['name'] : cookie['value']}
    s.cookies.update(c)
# print(s.cookies)

response = s.get('http://uspace.awp1.co.kr/discount/registration')
soup = BeautifulSoup(response.text,'html.parser')
# list_cars = soup.find_all("tr", attrs={"class":"odd_dhx_skyblue "})
list_cars = soup.find_next_siblings("tr")
# list_car = soup.find("tr", attrs={"class":"odd_dhx_skyblue "})
print(list_cars)
# print(list_car)
# print(soup.prettify())