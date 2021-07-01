# -*- coding: utf-8 -*-
# TODO (liaoli) ：
#  备注：判断某个key是否存在json中的
class checkJSON(object):
    keysAll_list = []
    def getKeys(self, data={}):   #遍历json所有key
        if(type(data) == type({})):
            keys = data.keys()
            for key in keys:
                value = data.get(key)
                if(type(value) != type({}) and type(value) != type([])):
                    self.keysAll_list.append( key)
                elif (type(value) == type({})):
                    self.keysAll_list.append(key)
                    self.getKeys(value)
                elif(type(value) == type([])):
                    self.keysAll_list.append(key)
                    for para in value:
                        if (type(para) == type({}) or type(para) == type([])):
                            self.getKeys(para)
                        else:
                            self.keysAll_list.append(para)
        return self.keysAll_list

    def isExtend(self, data, tagkey):
        #检测目标字段tagkey是否在data(json数据)中
        if(type(data) != type({})):
            print('please input a json!')
        else:
            key_list = self.getKeys(data)
            for key in key_list:
                if(key == tagkey):
                    print('存在')
                    return True
        print('不存在')
        return False


if __name__ == '__main__':
    check = checkJSON()
    data = {'code': '200', 'data': {'id': 2, 'name': 'liaoli'}}
    check.isExtend(data=data, tagkey='orderCode')
