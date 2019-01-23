import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('shilla_cosmetics.xlsx')
    sh = wb.sheet_by_name('Sheet1')
    shilla_cosmetics = open('shilla_cosmetics.csv', 'w')
    wr = csv.writer(shilla_cosmetics, delimiter=' ', quotechar='|', quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
        wr.writerow(sh.row_values(rownum))

        shilla_cosmetics.close()



# runs the csv_from_excel function:
csv_from_excel()
