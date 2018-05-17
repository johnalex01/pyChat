#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-19 21:59:35
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import time
import wx
import wx.xrc
#import ConfigParser

# cf = ConfigParser.RawConfigParser()
# cf.read("Config.conf")
# HOST = cf.get("portal", "HOST")
# PORT = cf.get("portal", "PORT")
# RECV_BUF = int(cf.get("portal", "RECV_BUF"))

HOST = "127.0.0.1"
PORT = 6624
RECV_BUF = 4096


class GlobalVal:
    root_gui = None
    createRoom = None
    enterRoom = None
    register = None
    userInfo = None
    friendList = None
    myInfo = None
    rooms = {}  # room_name: room_gui
    others = {}  # other_user_name: private_gui
    sockt = None
    #all_rooms = set([])
    # roomname: {admin: string, intro:string}
    all_roomsInfo = {}
    all_friendStatus = {}
    user_name = ''
    cur_time = ''
    total_time = ''
    login = False

    msgSoundFlag = 1
    requestSoundFlag = 1
    onlineSoundFlag = 1


# def setFontStyle(wx.TextCtrl):
#     pass


def updateTime():
    while True:
        try:
            GlobalVal.sockt.send('08', '')
            time.sleep(60)
        except Exception:
            pass


def runThread(target):
    t1 = threading.Thread(target=target)
    t1.setDaemon(True)
    t1.start()
    return t1
