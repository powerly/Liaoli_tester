# -*- coding: utf-8 -*-
import os
import yaml

from config import env_constant


def get_host(environ):
    # 获取不同环境下的host
    if environ == "test":
        host_dic = 'https://gaosieduapitest.gaosiedu.com'
        return host_dic
    if environ == "formal":
        host_dic = 'https://gaosieduapi.gaosiedu.com'
        return host_dic


def getData():
    # 从文件中获取数据，如登录接口需要的参数
    path = os.path.join(os.path.dirname(os.getcwd()), 'data\data_{}.yaml'.format(env_constant.ENVIORNMENT))
    with open(path, "r", encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data


if __name__ == '__main__':
    res = get_host(env_constant.ENVIORNMENT)
    print(res)

