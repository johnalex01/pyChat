#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-04-29 17:36:57
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Feb 27 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.lib.calendar

###########################################################################
# Class m_DialogReg
###########################################################################

month_dict = {'January': '1', 'February': '2', 'March': '3', 'April': '4', 'May': '5', 'June': '6',
              'July': '7', 'August': '8', 'September': '9', 'October': '10', 'November': '11', 'December': '12'}


class m_DialogReg (wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, id=wx.ID_ANY, title=u"注册", pos=wx.DefaultPosition, size=wx.Size(
            300, 400), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer6 = wx.FlexGridSizer(4, 1, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer6.Add((0, 40), 1, wx.EXPAND, 5)

        fgSizer9 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer9.Add((50, 0), 1, wx.EXPAND, 5)

        fgSizer8 = wx.FlexGridSizer(6, 2, 5, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticTextUser = wx.StaticText(
            self, wx.ID_ANY, u"您的昵称", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextUser.Wrap(-1)
        fgSizer8.Add(self.m_staticTextUser, 0, wx.ALL, 5)

        self.m_textCtrlUser = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer8.Add(self.m_textCtrlUser, 0, wx.ALL, 5)

        self.m_staticTextPass = wx.StaticText(
            self, wx.ID_ANY, u"您的密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextPass.Wrap(-1)
        fgSizer8.Add(self.m_staticTextPass, 0, wx.ALL, 5)

        self.m_textCtrlPass = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        fgSizer8.Add(self.m_textCtrlPass, 0, wx.ALL, 5)

        self.m_staticTextSurePass = wx.StaticText(
            self, wx.ID_ANY, u"确认密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextSurePass.Wrap(-1)
        fgSizer8.Add(self.m_staticTextSurePass, 0, wx.ALL, 5)

        self.m_textCtrlSurePass = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        fgSizer8.Add(self.m_textCtrlSurePass, 0, wx.ALL, 5)

        self.m_staticTextAge = wx.StaticText(
            self, wx.ID_ANY, u"年龄", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextAge.Wrap(-1)
        fgSizer8.Add(self.m_staticTextAge, 0, wx.ALL, 5)

        fgSizer5 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textCtrlAge = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), wx.TE_READONLY)
        self.m_textCtrlAge.SetMaxLength(2)
        fgSizer5.Add(self.m_textCtrlAge, 0, wx.ALL, 5)

        self.m_button3 = wx.Button(
            self, wx.ID_ANY, u".", wx.DefaultPosition, wx.Size(20, -1), 0)
        fgSizer5.Add(self.m_button3, 0, wx.ALL, 5)

        fgSizer8.Add(fgSizer5, 1, wx.EXPAND, 5)

        self.m_staticTextSex = wx.StaticText(
            self, wx.ID_ANY, u"性别", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextSex.Wrap(-1)
        fgSizer8.Add(self.m_staticTextSex, 0, wx.ALL, 5)

        m_choiceSexChoices = [u"男", u"女"]
        self.m_choiceSex = wx.Choice(
            self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceSexChoices, 0)
        self.m_choiceSex.SetSelection(0)
        fgSizer8.Add(self.m_choiceSex, 0, wx.ALL, 5)

        self.m_staticTextMotto = wx.StaticText(
            self, wx.ID_ANY, u"个性签名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextMotto.Wrap(-1)
        fgSizer8.Add(self.m_staticTextMotto, 0, wx.ALL, 5)

        self.m_textCtrlMotto = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer8.Add(self.m_textCtrlMotto, 0, wx.ALL, 5)

        fgSizer9.Add(fgSizer8, 1, wx.EXPAND, 5)

        fgSizer6.Add(fgSizer9, 1, wx.EXPAND, 5)

        fgSizer6.Add((0, 20), 1, wx.EXPAND, 5)

        fgSizer10 = wx.FlexGridSizer(1, 4, 0, 0)
        fgSizer10.SetFlexibleDirection(wx.BOTH)
        fgSizer10.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer10.Add((35, 0), 1, wx.EXPAND, 5)

        self.m_buttonSureReg = wx.Button(
            self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.Size(100, 30), 0)
        fgSizer10.Add(self.m_buttonSureReg, 0, wx.ALL, 5)

        self.m_buttonCancel = wx.Button(
            self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.Size(100, 30), 0)
        fgSizer10.Add(self.m_buttonCancel, 0, wx.ALL, 5)

        fgSizer6.Add(fgSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_button3.Bind(wx.EVT_BUTTON, self.OnButtonDate)
        self.m_buttonSureReg.Bind(wx.EVT_BUTTON, self.OnButtonSureReg)
        self.m_buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnButtonDate(self, event):
        dlg = wx.lib.calendar.CalenDlg(self)
        dlg.Centre()

        if dlg.ShowModal() == wx.ID_OK:
            result = dlg.result
            day = result[1]
            month = month_dict[result[2]]
            year = result[3]
            new_date = str(year) + '/' + str(month) + '/' + str(day)
            self.m_textCtrlAge.SetValue(new_date)
            #self.log.WriteText('Date Selected: %s\n' % new_date)
        else:
            self.m_textCtrlAge.SetValue('1')
            #self.log.WriteText('No Date Selected')
        event.Skip()

    def OnButtonSureReg(self, event):
    	print(m_textCtrlPass)
        print(self.m_choiceSex.GetStringSelection())
        print(self.m_textCtrlAge.GetValue())
        event.Skip()

    def OnButtonCancel(self, event):
        event.Skip()

    # def TestDlg(self, event):       # test the date dialog


if __name__ == '__main__':
    app = wx.App(None)
    frame = m_DialogReg(None)
    frame.Show()
    app.MainLoop()
