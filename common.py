import xlrd


def read_xls(file, *args):
    """
    读取xls文件
    :param file: 文件地址
    :param args: 需要的文件列数  (前置条件，请求方法，url，参数，断言方法，预期结果，状态码)
    :return:
    """
    _li = []
    workbook = xlrd.open_workbook(file)
    sheet = workbook.sheets()[0]
    for row in range(1, sheet.nrows):
        cur = []
        for col in args:
            cur.append(sheet.cell_value(row, col - 1))
        _li.append(cur)
    workbook.release_resources()
    del workbook
    return _li


def split_li(string):
    """
    字符串从空格分割成列表
    :param string:
    :return:
    """
    li = string.split(' ')
    return li


def new_eval(string):
    if not string:
        return eval(string)
    return string
