import common
case_interface_file = r'./case/interface_case.xls'
case_interface_li = common.read_xls(case_interface_file, 4, 5, 6, 7, 8, 9, 10)

if __name__ == '__main__':
    print(case_interface_li)