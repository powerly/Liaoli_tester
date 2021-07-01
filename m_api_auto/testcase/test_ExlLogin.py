# -*- coding: utf-8 -*-
# TODO (liaoli) ：
#  备注：利用excel写登录接口的case，并将运行将结果写入到excel中
import allure

from base_m_api.api_m import api_m
from common.common_info_m import get_host
from config import env_constant
from utils.excel_readwrite import excel_operation
from utils.get_data import getData


class Test_loginCase(object):
    @allure.step(title="case执行开始。初始数据准备")
    def test_setup(self):
        print("\n----------setup")

    @allure.step(title="case执行结束。")
    def test_teardown(self):
        print("\n----------teardown")

    @allure.step(title="case执行中。")
    def test_login(self):
        host = get_host(environ=env_constant.ENVIORNMENT)
        self.url = host + getData().get('url_Login')
        data_list = excel_operation().excel_read()
        for data in data_list:
            id = int(data[0])
            title = data[1]
            mobile = data[2]
            password = data[3]
            judge = data[4]
            # result = data[5]
            params = {
                'mobile': mobile,
                'password': password
            }
            api = api_m()
            res = api.pwdLogin(params=params)
            allure.attach('case{}:{}'.format(id, title))
            print('case{}:{}'.format(id, title))
            code = res.json().get('code')
            # print(code, judge)
            try:
                assert code == judge
                excel_operation().excel_write(case_nuber=id, result='Pass')
                allure.attach('Pass结果与期望一致：接口返回的code：{}，excel文档中的期望值：{}'.format(code, judge))
                print('Pass结果与期望一致：接口返回的code：{}，excel文档中的期望值：{}'.format(code, judge))
            except:
                excel_operation().excel_write(case_nuber=id, result='Fail')
                allure.attach('Fail结果与期望不一致：接口返回的code：{}，excel文档中的期望值：{}'.format(code, judge))
                print('Fail结果与期望不一致：接口返回的code：{}，excel文档中的期望值：{}'.format(code, judge))
                print('接口返回的结果：'.format(res.json()))


if __name__ == '__main__':
    api = Test_loginCase()
    api.test_login()
