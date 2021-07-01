# -*- coding: utf-8 -*-
# TODO (liaoli) ：
#  备注: 根据excel来读case，写入case运行的结果
import json
from xlutils.copy import copy
import xlrd


class excel_operation(object):
    def __init__(self):
        self.excel_file = 'D:\gaosi_mobile_web\m_api_auto\data\登录case.xlsx'
        self.book = xlrd.open_workbook(self.excel_file)

    def excel_read(self):
        data_list = []
        # title_list = []
        table = self.book.sheet_by_index(0)
        for norw in range(1, table.nrows):
            # 每行第2列 是否运行
            # if table.cell_value(norw, 1) == '否':
            #     continue
            # # 每行第3列， 标题单独拿出来
            # title_list.append(table.cell_value(norw, 1))

            case_id = table.cell_value(norw, 0)
            title = table.cell_value(norw, 1)
            mobile = table.cell_value(norw, 2)
            password = table.cell_value(norw, 3)
            judge = table.cell_value(norw, 4)
            result = table.cell_value(norw, 5)
            value = [case_id, title, mobile, password, judge, result]
            value = tuple(value)
            data_list.append(value)
        return data_list

    def excel_write(self, case_nuber, result):
        """
        :param case_number: 用例编号：case_001
        :param result: 需要写入的响应值
        :return:
        """
        # row = int(case_nuber.split('_')[1])
        row = case_nuber
        result = json.dumps(result, ensure_ascii=False)
        new_excel = copy(self.book)
        ws = new_excel.get_sheet(0)
        # 11 是 实际响应结果栏在excel中的列数-1
        ws.write(row, 6, result)
        new_excel.save(self.excel_file)


if __name__ == '__main__':
    api = excel_operation()
    # api.excel_read()
    api.excel_write(case_nuber=1, result='Pass')
