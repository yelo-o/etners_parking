from datetime import datetime

# 함수 정의
# def printing():
    
#     print("입차시간과 현재시간의 차이는", tdelta)
#     print("지금 현재시간은", time_now)
#     print(len(time_in))
#     print(time_interval)
#     print(len(time_interval))

now = datetime.now()
time_now = str(now.time())[0:8]

# 받아오는 시간 형태
time_in = '07:25:00'
time_out = '15:12:00'
time0_min = int(time_in[0:2])*60 + int(time_in[3:5])
time1_min = int(time_out[0:2])*60 + int(time_out[3:5])
tdelta = time1_min - time0_min

# 조건문
if int(tdelta) < 110:
    print("2시간 한 번 클릭")
elif int(tdelta) < 140:
    print("2시간 한 번 클릭")
    print("30분 한 번 클릭")
elif int(tdelta) < 170:
    print("2시간 한 번 클릭")
    print("30분 한 번 클릭")
    print("1시간 한 번 클릭")
elif int(tdelta) < 200:
    print("170~200 사이")
elif int(tdelta) < 230:
    print("200~230 사이")
elif int(tdelta) < 260:
    print("230~260 사이")

else:
    print("주차 시간이 많이 경과되었습니다. 주차 시간을 확인해주세요")
        
# FMT = '%H:%M:%S'
# tdelta = datetime.strptime(time_out, FMT) - datetime.strptime(time_in, FMT)
# time_interval = str(tdelta)

# if int() < 2:
#     print("2시간 충전")
# elif int(tdelta[0]) > 2 & int(tdelta[3:5]):
#     print("2시간과 3시간 사이네")
# else:
#     print("2시간보다 많네?")
    
    

# printing()