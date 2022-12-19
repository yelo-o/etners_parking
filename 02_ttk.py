import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import *
from tkinter import filedialog
def search_car():
    pass
def select_car():
    pass
def divMin10():
    pass
def divMin30():
    pass
def divHr1():
    pass
def enrollGrp():
    pass

# root = Tk()
root = ttk.Window()
# style = ttk.Style('darkly')
root.iconbitmap("./favicon.ico")
root.title("주차 자동 등록")
# root.geometry("700x700")
frame1 = ttk.Frame(root, width=700, height=500, bootstyle = "default") # 1번 프레임 좌측에 배치
frame1.pack(fill=tk.X, expand=True)
frame2 = ttk.Frame(root, width=700, height=100)
frame2.pack(fill=tk.X, expand=True)

# 프레임 1의 첫번째 열
sep1 = ttk.Separator(frame1, bootstyle = "danger")
myLabel1 = Label(frame1, text = "아래에 차량번호를 입력해주세요!")
myLabel2 = Label(frame1, text = "주차 차량 리스트")
carNumEntry = ttk.Entry(frame1, bootstyle="default")
carList = Listbox(frame1)
btn_search = ttk.Button(frame1, text="검색(10초 정도 소요됩니다.)", bootstyle="warning" ,command=search_car)
btn_select = ttk.Button(frame1, text="선택", bootstyle="warning" ,command=select_car)

sep1.grid(row=0, sticky="ew",pady=5)
myLabel1.grid(row=1, column=0, sticky="nsew",padx=5, pady=5)
carNumEntry.grid(row=2, column=0, sticky="ns",padx=5, pady=5)
btn_search.grid(row=3, column=0, sticky="ns",padx=5, pady=5)
myLabel2.grid(row=4, column=0, sticky="nsew",padx=5, pady=5)
carList.grid(row=5, column=0, sticky="nsew",padx=5, pady=5)
btn_select.grid(row=6, column=0, sticky="ns",padx=5, pady=5)

# 프레임1의 두번째 열
# lblCar = Label(frame1, text = "선택한 차량번호")
lblCar = ttk.Labelframe(frame1, text = "선택한 차량번호", bootstyle="dark")
btn0 = ttk.Button(frame1, text="10분 안에 나가요", bootstyle="primary" ,command=divMin10)
btn1 = ttk.Button(frame1, text="30분 안에 나가요", bootstyle="primary" ,command=divMin30)
btn2 = ttk.Button(frame1, text="1시간 안에 나가요", bootstyle="primary" ,command=divHr1)

lblCar.grid(row=2, column=1, sticky="nsew",padx=5, pady=5)
btn0.grid(row=4, column=1, sticky="nsew",padx=5, pady=5)
btn1.grid(row=5, column=1, sticky="ew",padx=5, pady=5)
btn2.grid(row=6, column=1, sticky="nsew",padx=5, pady=5)

# 프레임2
sep2 = ttk.Separator(frame2, bootstyle = "info")
sep2.pack(fill=ttk.X, pady=10)
btn3 = ttk.Button(frame2, text="단체 등록", bootstyle = SUCCESS, command=enrollGrp)
btn3.pack(padx=100,pady=20)

root.mainloop()