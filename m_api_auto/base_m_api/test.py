# -*- coding: utf-8 -*-
# TODO (liaoli) ：
#  备注

# c = lambda x, y: x+y
# print(c(3, 2))
# list1 = [1,2,3]
# list2= [4,5,6]
# list1.extend(list2)
# print(list1)
# print(int('111', 2))  # 二进制转为十进制 2的零次方+2的1次方+2的2次方
def multipliers():
    return [lambda x: i * x for i in range(11)]
# print([m(2) for m in multipliers()])
for m in multipliers():
    print(m(2))

# test = [{'name': 'tom', 'salary': 20000}, {'name': 'jack', 'salary': 15000}, {'name': 'liming', 'salary': 10000}]
# a = sorted(test, key=lambda x: x.get('salary'), reverse=True)
# print(a)
# b = sorted(test, key=lambda x: x.get('salary'), reverse=False)
# print(b)
# c = sorted(test, key=lambda x: x.get('salary'))
# print(c)

# L = [1, 2, 3, 11, 2, 5, 3, 2, 5, 3]
# l1 = list(set(L))
# print(l1)
# print(list(set(L))[::-1])
# print(L[20:])
# L1 = [1, 2, 3, 5, 6]
# s = ''
# for i in L1:
#     s = s+str(i)
#
# print(s)

# from base_m_api.api_m import api_m
# from utils.get_data import getData
#
# # data = getData()
# # mobile = data.get('mobile')
# # password = data.get('password')
# class loginapi(api_m):
#
#     def __init__(self):
#         self.data = getData()
#         self.mobile = self.data.get('mobile')
#         self.password = self.data.get('password')
#     def login_getMsg(self):
#         params = {
#             'mobile': self.mobile,
#             'password': self.password
#             }
#         result = super().pwdLogin(params=params)
#         code = result.json().get('code')
#         if code == '200':
#             message = [{'name': item.get('name'),
#                         'userCode': item.get('userCode'),
#                         'token': item.get('token')} for item in result.json().get('data')]
#             print(message)
# loginapi().login_getMsg()


# a = 'string'
# b = []
# for i in a:
#     b.append(i)
# print(type(b))  # 字符串转化为列表
# print(list(a))  # 字符串转化为列表
# c = 's t r i n g'
# print(c.split(' '))  # 字符串转化为列表
# print(''.join(b))  # 列表转化为字符串

# a = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
# b = []
# c = []
# for i in a:
#     if i > 0:
#         b.append(i)
#     elif i < 0:
#         c.append(i)
#     else:
#         pass
# print(b, len(b))
# print(c, len(c))

# 有两组数据分别为a=[1,2,3,4,5] b=[‘a’,'b','c','d','e']，通过python如何成c=['a1','b2','c3','d4','e5']
# a = [3, 2, 4, 1, 6]
# b = ['a', 'b', 'c', 'd', 'e']
# print([j+str(i) for i, j in zip(a, b)])

# for i in range(1, 10):
#     for j in range(1, i+1):
#         print('{}*{}={}'.format(i, j, i*j), end='    ')
#     print('')

# from utils.data_readwrite import amount
#
# amountPayable = 4
# banlan = 4
# goldCoinAmount = 3
# acount = amount(amountPayable=amountPayable, banlan=banlan, goldCoinAmount=goldCoinAmount)
# banlan1 = acount[0]
# goldCoinAmount1 = acount[1]
# print(banlan1, goldCoinAmount1)




