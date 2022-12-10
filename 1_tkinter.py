import time
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# 함수
def select_car():
    global car_number 
    car_number = str(listbox.get(listbox.curselection()))
    print(car_number)
    return car_number

# def close_window(self):
#     self.quit()

root = Tk()
root.title("nado")
root.geometry("640x480")
listbox = Listbox(root)
btn1 = Button(root, text="선택", command = lambda :[select_car(), root.quit()])
# 셀레니움
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.get("http://uspace.awp1.co.kr/login")

# 비밀번호는 보안을 위해 로컬 파일에 저장합니다. (pw.txt 파일 참조)
f = open("pw.txt", 'r')
uspaces = f.readlines() # 유스페이스 주차장 관리자 아이디와 비밀번호 List에 저장
uspaces = [uspace.rstrip('\n') for uspace in uspaces]
f.close()

# id, pw 저장 <= 추후에 입력한 값으로 받아서 하는것으로 진행 예정
car_number = '10'
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
input_car_number.send_keys(car_number)
search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
search_btn.click()
time.sleep(5)

list_car = browser.find_elements(By.XPATH,'//*[@id="gridMst"]/div[2]/table/tbody')
sim_list=[]
for car in list_car:
    for c in car.text.split('\n'):
        # print(c.split()[1])
        a = c.split()[1]
        sim_list.append(a)
        listbox.insert(END, a)
print(sim_list)

listbox.pack()
btn1.pack()
root.mainloop()

# 얻은 값을 토대로 재검색

browser = webdriver.Chrome()
browser.get("http://uspace.awp1.co.kr/login")
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
input_car_number.send_keys(car_number)
search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
search_btn.click()
time.sleep(5)