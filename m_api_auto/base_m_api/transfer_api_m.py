# -*- coding: utf-8 -*-
# TODO (liaoli) ：
#  备注：对接口的中转处理(输出需要的数据)

from base_m_api.api_m import api_m
from base_m_api.login_m import login_getMsg
from config import env_constant
from utils.data_readwrite import data_read


class transfer_api(object):
    def __init__(self):
        self.tsf_api = api_m()

    # 调用findGradeList()接口，获取年级字段的值value，过滤小\中\大班并返回grade_list
    def tsf_findGradeList(self, token):
        params = {}
        res = self.tsf_api.findGradeList(params=params, token=token)
        # print(res.json())
        if res.json().get('code') == '200':
            value = [item.get('value') for item in res.json().get('data').get('itemList')]
            grade_list = value[3:]
            return grade_list
        else:
            print('当前接口请求错误。\nparams = {}\nresult = {}'.format(params, res.json()))

    # 调用getXuekeListBy接口：根据grade获取对应科目，返回subject_list
    def tsf_getXuekeListBy(self, grade, token):
        res = self.tsf_api.getXuekeListBy(grade=grade, token=token)
        # print(res.json())
        subject_list = [item.get('subject') for item in res.json().get('data')]
        return subject_list

    # 调用findClassByCondition接口：根据grade、subject获取所有的班级编码classcode_list
    def tsf_findClassByCondition(self, grade, subject, token):
        res1 = self.tsf_api.findClassByCondition(pageIndex=1, grade=grade, subject=subject, token=token)
        # print(res1.json())
        count = res1.json().get('data').get('items').get('count')
        print('该年级、科目条件下总共有{}课程'.format(count))
        classcode_list = []
        # 判断该条件下是否有课count。若无课，重新变更条件进行请求接口；若有课，返回对应的课程编码
        while count == 0:
            print('当前年级({})、学科({})条件下无课程。'.format(grade, subject))
            res2 = self.tsf_api.findClassByCondition(pageIndex=1, grade=grade, subject=subject, token=token)
            count = res2.json().get('data').get('items').get('count')
        # 当前条件下 课程有多页情况,若超过一页，获取每页的课程编码，并存储到classcode_list中
        totalpage = res1.json().get('data').get('items').get('totalPage')
        for page in range(1, totalpage + 1):
            res3 = self.tsf_api.findClassByCondition(pageIndex=page, grade=grade, subject=subject, token=token)
            data_list = res3.json().get('data').get('items').get('list')
            code = [item.get('code') for item in data_list]
            classcode_list.extend(code)
        # print(classcode_list)
        return classcode_list

    # 调用findClassDetail接口：根据classCode查看班级详情，并返回关键信息class_msg
    def tsf_ClassDetail(self, classCode, token):
        res = self.tsf_api.findClassDetail(classCode=classCode, token=token)
        # print(res.json())
        class_msg = {'classCode': None, 'ClassStatus': None, 'type': None, 'purchased': None, 'hasQualification': None,
                     'semester': None, 'lessonNum': None, 'startLessonNo': None}
        classcode = res.json().get('data').get('code')  # 班级编码
        classstatus = res.json().get('data').get('classStatus')  # 班级状态1
        items = res.json().get('data').get('items')  # 是否拆班
        if items == []:
            type = 0
        else:
            type = 1
        purchased = res.json().get('data').get('purchased')  # 是否已购买
        hasQualification = res.json().get('data').get('hasQualification')  # 是否有资格
        semester = res.json().get('data').get('semester')  # 学期
        remainingLessonNum = res.json().get('data').get('remainingLessonNum')  # 剩余可报课次1
        class_msg['classCode'] = classcode
        class_msg['ClassStatus'] = classstatus
        class_msg['type'] = type
        class_msg['purchased'] = purchased
        class_msg['hasQualification'] = hasQualification
        class_msg['semester'] = semester
        class_msg['lessonNum'] = remainingLessonNum
        lessonNo_list = [{'status': i.get('status'),
                          'lessonNo': i.get('lessonNo')} for i in res.json().get('data').get('syllabi')]
        for i in range(0, len(lessonNo_list)):
            status = lessonNo_list[i].get('status')
            if status == 1:
                lessonNo = lessonNo_list[i].get('lessonNo')
                class_msg['startLessonNo'] = lessonNo
                break
        return class_msg

    # 调用webOrderFastSign接口：根据班级信息进行立即报名
    def tsf_webOrderFastSign(self, classCode, userCode, type, lessonNum, startLessonNo, token):
        res = self.tsf_api.webOrderFastSign(classCode=classCode, userCode=userCode, type=type, lessonNum=lessonNum,
                                      startLessonNo=startLessonNo, token=token)
        return res

    # 调用balance接口：输出学员的账户余额、金币
    def tsf_balance(self, userCode, token):
        res = self.tsf_api.balance(userCode=userCode, token=token)
        # print(res.json())
        balance_msg = {'balance': None, 'goldcoin': None}
        balance = res.json().get('data').get('balance')
        goldcoin = res.json().get('data').get('goldCoin')
        balance_msg['goldcoin'] = goldcoin
        balance_msg['balance'] = balance
        # print(balance_msg)
        return balance_msg

    # 调用calcprice接口：输出各种优惠items、地址deliveryAddress等信息
    def tsf_calcprice(self, classCode, lessonNum, startLessonNo, token):
        res = self.tsf_api.calcprice(classCode=classCode, lessonNum=lessonNum, startLessonNo=startLessonNo, token=token)
        # print(res.json())
        calcprice_msg = {'totalPrice': None, 'amountPayable': None, 'useramount': None, 'deliveryAddress': None,
                         'needDeliveryAddress': None, 'items': None}
        totalPrice = res.json().get('data').get('totalPrice')
        amountPayable = res.json().get('data').get('amountPayable')
        items = res.json().get('data').get('items')
        useramount = res.json().get('data').get('couponUsedStatus').get('amount')
        needDeliveryAddress = res.json().get('data').get('needDeliveryAddress')
        deliveryAddress = res.json().get('data').get('deliveryAddress')
        if needDeliveryAddress == True:
            calcprice_msg['deliveryAddress'] = deliveryAddress
        else:
            calcprice_msg['deliveryAddress'] = ''
        calcprice_msg['totalPrice'] = totalPrice
        calcprice_msg['amountPayable'] = amountPayable
        calcprice_msg['items'] = items
        calcprice_msg['useramount'] = useramount
        calcprice_msg['needDeliveryAddress'] = needDeliveryAddress
        # print(calcprice_msg)
        return calcprice_msg

    # 调用placeOrder接口：确认优惠后进行下单
    def tsf_placeOrder(self, userCode, account, goldCoinAmount, items, deliveryAddress, token):
        res = self.tsf_api.placeOrder(userCode=userCode, account=account, goldCoinAmount=goldCoinAmount, items=items,
                                      deliveryAddress=deliveryAddress, token=token)
        # print(res.json())
        code = res.json().get('code')
        if code == '200':
            orderCode = res.json().get('data').get('orderCode')
            amountPayable = res.json().get('data').get('amountPayable')
            return orderCode, amountPayable
        elif code == '401':
            print('用户未登录，重新登录')
            login_getMsg()
        # elif code == '1015':
        #     print(res.json().get('msg'))
        else:
            print('当前接口请求错误。\nresult = {}'.format(res.json()))

    # 调用findPayingOrder接口：学员是否存在待付款订单，若存在输入订单编号ordercode，若不存在输出None
    def tsf_findPayingOrder(self, userCode, token):
        res = self.tsf_api.findPayingOrder(userCode=userCode, token=token)
        # print(res.json())
        key_list = []
        for k, v in res.json().items():
            key_list.append(k)
        key1 = 'data'
        if key1 in key_list:
            ordercode = res.json().get('data').get('orderCode')
            print('存在待支付订单，订单编号: {}'.format(ordercode))
            # is_ordercode = True
            return ordercode
        else:
            print('无待支付订单')
            ordercode = None
            return ordercode

    # 调用findOrderDetail接口：待付款订单详情的状态Order_msg
    def tsf_findOrderDetail(self, orderId, token):
        res = self.tsf_api.findOrderDetail(orderId=orderId, token=token)
        # print(res.json())
        Order_msg = {'paymentStatus': None, 'orderClosedReason': None}
        orderClosedReason = res.json().get('data').get('orderClosedReason')
        paymentStatus = res.json().get('data').get('paymentStatus')
        Order_msg['paymentStatus'] = paymentStatus
        Order_msg['orderClosedReason'] = orderClosedReason
        # print(Order_msg)
        return Order_msg

    # 调用orderCancel接口：取消待付款订单
    def tsf_orderCancel(self, userCode, orderCode, token):
        res = self.tsf_api.orderCancel(userCode=userCode, orderCode=orderCode, token=token)
        # print(res.json())

    # 调用WeChatPay、AliPay、CMBPaying接口：封装三种支付方式
    def tsf_pay(self, pay_type, ordercode, appId, token):
        if pay_type == 1:
            self.tsf_api.WeChatPay(orderCode=ordercode, appId=appId, token=token)
        elif pay_type == 2:
            self.tsf_api.AliPay(orderCode=ordercode, appId=appId, token=token)
        else:
            self.tsf_api.CMBPaying(orderCode=ordercode, token=token)


if __name__ == '__main__':
    api = transfer_api()
    path = 'data\write_{}.yaml'.format(env_constant.ENVIORNMENT)
    token_msg = data_read(det_path=path)
    token = token_msg[0].get('token')
    userCode = token_msg[0].get('userCode')
    msg = api.tsf_findPayingOrder(userCode=userCode, token=token)
    print(msg[0])

    # api.tsf_orderCancel(userCode=userCode, orderCode=orderCode, token=token)
    # res = api.tsf_balance(userCode=userCode, token=token)
    # lessonNum = 10
    # startLessonNo = 1
    # res1 = api.tsf_calcprice(classCode='BJ21S0196', lessonNum=lessonNum, startLessonNo=startLessonNo, token=token)
    # account = res.get('balance')
    # goldCoinAmount = res.get('goldcoin')
    # items = res1.get('items')
    # api.tsf_placeOrder(userCode=userCode, account=account, goldCoinAmount=goldCoinAmount, items=items, token=token)

