#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-03 12:20:25
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
# Class m_frameHall
###########################################################################


class App(wx.App):

    def __init__(self):
        super(self.__class__, self).__init__()

    def OnInit(self):
        hall = m_frameHall(None)
        hall.Show()
        self.SetTopWindow(hall)

        return True

    def OnExit(self):
        print("exit")


class m_frameHall (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"大厅", pos=wx.DefaultPosition, size=wx.Size(
            640, 490), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer3 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textChatcontext = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(
            480, 340), wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
        fgSizer3.Add(self.m_textChatcontext, 0, wx.ALL |
                     wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.m_textInput = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(480, 50), 0)
        fgSizer3.Add(self.m_textInput, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer5 = wx.FlexGridSizer(1, 5, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer5.Add((130, 0), 1, wx.EXPAND, 5)

        fgSizer5.Add((80, 0), 1, wx.EXPAND, 5)

        fgSizer5.Add((80, 0), 1, wx.EXPAND, 5)

        self.m_buttonSend = wx.Button(
            self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(-1, 23), 0)
        fgSizer5.Add(self.m_buttonSend, 0, wx.ALL, 5)

        self.m_buttonclose = wx.Button(
            self, wx.ID_ANY, u"关闭", wx.DefaultPosition, wx.Size(-1, 23), 0)
        fgSizer5.Add(self.m_buttonclose, 0, wx.ALL, 5)

        fgSizer3.Add(fgSizer5, 1, wx.EXPAND, 5)

        fgSizer1.Add(fgSizer3, 1, wx.EXPAND, 5)

        fgSizer4 = wx.FlexGridSizer(7, 1, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer4.Add((0, 25), 1, wx.EXPAND, 5)

        self.fgSizer7 = wx.FlexGridSizer(1, 3, 0, 0)
        self.fgSizer7.SetFlexibleDirection(wx.HORIZONTAL)
        self.fgSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText = wx.StaticText(
            self, wx.ID_ANY, u"欢迎", wx.DefaultPosition,  wx.Size(30, -1), 0)
        self.m_staticText.Wrap(-1)
        self.m_staticText.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(
        ), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        self.fgSizer7.Add(self.m_staticText, 0, wx.ALL, 5)



        self.m_staticTextUserName = wx.StaticText(
            self, wx.ID_ANY, u"", wx.DefaultPosition,  wx.Size(60, -1) , 0)

        # self.m_staticTextUserName = wx.StaticText(
        #     self, wx.ID_ANY, u"小明", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextUserName.Wrap(-1)
        self.m_staticTextUserName.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(
        ), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))

        self.fgSizer7.Add(self.m_staticTextUserName, 0, wx.ALL, 5)

        self.m_buttonInfo = wx.Button(
            self, wx.ID_ANY, u"i", wx.DefaultPosition, wx.Size(20, 20), 0)
        self.fgSizer7.Add(self.m_buttonInfo, 0, wx.ALL, 5)

        fgSizer4.Add(self.fgSizer7, 1, wx.ALIGN_CENTER_VERTICAL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        fgSizer4.Add((0, 20), 1, wx.EXPAND, 5)

        fgSizer6 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_buttonLogin = wx.Button(
            self, wx.ID_ANY, u"登陆", wx.DefaultPosition, wx.Size(120, 25), 0)
        fgSizer6.Add(self.m_buttonLogin, 0, wx.ALL, 5)

        self.m_buttonReg = wx.Button(
            self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.Size(120, 25), 0)
        fgSizer6.Add(self.m_buttonReg, 0, wx.ALL, 5)

        # self.m_buttonCreate = wx.Button(
        #     self, wx.ID_ANY, u"创建房间", wx.DefaultPosition, wx.Size(120, 25), 0)
        # fgSizer6.Add(self.m_buttonCreate, 0, wx.ALL, 5)

        # self.m_buttonEnter = wx.Button(
        #     self, wx.ID_ANY, u"进入房间", wx.DefaultPosition, wx.Size(120, 25), 0)
        # fgSizer6.Add(self.m_buttonEnter, 0, wx.ALL, 5)

        fgSizer4.Add(fgSizer6, 1, wx.EXPAND, 5)

        fgSizer4.Add((0, 20), 1, wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(
            self, wx.ID_ANY, u"大厅用户", wx.Point(-1, -1), wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)
        self.m_staticText2.SetFont(wx.Font(wx.NORMAL_FONT.GetPointSize(
        ), wx.FONTFAMILY_TELETYPE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Arial"))
        self.m_staticText2.SetForegroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))

        fgSizer4.Add(self.m_staticText2, 0, wx.ALL, 5)

        self.m_listPeopleOnline = wx.ListCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(120, 248), wx.LC_REPORT)
        fgSizer4.Add(self.m_listPeopleOnline, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer4, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnLeaveRoom)
        self.m_textInput.Bind(wx.EVT_TEXT_ENTER, self.OnMessageEnter)
        self.m_buttonSend.Bind(wx.EVT_BUTTON, self.OnbuttonSend)
        self.m_buttonclose.Bind(wx.EVT_BUTTON, self.OnbuttonClose)
        # self.m_buttonCreate.Bind(wx.EVT_BUTTON, self.OnbuttonCreate)
        # self.m_buttonEnter.Bind(wx.EVT_BUTTON, self.OnbuttonEnter)
        self.m_buttonLogin.Bind(wx.EVT_BUTTON, self.OnButtonLogin)
        self.m_buttonReg.Bind(wx.EVT_BUTTON, self.OnbuttonReg)
        self.m_listPeopleOnline.Bind(
            wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnHalluserRightClick)
        self.m_listPeopleOnline.Bind(
            wx.EVT_LIST_ITEM_SELECTED, self.OnUserSelected)

        self.m_listPeopleOnline.InsertColumn(0, "群聊成员")
        self.m_listPeopleOnline.SetColumnWidth(0, 100)
        index = self.m_listPeopleOnline.InsertItem(
            self.m_listPeopleOnline.GetItemCount(), "roomInfo[0]")

        # self.m_listPeopleOnline.InsertItem(
        #     self.m_listPeopleOnline.GetItemCount(), "xxxx")

    # Virtual event handlers, overide them in your derived class
    def OnLeaveRoom(self, event):
        event.Skip()

    def OnMessageEnter(self, event):
        event.Skip()

    def OnbuttonSend(self, event):
        msg = str(self.m_textInput.GetLineText(0)).strip()
        print(msg)
        event.Skip()

    def OnbuttonClose(self, event):
        #f = RoomContol(None, wx.ID_ANY, "111")
        # f = m_framePrivateChat(None)
        f = m_DialogUpdatePass()
        f.ShowModal()
        # f.Show()

    def OnbuttonCreate(self, event):
        print("Create")
        createDialog = m_DialogCreateroom()
        createDialog.ShowModal()
        event.Skip()

    def OnbuttonEnter(self, event):
        roomlistDialog = m_DialogRoomlist(self.RecvEnterroom)
        roomlistDialog.ShowModal()
        event.Skip()

    def OnButtonLogin(self, event):
        print("Login")
        loginDialog = m_DialogLogin()
        loginDialog.ShowModal()
        self.m_buttonLogin.SetLabelText(u"创建房间")
        self.m_buttonReg.SetLabelText(u"进入房间")

        self.m_buttonLogin.Unbind(
            wx.EVT_BUTTON)
        self.m_buttonReg.Unbind(
            wx.EVT_BUTTON)

        self.m_buttonLogin.Bind(wx.EVT_BUTTON, self.OnbuttonCreate)
        self.m_buttonReg.Bind(wx.EVT_BUTTON, self.OnbuttonEnter)
        self.m_staticText.SetLabel(u'用户名: ')
        self.m_staticTextUserName.SetLabel(u' 小明')
        # self.m_buttonInfo = wx.Button(
        #     self, wx.ID_ANY, u"i", wx.DefaultPosition, wx.Size(200, 20), 0)
        # self.fgSizer7.Add(self.m_buttonInfo, 0, wx.ALL, 5)

        event.Skip()

    def RecvLogin(self, account, password):
        print(account)
        pass

    def RecvCreate(self, roomname, roomIntro):
        print(roomname)
        pass

    def RecvEnterroom(self, roomname):
        print("RecvEnterroom" + roomname)
        pass

    def OnbuttonReg(self, event):
        regDialog = m_DialogReg(None)
        regDialog.ShowModal()
        event.Skip()

    def OnHalluserRightClick(self, event):
                                # only do this part the first time so the events are only bound
                # once
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()

            self.Bind(wx.EVT_MENU, self.OnPopupOne, id=self.popupID1)
            self.Bind(wx.EVT_MENU, self.OnPopupTwo, id=self.popupID2)

        # make a menu
        menu = wx.Menu()
        # add some items
        menu.Append(self.popupID1, "与他聊天")
        menu.Append(self.popupID2, "查看资料")
        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()

    def OnPopupOne(self, event):

        print("与他聊天" + self.currentSelectUser)

    def OnPopupTwo(self, event):
        userInfo = m_DialogInfo()
        userInfo.ShowModal()

        print("chakan:" + self.currentSelectUser)

    def OnUserSelected(self, event):
        self.currentSelectUserIndex = event.Index
        self.currentSelectUser = self.m_listPeopleOnline.GetItemText(
            self.currentSelectUserIndex)


class m_DialogLogin (wx.Dialog):

    def __init__(self):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=u"登陆", pos=wx.DefaultPosition, size=wx.Size(
            300, 200), style=wx.DEFAULT_DIALOG_STYLE)

       # self.func_callback = func_callback

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer6 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer6.Add((0, 40), 1, wx.EXPAND, 5)

        fgSizer9 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer9.Add((45, 0), 1, wx.EXPAND, 5)

        fgSizer8 = wx.FlexGridSizer(2, 2, 5, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticTextUser = wx.StaticText(
            self, wx.ID_ANY, u"用户名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextUser.Wrap(-1)
        fgSizer8.Add(self.m_staticTextUser, 0, wx.ALL, 5)

        self.m_textCtrlUser = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer8.Add(self.m_textCtrlUser, 0, wx.ALL, 5)

        self.m_staticTextPass = wx.StaticText(
            self, wx.ID_ANY, u"密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextPass.Wrap(-1)
        fgSizer8.Add(self.m_staticTextPass, 0, wx.ALL, 5)

        self.m_textCtrlPass = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        fgSizer8.Add(self.m_textCtrlPass, 0, wx.ALL, 5)

        fgSizer9.Add(fgSizer8, 1, wx.EXPAND, 5)

        fgSizer6.Add(fgSizer9, 1, wx.EXPAND, 5)

        fgSizer10 = wx.FlexGridSizer(1, 4, 0, 0)
        fgSizer10.SetFlexibleDirection(wx.BOTH)
        fgSizer10.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer10.Add((35, 0), 1, wx.EXPAND, 5)

        self.m_buttonSure = wx.Button(
            self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.Size(100, 30), 0)
        fgSizer10.Add(self.m_buttonSure, 0, wx.ALL, 5)

        self.m_buttonCancel = wx.Button(
            self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.Size(100, 30), 0)
        fgSizer10.Add(self.m_buttonCancel, 0, wx.ALL, 5)

        fgSizer6.Add(fgSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_buttonSure.Bind(wx.EVT_BUTTON, self.OnButtonSure)
        self.m_buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnButtonSure(self, event):
        # print("LoginSure")
        self.a = self.m_textCtrlUser.GetValue()
        self.b = self.m_textCtrlPass.GetValue()
        # self.func_callback(a, b)
        self.Destroy()
        event.Skip()

    def OnButtonCancel(self, event):
        self.Destroy()
        event.Skip()


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

        self.m_textCtrlAge = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_textCtrlAge.SetMaxLength(2)
        fgSizer8.Add(self.m_textCtrlAge, 0, wx.ALL, 5)

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

        self.m_buttonSure = wx.Button(
            self, wx.ID_ANY, u"注册", wx.DefaultPosition, wx.Size(100, 30), 0)
        fgSizer10.Add(self.m_buttonSure, 0, wx.ALL, 5)

        self.m_buttonCancel = wx.Button(
            self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.Size(100, 30), 0)
        fgSizer10.Add(self.m_buttonCancel, 0, wx.ALL, 5)

        fgSizer6.Add(fgSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_buttonSure.Bind(wx.EVT_BUTTON, self.OnButtonSure)
        self.m_buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnButtonSure(self, event):
        print(self.m_choiceSex.GetStringSelection())
        event.Skip()

    def OnButtonCancel(self, event):
        event.Skip()


class m_DialogCreateroom (wx.Dialog):

    def __init__(self):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=u"创建房间", pos=wx.DefaultPosition, size=wx.Size(
            250, 180), style=wx.DEFAULT_DIALOG_STYLE)

        #self.func_callback = func_callback
        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer6 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer6.Add((0, 20), 1, wx.EXPAND, 5)

        fgSizer9 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer9.Add((25, 0), 1, wx.EXPAND, 5)

        fgSizer8 = wx.FlexGridSizer(2, 2, 5, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticTextRoomname = wx.StaticText(
            self, wx.ID_ANY, u"房间名称", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextRoomname.Wrap(-1)
        fgSizer8.Add(self.m_staticTextRoomname, 0, wx.ALL, 5)

        self.m_textCtrlRoomname = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer8.Add(self.m_textCtrlRoomname, 0, wx.ALL, 5)

        self.m_staticTextRoomintro = wx.StaticText(
            self, wx.ID_ANY, u"房间简介", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextRoomintro.Wrap(-1)
        fgSizer8.Add(self.m_staticTextRoomintro, 0, wx.ALL, 5)

        self.m_textCtrlIntro = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer8.Add(self.m_textCtrlIntro, 0, wx.ALL, 5)

        fgSizer9.Add(fgSizer8, 1, wx.EXPAND, 5)

        fgSizer6.Add(fgSizer9, 1, wx.EXPAND, 5)

        fgSizer10 = wx.FlexGridSizer(1, 4, 0, 0)
        fgSizer10.SetFlexibleDirection(wx.BOTH)
        fgSizer10.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer10.Add((30, 0), 1, wx.EXPAND, 5)

        self.m_buttonSure = wx.Button(
            self, wx.ID_ANY, u"确认", wx.DefaultPosition, wx.Size(80, 30), 0)
        fgSizer10.Add(self.m_buttonSure, 0, wx.ALL, 5)

        self.m_buttonCancel = wx.Button(
            self, wx.ID_ANY, u"取消", wx.DefaultPosition, wx.Size(80, 30), 0)
        fgSizer10.Add(self.m_buttonCancel, 0, wx.ALL, 5)

        fgSizer6.Add(fgSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_buttonSure.Bind(wx.EVT_BUTTON, self.OnButtonSure)
        self.m_buttonCancel.Bind(wx.EVT_BUTTON, self.OnButtonCancel)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnButtonSure(self, event):
        print("CreateSure")
        self.a = self.m_textCtrlRoomname.GetValue()
        self.b = self.m_textCtrlIntro.GetValue()
        #self.func_callback(a, b)
        self.Destroy()

    def OnButtonCancel(self, event):
        self.Destroy()
        event.Skip()


class m_DialogRoomlist (wx.Dialog):

    def __init__(self, func_callback):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=u"房间列表", pos=wx.DefaultPosition, size=wx.Size(
            400, 300), style=wx.DEFAULT_DIALOG_STYLE)

        self.func_callback = func_callback

        self.SetSizeHints(wx.Size(400, 300), wx.Size(400, 300))

        fgSizer1 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer2 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer2.Add((140, 0), 1, wx.EXPAND, 5)

        self.m_staticText1 = wx.StaticText(
            self, wx.ID_ANY, u"房间列表", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText1.Wrap(-1)
        self.m_staticText1.SetFont(wx.Font(
            15, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString))

        fgSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer2, 1, wx.EXPAND, 5)

        fgSizer3 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer3.Add((40, 0), 1, wx.EXPAND, 5)

        self.m_listCtrl1 = wx.ListCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(300, 180), wx.LC_REPORT | wx.NO_BORDER)
        fgSizer3.Add(self.m_listCtrl1, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer3, 1, wx.EXPAND, 5)

        fgSizer4 = wx.FlexGridSizer(1, 4, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer4.Add((80, 0), 1, wx.EXPAND, 5)

        self.m_buttonEnterroom = wx.Button(
            self, wx.ID_ANY, u"进入房间", wx.DefaultPosition, wx.Size(-1, 30), 0)
        fgSizer4.Add(self.m_buttonEnterroom, 0, wx.ALL, 5)

        self.m_buttonReturn = wx.Button(
            self, wx.ID_ANY, u"创建房间", wx.DefaultPosition, wx.Size(-1, 30), 0)
        fgSizer4.Add(self.m_buttonReturn, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer4, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # # Connect Events
        # self.m_buttonEnterroom.Bind(wx.EVT_BUTTON, self.OnButtonEnterroom)
        # self.m_buttonReturn.Bind(wx.EVT_BUTTON, self.OnButtonReturn)

        self.m_listCtrl1.InsertColumn(0, "房间名")
        self.m_listCtrl1.InsertColumn(1, "房主")
        #self.m_listCtrl1.InsertColumn(2, "房间简介")

        self.m_listCtrl1.SetColumnWidth(0, 80)
        self.m_listCtrl1.SetColumnWidth(1, 80)
        #self.m_listCtrl1.SetColumnWidth(2, 180)

        #self.m_listCtrl1.SetItem(0.0, 0, "roomInfo[2]")
        # self.m_listCtrl1.InsertItem()
        index = self.m_listCtrl1.InsertItem(
            self.m_listCtrl1.GetItemCount(), "roomInfo[0]")
        self.m_listCtrl1.SetItem(index, 1, "roomInfo[1]")
        #self.m_listRoom.SetItem(index, 2, roomInfo[2])

        # Connect Events
        self.m_listCtrl1.Bind(wx.EVT_LIST_ITEM_SELECTED, self.Onroomselect)
        self.m_buttonEnterroom.Bind(wx.EVT_BUTTON, self.OnButtonEnterroom)
        self.m_buttonReturn.Bind(wx.EVT_BUTTON, self.OnButtonReturn)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def Onroomselect(self, event):
        self.currentSelectRoomIndex = event.Index
        self.currentSelectRoom = self.m_listCtrl1.GetItemText(
            self.currentSelectRoomIndex)
        # print(self.currentSelectRoom)
        event.Skip()

    def OnButtonEnterroom(self, event):
        self.func_callback(self.currentSelectRoom)
        event.Skip()

    def OnButtonReturn(self, event):
        createDialog = m_DialogCreateroom()
        createDialog.ShowModal()
        event.Skip()
        event.Skip()


class m_DialogInfo (wx.Dialog):

    def __init__(self):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=u"用户信息",
                           pos=wx.DefaultPosition, size=wx.Size(250, 280), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer6 = wx.FlexGridSizer(4, 1, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer6.Add((0, 20), 1, wx.EXPAND, 5)

        fgSizer9 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer9.Add((20, 0), 1, wx.EXPAND, 5)

        fgSizer8 = wx.FlexGridSizer(4, 2, 5, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticTextUser = wx.StaticText(
            self, wx.ID_ANY, u"昵称", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextUser.Wrap(-1)
        fgSizer8.Add(self.m_staticTextUser, 0, wx.ALL, 5)

        self.m_textCtrlUser = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        fgSizer8.Add(self.m_textCtrlUser, 0, wx.ALL, 5)

        self.m_staticTextAge = wx.StaticText(
            self, wx.ID_ANY, u"生日", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextAge.Wrap(-1)
        fgSizer8.Add(self.m_staticTextAge, 0, wx.ALL, 5)

        self.m_textCtrlAge = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, -1), wx.TE_READONLY)
        self.m_textCtrlAge.SetMaxLength(2)
        fgSizer8.Add(self.m_textCtrlAge, 0, wx.ALL, 5)

        self.m_staticTextSex = wx.StaticText(
            self, wx.ID_ANY, u"性别", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextSex.Wrap(-1)
        fgSizer8.Add(self.m_staticTextSex, 0, wx.ALL, 5)

        self.m_textCtrlSex = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY)
        fgSizer8.Add(self.m_textCtrlSex, 0, wx.ALL, 5)

        self.m_textCtrlSex.SetValue('nan')

        self.m_staticTextMotto = wx.StaticText(
            self, wx.ID_ANY, u"个性签名", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextMotto.Wrap(-1)
        fgSizer8.Add(self.m_staticTextMotto, 0, wx.ALL, 5)

        self.m_textCtrlMotto = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(-1, 60), wx.TE_MULTILINE | wx.TE_READONLY)
        fgSizer8.Add(self.m_textCtrlMotto, 0, wx.ALL, 5)

        fgSizer9.Add(fgSizer8, 1, wx.EXPAND, 5)

        fgSizer6.Add(fgSizer9, 1, wx.EXPAND, 5)

        fgSizer10 = wx.FlexGridSizer(1, 4, 0, 0)
        fgSizer10.SetFlexibleDirection(wx.BOTH)
        fgSizer10.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer10.Add((60, 0), 1, wx.EXPAND, 5)

        self.m_buttonAdd = wx.Button(
            self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.Size(100, 30), 0)
        fgSizer10.Add(self.m_buttonAdd, 0, wx.ALL, 5)

        fgSizer6.Add(fgSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnIconClose)
        self.m_buttonAdd.Bind(wx.EVT_BUTTON, self.OnButtonAdd)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnIconClose(self, event):
        event.Skip()

    def OnButtonAdd(self, event):
        event.Skip()


class m_DialogUpdatePass (wx.Dialog):

    def __init__(self):
        wx.Dialog.__init__(self, parent=None, id=wx.ID_ANY, title=u"修改密码",
                           pos=wx.DefaultPosition, size=wx.Size(230, 230), style=wx.DEFAULT_DIALOG_STYLE)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer6 = wx.FlexGridSizer(4, 1, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer6.Add((0, 20), 1, wx.EXPAND, 5)

        fgSizer9 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer9.Add((10, 0), 1, wx.EXPAND, 5)

        fgSizer8 = wx.FlexGridSizer(6, 2, 5, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticTextOriginPass = wx.StaticText(
            self, wx.ID_ANY, u"原密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextOriginPass.Wrap(-1)
        fgSizer8.Add(self.m_staticTextOriginPass, 0, wx.ALL, 5)

        self.m_textCtrlOriginPass = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        fgSizer8.Add(self.m_textCtrlOriginPass, 0, wx.ALL, 5)

        self.m_staticTextNewPass = wx.StaticText(
            self, wx.ID_ANY, u"新密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextNewPass.Wrap(-1)
        fgSizer8.Add(self.m_staticTextNewPass, 0, wx.ALL, 5)

        self.m_textCtrlnewPass = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        fgSizer8.Add(self.m_textCtrlnewPass, 0, wx.ALL, 5)

        self.m_staticTextSurePass = wx.StaticText(
            self, wx.ID_ANY, u"确认密码", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextSurePass.Wrap(-1)
        fgSizer8.Add(self.m_staticTextSurePass, 0, wx.ALL, 5)

        self.m_textCtrlSureNewPass = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD)
        fgSizer8.Add(self.m_textCtrlSureNewPass, 0, wx.ALL, 5)

        fgSizer9.Add(fgSizer8, 1, wx.EXPAND, 5)

        fgSizer6.Add(fgSizer9, 1, wx.EXPAND, 5)

        fgSizer6.Add((0, 10), 1, wx.EXPAND, 5)

        fgSizer10 = wx.FlexGridSizer(1, 4, 0, 0)
        fgSizer10.SetFlexibleDirection(wx.BOTH)
        fgSizer10.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer10.Add((50, 0), 1, wx.EXPAND, 5)

        self.m_buttonSureUpdatePass = wx.Button(
            self, wx.ID_ANY, u"确认修改", wx.DefaultPosition, wx.Size(100, 30), 0)
        fgSizer10.Add(self.m_buttonSureUpdatePass, 0, wx.ALL, 5)

        fgSizer6.Add(fgSizer10, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer6)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnIconClose)
        self.m_buttonSureUpdatePass.Bind(
            wx.EVT_BUTTON, self.OnButtonSureUpdatePass)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnIconClose(self, event):
        event.Skip()

    def OnButtonSureUpdatePass(self, event):
        event.Skip()


class m_frameRoomChat (wx.Frame):

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, pos=wx.DefaultPosition, size=wx.Size(
            500, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(500, 500), wx.Size(500, 500))

        fgSizer1 = wx.FlexGridSizer(4, 1, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer1.Add((0, 5), 1, wx.EXPAND, 5)

        fgSizer2 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer2.Add((10, 0), 1, wx.EXPAND, 5)

        self.m_textCtrlRoomMessage = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(
            460, 345), wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        fgSizer2.Add(self.m_textCtrlRoomMessage, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer2, 1, wx.EXPAND, 5)

        fgSizer21 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer21.SetFlexibleDirection(wx.BOTH)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer21.Add((10, 0), 1, wx.EXPAND, 5)

        self.m_textCtrlMyMessage = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(460, 60), 0)
        fgSizer21.Add(self.m_textCtrlMyMessage, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer21, 1, wx.EXPAND, 5)

        fgSizer211 = wx.FlexGridSizer(1, 4, 0, 0)
        fgSizer211.SetFlexibleDirection(wx.BOTH)
        fgSizer211.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer211.Add((240, 0), 1, wx.EXPAND, 5)

        self.m_buttonSend = wx.Button(
            self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(100, 20), 0)
        fgSizer211.Add(self.m_buttonSend, 0, wx.ALL, 5)

        fgSizer211.Add((10, 0), 1, wx.EXPAND, 5)

        self.m_buttonClose = wx.Button(
            self, wx.ID_ANY, u"关闭", wx.DefaultPosition, wx.Size(100, 20), 0)
        fgSizer211.Add(self.m_buttonClose, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer211, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_textCtrlMyMessage.Bind(wx.EVT_TEXT_ENTER, self.OntextEnter)
        self.m_buttonSend.Bind(wx.EVT_BUTTON, self.OnButtonSend)
        self.m_buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonClose)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OntextEnter(self, event):
        event.Skip()

    def OnButtonSend(self, event):
        event.Skip()

    def OnButtonClose(self, event):
        event.Skip()


class m_framePrivateChat (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"房间：", pos=wx.DefaultPosition, size=wx.Size(
            620, 500), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(-1, -1), wx.Size(-1, -1))

        fgSizer1 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer5 = wx.FlexGridSizer(4, 1, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer5.Add((0, 5), 1, wx.EXPAND, 5)

        fgSizer2 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer2.Add((10, 0), 1, wx.EXPAND, 5)

        self.m_textCtrlRoomMessage = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(
            460, 345), wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_RICH2)
        fgSizer2.Add(self.m_textCtrlRoomMessage, 0, wx.ALL, 5)

        fgSizer5.Add(fgSizer2, 1, wx.EXPAND, 5)

        fgSizer21 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer21.SetFlexibleDirection(wx.BOTH)
        fgSizer21.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer21.Add((10, 0), 1, wx.EXPAND, 5)

        self.m_textCtrlMyMessage = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(460, 60), 0)
        fgSizer21.Add(self.m_textCtrlMyMessage, 0, wx.ALL, 5)

        fgSizer5.Add(fgSizer21, 1, wx.EXPAND, 5)

        fgSizer211 = wx.FlexGridSizer(1, 4, 0, 0)
        fgSizer211.SetFlexibleDirection(wx.BOTH)
        fgSizer211.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer211.Add((240, 0), 1, wx.EXPAND, 5)

        self.m_buttonSend = wx.Button(
            self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(100, 20), 0)
        fgSizer211.Add(self.m_buttonSend, 0, wx.ALL, 5)

        fgSizer211.Add((10, 0), 1, wx.EXPAND, 5)

        self.m_buttonClose = wx.Button(
            self, wx.ID_ANY, u"离开房间", wx.DefaultPosition, wx.Size(100, 20), 0)
        fgSizer211.Add(self.m_buttonClose, 0, wx.ALL, 5)

        fgSizer5.Add(fgSizer211, 1, wx.EXPAND, 5)

        fgSizer1.Add(fgSizer5, 1, wx.EXPAND, 5)

        self.fgSizer7 = wx.FlexGridSizer(6, 1, 0, 0)
        self.fgSizer7.SetFlexibleDirection(wx.BOTH)
        self.fgSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.fgSizer7.Add((0, 10), 1, wx.EXPAND, 5)

        self.m_staticTextOwnername = wx.StaticText(
            self, wx.ID_ANY, u"房主：", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticTextOwnername.Wrap(-1)
        self.fgSizer7.Add(self.m_staticTextOwnername, 0, wx.ALL, 5)

        self.fgSizer7.Add((0, 10), 1, wx.EXPAND, 5)

        fgSizer8 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_buttonSetHost = wx.Button(
            self, wx.ID_ANY, u"设为房主", wx.DefaultPosition, wx.Size(100, 30), 0)
        fgSizer8.Add(self.m_buttonSetHost, 0, wx.ALL, 5)

        self.m_buttonKick = wx.Button(
            self, wx.ID_ANY, u"踢出房间", wx.DefaultPosition, wx.Size(100, 30), 0)
        fgSizer8.Add(self.m_buttonKick, 0, wx.ALL, 5)

        self.fgSizer7.Add(fgSizer8, 1, wx.EXPAND, 5)

        self.fgSizer7.Add((0, 10), 1, wx.EXPAND, 5)

        self.m_listRoomPeople = wx.ListCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(100, 300), wx.LC_REPORT | wx.NO_BORDER)
        self.fgSizer7.Add(self.m_listRoomPeople, 0, wx.ALL, 5)

        fgSizer1.Add(self.fgSizer7, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        self.m_listRoomPeople.InsertColumn(0, "群聊成员")
        self.m_listRoomPeople.SetColumnWidth(0, 100)

        # Connect Events
        self.m_textCtrlMyMessage.Bind(wx.EVT_TEXT_ENTER, self.OntextEnter)
        self.m_buttonSend.Bind(wx.EVT_BUTTON, self.OnButtonSend)
        self.m_buttonClose.Bind(wx.EVT_BUTTON, self.OnButtonClose)
        self.m_listRoomPeople.Bind(
            wx.EVT_LIST_ITEM_RIGHT_CLICK, self.OnRoomuserRightClick)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OntextEnter(self, event):
        event.Skip()

    def OnButtonSend(self, event):
        event.Skip()

    def OnButtonClose(self, event):
        event.Skip()

    def OnRoomuserRightClick(self, event):
                        # only do this part the first time so the events are only bound
                # once
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()
            self.popupID3 = wx.NewId()

            self.Bind(wx.EVT_MENU, self.OnPopupOne, id=self.popupID1)
            self.Bind(wx.EVT_MENU, self.OnPopupTwo, id=self.popupID2)
            self.Bind(wx.EVT_MENU, self.OnPopupThree, id=self.popupID3)

        # make a menu
        menu = wx.Menu()
        # add some items
        menu.Append(self.popupID1, "与他聊天")
        menu.Append(self.popupID2, "设为房主")
        menu.Append(self.popupID3, "踢出房间")
        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()

    def OnPopupOne(self, event):

        print("与他聊天" + self.currentSelectUser)

    def OnPopupTwo(self, event):
        print("设为房主")

    def OnPopupThree(self, event):
        print("踢出房间")


class RoomContol(m_frameRoomChat):
    """docstring for RoomContol"""

    def __init__(self, parent, id, title):
        super(RoomContol, self).__init__(parent, id, title)
        # self.parent = parent
        # self.title = title

if __name__ == '__main__':
    app = wx.App(None)
    frame = m_frameHall(None)
    frame.Show()
    app.MainLoop()
