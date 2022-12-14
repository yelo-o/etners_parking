import openpyxl
filename = 'parking.xlsx'
book = openpyxl.load_workbook(filename)
ws = book.active 
row_max = ws.max_row # row_max = 엑셀 파일 내 행숫자를 읽음 ※ 주의 0부터 읽는거 아님 1부터 읽음
print("row_max는", row_max)
data = []
# print("ws.rows는", ws.rows[0].value)
# sheet = book.worksheets[0]
# for i in range(row_max-1): # row_max가 3이면 i = 0,1,2
for row in ws.rows:
    # print(row[0].value)
    # data.append([row[i].value])
    data.append([row[0].value,row[1].value])
print("data는", data)
print("data[0]는",data[0])
print("data[0][0]는",data[0][0])
print("data의 크기는", len(data))
# data[0] 부터 data[row_max-1] 까지 반복문 생성 예정
for i in range(len(data)): # len(data) = 6 # i = 0, 1, 2
    car_num = data[i][0]
    reason = data[i][1]
    print("차량번호는",car_num)
    print("주차사유는",reason)