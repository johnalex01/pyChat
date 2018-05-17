#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-05-10 22:44:41
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$

import winsound
MSGSOUND = 'sounds/msg.wav'
REQUESTSOUND = 'sounds/system.wav'
ONLINESOUND = 'sounds/Global.wav'


class SoundManager(object):
    """docstring for SoundManager"""

    def __init__(self):
        super(SoundManager, self).__init__()
        self.msgfile = MSGSOUND
        self.reqfile = REQUESTSOUND
        self.onlinefile = ONLINESOUND

    def playMsgSound(self, flag):
        if flag == 1:
            try:
                winsound.PlaySound(
                    self.msgfile, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception as e:
                pass

    def playRequestSound(self, flag):
        if flag == 1:
            try:
                winsound.PlaySound(
                    self.reqfile, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception as e:
                pass

    def playOnlineSound(self, flag):
        if flag == 1:
            try:
                winsound.PlaySound(
                    self.onlinefile, winsound.SND_FILENAME | winsound.SND_ASYNC)
            except Exception as e:
                pass


smanager = SoundManager()
# smanager.playRequestSound()

# winsound.PlaySound('SystemExclamation',
#                    winsound.SND_FILENAME | winsound.SND_ALIAS)
