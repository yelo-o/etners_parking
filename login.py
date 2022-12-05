import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("ETNERS PARKING")
root.iconbitmap("./favicon.ico")

uspace = ["2b-704","20200801"]

# 함수 정의 부분
def login():
    print("data saved.")
    info_get = [entry1.get(),entry2.get()]
    print(info_get)
    if info_get == uspace:
        print("로그인합니다.")
    else:
        print("아이디와 비밀번호를 확인해주세요.")

def autofill():
    entry1.configure(textvariable=uspace[0]).get()
    entry2.configure(textvariable=uspace[1]).get()


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login system", font=("Roboto", 24))
label.pack(pady=12, padx=10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

btn = customtkinter.CTkButton(master=frame, text="AutoFill", command=autofill)
btn.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

root.mainloop()