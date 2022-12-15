from tkinter import *
class ProcessButtonEvent:
    def __init__(self):
        window = Tk()
        btOK = Button(window, text = "OK", fg = "red", command = self.processOK)
        btCancel = Button(window, text="Cancel", bg = "yellow", command = self.processCancel)
        
        btOK.pack()
        btCancel.pack()
        window.mainloop()
        
    def processOK(self):
        print("OK button is clicked.")
    def processCancel(self):
        print("Cancel button is clicked.")
        
ProcessButtonEvent() # __init__ 메소드를 호출하는 오브젝트 생성
        