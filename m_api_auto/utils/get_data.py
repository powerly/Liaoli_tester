# -*- coding: utf-8 -*-
# TODO (liaoli) ：
#  备注
import os
import yaml


def getData():
    # 需要的数据写入文件中，供接口使用
    path = os.path.join(os.path.dirname(os.getcwd()), 'data\data_test.yaml')
    # path = os.path.join(os.path.dirname(os.getcwd()), 'data\data_{}.yaml'.format(env))
    with open(path, "r", encoding='utf-8') as f:
        data = yaml.safe_load(f)
        # print(data)
    return data

def date_write(writedata):
    # 将数据写入到文件中
    with open(path, "w", encoding="utf-8") as f:
        # yaml.dump(writedata, f, Dumper=yaml.RoundTripDumper, allow_unicode=True)
        # 从json --》文件
        yaml.dump(writedata, f, default_flow_style=False, allow_unicode=True)
        f.write('\n')
        f.close()
    print('成功写入数据。')
