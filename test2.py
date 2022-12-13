import openpyxl
filename = 'parking_data.xlsx'
book = openpyxl.load_workbook(filename)

data = []
sheet = book.worksheets[0]
for row in sheet.rows:
    data.append([row[0].value, row[1].value])
print(data)
print(data[0])
