pip install xlrd
pip install xlwt

import xlrd
workbook = xlrd.open_workbook('my_file_name.xls')
workbook = xlrd.open_workbook('my_file_name.xls', on_demand = True)
worksheet = workbook.sheet_by_name('My_Sheet_Name')

worksheet = workbook.sheet_by_index(0)
# Value of 1st row and 1st column
sheet.cell(0, 0).value

if sheet.cell(0, 0).value == xlrd.empty_cell.value:
    # Do something
