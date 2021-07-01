# -*- coding: utf-8 -*-

import allure

from random import choice
from base_m_api.transfer_api_m import transfer_api
from config import env_constant
# from testcase.test_api import tsfapi
from utils.data_readwrite import data_read

class TestMain:
    @allure.story("M站业务流")
    @allure.title('开始执行。。。')
    @allure.severity('blocker')
    def setup_class(self):
        print("当前环境{}".format(env_constant.ENVIORNMENT))
        print('M站业务流：随机获取年级学科——>根据年级学科筛选课程——>查看课程获取关键信息——>立即报名——>计算优惠——>'
              '立即下单——>微信/支付宝/一卡通支付——>取消待支付订单')
        self.tsfapi = transfer_api()
        # 读取yaml中的数据
        path = 'D:\\gaosi_mobile_web\\m_api_auto\\data\\write_{}.yaml'.format(env_constant.ENVIORNMENT)
        token_msg = data_read(det_path=path)
        self.token = token_msg[0].get('token')
        self.userCode = token_msg[0].get('userCode')
        self.grade_l = {-2: '小班', -1: '中班', 0: '大班', 1: '一年级', 2: '二年级', 3: '三年级', 4: '四年级', 5: '五年级', 6: '六年级',
                   7: '初一', 8: '初二', 9: '初三', 10: '高一', 11: '高二', 12: '高三'}
        self.subject_l = {1: '数学', 2: '语文', 3: '英语', 4: '物理', 7: '生物', 15: '历史', 17: '地理', 18: '政治'}

    @allure.story("M站业务流")
    @allure.title('开始执行。。。')
    @allure.severity('blocker')
    def test_run(self):
        grade_list = self.tsfapi.tsf_findGradeList(token=self.token)
        # 从grade_list中随机获取的grade
        grade = choice(grade_list)
        # print('随机获取的年级是{}'.format(grade))
        for k, v in self.grade_l.items():
            if k == grade:
                print('随机获取的年级是{}: {}'.format(grade, v))
        # 从subject_list中随机获取的subject
        subject_list = self.tsfapi.tsf_getXuekeListBy(grade=grade, token=self.token)
        subject = choice(subject_list)
        for k, v in self.subject_l.items():
            if k == subject:
                print('随机获取的学科是{}: {}'.format(subject, v))
        # 从class_list中随机获取classcode
        class_list = self.tsfapi.tsf_findClassByCondition(grade=grade, subject=subject, token=self.token)
        classcode = choice(class_list)
        # classcode = 'BJ21S2537'
        print('随机获取的班级编码是:{}'.format(classcode))
# import pytest
# import allure
#
#
# class Test_all(object):
#     @allure.story('test_setup story')
#     @allure.step(title="allure通过注解方式完成内容的展示，setp表示测试步骤1...")
#     def test_setup(self):
#         print("我就是打酱油的setup")
#         allure.attach('我是setup')
#
#     @allure.step(title="run就是一个正常的方法.")
#     def test_run(self):
#         allure.attach("自定义描述1", "描述内容，自定义")
#         print("我要运行")
#         assert True
#
#     def test_skip(self):
#         print("我要跳过")
#
#     @allure.severity(allure.severity_level.BLOCKER)  # 严重级别
#     @allure.testcase("http://www.baidu.com/", "测试用例的地址")
#     @allure.issue("http://music.migu.cn/v3/music/player/audio", "点击可跳转到bug地址")
#     def test_error(self):
#         with allure.attach("自定义描述1", "我需要让他进行错误"):
#             print("我错误了")
#             assert False
#
# if __name__ == '__main__':
#     pytest.main(['-s', '-q', '--alluredir', './report'])
'''方式1：在控制台允许'''
# 在控制台第一次运行方式，生成数据：pytest test_flow1.py --alluredir report/other
# 在控制台第二次把数据生成报告：allure generate report/other -o report/html
# pytest test_api.py --alluredir report/other
# allure generate report/other -o report/html
'''方式2：执行py文件'''
# 1）进入运行项目的目录下，执行命令 pytest 运行的py文件
# 2）再使用命令生成报告：allure generate report/ -o report/html

# pytest 运行命令时加入 --alluredir=path，生成测试报告结果数据到文件夹:pytest --alluredir=./myallure
# 直接打开测试报告：allure serve ./myallure
# 将测试报告结果数据生成一个html测试报告到另一个文件report下：  allure generate ./myallure/ -o ./report/ --clean
# 打开测试报告：allure open -h 127.0.0.1 -p 8883 ./report

