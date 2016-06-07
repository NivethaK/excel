
import xlrd

workbook = xlrd.Workbook()
workbook.save('my_file.xls')

sheet = workbook.add_sheet('Sheet_1')
sheet.write(0, 0,'Inserting data in 1st Row and 1st Column')
row = sheet.row(1) # Selecting the second row
row.write(0,'2nd Row and 1st Column')
row.write(1,'1st Row and 2nd Column')
row.flush_row_data()
sheet.col(0).width = 625 # In pixels

style = xlrd.XFStyle()

font = xlrd.Font('Arial')
style.font = font

pattern = xlrd.Pattern()
pattern.pattern = xlrd.Pattern.SOLID_PATTERN
pattern.pattern_fore_colour = xlrd.Style.colour_map['red']

style.pattern = pattern

sheet.write(0, 0, "Some data", style)
