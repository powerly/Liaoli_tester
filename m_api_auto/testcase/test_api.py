# -*- coding: utf-8 -*-
# TODO (liaoli) ：
#  备注
import allure

from time import sleep
from random import choice
from base_m_api.login_m import login_getMsg
from base_m_api.transfer_api_m import transfer_api
from config import env_constant
from utils.data_readwrite import data_read, amount


print("当前环境{}".format(env_constant.ENVIORNMENT))
print('M站业务流：随机获取年级学科——>根据年级学科筛选课程——>查看课程获取关键信息——>立即报名——>计算优惠——>'
      '立即下单——>微信/支付宝/一卡通支付——>取消待支付订单')
tsfapi = transfer_api()
# 读取yaml中的数据
path = 'D:\\gaosi_mobile_web\\m_api_auto\\data\\write_{}.yaml'.format(env_constant.ENVIORNMENT)
token_msg = data_read(det_path=path)
token = token_msg[0].get('token')
userCode = token_msg[0].get('userCode')
grade_l = {-2: '小班', -1: '中班', 0: '大班', 1: '一年级', 2: '二年级', 3: '三年级', 4: '四年级', 5: '五年级', 6: '六年级',
           7: '初一', 8: '初二', 9: '初三', 10: '高一', 11: '高二', 12: '高三'}
subject_l = {1: '数学', 2: '语文', 3: '英语', 4: '物理', 7: '生物', 15: '历史', 17: '地理', 18: '政治'}


@allure.story("M站业务流")
@allure.title('开始执行。。。')
@allure.severity('blocker')
def test_run():
    grade_list = tsfapi.tsf_findGradeList(token=token)
    while True:
        # 从grade_list中随机获取的grade
        grade = choice(grade_list)
        for k, v in grade_l.items():
            if k == grade:
                print('随机获取的年级是{}: {}'.format(grade, v))
        # 从subject_list中随机获取的subject
        subject_list = tsfapi.tsf_getXuekeListBy(grade=grade, token=token)
        subject = choice(subject_list)
        for k, v in subject_l.items():
            if k == subject:
                print('随机获取的学科是{}: {}'.format(subject, v))
        # 从class_list中随机获取classcode
        class_list = tsfapi.tsf_findClassByCondition(grade=grade, subject=subject, token=token)
        classcode = choice(class_list)
        # classcode = 'BJ21S2537'
        print('随机获取的班级编码是:{}'.format(classcode))
        allure.attach("从grade_list中随机获取的grade: {}, 从subject_list中随机获取的subject: {}".format(grade, subject))
        # 根据classcode查看课程详情，返回课程的关键信息class_msg
        class_msg = tsfapi.tsf_ClassDetail(classCode=classcode, token=token)
        # print('该课程的关键信息: {}'.format(class_msg))
        allure.attach("从class_list中随机获取的classcode： {}, 该课程的关键信息： {}".format(classcode, class_msg))
        classstatus = class_msg['ClassStatus']
        hasqualification = class_msg['hasQualification']
        classstatus_list = {'未开', '预满', '已满', '结束'}
        purchased = class_msg['purchased']
        startlessonno = class_msg['startLessonNo']
        # 判断是否需要诊断/当前班级状态/是否有可报讲次，若是（is_findclass=True）返回重新选课；若否，则可以报名
        if hasqualification == False:
            print('需要诊断{}-----------请重新选课'.format(hasqualification))
            allure.attach('需要诊断{}-----------请重新选课'.format(hasqualification))
        elif classstatus in classstatus_list:
            print('当前班级状态:{},无法报名(在未开、预满、已满及结束内)-----------请重新选课'.format(classstatus))
            allure.attach('当前班级状态:{},无法报名(在未开、预满、已满及结束内)-----------请重新选课'.format(classstatus))
        elif purchased == True:
            print('当前班级已购买:{}-----------请重新选课'.format(purchased))
            allure.attach('当前班级已购买:{}-----------请重新选课'.format(purchased))
        elif startlessonno == None:
            print('当前无讲次可报1-----------请重新选课')
            allure.attach('当前无讲次可报1-----------请重新选课')
        else:
            type = class_msg['type']
            if type == 0:
                print('{}班级为拆班班级'.format(classcode))
            else:
                print('{}该班级为非拆班班级'.format(classcode))
            print('可进行报名，调用立即报名接口')
            allure.attach("当前班级可进行报名")
            code = class_msg['classCode']
            assert code == classcode
            lessonNum = class_msg['lessonNum']
            res = tsfapi.tsf_webOrderFastSign(classCode=classcode, userCode=userCode, type=type, lessonNum=lessonNum,
                                              startLessonNo=startlessonno, token=token)
            code = res.json().get('code')
            if code != '200':
                if code == '401':
                    print('用户未登录，重新登录')
                    allure.attach('用户未登录，重新登录')
                    login_getMsg()
                elif code == '1008':
                    print('{}-----------请重新选课'.format(res.json().get('msg')))
                    allure.attach('{}-----------请重新选课'.format(res.json().get('msg')))
                    sleep(10)
                elif code == '1015':
                    print('{}-----------请重新选课'.format(res.json().get('msg')))
                    allure.attach('{}-----------请重新选课'.format(res.json().get('msg')))
                else:
                    print('当前接口请求错误。result = {}'.format(res.json()))
                    allure.attach('当前接口请求错误。result = {}'.format(res.json()))
            else:
                # 当前账户余额、金币(balan_msg)；相关优惠：优惠券、课程优惠等(cal_msg)
                balan_msg = tsfapi.tsf_balance(userCode=userCode, token=token)
                cal_msg = tsfapi.tsf_calcprice(classCode=classcode, lessonNum=lessonNum, startLessonNo=startlessonno, token=token)
                account = balan_msg.get('balance')
                goldCoinAmount = balan_msg.get('goldcoin')
                items = cal_msg.get('items')
                deliveryAddress = cal_msg.get('deliveryAddress')
                amountPayable = cal_msg.get('amountPayable')  # 应付金额
                acount = amount(amountPayable=amountPayable, banlan=account, goldCoinAmount=goldCoinAmount)
                banlan = acount[0]
                goldCoinAmount1 = acount[1]
                allure.attach('订单应付金额:{}, 余额支付:{}, 金币支付:{}'.format(amountPayable, banlan, goldCoinAmount1))
                # 判断是否存在待支付订单 若存在True，查看待付款订单
                order = tsfapi.tsf_findPayingOrder(userCode=userCode, token=token)
                if order != None:
                    order_msg = tsfapi.tsf_findOrderDetail(orderId=order, token=token)
                    paymentStatus = order_msg['paymentStatus']
                    orderClosedReason = order_msg['orderClosedReason']
                    if paymentStatus == 0:
                        print('可进行取消')
                        tsfapi.tsf_orderCancel(userCode=userCode, orderCode=order, token=token)
                        print('*'*10 + '成功取消待支付订单' + '*'*10)
                        allure.attach('成功取消待支付订单')
                else:
                    # 循环调用三种支付方式，并取消
                    pay_type = {1: '微信支付', 2: '支付宝支付', 3: '一网通支付'}
                    for k, v in pay_type.items():
                        placeOrder_msg = tsfapi.tsf_placeOrder(userCode=userCode, account=banlan,
                                                               goldCoinAmount=goldCoinAmount1, items=items,
                                                               deliveryAddress=deliveryAddress, token=token)
                        orderCode = placeOrder_msg[0]
                        if placeOrder_msg[1] == 0:
                            print('该订单为0元，直接下单成功。')
                            allure.attach('该订单为0元，直接下单成功。')
                            break
                        else:
                            tsfapi.tsf_pay(pay_type=k, ordercode=orderCode, appId='wx2bb0c8979d86eea8', token=token)
                            print('使用{}进行重新下单，下单成功后的订单编号为: {}'.format(v, orderCode))
                            allure.attach('使用{}，支付成功后的订单编号为: {}'.format(v, orderCode))
                            tsfapi.tsf_orderCancel(userCode=userCode, orderCode=orderCode, token=token)
                            print('成功取消该订单')
                            allure.attach('成功取消该订单，换一种支付方式进行下单')
                    break


# test_run()

