import tkinter
from tkinter import *
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

root = Tk()
root.iconbitmap("./favicon.ico")
root.title("주차 자동 등록")
# root.geometry("700x700")
frame1 = tkinter.Frame(root, width=700, height=500, bg = "red") # 1번 프레임 좌측에 배치
frame1.pack(fill=tkinter.X)
frame2 = tkinter.Frame(root, width=700, height=100, bg = 'yellow')
frame2.pack(fill=tkinter.X)

# 프레임 1의 첫번째 열
myLabel1 = Label(frame1, text = "아래에 차량번호를 입력해주세요!")
myLabel2 = Label(frame1, text = "주차 차량 리스트")
carNumEntry = Entry(frame1)
carList = Listbox(frame1)
btn_search = Button(frame1, text="검색(10초 정도 소요됩니다.)", command=search_car)
btn_select = Button(frame1, text="선택", command=select_car)

myLabel1.grid(row=0, column=0, sticky="nsew",padx=5, pady=5)
carNumEntry.grid(row=1, column=0, sticky="ns",padx=5, pady=5)
btn_search.grid(row=2, column=0, sticky="ns",padx=5, pady=5)
myLabel2.grid(row=3, column=0, sticky="nsew",padx=5, pady=5)
carList.grid(row=4, column=0, sticky="nsew",padx=5, pady=5)
btn_select.grid(row=5, column=0, sticky="ns",padx=5, pady=5)

# 프레임1의 두번째 열
lblCar = Label(frame1, text = "차량번호")
btn0 = Button(frame1, text="10분 안에 나가요", command=divMin10)
btn1 = Button(frame1, text="30분 안에 나가요", command=divMin30)
btn2 = Button(frame1, text="1시간 안에 나가요", command=divHr1)

lblCar.grid(row=0, column=1, sticky="nsew",padx=5, pady=5)
btn0.grid(row=2, column=1, sticky="nsew",padx=5, pady=5)
btn1.grid(row=4, column=1, sticky="ew",padx=5, pady=5)
btn2.grid(row=6, column=1, sticky="nsew",padx=5, pady=5)

# 프레임3 
btn3 = Button(frame2, text="단체 등록", bg = "green", command=enrollGrp)
btn3.pack(padx=100,pady=20)

root.mainloop()