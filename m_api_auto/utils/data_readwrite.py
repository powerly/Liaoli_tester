# -*- coding: utf-8 -*-
# TODO (liaoli)
#  备注：从接口返回的数据进行写入和读取
import os
import yaml


def data_write(det_path, writedata):
    # 将数据写入到文件中  'data\writedata_test.yaml'
    path = os.path.join(os.path.dirname(os.getcwd()), det_path)
    with open(path, "w", encoding="utf-8") as f:
        yaml.dump(writedata, f, default_flow_style=False, allow_unicode=True)
        f.write('\n')
        f.close()
    # print('成功写入数据。')


def data_read(det_path):
    # 从文件中读取数据
    path = os.path.join(os.path.dirname(os.getcwd()), det_path)
    with open(path, "r", encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


def amount(amountPayable, banlan, goldCoinAmount):
    if amountPayable < goldCoinAmount + banlan:
        # print('余额和高思币支付总额 超出 订单应付金额')
        if amountPayable>banlan:
            # print('余额不够, 需要金币兑换')
            goldCoinAmount = amountPayable-banlan
            print('订单应付金额:{}, 余额支付:{}, 金币支付:{}'.format(amountPayable, banlan, goldCoinAmount))
            return banlan, goldCoinAmount
        elif amountPayable==banlan:
            # print('余额足够，不需要金币')
            goldCoinAmount = 0
            print('订单应付金额:{}, 余额支付:{}, 金币支付:{}'.format(amountPayable, banlan, goldCoinAmount))
            return banlan, goldCoinAmount
        else:
            # print('订单应付金额 小于 余额, 余额足够不需要金币兑换')
            banlan = amountPayable
            goldCoinAmount = 0
            print('订单应付金额:{}, 余额支付:{}, 金币支付:{}'.format(amountPayable, banlan, goldCoinAmount))
            return banlan, goldCoinAmount
    else:
        # print('余额和高思币支付总额 等于 订单应付金额')
        print('订单应付金额:{}, 余额支付:{}, 金币支付:{}'.format(amountPayable, banlan, goldCoinAmount))
        return banlan, goldCoinAmount

if __name__ == '__main__':
    data = {
        'platformName': 'Android',
        'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
    }
    path = 'data\write_test.yaml'
    data_write(det_path=path, writedata=data)
    data = data_read(det_path=path)

