import tkinter
import customtkinter

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

# 함수 정의
def enter_number():
    car_info = label2.configure(text=entry3.get(),font=("nanum", 18))

# 대제목 : 차량번호 입력
label1 = customtkinter.CTkLabel(master=frame, text="차량번호입력", font=("Roboto", 24))
label1.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(master=frame, placeholder_text="ex)123바5678",font=("nanum", 12))
entry3.pack(pady=12, padx=10)
# 차량 정보 저장
# car_info = entry3.get()

button1 = customtkinter.CTkButton(master=frame, text="입력", command=enter_number)
button1.pack(pady=12, padx=10)

label2 = customtkinter.CTkLabel(master=frame, text="차량 정보", font=("Roboto", 24))
label2.pack(pady=12, padx=10)


root.mainloop()