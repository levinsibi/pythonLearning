import pandas

excel_data_df = pandas.read_excel('../Data/records.xlsx', sheet_name='Employees')
dic = excel_data_df.to_dict(orient='record')
# print whole sheet data
# print(dic)
# print('Excel Sheet to Dict:', excel_data_df.to_dict(orient='record'))
print(len(dic))
for i in range (len(dic)):
    if(dic[i].get('TC')=='TC2'):
        print(dic[i])

# print(dic[1])