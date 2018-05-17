#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-03 12:20:25
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$

###########################################################################
# Python code generated with wxFormBuilder (version Feb 27 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class m_frameLogin
###########################################################################


class m_frameLogin (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"python聊天系统", pos=wx.DefaultPosition, size=wx.Size(
            314, 306), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU)
        wx.Frame.__init__()

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer4 = wx.GridSizer(1, 1, 0, 0)

        fgSizer2 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer2.Add((0, 80), 1, wx.EXPAND, 5)

        fgSizer3 = wx.FlexGridSizer(3, 2, 0, 20)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_statictextportName = wx.StaticText(
            self, wx.ID_ANY, u"服务器端口", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_statictextportName.Wrap(-1)
        self.m_statictextportName.SetFont(wx.Font(
            15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas"))

        fgSizer3.Add(self.m_statictextportName, 0, wx.ALL | wx.ALIGN_RIGHT, 5)

        self.m_textPort = wx.TextCtrl(
            self, wx.ID_ANY, u"127.0.0.1:", wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_textPort.SetMaxLength(30)
        self.m_textPort.SetFont(wx.Font(
            13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizer3.Add(self.m_textPort, 0, wx.ALL, 5)

        self.m_statictextUsername = wx.StaticText(
            self, wx.ID_ANY, u"账号", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_statictextUsername.Wrap(-1)
        self.m_statictextUsername.SetFont(wx.Font(
            15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas"))

        fgSizer3.Add(self.m_statictextUsername, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textUsername = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, -1), 0)
        self.m_textUsername.SetMaxLength(30)
        self.m_textUsername.SetFont(wx.Font(
            13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizer3.Add(self.m_textUsername, 0, wx.ALL | wx.EXPAND, 5)

        self.m_statictextUserpass = wx.StaticText(
            self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_statictextUserpass.Wrap(-1)
        self.m_statictextUserpass.SetFont(wx.Font(
            15, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Consolas"))

        fgSizer3.Add(self.m_statictextUserpass, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textUserpassword = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(150, -1), wx.TE_PASSWORD)
        self.m_textUserpassword.SetMaxLength(30)
        self.m_textUserpassword.SetFont(wx.Font(
            13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizer3.Add(self.m_textUserpassword, 0, wx.ALL, 5)

        fgSizer2.Add(fgSizer3, 1, wx.EXPAND, 5)

        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer16.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_buttonLogin = wx.Button(
            self, wx.ID_ANY, u"登陆", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.m_buttonLogin, 0, wx.ALL, 5)

        self.m_buttonRegister = wx.Button(
            self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer16.Add(self.m_buttonRegister, 0, wx.ALL, 5)

        bSizer16.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer2.Add(bSizer16, 0, wx.EXPAND, 5)

        gSizer4.Add(fgSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer4)
        self.Layout()

        self.Centre(wx.HORIZONTAL)

        # Connect Events
        self.m_buttonLogin.Bind(wx.EVT_BUTTON, self.on_loginbutton_click)
        self.m_buttonRegister.Bind(wx.EVT_BUTTON, self.on_loginbutton_register)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_loginbutton_click(self, event):
        event.Skip()

    def on_loginbutton_register(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.App(None)
    frame = m_frameLogin(None)
    frame.Show()
    app.MainLoop()
