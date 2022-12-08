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
time_out = '11:45:00'
time0_min = int(time_in[0:2])*60 + int(time_in[3:5])
time1_min = int(time_out[0:2])*60 + int(time_out[3:5])
tdelta = time1_min - time0_min
print('입차시간과 현재시간은 {}분 차이입니다.'.format(tdelta))
btn0 = '2시간 추가'
btn1 = '1시간 추가'
btn2 = '30분 추가'
btn = [120,60,30]
t_table = [110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800]
# 조건문
if int(tdelta) < int(t_table[0]): # 110
    print(btn[0])
elif int(tdelta) < int(t_table[1]): # 140 < 120+30
    print(btn[0])
    print(btn[2])
elif int(tdelta) < int(t_table[2]): # 170 < 120+60
    print(btn[0])
    print(btn[1])
elif int(tdelta) < int(t_table[3]): # 200 < 120+60+30
    print(btn[0])
    print(btn[1])
    print(btn[2])
elif int(tdelta) < int(t_table[4]): # 230 < 120+60+60
    print(btn[0])
    print(btn[1])
    print(btn[1])
    print("200~230 사이")
elif int(tdelta) < int(t_table[5]): # 260 <120+60+60+30
    print(btn[0])
    print(btn[1])
    print(btn[1])
    print(btn[2])
    print("230~260 사이")
elif int(tdelta) < int(t_table[6]): # 290 < 120+60+60+60
    print(btn[0])
    print(btn[1])
    print(btn[1])
    print(btn[1])
    print("260~290 사이")
elif int(tdelta) < int(t_table[7]): # 320 <120+60+60+60+30
    print(btn[0])
    print(btn[1])
    print(btn[1])
    print(btn[1])
    print(btn[2])
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