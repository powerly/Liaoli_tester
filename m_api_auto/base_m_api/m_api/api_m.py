# -*- coding: utf-8 -*-
# TODO (liaoli) ：2021-02-19
#  备注：所有接口
import constants
from common.common_req_m import Common
from utils.tools_print import better_print


class ParentPayment(Common):
    def __init__(self, root_url):
        super(ParentPayment, self).__init__(root_url)
        self.root_url = root_url
        self.StudentCode = constants.StudentCode
        self.token = {
            "token": constants.Token
        }

    def loginPassWord(self, url='/api/v1/login/password'):
        """
        M站---登录接口
        :param url: '/api/v1/login/password'
        :return:
        """

        res = self.mpost(
            url=url,
            params={
                "mobile": "15868153950",
                "password": "1234567a"
            }
        )
        print(better_print(res.content))
        return res

    def accountBalance(self, url='/api/v1/account/balance'):
        """
        M站---查询学生账户余额
        :param url: '/api/v1/account/balance'
        :return:
        """

        res = self.mpost(
            url=url,
            params={
                "studentCode": self.StudentCode
            },
            **self.token
        )
        print(better_print(res.content))
        return res

    def addressInsert(self, url='/api/v1/user/delivery/address/insert'):
        """
                M站---新建收货地址
                :param url: '/api/v1/account/balance'
                :return:
                """
        res = self.mpost(
            url=url,
            params={
                "studentCode": self.StudentCode,
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
            },
            **self.token
        )
        print(better_print(res.content))
        return res

    def addressList(self, url='/api/v1/user/delivery/address/list'):
        """
        M站---收货地址列表
        :param url: '/api/v1/account/balance'
        :return:
        """
        res = self.mpost(
            url=url,
            params={
                "studentCode": self.StudentCode,
            },
            **self.token
        )
        address = [{"address": iterm.get("address"),
                    "area": iterm.get("area"),
                    "areaId": iterm.get("areaId"),
                    "city": iterm.get("city"),
                    "cityId": iterm.get("cityId"),
                    "contactNumber": iterm.get("contactNumber"),
                    "contacts": iterm.get("contacts"),
                    "province": iterm.get("province"),
                    "provinceId": iterm.get("provinceId")
                    }
                   for iterm in res.json().get("data")]
        return address[0]

    def collectionCourse(self, url='/api/v1/webOrder/collectionCourse'):
        """
        M站---收藏课程
        :param url: '/api/v1/account/balance'
        :return:
        """
        res = self.mpost(
            url=url,
            params={
                "studentCode": self.StudentCode,
                "classCodes": ["BJ21H0399"]
            },
            **self.token
        )
        print(better_print(res.content))
        return res

    def removeCollectionCourse(self, url='/api/v1/webOrder/removeCollectionCourse'):
        """
        M站---取消收藏
        :param url: '/api/v1/account/balance'
        :return:
        """
        res = self.mpost(url=url,
                         params={
                             "studentCode": self.StudentCode,
                             "classCodes": ["BJ21H0399"]
                         },
                         **self.token)
        print(better_print(res.content))

    def reserveOriginal(self, url='/api/v1/webOrder/reserveoriginal'):
        """
        M站---添加选课单
        :param url:
        :return:
        """
        res = self.mpost(url=url,
                         params={
                             'classCode': 'BJ21H0399',
                             'studentCode': self.StudentCode
                         },
                         **self.token
                         )
        print(better_print(res.content))

    def webOrderFastSign(self, url='/api/v1/webOrder/fastSign'):
        """
        立即报名
        :param url:
        :param “classCode”: 班级编码
               "lessonNum": 报名课次
               "startLessonNo": 报名开始课节
               "studentCode": 学生编码
               "type": 购课类型：0：剩余课次，1：全部课次
        :return:
        """
        res = self.mpost(url=url,
                         params={
                             "classCode": "BJ21H0397",
                             "lessonNum": 7,
                             "startLessonNo": 1,
                             "studentCode": self.StudentCode,
                             "type": 0
                         },
                         **self.token)

        print(better_print(res.content))

    def webOrderPlaceOrder(self, url='/api/v1/webOrder/placeOrder'):
        """
        M站---下单接口
        :param url:
        :return:
        """
        res = self.mpost(
            url=url,
            params={
                'studentCode': self.StudentCode,
                'items': [{'classCode': 'BJ21S0132',
                           'regLessonNum': 7,
                           'startLessonNo': 1
                           }],
                'channel': 7,
                'deliveryAddress': self.addressList()
            },
            **self.token
        )
        print(better_print(res.content))

    def findPayingOrder(self, url='/api/v1/webOrder/findPayingOrder'):
        """
        获取待支付订单
        :param url:
        :return:
        """
        res = self.mpost(
            url=url,
            params={
                "studentCode": self.StudentCode
            },
            **self.token)
        print(better_print(res.content))


if __name__ == '__main__':
    p = ParentPayment('http://gaosieduapitest.gaosiedu.com')
    # p.collectionCourse()  # 收藏课程
    # p.removeCollectionCourse()  # 取消收藏
    # p.accountBalance()  # 查询学生账户余额
    # p.addressInsert()   # 新建地址
    # p.addressList()     # 收货地址列表
    # p.reserveOriginal()      # 添加选课单
    # p.webOrderFastSign()          # 立即报名
    p.webOrderPlaceOrder()  # 下单 21297323956043845
    p.findPayingOrder()  # 获取待支付订单

