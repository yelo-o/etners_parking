import openpyxl
filename = 'parking_data.xlsx'
book = openpyxl.load_workbook(filename)
ws = book.active 
row_max = ws.max_row # row_max = 엑셀 파일 내 행숫자를 읽음 ※ 주의 0부터 읽는거 아님 1부터 읽음
data = []
# sheet = book.worksheets[0]
for i in range(row_max-1):
    for row in ws.rows:
        data.append([row[i].value, row[i+1].value])
# print(data)
# print(data[0])
# print(data[0][0])
# print(len(data))
# data[0] 부터 data[row_max-1] 까지 반복문 생성 예정
for i in range(len(data)-1):
    car_num = data[i][0]
    reason = data[i][1]
    print(car_num)
    print(reason)