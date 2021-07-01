# -*- coding: utf-8 -*-
# TODO (liaoli) ：
#  备注：密码登录后的token、userCode等信息的写入，以便后期调用
from base_m_api.api_m import api_m
from config import env_constant
from utils.data_readwrite import data_write
from utils.get_data import getData

data = getData()
mobile = data.get('mobile')
password = data.get('password')


def login_getMsg():
    api = api_m()
    params = {
        'mobile': mobile,
        'password': password
        }
    result = api.pwdLogin(params=params)
    code = result.json().get('code')
    try:
        assert code == '200'
        message = [{'name': item.get('name'),
                    'userCode': item.get('userCode'),
                    'token': item.get('token')} for item in result.json().get('data')]
        # print(message)
        path = 'data\write_{}.yaml'.format(env_constant.ENVIORNMENT)
        data_write(det_path=path, writedata=message)
    except:
        print('当前接口请求错误。result = {}'.format(result.json()))

    # if code == '200':
    #     message = [{'name': item.get('name'),
    #                 'userCode': item.get('userCode'),
    #                 'token': item.get('token')} for item in result.json().get('data')]
    #     # print(message)
    #     path = 'data\write_{}.yaml'.format(env_constant.ENVIORNMENT)
    #     data_write(det_path=path, writedata=message)
    # else:
    #     print('当前接口请求错误。result = {}'.format(result.json()))


login_getMsg()


# 用super的方式实现
# data = getData()
# mobile = data.get('mobile')
# password = data.get('password')
# class loginapi(api_m):
#     def __init__(self):
#         self.data = getData()
#         self.mobile = self.data.get('mobile')
#         self.password = self.data.get('password')
#
#     def login_getMsg(self):
#         params = {
#             'mobile': self.mobile,
#             'password': self.password
#         }
#         result = super().pwdLogin(params=params)
#         code = result.json().get('code')
#         if code == '200':
#             message = [{'name': item.get('name'),
#                         'userCode': item.get('userCode'),
#                         'token': item.get('token')} for item in result.json().get('data')]
#             print(message)
#
#
# loginapi().login_getMsg()

