# 가짜 버튼 입력 함수
def min120():
    print("2시간 버튼 클릭")

def min60():
    print("1시간 버튼 클릭")

def min30():
    print("30분 버튼 클릭")

t_table = [0,110,140,170,200,230,260,290,320,350,380,410,440,470,500,530,560,590,620,650,680,710,740,770,800,830,860,890,920]

tdelta = 180
for i in range(1,28):
    if int(t_table[i-1]) < tdelta <= int(t_table[i]): # 110~920까지 차례로 대입
        std = int(t_table[i]-110)/60
        if int(t_table[i]) <= 110:
            min120()
        elif isinstance(int(t_table[i]-110)/60, int) == True:
            min120()
            for j in range(int(std)):
                min60()
        elif isinstance(int(t_table[i]-110)/60, int) == False:
            min120()
            min30()
            for j in range(int(std)):
                min60()
    else:
        pass
                
    # elif tdelta < int(t_table[i]): # 140 - 110 = 30
    #     print(f"주차 시간은 {tdelta}분으로 {t_table[0]} < {t_table[1]}")
    #     min120()
    #     min30()
    # elif tdelta < int(t_table[i]): # 170 - 110 = 60
    #     print(f"주차 시간은 {tdelta}분으로 {t_table[1]} < {t_table[2]}")
    #     min120()
    #     min60()
    # elif tdelta < int(t_table[i]): # 200 < 120+60+30
    #     print(f"주차 시간은 {tdelta}분으로  {t_table[2]} < {t_table[3]}")

    # else:
    #     print("주차 시간이 많이 경과되었습니다. 주차 시간을 확인해주세요")