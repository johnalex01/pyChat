
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-19 21:58:28
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$

import sys
import socket
import struct
import traceback
from utils import *
import wx


class ClientHandler:

    def __init__(self):
        self.is_Connect = False
        self.sock = None
        self.msg_Len = 0
        self.buffer = ''
        self.rest_Buffer = ''
        self.is_Header = True

        pass

    def connect(self):
        try:
            if not self.is_Connect:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.sock.connect((HOST, PORT))
                self.sock.setblocking(0)
        except Exception as e:
            return False
        self.is_Connect = True
        return True

    def send(self, header_code, s):
        content = header_code.encode(
            "utf-8") + struct.pack("<I", len(s)) + b' ' + s.encode('utf-8')
        ###################################
        ##############################

        self.sock.send(content)

    def handleMsg(self):
        if self.rest_Buffer == '':
            data = self.sock.recv(RECV_BUF).decode('utf-8')
        else:
            data = self.rest_Buffer
            self.rest_Buffer = ''

        # print(data)
        if self.is_Header:
            if len(data) < 4:
                return -1
            self.msg_Len = struct.unpack("<I", data[0:4].encode('utf-8'))[0]
            self.buffer = data[5:]
            if self.msg_Len < RECV_BUF and self.msg_Len <= len(self.buffer):
                self.rest_Buffer = self.buffer[self.msg_Len:]
                self.buffer = self.buffer[:self.msg_Len]
                return self.__handle()
            else:
                self.is_Header = False
        else:
            rest_Len = self.self.msg_Len - len(self.buffer)
            if rest_Len < len(data):
                self.buffer += data[:rest_Len]
                self.rest_Buffer = data[rest_Len:]
                self.is_Header = True
                return self.__handle()
            else:
                self.buffer += data

        return 0

    def __handle(self):
        if self.buffer[:5] == 's@reg':
            if self.buffer[6:] == 'create account successfully':
                wx.MessageBox("注册成功，使用用户名和密码登陆", "提示",
                              wx.OK | wx.ICON_INFORMATION)
            elif self.buffer[6:] == 'account already exists':
                wx.MessageBox("注册失败，已经有相同的用户", "提示",
                              wx.OK | wx.ICON_INFORMATION)

        elif self.buffer[:10] == 's@trylogin':
            # 此处应对登陆响应
            GlobalVal.root_gui.handleLogin(self.buffer[11:])
            # logging.info("%s" % self.buffer[11:])

        elif self.buffer[:7] == 's@login':
            # print('s@login ' + self.buffer[8:])
            user = self.buffer[8:]
            try:
                GlobalVal.root_gui.recvNotice(
                    "用户<" + user + ">", "上线了")
            except Exception as e:
                pass
            GlobalVal.sockt.send('09', '')
            # if user == GlobalVal.user_name:
            #     GlobalVal.sockt.send('17', '')
            if user in GlobalVal.all_friendStatus.keys():
                GlobalVal.root_gui.recvNotice(
                    "您的好友<" + user + ">", "上线了")

        elif self.buffer[:8] == 's@logout':
            try:
                GlobalVal.root_gui.recvNotice(
                    "<" + self.buffer[9:] + ">", "下线了")
            except Exception as e:
                pass
            GlobalVal.sockt.send('09', '')
        elif self.buffer[:9] == 's@hallmsg':
            username, msg = self.buffer[10:].split(' ', 1)
            GlobalVal.root_gui.recvMsg(username, msg)

        elif self.buffer[:9] == 's@roommsg':
            # print('s@roommsg ' + self.buffer[10:])
            roomname, speakman, msg = self.buffer[10:].split(' ', 2)
            if roomname in GlobalVal.rooms.keys():
                GlobalVal.rooms[roomname].recvRoomMsg(speakman, msg)

        elif self.buffer[:12] == 's@privatemsg':
           # print('s@privatemsg ' + self.buffer[13:])
            privateUser, msg = self.buffer[13:].split(' ', 1)
            if privateUser not in GlobalVal.others.keys():
                wx.CallAfter(GlobalVal.root_gui.createPrivateUI, privateUser)
                time.sleep(0.1)
                wx.CallAfter(GlobalVal.others[
                    privateUser].recvPrivateMsg, privateUser, msg)
            else:
                GlobalVal.others[privateUser].recvPrivateMsg(privateUser, msg)

        elif self.buffer[:10] == 's@halluser':
            GlobalVal.root_gui.updateHalluser(self.buffer[11:])
        elif self.buffer[:10] == 's@roomuser':
            room, userbuff = self.buffer[11:].split(' ', 1)
            if room in GlobalVal.rooms.keys():
                GlobalVal.rooms[room].updateRoomuser(userbuff)
            pass
        elif self.buffer[:8] == 's@lsroom':
            roomInfo = self.buffer[9:].strip('\n').split('\n')
            if GlobalVal.enterRoom:
                GlobalVal.enterRoom.Updateroomlist(roomInfo)

        elif self.buffer[:12] == 's@createroom':
            username, roomname = self.buffer[13:].split(' ', 1)
            # 大厅收到创建房间的消息
            GlobalVal.root_gui.recvNotice(
                username, "创建了房间 <<" + roomname + ">>")
            if GlobalVal.user_name == username:
                wx.CallAfter(GlobalVal.root_gui.createRoomUI,
                             username + ' ' + roomname)
                GlobalVal.sockt.send('10', roomname)

        elif self.buffer[:11] == 's@enterroom':
            username, roomname, roomadmin = self.buffer[12:].split(' ', 2)
            if roomname not in GlobalVal.rooms.keys():
                wx.CallAfter(GlobalVal.root_gui.createRoomUI,
                             roomadmin + ' ' + roomname)
            else:
                GlobalVal.rooms[roomname].recvNotice(
                    "<" + username + ">", "进入了房间")
                # 其他房间UI收到用户进入消息并更新在线用户
            GlobalVal.sockt.send('10', roomname)
            pass
        elif self.buffer[:6] == 's@time':
            print(self.buffer[7:])

            pass
        elif self.buffer[:11] == 's@leaveroom':
            roomname, username = self.buffer[12:].split(' ', 1)
            GlobalVal.rooms[roomname].recvNotice("<" + username + ">", "离开了房间")
            self.send('10', roomname)
        elif self.buffer[:10] == 's@setadmin':
            print("admin:" + self.buffer[11:])
            room, newadmin = self.buffer[11:].split(' ', 1)
            if room in GlobalVal.rooms.keys():
                GlobalVal.rooms[room].recvNotice(
                    "<" + newadmin + ">", "成为了新房主")
                GlobalVal.rooms[room].updateAdminUser(newadmin)
            pass
        elif self.buffer[:12] == 's@removeroom':
            GlobalVal.root_gui.recvNotice(
                "房间<" + self.buffer[13:] + ">", "已被移除")
            pass
        elif self.buffer[:12] == 's@kickpeople':
            #print("admin:" + self.buffer[11:])
            room, kickuser = self.buffer[13:].split(' ', 1)
            if GlobalVal.user_name == kickuser:
                GlobalVal.rooms[room].BeKicked(room)
            if room in GlobalVal.rooms.keys():
                GlobalVal.rooms[room].recvNotice(
                    "<" + kickuser + ">", "被踢出了房间")
            # self.send('10', room)
            GlobalVal.sockt.send('10', room)

        elif self.buffer[:10] == 's@userinfo':
            # print(self.buffer[11:])
            username, borndate, sex, motto = self.buffer[11:].split(' ', 3)
            # print(username)
            if GlobalVal.userInfo is not None and username != GlobalVal.user_name:
                wx.CallAfter(GlobalVal.userInfo.showUserInfo,
                             username, borndate, sex, motto)
                #GlobalVal.userInfo.showUserInfo(username, borndate, sex, motto)
            elif GlobalVal.myInfo is not None and username == GlobalVal.user_name:
                wx.CallAfter(GlobalVal.myInfo.showUserInfo,
                             username, borndate, sex, motto)
                #GlobalVal.myInfo.showUserInfo(username, borndate, sex, motto)
        elif self.buffer == 's@updatemotto':
            wx.MessageBox("签名修改成功", "提示", wx.OK | wx.ICON_INFORMATION)
        elif self.buffer == 's@updatepass':
            wx.CallAfter(GlobalVal.myInfo.closeUpdatePass)

        elif self.buffer[:10] == 's@lsfriend':
            friendInfo = self.buffer[11:].strip('\n').split('\n')
            # print(friendInfo)
            if GlobalVal.friendList:
                wx.CallAfter(GlobalVal.friendList.Updatefriendlist, friendInfo)
                # GlobalVal.friendList.Updatefriendlist(friendInfo)
        elif self.buffer[:11] == 's@askfriend':
            askfriendName = self.buffer[12:]
            wx.CallAfter(GlobalVal.root_gui.friendRequest, askfriendName)
        elif self.buffer[:14] == 's@deletefriend':
            wx.MessageBox(self.buffer[15:], "提示", wx.OK | wx.ICON_INFORMATION)
            GlobalVal.sockt.send('17', '')
            # self.send(17, '')

        else:
            if GlobalVal.login:
                wx.MessageBox(self.buffer, "提示", wx.OK | wx.ICON_INFORMATION)
                # print("Error buffer: " + self.buffer)
        self.buffer = ''

    def runOnce(self):
        try:
            self.handleMsg()
        except socket.error:
            pass
        except Exception:
            exstr = traceback.format_exc()
            print(exstr)
            if GlobalVal.root_gui is not None:
                pass
            # GlobalVal.root_gui.Destory()
