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
# Class m_frameChatRoom
###########################################################################


class m_frameChatRoom (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition, size=wx.Size(
            640, 480), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer3 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textChatcontext = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(
            480, 380), wx.TE_MULTILINE | wx.TE_READONLY | wx.VSCROLL)
        fgSizer3.Add(self.m_textChatcontext, 0, wx.ALL |
                     wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer4 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textChatsNotice = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(
            120, 185), wx.TE_MULTILINE | wx.TE_NO_VSCROLL | wx.TE_READONLY)
        fgSizer4.Add(self.m_textChatsNotice, 0, wx.ALL, 5)

        self.m_listPeopleOnline = wx.ListCtrl(
            self, wx.ID_ANY, wx.DefaultPosition, wx.Size(120, 185), wx.LC_REPORT)
        fgSizer4.Add(self.m_listPeopleOnline, 0, wx.ALL, 5)

        self.m_listPeopleOnline.InsertColumn(0, "在线用户")

        self.m_listPeopleOnline.SetColumnWidth(0, 120)

        fgSizer3.Add(fgSizer4, 1, wx.EXPAND, 5)

        fgSizer1.Add(fgSizer3, 1, wx.EXPAND, 5)

        fgSizer2 = wx.FlexGridSizer(1, 5, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.HORIZONTAL)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_textInput = wx.TextCtrl(
            self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(440, 40), 0)
        fgSizer2.Add(self.m_textInput, 0, wx.ALL |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_buttonSend = wx.Button(
            self, wx.ID_ANY, u"发送", wx.DefaultPosition, wx.Size(60, 40), wx.BU_EXACTFIT)
        fgSizer2.Add(self.m_buttonSend, 0, wx.ALL |
                     wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_buttonRefresh = wx.Button(
            self, wx.ID_ANY, u"刷新", wx.DefaultPosition, wx.Size(60, 40), 0)
        fgSizer2.Add(self.m_buttonRefresh, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer2, 1, wx.EXPAND |
                     wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnLeaveRoom)
        self.m_textInput.Bind(wx.EVT_TEXT_ENTER, self.OnMessageEnter)
        self.m_buttonSend.Bind(wx.EVT_BUTTON, self.OnMessageSend)
        self.m_buttonRefresh.Bind(wx.EVT_BUTTON, self.OnStatusRefresh)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnLeaveRoom(self, event):
        event.Skip()

    def OnMessageEnter(self, event):
        event.Skip()

    def OnMessageSend(self, event):
        event.Skip()

    def OnStatusRefresh(self, event):
        event.Skip()


# unit TEST
if __name__ == '__main__':
    app = wx.App(None)
    frame = m_frameChatRoom(None)
    frame.Show()
    app.MainLoop()
