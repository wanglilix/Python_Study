#! python
import xlsxwriter

workbook = xlsxwriter.Workbook('chart_scatter.xlsx')

worksheet1 = workbook.add_worksheet()
worksheet2 = workbook.add_worksheet()

headings = ['Number','Batch 1','Batch 2']
data = [
    [2,3,4,5,6,7],
    [10,40,50,20,10,50],
    [30,60,70,50,40,30],
    ]



worksheet = worksheet1
worksheet.write_row('A1',headings)
worksheet.write_column('A2',data[0])
worksheet.write_column('B2',data[1])
worksheet.write_column('C2',data[2])

chart1 = workbook.add_chart({'type':'line'})
chart1.add_series(
    {'name'        :'=Sheet1!$B$1'
    ,'categories'  :'=Sheet1!$A$2:$A$7'
    ,'values'      :'=Sheet1!$B$2:$B$7',})

chart1.add_series(
    {'name'       :['Sheet1',0,2]
     ,'categories':['Sheet1',1,0,6,0]
     ,'values'    :['Sheet1',1,2,6,2],})

worksheet.insert_chart('D2',chart1,{'x_offset': 25, 'y_offset': 10})


chart2 = workbook.add_chart({'type':'column'})
chart2.add_series(
    {'name'       :['Sheet1',0,2]
     ,'categories':['Sheet1',1,0,6,0]
     ,'values'    :['Sheet1',1,2,6,2],})
chart2.add_series(
    {'name':'=Sheet1!$B$1'
     ,'categories':'=Sheet1!$A$2:$A$7'
     ,'values':'=Sheet1!$B$2:$B$7',})

worksheet.insert_chart('D20',chart2,{'x_offset': 25, 'y_offset': 10})

workbook.close()















