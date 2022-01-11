import xlsxwriter

path = input("Input path to file\n")
path = path.strip('"')
with open(path, 'r', encoding="utf-8") as f:
    lines = f.read()


workbook = xlsxwriter.Workbook("data.xlsx")
worksheet = workbook.add_worksheet("Charlength")

worksheet.write('A1', 'Number of Characters')
worksheet.write('B1', 'Matches')
rowIndex = 2


max_word_length = int(input("Input max character length\n")) 

for i in range(1,max_word_length + 1):
     cell1 = (i)
     cell2 = len([word for word in lines.split() if len(word) == i])
     print (cell1, cell2)
     worksheet.write('A' + str(cell1 + 1), cell1)
     worksheet.write('B' + str(cell1 + 1), cell2)
rowIndex += 1

workbook.close()
