# -*- coding: utf-8 -*-

import pymysql

db = pymysql.connect(host="192.168.245.128",
                     port=3306,
                     user="root",
                     passwd="mysql",
                     db="rouchi",
                     charset="utf8")


def getTeacherId(email):
    # 通过邮箱获取老师的id值
    cursor = db.cursor()
    sql = "SELECT * FROM `student` WHERE `email`=%s"
    cursor.execute(sql, email)
    re = cursor.fetchone()
    des = [i[0] for i in cursor.description]
    dic = dict(zip(des, re))
    cursor.close()
    return dic


def getcourseId(no):
    cursor = db.cursor()
    sql = "SELECT * FROM `course` WHERE `no`=%s"
    cursor.execute(sql, no)
    re = cursor.fetchone()
    des = [i[0] for i in cursor.description]
    dic = dict(zip(des, re))
    cursor.close()
    return dic


def getTieba():
    cursor = db.cursor()
    sql = "select * from tieba order by id desc limit 100"
    cursor.execute(sql)
    re = cursor.fetchall()
    return re


def updatestudent(name, age, gender):
    cursor = db.cursor()

    # SQL 插入语句  里面的数据类型要对应
    sql = "insert into student values(0,'{}',{},{}) ".format(name, age, gender)
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
    except:
        # 发生错误时回滚
        db.rollback()

    # 关闭数据库连接
    db.close()


def inserttieba(name, title, link):
    cursor = db.cursor()
    sql = "insert into tieba values(0,'{}','{}','{}') ".format(name, title, link)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    # db.close()


def insertdouyu(title, type, owner, number, image_url):
    cursor = db.cursor()
    sql = "insert into douyu values(0,'{}','{}','{}','{}','{}') ".format(title, type, owner, number, image_url)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    # db.close()


if __name__ == '__main__':
    # updatestudent(name='fangfang3', age=30, gender=0)
    # inserttieba("gusiyuan", "www.baidu.com")
    insertdouyu('213132','312313','3123123','4万','https://wwewwww.com')