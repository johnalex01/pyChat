#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-19 12:47:28
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$

import logging
import struct
import time
import json

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] [%(levelname)s] %(message)s',
                    datefmt='%H:%M:%S',
                    filename='logs/Server6624_' +
                    time.strftime('%Y_%m_%d', time.localtime(
                        time.time())) + '.log',
                    filemode='a')

HOST = "127.0.0.1"
PORT = 6624
RECV_BUF = 4096  # no less than 2048
MAX_CONNECTION = 5000


class GlobalVal:
    user_data = {}  # username: (pwd, onlinetime)
    # roomname: {users: [username], game_open: bool, admin: string}
    room_dict = {}
    clients = {}  # socket: serverProxy
    login_dict = {}  # username: socket
    sockts = []
    server = None



def addHead(s):
    content = struct.pack("<I", len(s)) + b' ' + s.encode('utf-8')
    return content


def userDataLoad():
    with open('users.db', 'r') as f:
        try:
            GlobalVal.user_data = json.load(f)
        except Exception:
            pass
    f.close()


def userDataDump():
    with open('users.db', 'w') as f:
        json.dump(GlobalVal.user_data, f)
    f.close()


def getTimeStr(tm):
    m, s = divmod(round(tm), 60)
    h, m = divmod(m, 60)
    return "%d h %d m" % (h, m)
