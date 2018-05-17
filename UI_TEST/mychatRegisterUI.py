#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-29 16:43:22
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$

# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Feb 27 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class m_frameRegister
###########################################################################


class m_frameRegister (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"注册", pos=wx.DefaultPosition, size=wx.Size(
            216, 263), style=wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.SYSTEM_MENU)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        gSizer4 = wx.GridSizer(1, 1, 0, 0)

        fgSizer2 = wx.FlexGridSizer(3, 1, 20, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer2.Add((0, 20), 1, wx.EXPAND, 5)

        fgSizer3 = wx.FlexGridSizer(3, 2, 10, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_statictextportName = wx.StaticText(
            self, wx.ID_ANY, u"昵称", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_statictextportName.Wrap(-1)
        self.m_statictextportName.SetFont(wx.Font(
            12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))

        fgSizer3.Add(self.m_statictextportName, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textUserNickname = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), 0)
        self.m_textUserNickname.SetMaxLength(30)
        self.m_textUserNickname.SetFont(wx.Font(
            13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizer3.Add(self.m_textUserNickname, 0, wx.ALL, 5)

        self.m_statictext = wx.StaticText(
            self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_statictext.Wrap(-1)
        self.m_statictext.SetFont(wx.Font(
            12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))

        fgSizer3.Add(self.m_statictext, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textUserpass = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, -1), wx.TE_PASSWORD)
        self.m_textUserpass.SetMaxLength(30)
        self.m_textUserpass.SetFont(wx.Font(
            13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizer3.Add(self.m_textUserpass, 0, wx.ALL | wx.EXPAND, 5)

        self.m_statictextUserpass = wx.StaticText(
            self, wx.ID_ANY, u"确认密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_statictextUserpass.Wrap(-1)
        self.m_statictextUserpass.SetFont(wx.Font(
            12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体"))

        fgSizer3.Add(self.m_statictextUserpass, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_textUserpass1 = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(120, -1), wx.TE_PASSWORD)
        self.m_textUserpass1.SetMaxLength(30)
        self.m_textUserpass1.SetFont(wx.Font(
            13, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        fgSizer3.Add(self.m_textUserpass1, 0, wx.ALL, 5)

        fgSizer2.Add(fgSizer3, 1, wx.EXPAND, 5)

        bSizer16 = wx.BoxSizer(wx.HORIZONTAL)

        bSizer16.Add((0, 0), 1, wx.EXPAND, 5)

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
        self.m_buttonRegister.Bind(wx.EVT_BUTTON, self.on_button_register)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def on_button_register(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.App(None)
    frame = m_frameRegister(None)
    frame.Show()
    app.MainLoop()
