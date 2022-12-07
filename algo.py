from datetime import datetime

# 함수 정의
def printing():
    
    print("입차시간과 현재시간의 차이는", tdelta)
    print("지금 현재시간은", time_now)
    print(len(time_in))
    print(time_interval)
    print(len(time_interval))

now = datetime.now()
time_now = str(now.time())[0:8]

time_in = '07:24:00'
time_out = '08:12:00'
FMT = '%H:%M:%S'
tdelta = datetime.strptime(time_out, FMT) - datetime.strptime(time_in, FMT)
time_interval = str(tdelta)

if int(time_interval[0]) < 2:
    print("2시간 충전")
elif int(time_interval[0]) > 2 & int(time_interval[3:5]):
    print("2시간과 3시간 사이네")
else:
    print("2시간보다 많네?")
    
    

printing()