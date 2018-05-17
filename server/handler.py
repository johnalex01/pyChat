#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-19 12:16:00
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$

import struct
import time
import threading
from mychatdbbasedriver import my_dbDriver
from myglobal import GlobalVal
from myglobal import *

# HOST = "127.0.0.1"
# PORT = 6660
# RECV_BUF = 4096  # no less than 2048
# MAX_CONNECTION = 5000


class ServerHandler(object):

    def __init__(self, sock, addr):
        self.sock = sock
        self.addr = addr
        self.is_Header = True
        self.buffer = ''
        self.rest_buffer = ""
        self.msg_len = 0
        self.header_Code = ""
        self.user_name = ""
        self.start_time = 0
        self.history_time = 0
        pass

    def handleMsg(self):
        try:
            if self.rest_buffer == "":
                # data = self.sock.recv(RECV_BUF).decode('gbk')
                data = self.sock.recv(RECV_BUF).decode('utf-8')

                logging.info('data: %s' % data)

            else:
                data = self.rest_buffer
                self.rest_buffer = ""

            if self.is_Header:
                if len(data) < 6:
                    logging.info("Client (%s, %s) is closed" % self.addr)
                    return -1

                self.header_Code = data[:2]
                self.msg_len = struct.unpack(
                    "<I", data[2:6].encode('utf-8'))[0]
                self.buffer = data[7:]
                logging.info('%s@%s: msg len: %s, buffer: %s， len(buffer): %d'
                             % (self.user_name, self.addr, self.msg_len, self.buffer, len(self.buffer)))
                if self.msg_len < RECV_BUF and self.msg_len <= len(self.buffer):
                    self.rest_buffer = self.buffer[self.msg_len:]
                    self.buffer == self.buffer[:self.msg_len]
                    ret = self._handle()
                    if self.rest_buffer != '':
                        return ret + self.handleMsg()
                    else:
                        return ret
                else:
                    self.is_Header = False
            else:
                rest_len = self.msg_len - len(self.buffer)
                logging.info('%s@%s: buffer: %s' %
                             (self.user_name, self.addr, data[:rest_len]))
                if rest_len <= len(data):
                    self.buffer += data[:rest_len]
                    self.buffer = self.buffer
                    self.rest_buffer = data[rest_len:]
                    self.is_Header = True
                    ret = self._handle()
                    if self.rest_buffer != '':
                        return ret + self.handleMsg()
                    else:
                        return ret
                else:
                    self.buffer += data
            return 0

        except Exception as e:
            raise e

        pass

    def _handle(self):
        logging.info("%s@%s: [%s] %s" % (self.user_name,
                                         self.addr, self.header_Code, self.buffer))
        if self.user_name == ''and self.header_Code != '00' and self.header_Code != '01':
            self.sock.send(addHead('login first'))
            self.buffer = ""
            return 0

        if self.header_Code == '00':
            temp = self.buffer.strip().split(' ')
            username, pwd, borndate, sex, motto = temp
            code = my_dbDriver.sign_up(username, pwd, borndate, sex, motto)
            if code == 1:
                self.sock.send(
                    addHead("s@reg create account successfully"))
            elif code == 0:
                self.sock.send(
                    addHead("s@reg account already exists"))
                # userDataDump()
        elif self.header_Code == '01':
            # print(self.buffer)
            tempbuff = self.buffer.strip().split(' ')
            username, password = tempbuff
            code = my_dbDriver.check_password(username, password)
            if code == 1:
                self.sock.send(
                    addHead('s@trylogin account does not exist'))
            elif code == 2:
                self.sock.send(
                    addHead('s@trylogin password incorrect'))
            elif code == 3:
                if username in GlobalVal.login_dict.keys():
                    self.sock.send(
                        addHead('s@trylogin %s already online' % username))
                    GlobalVal.server.clientRemove(self.sock, self.addr)
                    return 0
                GlobalVal.login_dict[username] = self.sock
                self.user_name = username
                self.start_time = time.time()
                #self.history_time = GlobalVal.user_data[username][1]
                self.history_time = my_dbDriver.get_onlineTime(username)
                # print(self.history_time)
                self.sock.send(
                    addHead('s@trylogin login successfully'))
                t = threading.Thread(target=self.updateTime)
                t.setDaemon(True)
                t.start()
                for so in GlobalVal.clients.keys():
                    so.send(addHead('s@login %s' % self.user_name))
        # 大厅消息
        elif self.header_Code == "02":
            for so in GlobalVal.clients.keys():
                # if so != self.sock:
                so.send(addHead("s@hallmsg %s %s" %
                                (self.user_name, self.buffer)))
        # 房间消息
        elif self.header_Code == "03":
            tmp = self.buffer.split(' ', 1)
            if len(tmp) != 2:
                self.sock.send(
                    addHead("there should be a space between room name and message"))
            else:
                for val in GlobalVal.room_dict[tmp[0]]['users']:
                    # if val != self.user_name:
                    GlobalVal.login_dict[val].send(
                        addHead('s@roommsg %s %s %s' % (tmp[0], self.user_name, tmp[1])))

        # 私聊消息
        elif self.header_Code == "04":
            tmp = self.buffer.split(' ', 1)
            if len(tmp) != 2:
                self.sock.send(
                    addHead("there should be a space between user name and message"))
            else:
                if tmp[0] in GlobalVal.login_dict.keys():
                    GlobalVal.login_dict[tmp[0]].send(
                        addHead('s@privatemsg %s %s' % (self.user_name, tmp[1])))
                else:
                    self.sock.send(addHead('您的好友不在线'))

        # 创建房间
        elif self.header_Code == '05':
            if self.buffer not in GlobalVal.room_dict.keys():
                GlobalVal.room_dict[self.buffer] = {
                    'users': [self.user_name], 'game_open': False, 'admin': self.user_name}
                for so in GlobalVal.clients.keys():
                    so.send(addHead('s@createroom %s %s' %
                                    (self.user_name, self.buffer)))
            else:
                self.sock.send(addHead('room already exist'))
        # 进入房间06
        elif self.header_Code == '06':
            # print("rooname: " + self.buffer)
            # print("roomonserver:")
            # for k in GlobalVal.room_dict.keys():
            #     print(k)
            if self.buffer not in GlobalVal.room_dict.keys():
                self.sock.send(addHead('room not exist'))
            elif self.user_name in GlobalVal.room_dict[self.buffer]['users']:
                self.sock.send(addHead('already in'))
            else:
                GlobalVal.room_dict[self.buffer][
                    'users'].append(self.user_name)
                for val in GlobalVal.room_dict[self.buffer]['users']:
                    GlobalVal.login_dict[val].send(
                        addHead('s@enterroom %s %s %s' % (self.user_name, self.buffer, GlobalVal.room_dict[self.buffer]['admin'])))

        # 退出房间07
        elif self.header_Code == '07':
            GlobalVal.room_dict[self.buffer]['users'].remove(self.user_name)
            if len(GlobalVal.room_dict[self.buffer]['users']) == 0:
                GlobalVal.room_dict.pop(self.buffer)
                for key in GlobalVal.clients.keys():
                    key.send(addHead('s@removeroom %s' % self.buffer))
            else:
                for user in GlobalVal.room_dict[self.buffer]['users']:
                    GlobalVal.login_dict[user].send(
                        addHead('s@leaveroom %s %s' % (self.buffer, self.user_name)))
                    if self.user_name == GlobalVal.room_dict[self.buffer]['admin']:
                        tempadmin = GlobalVal.room_dict[
                            self.buffer]['users'][0]
                        GlobalVal.room_dict[self.buffer]['admin'] = tempadmin
                        for other_online_user in GlobalVal.room_dict[self.buffer]['users']:
                            GlobalVal.login_dict[other_online_user].send(
                                addHead('s@setadmin %s %s' % (self.buffer, tempadmin)))

            pass

        # 获取在线时间08
        # 获得大厅在线用户09
        elif self.header_Code == "09":
            tmp = 's@halluser '
            for val in GlobalVal.login_dict.keys():
                tmp += val + '\n'
            for so in GlobalVal.clients.keys():
                so.send(addHead(tmp))
        # 获得房间在线用户10
        elif self.header_Code == '10':
            tmp = 's@roomuser %s ' % self.buffer
            for val in GlobalVal.room_dict[self.buffer]['users']:
                tmp += val + '\n'
            self.sock.send(addHead(tmp))
        # 获得房间列表11
        elif self.header_Code == '11':
            tmp = 's@lsroom '
            for key in GlobalVal.room_dict.keys():
                tmp += (key + '|' + GlobalVal.room_dict[key]['admin'] + '\n')
            self.sock.send(addHead(tmp))

        # 设置房主12
        elif self.header_Code == '12':
            tmp = self.buffer.split(' ', 1)
            room, newadmin = tmp
            # print("newadmin:" + newadmin)
            if GlobalVal.room_dict[room]['admin'] != self.user_name:
                self.sock.send(addHead('你无此权限'))
            elif newadmin not in GlobalVal.room_dict[room]['users']:
                self.sock.send(addHead('该用户已经离开房间'))
            else:
                GlobalVal.room_dict[room]['admin'] = newadmin
                for val in GlobalVal.room_dict[room]['users']:
                    GlobalVal.login_dict[val].send(
                        addHead('s@setadmin %s %s' % (room, newadmin)))
            # 踢人
        elif self.header_Code == '13':
            tmp = self.buffer.split(' ', 1)
            room, kickuser = tmp
            if GlobalVal.room_dict[room]['admin'] != self.user_name:
                self.sock.send(addHead('你无此权限'))
            else:
                for val in GlobalVal.room_dict[room]['users']:
                    GlobalVal.login_dict[val].send(
                        addHead('s@kickpeople %s %s' % (room, kickuser)))
                GlobalVal.room_dict[room]['users'].remove(kickuser)
        # 查看资料
        elif self.header_Code == '14':
            username = self.buffer
            res = my_dbDriver.get_userInfo(username)
            # print(res)
            self.sock.send(addHead('s@userinfo %s %s %s %s' %
                                   (res[0], res[2], res[3], res[4])))
            # print(res[0] + ' ' + res[2] + ' ' + res[3] + ' ' + res[4])
        # 修改个人签名
        elif self.header_Code == '15':
            newmotto = self.buffer
            code = my_dbDriver.update_motto(self.user_name, newmotto)
            if code == 1:
                self.sock.send(addHead('s@updatemotto'))
            elif code == 0:
                self.sock.send(addHead('修改失败'))
        # 修改个人密码
        elif self.header_Code == '16':
            old, new = self.buffer.split(' ')
            code = my_dbDriver.update_pass(self.user_name, old, new)
            if code == -1:
                self.sock.send(addHead('原密码错误'))
            elif code == -2:
                self.sock.send(addHead('新密码与原密码不能相同'))
            elif code == 1:
                self.sock.send(addHead('s@updatepass'))
            else:
                self.sock.send(addHead('密码修改失败'))

        # 查看好友
        elif self.header_Code == '17':
            tmp = 's@lsfriend '
            res = my_dbDriver.get_friend(self.user_name)
            print(res)
            for r in res:
                if r[0] in GlobalVal.login_dict.keys():
                    tmp += (r[0] + '|1' + '\n')
                else:
                    tmp += (r[0] + '|0' + '\n')

            self.sock.send(addHead(tmp))
            pass

        # 请求添加好友
        elif self.header_Code == '18':
            friendList = my_dbDriver.get_friend(self.user_name)
            asked_user = self.buffer
            if asked_user in friendList:
                self.sock.send(addHead('你们已经是好友不能重复添加'))
            else:
                tmp = 's@askfriend ' + self.user_name
                GlobalVal.login_dict[asked_user].send(addHead(tmp))

            pass

        # 回应好友请求
        elif self.header_Code == '19':
            tmp = 's@addreq '
            user = self.buffer[2:]
            if self.buffer[:1] == '1':
                # 同意
                print('同意了')
                my_dbDriver.add_friend(self.user_name, user)
                GlobalVal.login_dict[user].send(
                    addHead(self.user_name + ' 同意了你的好友请求'))
                pass

            elif self.buffer[:1] == '0':
                # 不同意
                GlobalVal.login_dict[user].send(
                    addHead(self.user_name + ' 拒绝了你的好友请求'))
                pass

        # 删除好友
        elif self.header_Code == '20':
            tmp = 's@deletefriend '
            code = my_dbDriver.del_friend(self.user_name, self.buffer)
            if code == 1:
                self.sock.send(addHead(tmp + '删除成功'))
            else:
                self.sock.send(addHead('删除失败，或许已删除'))
            pass

        elif self.header_Code == '-1':
            GlobalVal.server.clientRemove(self.sock, self.addr)

        else:
            self.buffer = ""
            return -1
        self.buffer = ""
        return 0

        pass

    def updateTime(self):
        while True:
            try:
                interval = time.time() - self.start_time
                self.sock.send(addHead('s@time %s,%s' %
                                       (getTimeStr(interval), getTimeStr(interval + self.history_time))))
                time.sleep(60)
            except Exception:
                GlobalVal.server.clientRemove(self.sock, self.addr)
                break
