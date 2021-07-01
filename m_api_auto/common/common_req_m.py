# -*- coding: utf-8 -*-
# TODO (liaoli) ：2021-02-19
#  备注：接口封装（含头信息）
import logging
import requests

from common.common_info_m import get_host
from config import env_constant
from utils.gs_logs import Mylogger
from utils.m_sign import m_SignPost


def mpost(url, params, token=None):
    logging.captureWarnings(True)
    host = get_host(env_constant.ENVIORNMENT)
    URL = host + url
    # print(URL)
    logger = Mylogger(url)
    logger.logger('*' * 40)
    logger.logger('url= {}'.format(url))
    logger.logger('req_params= {}'.format(params))
    sign = m_SignPost(data=params)
    headers = {
        "partner": "10025",
        "sign": sign,
        "Content-Type": "application/json"
    }
    if all([token]):
        headers.update({
            "token": token
        })

    res = requests.post(url=URL, json=params, headers=headers, verify=False)
    # print(res.content)
    logger.logger('status_code={}'.format(res.status_code))
    # logger.logger('resp_headers={}'.format(res.headers))
    logger.logger('resp_body={}'.format(res.text))
    logger.logger('*' * 40)
    return res


