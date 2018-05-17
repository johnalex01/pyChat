#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-29 17:22:40
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$

import pymysql

insert_sql = '''INSERT INTO `chatroom`.`User` ( `UserName`, `Password`, `Age`,`Sex`,`Motto`,`RegisterTime`) 
             VALUES(%s, %s,%s,%s,%s, CURRENT_TIMESTAMP);'''

find_sql = '''SELECT * FROM `user` WHERE `UserName` = %s '''

update_sql = '''UPDATE `user` SET`Password`=%s,`Age`=%s,`Sex`=%s,`Motto`=%s  WHERE `UserName`=%s '''

update_motto_sql = '''UPDATE `user` SET`Motto`=%s  WHERE `UserName`=%s '''

update_pass_sql = '''UPDATE `user` SET`Password`=%s  WHERE `UserName`=%s '''

updateTime_sql = '''UPDATE `user` SET`OnlineTime`=%s  WHERE `UserName`=%s '''

find_friend_sql = '''SELECT fName FROM `friend` WHERE `uName` = %s '''

insert_friend_sql = '''INSERT INTO `chatroom`.`friend` ( `uName`, `fName`) 
             VALUES(%s, %s);'''

del_friend_sql = '''DELETE FROM `friend` WHERE `uName`=%s AND `fName`=%s;'''


class DbDriver(object):
    """docstring for DbDriver"""

    def __init__(self):
        super(DbDriver, self).__init__()
        try:
            self.conn = pymysql.connect(host='localhost', user='root',
                                        password='123456', database='chatroom', charset='utf8')
        except pymysql.err.Error as e:
            print('connect fails!{}'.format(e))

    def sign_up(self, name, password, age, sex, motto):
        cur = self.conn.cursor()
        cur.execute(find_sql, [name])
        res = cur.fetchone()
        if res is None:
            cur.execute(insert_sql, [name, password, age, sex, motto])
            self.conn.commit()
            cur.close()
            return 1
        else:
            return 0
        # conn.close()

    def find_user(self, name):
        cur = self.conn.cursor()
        cur.execute(find_sql, [name])
        res = cur.fetchone()
        self.conn.commit()
        cur.close()
        if res is not None:
            return 0
        else:
            return 1

    def check_password(self, name, password):
        cur = self.conn.cursor()
        cur.execute(find_sql, [name])

        res = cur.fetchone()
        # 未注册
        # print(res)
        self.conn.commit()
        cur.close()
        if res is None:
            return 1
        # 密码错误
        elif res[1] != password:
            return 2
        else:
            return 3

    def update_motto(self, name, motto):
        try:
            cur = self.conn.cursor()
            cur.execute(update_motto_sql, [motto, name])
            self.conn.commit()
            cur.close()
            return 1
        except Exception as e:
            return 0

    def update_pass(self, name, oldpass, newpass):
        cur = self.conn.cursor()
        cur.execute(find_sql, [name])
        res = cur.fetchone()
        if res[1] != oldpass:
            return -1
        else:
            try:
                cur.execute(update_pass_sql, [newpass, name])
                self.conn.commit()
                cur.close()
                return 1
            except Exception as e:
                return 0

    def get_onlineTime(self, name):
        cur = self.conn.cursor()
        cur.execute(find_sql, [name])

        res = cur.fetchone()
        self.conn.commit()
        cur.close()
        return res[5]

    def get_userInfo(self, name):
        cur = self.conn.cursor()
        cur.execute(find_sql, [name])

        res = cur.fetchone()
        self.conn.commit()
        cur.close()
        return res

    def update_onlineTime(self, name, newtime):
        cur = self.conn.cursor()
        cur.execute(updateTime_sql, [newtime, name])
        self.conn.commit()
        cur.close()
        return 1

        pass

    def get_friend(self, name):
        cur = self.conn.cursor()
        cur.execute(find_friend_sql, [name])

        res = cur.fetchall()
        # self.conn.commit()
        cur.close()
        return res

    def add_friend(self, name, fName):
        cur = self.conn.cursor()
        cur.execute(insert_friend_sql, [name, fName])
        cur.execute(insert_friend_sql, [fName, name])
        self.conn.commit()
        cur.close()

    def del_friend(self, name, fName):
        try:
            cur = self.conn.cursor()
            cur.execute(del_friend_sql, [name, fName])
            cur.execute(del_friend_sql, [fName, name])
            self.conn.commit()
            cur.close()
            return 1
        except Exception as e:
            return 0


my_dbDriver = DbDriver()
# print(my_dbDriver.get_userInfo('yyt')[4])
# print(my_dbDriver.get_friend('1111')[1][0])
# my_dbDriver.del_friend('yyt', '大四')
# # my_dbDriver.update_onlineTime('877', 222)
# # #my_dbDriver.update_info('777', '123', '21', 'm', 'la的发生1')
