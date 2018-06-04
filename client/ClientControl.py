#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-21 14:47:50
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$

from ClientUI import *
from ClientUI import m_frameHall
# from ClientUI import LoginUI
from utils import *
from ClientHandler import ClientHandler
import threading
from soundManager import smanager


class App(wx.App):

    def __init__(self):
        super(self.__class__, self).__init__()

    def OnInit(self):
        hall = Hallcontrol(self.newchatUI)
        # hall.Show()
        self.SetTopWindow(hall)

        return True

    def newchatUI(self, type, name):
        # 1创建群聊房间
        if type == 1:
            hostname, roomname = name.split(' ', 1)
            #print("roomname;" + roomname)
            GlobalVal.rooms[roomname] = PrivateControl(
                None, wx.ID_ANY, roomname, hostname, self.newchatUI)
            GlobalVal.rooms[roomname].Show()
        # 2创建私聊房间
        elif type == 2:
            GlobalVal.others[name] = RoomControl(None, wx.ID_ANY, name)
            GlobalVal.others[name].Show()

        # def OnExit():
        #     print("exit")
        #     pass


class Hallcontrol(m_frameHall):
    """docstring for ClassName"""

    def __init__(self, newUI=None):
        super(Hallcontrol, self).__init__()
        GlobalVal.sockt = ClientHandler()
        GlobalVal.sockt.connect()

        self.newchatUI = newUI

        self.timer = threading.Timer(0.1, self.run_timer)
        self.timer.start()
        GlobalVal.root_gui = self

    def recvLogin(self, userName, password):
        #print(userName + ' ' + password)
        try:
            GlobalVal.sockt.send('01', '%s %s' % (userName, password))
            GlobalVal.user_name = userName
        except Exception:
            wx.MessageBox("连接失败", "错误", wx.OK | wx.ICON_ERROR)

    def recvReg(self, username, pw1, borndate, sex, motto):
        try:
            GlobalVal.sockt.send('00', '%s %s %s %s %s' %
                                 (username, pw1, borndate, sex, motto))
        except Exception:
            wx.MessageBox("连接失败", "错误", wx.OK | wx.ICON_ERROR)
        pass

    def recvCreateroom(self, roomname, roomintro):
        GlobalVal.sockt.send('11', '')
        if roomname in GlobalVal.all_roomsInfo.keys():
            wx.MessageBox("已存在房间", "提示", wx.OK | wx.ICON_INFORMATION)
        else:
            GlobalVal.sockt.send('05', roomname)
        pass

    def recvEnterroom(self, roomname):
        #GlobalVal.sockt.send('11', '')
        if roomname not in GlobalVal.all_roomsInfo.keys():
            wx.MessageBox("不存在该房间", "提示", wx.OK | wx.ICON_INFORMATION)
        elif roomname in GlobalVal.rooms.keys():
            wx.MessageBox("你已经在该房间", "提示", wx.OK | wx.ICON_INFORMATION)
        else:
            GlobalVal.sockt.send('06', roomname)
        #print("RecvEnterroom " + roomname)
        pass

    def handleLogin(self, data):

        if not data:
            wx.MessageBox("服务器未响应", "提示", wx.OK | wx.ICON_INFORMATION)
        elif data == "login successfully":
            GlobalVal.login = True
            self.DoUIchange(GlobalVal.user_name)
            GlobalVal.sockt.send('17', '')
            print(GlobalVal.friendList)
        elif data == ("%s already online" % GlobalVal.user_name):
            wx.MessageBox("该用户已上线", "提示", wx.OK | wx.ICON_INFORMATION)
        elif data == 'password incorrect':
            wx.MessageBox("密码错误", "错误", wx.OK | wx.ICON_ERROR)
        elif data == 'account does not exist':
            wx.MessageBox("该用户不存在", "提示", wx.OK | wx.ICON_INFORMATION)

    def OnbuttonCreate(self, event):

        if GlobalVal.friendList is None:
            GlobalVal.sockt.send('17', '')
            GlobalVal.friendList = m_DialogFriendlist()
            GlobalVal.friendList.ShowModal()

    def OnbuttonMyinfo(self, event):
        GlobalVal.sockt.send('14', GlobalVal.user_name)
        GlobalVal.myInfo = m_DialogMyInfo()

    def OnbuttonEnter(self, event):
        # print(type(GlobalVal.enterRoom))
        if GlobalVal.enterRoom is None:
            GlobalVal.sockt.send('11', '')
            # print('OnbuttonEnter')
            GlobalVal.enterRoom = m_DialogRoomlist(self.recvEnterroom)
            GlobalVal.enterRoom.ShowModal()

    def OnMessageEnter(self, event):
        self.sendMsg()

    def OnbuttonSend(self, event):
        self.sendMsg()

    def OnPopupOne(self, event):
        if self.currentSelectUser != GlobalVal.user_name:
            self.newchatUI(2, self.currentSelectUser)
        elif self.currentSelectUser in GlobalVal.others.keys():
            wx.MessageBox("正在和该用户聊天", "提示", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("不能和自己聊天", "提示", wx.OK | wx.ICON_INFORMATION)

    def OnPopupTwo(self, event):
        if GlobalVal.userInfo is None:
            GlobalVal.sockt.send('14', self.currentSelectUser)
            GlobalVal.userInfo = m_DialogInfo()

    def OnPopupThree(self, event):
        # if self.currentSelectUser in GlobalVal.all_friendStatus.keys():
        #     wx.MessageBox("你们已经是好友，不能重复添加", "提示", wx.OK | wx.ICON_INFORMATION)
        if self.currentSelectUser == GlobalVal.user_name:
            wx.MessageBox("不能添加自己为好友", "提示", wx.OK | wx.ICON_INFORMATION)
        else:
            # 发送好友请求
            GlobalVal.sockt.send('18', self.currentSelectUser)
            pass
        event.Skip()

    def friendRequest(self, askfriendName):
        smanager.playRequestSound(GlobalVal.requestSoundFlag)
        dlg = wx.MessageDialog(None, askfriendName + '请求添加你为好友', "好友请求",
                               wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            GlobalVal.sockt.send('19', '1 ' + askfriendName)
        elif dlg.ShowModal() == wx.ID_NO:
            GlobalVal.sockt.send('19', '0 ' + askfriendName)
        dlg.Destroy()

    # def showUserInfo(self, username, borndate, sex, motto):
    #     GlobalVal.userInfo.m_textCtrlUser.SetValue(username)
    #     GlobalVal.userInfo.m_textCtrlAge.SetValue(borndate)
    #     GlobalVal.userInfo.m_textCtrlSex.SetValue(sex)
    #     GlobalVal.userInfo.m_textCtrlMotto.SetValue(motto)
    #     GlobalVal.userInfo.ShowModal()

    def OnDownline(self, event):
        if GlobalVal.login == False:
            event.Skip()
        else:
            dlg = wx.MessageDialog(None, '您确定退出登陆吗', "消息",
                                   wx.YES_NO | wx.ICON_QUESTION)
            if dlg.ShowModal() == wx.ID_YES:
                GlobalVal.sockt.send('-1', '')
                self.Destroy()
                GlobalVal.login = False
            dlg.Destroy()

        pass
        # try:
        #     GlobalVal.sockt.send('-1', '')
        # except Exception as e:
        #     event.Skip()

        #print("与他聊天" + self.currentSelectUser)

    def sendMsg(self):
        msg = str(self.m_textInput.GetLineText(0)).strip()
        if msg == '':
            wx.MessageBox("内容不能为空", "提示", wx.OK | wx.ICON_INFORMATION)
        else:
            GlobalVal.sockt.send('02', msg)
            self.m_textInput.Clear()
        pass

    def recvMsg(self, username, msg):
        smanager.playMsgSound(GlobalVal.msgSoundFlag)
        currPos = self.m_textChatcontext.GetLastPosition()
        self.m_textChatcontext.AppendText(username + ":\n")
        self.m_textChatcontext.AppendText(msg + '\n')
        self.setMsgFontStyle(currPos, username, msg)
        # print(currPos)
        # self.m_textChatcontext.SetStyle(
        # currPos, currPos + len(username) + 2, wx.TextAttr("BLUE",
        # wx.NullColour))
        pass

    def recvNotice(self, sth, notice):
        currPos = self.m_textChatcontext.GetLastPosition()
        msg = "系统通知:  " + sth + ' ' + notice + '\n'
        self.m_textChatcontext.AppendText(msg)
        # self.m_textChatcontext.AppendText(sth + ' ' + notice + '\n')
        f = wx.Font(self.m_textChatcontext.GetFont().GetPointSize() + 1, wx.FONTFAMILY_TELETYPE,
                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True)
        self.m_textChatcontext.SetStyle(
            currPos, currPos + len(msg) + 1, wx.TextAttr("RED",
                                                         wx.NullColour, f))
        pass

    def setMsgFontStyle(self, currPos, a, b):

        namecolor = 'RED'
        if a == GlobalVal.user_name:
            namecolor = 'GREEN'
        elif a == '':
            namecolor = 'RED'
        else:
            namecolor = 'BLUE'
        points = self.m_textChatcontext.GetFont().GetPointSize()
        f = wx.Font(points + 2, wx.FONTFAMILY_DEFAULT,
                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.m_textChatcontext.SetStyle(
            currPos, currPos + len(a) + 1, wx.TextAttr(namecolor, wx.NullColour, f))
        points = self.m_textChatcontext.GetFont().GetPointSize()
        f = wx.Font(points + 4, wx.FONTFAMILY_TELETYPE,
                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.m_textChatcontext.SetStyle(
            currPos + len(a) + 2, currPos + len(a + b) + 2, wx.TextAttr("BLACK", wx.NullColour, f))

    def createRoomUI(self, roomname):
        self.newchatUI(1, roomname)

    def createPrivateUI(self, username):
        self.newchatUI(2, username)

    def updateHalluser(self, _buffer):
        peopleList = _buffer.strip('\n').split('\n')
        self.m_listPeopleOnline.DeleteAllItems()
        for p in peopleList:
            self.m_listPeopleOnline.InsertItem(
                self.m_listPeopleOnline.GetItemCount(), p)

    def run_timer(self):
        # print("Timer")
        GlobalVal.sockt.runOnce()
        self.timer = threading.Timer(0.2, self.run_timer)
        self.timer.start()

# 私人聊天


class RoomControl(m_frameRoomChat):
    """docstring for RoomControl"""

    def __init__(self, parent, id, title):
        super(RoomControl, self).__init__(parent, id, "与 " + title + " 的聊天")
        self.privateUsername = title

    def sendPrivateMsg(self):
        msg = str(self.m_textCtrlMyMessage.GetLineText(0)).strip()
        if msg == '':
            wx.MessageBox("内容不能为空", "提示", wx.OK | wx.ICON_INFORMATION)
        else:
            GlobalVal.sockt.send('04', "%s %s" % (self.privateUsername, msg))
            self.m_textCtrlMyMessage.Clear()

        currPos = self.m_textCtrlRoomMessage.GetLastPosition()
        self.m_textCtrlRoomMessage.AppendText(GlobalVal.user_name + ":\n")
        self.m_textCtrlRoomMessage.AppendText(msg + '\n')
        self.setMsgFontStyle(currPos, GlobalVal.user_name, msg)
        pass

    def OntextEnter(self, event):
        self.sendPrivateMsg()

    def OnButtonSend(self, event):
        self.sendPrivateMsg()

    def recvPrivateMsg(self, username, msg):
        smanager.playMsgSound(GlobalVal.msgSoundFlag)
        currPos = self.m_textCtrlRoomMessage.GetLastPosition()
        self.m_textCtrlRoomMessage.AppendText(username + ":\n")
        self.m_textCtrlRoomMessage.AppendText(msg + '\n')
        self.setMsgFontStyle(currPos, username, msg)
        # self.m_textCtrlRoomMessage.AppendText(username + ":\n")
        # self.m_textCtrlRoomMessage.AppendText(msg + '\n')
        pass

    def setMsgFontStyle(self, currPos, a, b):

        namecolor = 'RED'
        if a == GlobalVal.user_name:
            namecolor = 'GREEN'
        elif a == '':
            namecolor = 'RED'
        else:
            namecolor = 'BLUE'
        points = self.m_textCtrlRoomMessage.GetFont().GetPointSize()
        f = wx.Font(points + 2, wx.FONTFAMILY_DEFAULT,
                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.m_textCtrlRoomMessage.SetStyle(
            currPos, currPos + len(a) + 1, wx.TextAttr(namecolor, wx.NullColour, f))
        points = self.m_textCtrlRoomMessage.GetFont().GetPointSize()
        f = wx.Font(points + 4, wx.FONTFAMILY_TELETYPE,
                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.m_textCtrlRoomMessage.SetStyle(
            currPos + len(a) + 2, currPos + len(a + b) + 2, wx.TextAttr("BLACK", wx.NullColour, f))

    def OnIconClose(self, event):
        self.closePrivatechat()

    def OnButtonClose(self, event):
        self.closePrivatechat()

    def closePrivatechat(self):
        if self.privateUsername in GlobalVal.others.keys():
            GlobalVal.others.pop(self.privateUsername)
        self.Destroy()

# 房间聊天


class PrivateControl(m_framePrivateChat):
    """docstring for PrivateControl"""

    def __init__(self, parent, id, title, hostname, newUI):
        super(PrivateControl, self).__init__(
            parent, id, "房间： " + title, hostname)
        self.newchatUI = newUI
        self.room_name = title
        self.host_name = hostname

    def sendRoomMsg(self):
        msg = str(self.m_textCtrlMyMessage.GetLineText(0)).strip()
        if msg == '':
            wx.MessageBox("内容不能为空", "提示", wx.OK | wx.ICON_INFORMATION)
        else:
            GlobalVal.sockt.send('03', "%s %s" % (self.room_name, msg))
            self.m_textCtrlMyMessage.Clear()
        pass

    def OntextEnter(self, event):
        self.sendRoomMsg()

    def OnButtonSend(self, event):
        self.sendRoomMsg()

    def recvRoomMsg(self, username, msg):
        if username != GlobalVal.user_name:
            smanager.playMsgSound(GlobalVal.msgSoundFlag)
        currPos = self.m_textCtrlRoomMessage.GetLastPosition()
        self.m_textCtrlRoomMessage.AppendText(username + ":\n")
        self.m_textCtrlRoomMessage.AppendText(msg + '\n')
        self.setMsgFontStyle(currPos, username, msg)
        pass

    def recvNotice(self, sth, notice):
        currPos = self.m_textCtrlRoomMessage.GetLastPosition()
        msg = "系统通知:  " + sth + ' ' + notice + '\n'
        self.m_textCtrlRoomMessage.AppendText(msg)
        # self.m_textChatcontext.AppendText(sth + ' ' + notice + '\n')
        f = wx.Font(self.m_textCtrlRoomMessage.GetFont().GetPointSize() + 1, wx.FONTFAMILY_TELETYPE,
                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, True)
        self.m_textCtrlRoomMessage.SetStyle(
            currPos, currPos + len(msg) + 1, wx.TextAttr("RED",
                                                         wx.NullColour, f))
        pass

    def setMsgFontStyle(self, currPos, a, b):

        namecolor = 'RED'
        if a == GlobalVal.user_name:
            namecolor = 'GREEN'
        elif a == '':
            namecolor = 'RED'
        else:
            namecolor = 'BLUE'
        points = self.m_textCtrlRoomMessage.GetFont().GetPointSize()
        f = wx.Font(points + 2, wx.FONTFAMILY_DEFAULT,
                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False)
        self.m_textCtrlRoomMessage.SetStyle(
            currPos, currPos + len(a) + 1, wx.TextAttr(namecolor, wx.NullColour, f))
        points = self.m_textCtrlRoomMessage.GetFont().GetPointSize()
        f = wx.Font(points + 4, wx.FONTFAMILY_TELETYPE,
                    wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False)
        self.m_textCtrlRoomMessage.SetStyle(
            currPos + len(a) + 2, currPos + len(a + b) + 2, wx.TextAttr("BLACK", wx.NullColour, f))

    def OnIconClose(self, event):
        self.closeRoomchat()

    def OnButtonClose(self, event):
        self.closeRoomchat()

    def closeRoomchat(self):
        GlobalVal.rooms.pop(self.room_name)
        GlobalVal.sockt.send('07', self.room_name)
        self.Destroy()

    def OnButtonSetHost(self, event):
        self.setHost()

    def OnbuttonKick(self, event):
        self.kick()

    def OnPopupOne(self, event):
        if self.currentSelectUser != GlobalVal.user_name:
            self.newchatUI(2, self.currentSelectUser)
        elif self.currentSelectUser in GlobalVal.others.keys():
            wx.MessageBox("已经再和该用户聊天", "提示", wx.OK | wx.ICON_INFORMATION)
        else:
            wx.MessageBox("不能和自己聊天", "提示", wx.OK | wx.ICON_INFORMATION)

    def OnPopupTwo(self, event):
        # print("设为房主")
        self.setHost()

    def setHost(self):
        if GlobalVal.user_name != self.host_name:
            wx.MessageBox("你无此权限", "提示", wx.OK | wx.ICON_INFORMATION)
        elif GlobalVal.user_name == self.currentSelectUser and GlobalVal.user_name == self.host_name:
            wx.MessageBox("你已经是房主", "提示", wx.OK | wx.ICON_INFORMATION)
        elif GlobalVal.user_name == self.host_name:
            GlobalVal.sockt.send('12', '%s %s' %
                                 (self.room_name, self.currentSelectUser))

    def OnPopupThree(self, event):
        self.kick()

    def kick(self):
        if GlobalVal.user_name != self.host_name:
            wx.MessageBox("你无此权限", "提示", wx.OK | wx.ICON_INFORMATION)
        elif GlobalVal.user_name == self.currentSelectUser:
            wx.MessageBox("你不能踢出自己", "提示", wx.OK | wx.ICON_INFORMATION)
        elif GlobalVal.user_name == self.host_name:
            GlobalVal.sockt.send('13', '%s %s' %
                                 (self.room_name, self.currentSelectUser))
        # print("踢出房间")

    def BeKicked(self, roomname):
        wx.MessageBox("你被踢出了房间 <%s>" % roomname, "提示",
                      wx.OK | wx.ICON_INFORMATION)
        GlobalVal.rooms.pop(roomname)
        self.Destroy()
        pass

    def updateRoomuser(self, _buffer):
        peopleList = _buffer.strip('\n').split('\n')
        self.m_listRoomPeople.DeleteAllItems()
        for p in peopleList:
            self.m_listRoomPeople.InsertItem(
                self.m_listRoomPeople.GetItemCount(), p)
        pass

    def updateAdminUser(self, newhost):
        self.host_name = newhost
        self.m_staticTextOwnername.SetLabel('房主： ' + self.host_name)


if __name__ == "__main__":
    app = App()
    # frame = Hallcontrol()
    # frame.Show()
    app.MainLoop()
