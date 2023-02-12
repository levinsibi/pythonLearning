import pandas


def read_from_excel(file_name, sheet_name, tc_name, col_name):
    excel_data_df = pandas.read_excel('../Data/' + file_name + '.xlsx', sheet_name=sheet_name)
    dic = excel_data_df.to_dict('records')
    print(len(dic))
    for i in range(len(dic)):
        if dic[i].get('TC') == tc_name:
            print(dic[i])
            return dic[i].get(col_name)


# print(dic[1])

print(read_from_excel('records', 'Employees', 'TC2', 'Pwd'))
print(read_from_excel('records', 'Emp', 'TC2', 'Pwd'))