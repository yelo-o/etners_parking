import tkinter
import customtkinter
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# 계정 정보
f = open("pw.txt", 'r')
uspaces = f.readlines() # 유스페이스 주차장 관리자 아이디와 비밀번호 List에 저장
uspaces = [uspace.rstrip('\n') for uspace in uspaces]
f.close()

# Headless 웹드라이버

#     # 옵션 생성
# options = webdriver.ChromeOptions()
#     # 창 숨기는 옵션 추가
# options.add_argument("headless")

#     # driver 실행
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
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

"""
원하는 작업 실행
"""
# 함수 정의
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

def enter_number():
    car_info = label2.configure(text=entry3.get(),font=("nanum", 18))
    entry3.get()

# GUI 색상 설정
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# 크기 설정
root = customtkinter.CTk()
root.geometry("500x350")
root.title("ETNERS PARKING")
root.iconbitmap("./favicon.ico")

# 기본 프레임 설정
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

    

# 대제목 : 차량번호 입력
label1 = customtkinter.CTkLabel(master=frame, text="차량번호입력", font=("Roboto", 24))
label1.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="ex)123바5678",font=("nanum", 12))
entry3.pack(pady=12, padx=10)
# 차량 정보 저장
# car_info = entry3.get()
# 버튼 클릭
button1 = customtkinter.CTkButton(master=frame, text="입력", command=enter_number)
button1.pack(pady=12, padx=10)
print(entry3.get())
# 셀레니움
    #차량 검색


label2 = customtkinter.CTkLabel(master=frame, text="차량 정보", font=("Roboto", 24))
label2.pack(pady=12, padx=10)

# 아래의 차량 번호 리스틑 업데이트 필요
car_numbers=['236수8859', '281나8558', '285수5683', '145버7854', '173보8500', '36보3853', '153조8560', '38루2855', '128주1856', '68나7853']
combobox = customtkinter.CTkOptionMenu(master=frame,
                                       values=car_numbers,
                                       command=optionmenu_callback)
combobox.pack(padx=20, pady=10)
combobox.set("차량번호")  # set initial value
root.mainloop()

input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
input_car_number.send_keys(entry3.get())
search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
search_btn.click()

browser.quit()