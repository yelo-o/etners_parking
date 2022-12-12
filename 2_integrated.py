import time
from datetime import datetime
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as pg
# 함수
def select_car():
    global car_number 
    car_number = str(listbox.get(listbox.curselection()))
    print(car_number)
    return car_number
# # 가짜 버튼 입력 함수
# def min120():
#     print("2시간 버튼 클릭")

# def min60():
#     print("1시간 버튼 클릭")

# def min30():
#     print("30분 버튼 클릭")
# # 진짜 버튼 입력 함수
def min120():
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
    
# 1. 차량번호 및 사유 입력 (프롬프트)
# def close_window(self):
#     self.quit()
car_number = pg.prompt(text = "차량번호를 입력하세요", title='번호')
reason = pg.prompt(text = "사유를 입력하세요", title='사유')
root = Tk()
root.title("nado")
root.geometry("640x480")
listbox = Listbox(root)
btn1 = Button(root, text="선택", command = lambda :[select_car(), root.quit()])

# 2. 번호에 해당하는 차량번호 리스트를 가져오기 위해 임시 셀레니움 실행 및 종료
    # 옵션 생성
options = webdriver.ChromeOptions()
    # 창 숨기는 옵션 추가
options.add_argument("headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.get("http://uspace.awp1.co.kr/login")

# 비밀번호는 보안을 위해 로컬 파일에 저장합니다. (pw.txt 파일 참조)
f = open("pw.txt", 'r')
uspaces = f.readlines() # 유스페이스 주차장 관리자 아이디와 비밀번호 List에 저장
uspaces = [uspace.rstrip('\n') for uspace in uspaces]
f.close()

# id, pw 저장 <= 추후에 입력한 값으로 받아서 하는것으로 진행 예정
# car_number = '10'
input_id = browser.find_element(By.XPATH,'//*[@id="userId"]')
input_pw = browser.find_element(By.XPATH,'//*[@id="loginForm"]/li[3]/input')
input_id.send_keys(uspaces[0])
input_pw.send_keys(uspaces[1])
close_btn= browser.find_element(By.XPATH,'//*[@id="modal-window"]/div/div/div[3]/a[2]')
login_btn= browser.find_element(By.CLASS_NAME,'login_area_btn')
close_btn.click()
login_btn.click()
time.sleep(2)

input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
input_car_number.send_keys(car_number)
search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
search_btn.click()
time.sleep(2)

list_car = browser.find_elements(By.XPATH,'//*[@id="gridMst"]/div[2]/table/tbody')
sim_list=[]
for car in list_car:
    for c in car.text.split('\n'):
        # print(c.split()[1])
        a = c.split()[1]
        sim_list.append(a)
        listbox.insert(END, a)
print(sim_list)
browser.quit() # 브라우저 닫기

listbox.pack()
btn1.pack()
root.mainloop()

# 3. 얻은 값을 토대로 재검색
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
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
time.sleep(3)

input_car_number = browser.find_element(By.XPATH, '//*[@id="schCarNo"]')
input_car_number.send_keys(car_number)
search_btn = browser.find_element(By.XPATH, '//*[@id="sForm"]/input[3]')
search_btn.click()
time.sleep(5)

# 선택한 차량에 대한 알고리즘 실행
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
# btn_ok = browser.find_element(By.XPATH, '//*[@id="modal-window"]/div/div/div[3]/a')
t_table = [110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800,830,860,890,920]

    
if tdelta < int(t_table[0]): # 110
    print(f"주차 시간은 {tdelta}분으로 2시간 이하입니다.")
    min120()
elif tdelta < int(t_table[1]): # 140 < 120+30
    print(f"주차 시간은 {tdelta}분으로 {t_table[0]} < {t_table[1]}")
    min120()
    min30()
elif tdelta < int(t_table[2]): # 170 < 120+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[1]} < {t_table[2]}")
    min120()
    min60()
elif tdelta < int(t_table[3]): # 200 < 120+60+30
    print(f"주차 시간은 {tdelta}분으로  {t_table[2]} < {t_table[3]}")
    min120()
    min60()
    min30()
elif tdelta < int(t_table[4]): # 230 < 120+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[3]} < {t_table[4]}")
    min120()
    min60()
    min60()
elif tdelta < int(t_table[5]): # 260 <120+60+60+30
    print(f"주차 시간은 {tdelta}분으로 {t_table[4]} < {t_table[5]}")
    min120()
    min60()
    min60()
    min30()
elif tdelta < int(t_table[6]): # 290 < 120+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[5]} < {t_table[6]}")
    min120()
    min60()
    min60()
    min60()
    print("260~290 사이")
elif tdelta < int(t_table[7]): # 320 <120+60+60+60+30
    print(f"주차 시간은 {tdelta}분으로 {t_table[6]} < {t_table[7]}")
    min120()
    min60()
    min60()
    min60()
    min30()
elif tdelta < int(t_table[8]): # 350 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[7]} < {t_table[8]}")
    min120()
    min60()
    min60()
    min60()
    min60()
elif tdelta < int(t_table[9]): # 380 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[8]} < {t_table[9]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min30()
elif tdelta < int(t_table[10]): # 410 <120+60+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[9]} < {t_table[10]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
elif tdelta < int(t_table[11]): # 440 <120+60+60+60+60+30
    print(f"주차 시간은 {tdelta}분으로 {t_table[10]} < {t_table[11]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min30()
elif tdelta < int(t_table[12]): # 470 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[11]} < {t_table[12]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
elif tdelta < int(t_table[13]): # 500 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[12]} < {t_table[13]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min30()
elif tdelta < int(t_table[14]): # 530 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[13]} < {t_table[14]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
elif tdelta < int(t_table[15]): # 560 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[14]} < {t_table[15]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min30()
elif tdelta < int(t_table[16]): # 590 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[15]} < {t_table[16]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
elif tdelta < int(t_table[17]): # 620 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[16]} < {t_table[17]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min30()
elif tdelta < int(t_table[18]): # 650 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[17]} < {t_table[18]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
elif tdelta < int(t_table[19]): # 680 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[18]} < {t_table[19]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min30()
elif tdelta < int(t_table[20]): # 710 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[19]} < {t_table[20]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
elif tdelta < int(t_table[21]): # 740 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[20]} < {t_table[21]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min30()
elif tdelta < int(t_table[22]): # 770 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[21]} < {t_table[22]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
elif tdelta < int(t_table[23]): # 800 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[22]} < {t_table[23]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min30()
elif tdelta < int(t_table[24]): # 830 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[23]} < {t_table[24]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
elif tdelta < int(t_table[25]): # 860 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[24]} < {t_table[25]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min30()
elif tdelta < int(t_table[26]): # 890 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[25]} < {t_table[26]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
elif tdelta < int(t_table[27]): # 920 <120+60+60+60+60
    print(f"주차 시간은 {tdelta}분으로 {t_table[26]} < {t_table[27]}")
    min120()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min60()
    min30()
else:
    print("주차 시간이 많이 경과되었습니다. 주차 시간을 확인해주세요")

# if tdelta < int(t_table[0]): # 110
#     print(f"{tdelta} is {t_table[0]} 보다 작다.")
#     print(f"{tdelta/60}시간 {tdelta%60}분으로 {t_table[0]} 보다 작다.")
# else: 
#     print(f"{tdelta} is {t_table[0]} 보다 크다.")