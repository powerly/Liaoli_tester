# -*- coding: utf-8 -*-
# TODO (liaoli) ：
#  备注：原始接口

from common.common_info_m import getData
from common.common_req_m import mpost
from config import env_constant
from utils.data_readwrite import data_read


class api_m(object):
    def __init__(self):
        self.data = getData()
        self.mobile = self.data.get('mobile')
        self.password = self.data.get('password')

    def pwdLogin(self, params):
        '''
        密码登录
        :param  params
        :return: res
        '''
        url = self.data.get('url_Login')
        res = mpost(url=url, params=params, token=None)
        return res

    def findGradeList(self, params, token):
        '''
        获取年级列表
        :return: res
        '''
        url = '/api/v1/class/findGradeList'
        res = mpost(url=url, params=params, token=token)
        return res

    def getXuekeListBy(self, grade, token):
        '''
        根据年级获取学科列表
        :param  grade:年级
        :return: res
        '''
        url = '/api/v1/class/getxuekelistby'
        params = {'grade': grade}
        res = mpost(url=url, params=params, token=token)
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))

    def findClassByCondition(self, pageIndex, grade, subject, token):
        '''
        根据条件筛选班级
        :param pageIndex：页数、grade:年级、subject:学科
        :return res
        '''
        url = '/api/v1/class/findClassByCondition'
        params = {'pageSize': 10,
                  'pageIndex': pageIndex,
                  'grade': grade,
                  'subject': subject
                  }
        res = mpost(url=url, params=params, token=token)
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))

    def findClassDetail(self, classCode, token):
        '''
        获取班级详情
        :param  classCode班级编码
        :return: res
        '''
        url = '/api/v1/class/findClassDetail'
        params = {'code': classCode}
        res = mpost(url=url, params=params, token=token)
        # print(res.json())
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))

    # def isHasPaper(self, classTypeCode, token):
    #     """
    #     M站---查看是否有试卷-诊断
    #     :param url: '/api/v1/papers/isHasPaper'
    #     :return:
    #     """
    #     url = '/api/v1/papers/isHasPaper'
    #     params = {
    #         "classTypeCode": classTypeCode,
    #         # "grade": "",
    #         # "pageIndex": 1,
    #         # "pageSize": 20,
    #         "purposesname": "入学诊断"
    #         # "semester": 4,
    #         # "studentCode": "BJ347513",
    #         # "year": 2021
    #     }
    #     res = mpost(url=url, params=params, token=token)
    #     return res

    def webOrderFastSign(self, classCode, userCode, type, lessonNum, startLessonNo, token):
        """
        立即报名
        :param url:
        :param classCode班级编码、userCode学生编码、type购课类型：0：剩余课次，1：全部课次、lessonNum报名课次、startLessonNo报名开始课节
        :return:
        """
        url = '/api/v1/webOrder/fastSign'
        params = {
            "classCode": classCode,
            "lessonNum": lessonNum,
            "startLessonNo": startLessonNo,
            "studentCode": userCode,
            "type": type
        }
        res = mpost(url=url, params=params, token=token)
        # print(res.json())
        return res

    def balance(self, userCode, token):
        """
        M站---查询学生账户余额
        :param userCode
        :return:res
        """
        url = '/api/v1/account/balance'
        params = {
            "studentCode": userCode
        }
        res = mpost(url=url, params=params, token=token)
        # print(res.json())
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))

    def calcprice(self, classCode, lessonNum, startLessonNo, token):
        """
        M站---计算价格
        :param classCode：班级编码、lessonNum：剩余购买课次数、startLessonNo：开始课次、
        selectedCouponIds:选择使用的优惠券id
        :return:
        """
        url = '/api/v1/account/calcprice'
        params = {
            "channel": 7,
            "choosedCoupon": True,
            "orderClassList": [{
                "classCode": classCode,
                "lessonNum": lessonNum,
                "startLessonNo": startLessonNo
                }],
            "selectedCouponIds": [],
            "isGroupBooking": False
            }
        res = mpost(url=url, params=params, token=token)
        # print(res.json())
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))

    def addressInsert(self, userCode, token):
        """
        M站---新建收货地址
        :param usercode
        :return:
        """
        url = '/api/v1/user/delivery/address/insert'
        params = {
            "studentCode": userCode,
            "address": "c测试地址",
            "Area": "东城区",
            "AreaId": 110101,
            "City": "北京市",
            "CityId": 1101,
            "ContactNumber": "13611112222",
            "Contacts": "cs",
            "Id": 47608,
            "IsDefault": True,
            "Province": "北京",
            "ProvinceId": 1100,
            "SortNo": 1
        }
        res = mpost(url=url, params=params, token=token)
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))

    # def addressList(self, userCode, token):
    #     """
    #     M站---收货地址列表
    #     :param url: '/api/v1/account/balance'
    #     :return:
    #     """
    #     url = '/api/v1/user/delivery/address/list'
    #     params = {
    #         "studentCode": userCode,
    #     }
    #     res = mpost(url=url, params=params, token=token)
    #     address = [{"address": iterm.get("address"),
    #                 "area": iterm.get("area"),
    #                 "areaId": iterm.get("areaId"),
    #                 "city": iterm.get("city"),
    #                 "cityId": iterm.get("cityId"),
    #                 "contactNumber": iterm.get("contactNumber"),
    #                 "contacts": iterm.get("contacts"),
    #                 "province": iterm.get("province"),
    #                 "provinceId": iterm.get("provinceId")
    #                 }
    #                for iterm in res.json().get("data")]
    #     return address[0]

    def findPayingOrder(self, userCode, token ):
        """
        获取待支付订单
        :param userCode
        :return:
        """
        url = '/api/v1/webOrder/findPayingOrder'
        params = {
            "studentCode": userCode
            }
        res = mpost(url=url, params=params, token=token)
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))

    def placeOrder(self, userCode, account, goldCoinAmount, items, deliveryAddress, token):
        """
        M站---下单接口
        :param  userCode、deliveryAddress
        :return:
        """
        url = '/api/v1/webOrder/placeOrder'
        params = {
            'studentCode': userCode,
            "accountBalanceAmount": account,
            "goldCoinAmount": goldCoinAmount,
            "items": items,
            "channel": 7,
            'deliveryAddress': deliveryAddress
        }
        res = mpost(url=url, params=params, token=token)
        return res

    def findOrderDetail(self, orderId, token):
        """
        M站---订单详情
        :param  orderId
        :return:
        """
        url = '/api/v1/webOrder/findOrderDetail'
        params = {
            'orderId': orderId
            }
        res = mpost(url=url, params=params, token=token)
        # print(res.json())
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))

    def orderCancel(self, userCode, orderCode, token):
        """
        M站---订单取消
        :param  orderId、userCode
        :return:
        """
        url = '/api/v1/webOrder/orderCancel'
        params = {
            "studentCode": userCode,
            'orderCode': orderCode
            }
        res = mpost(url=url, params=params, token=token)
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))

    def WeChatPay(self, orderCode, appId, token):
        """
        M站---微信支付
        :param  orderId, appId
        :return:
        """
        url = '/api/v1/webOrder/findWeChatPayH5Param'
        params = {
            "appId": appId,
            'orderCode': orderCode
            }
        res = mpost(url=url, params=params, token=token)
        # print(res.json())
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))

    def AliPay(self, orderCode, appId, token):
        """
        M站---支付宝支付
        :param  orderId、appId
        :return:
        """
        url = '/api/v1/webOrder/findAliPayH5Param'
        params = {
            "appId": appId,
            'orderCode': orderCode
            }
        res = mpost(url=url, params=params, token=token)
        # print(res.json())
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))

    def CMBPaying(self, orderCode, token):
        """
        M站---一网通支付
        :param  orderId
        :return:
        """
        url = '/api/v1/webOrder/findCMBPayingParam'
        params = {
            'orderCode': orderCode,
            "channel": "PC"
            }
        res = mpost(url=url, params=params, token=token)
        # print(res.json())
        if res.json().get('code') == '200':
            return res
        else:
            print('当前接口请求错误。\nurl = {}\ndata = {}\nresult = {}'.format(url, params, res.json()))


if __name__ == '__main__':
    api = api_m()
    path = 'data\write_{}.yaml'.format(env_constant.ENVIORNMENT)
    token_msg = data_read(det_path=path)
    token = token_msg[0].get('token')
    userCode = token_msg[0].get('userCode')
    api.WeChatPay(orderCode='21947388060565574', appId='wx2bb0c8979d86eea8', token=token)
    # api.orderCancel(userCode=userCode, orderId='21926406727336004', token=token)
    # api.findOrderDetail(orderId='21926406727336004', token=token)
    lessonNum = 12
    startLessonNo = 1



