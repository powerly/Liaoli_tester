# -*- coding: utf-8 -*-
# TODO (liaoli) ：2021-02-19
#  备注：获取验签
'''js验签规则
import  md5  from './md5';
export const generateSignPost=(params, partner, appKey)=> {
    const str = `partner=${partner}&${JSON.stringify(params)}${appKey}`;
    return md5.md5(str);
  }
const partner = "10025";
const appKey= "gaosionline"
 '''
import hashlib
import json


def m_SignPost(data, partner="10025", appKey="gaosionline"):
    data = json.dumps(data)
    str3 = 'partner={}&{}{}'.format(partner, data, appKey)
    # print(str3)
    m1 = hashlib.md5()
    m1.update(str3.encode("utf-8"))
    sign = m1.hexdigest()
    # print(sign)
    return sign


if __name__ == '__main__':
    params = {
      "phone": 13611112222
    }
    m_SignPost(data=params)

