import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("500x350")
root.title("ETNERS PARKING")
root.iconbitmap("./favicon.ico")

# 비밀번호는 보안을 위해 로컬 파일에 저장합니다. (pw.txt 파일 참조)
f = open("pw.txt", 'r')
uspaces = f.readlines() # 유스페이스 주차장 관리자 아이디와 비밀번호 List에 저장
uspaces = [uspace.rstrip('\n') for uspace in uspaces]
f.close()


# 함수 정의 부분
def login():
    print("data saved.")
    info_get = [entry1.get(),entry2.get()]
    print("입력한 값은", info_get)
    print("텍스트 파일에서 불러 온 값은", uspaces)
    if info_get == uspaces:
        print("로그인합니다.")
    else:
        print("아이디와 비밀번호를 확인해주세요.")

def autofill():
    entry1.configure(placeholder_text=uspaces[0])
    entry2.configure(placeholder_text=uspaces[1], show="*")


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