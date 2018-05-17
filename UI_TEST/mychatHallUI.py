#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-02 12:30:53
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
#from mychatLoginUI import LoginWindow

musicdata = {
    1: ("Bad English", "The Price Of Love", "Rock"),
    2: ("DNA featuring Suzanne Vega", "Tom's Diner", "Rock"),
    3: ("George Michael", "Praying For Time", "Ro12adsddasdadsack"),
}

###########################################################################
# Class m_frameRoomlist
###########################################################################


class m_frameRoomlist (wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"房间列表", pos=wx.DefaultPosition, size=wx.Size(
            550, 350), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        fgSizer1 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_listRoom = wx.ListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(
            410, 300), wx.LC_REPORT | wx.NO_BORDER)
        fgSizer1.Add(self.m_listRoom, 0, wx.ALL, 5)

        fgSizer2 = wx.FlexGridSizer(7, 1, 20, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_buttonEnter = wx.Button(
            self, wx.ID_ANY, u"进入房间", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.m_buttonEnter, 0, wx.ALL, 5)

        self.m_buttonRefresh = wx.Button(
            self, wx.ID_ANY, u"刷新列表", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.m_buttonRefresh, 0, wx.ALL, 5)

        self.m_buttonCreate = wx.Button(
            self, wx.ID_ANY, u"创建房间", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.m_buttonCreate, 0, wx.ALL, 5)

        fgSizer2.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_buttonExit = wx.Button(
            self, wx.ID_ANY, u"退出登陆", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer2.Add(self.m_buttonExit, 0, wx.ALL, 5)

        fgSizer1.Add(fgSizer2, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.m_listRoom.Bind(wx.EVT_LIST_ITEM_RIGHT_CLICK,
                             self.OnRoomRightClick)
        self.m_listRoom.Bind(wx.EVT_LIST_ITEM_SELECTED, self.OnRoomSelected)
        self.m_buttonEnter.Bind(wx.EVT_BUTTON, self.OnEnterRoom)
        self.m_buttonRefresh.Bind(wx.EVT_BUTTON, self.OnRefreshList)
        self.m_buttonCreate.Bind(wx.EVT_BUTTON, self.OnCreateRoom)
        self.m_buttonExit.Bind(wx.EVT_BUTTON, self.OnExit)

        self.m_listRoom.InsertColumn(0, "房间名")
        self.m_listRoom.InsertColumn(1, "房主")
        self.m_listRoom.InsertColumn(2, "房间简介")

        self.m_listRoom.SetColumnWidth(0, 80)
        self.m_listRoom.SetColumnWidth(1, 80)
        self.m_listRoom.SetColumnWidth(2, 180)

        items = musicdata.items()
        for key, data in items:
            index = self.m_listRoom.InsertItem(
                self.m_listRoom.GetItemCount(), data[0])
        #     self.log.WriteText(str(self.list.GetItemCount()))
        # self.log.WriteText(str(type(musicdata)))
            self.m_listRoom.SetItem(index, 1, data[1])
            self.m_listRoom.SetItem(index, 2, data[2])
            # self.m_listRoom.SetItemData(index, key)

        self.Show()

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnRoomRightClick(self, event):
                # only do this part the first time so the events are only bound once
        if not hasattr(self, "popupID1"):
            self.popupID1 = wx.NewId()
            self.popupID2 = wx.NewId()


            self.Bind(wx.EVT_MENU, self.OnPopupOne, id=self.popupID1)
            self.Bind(wx.EVT_MENU, self.OnPopupTwo, id=self.popupID2)

        # make a menu
        menu = wx.Menu()
        # add some items
        menu.Append(self.popupID1, "添加好友")
        menu.Append(self.popupID2, "查看资料")
        # Popup the menu.  If an item is selected then its handler
        # will be called before PopupMenu returns.
        self.PopupMenu(menu)
        menu.Destroy()

    def OnPopupOne(self, event):
        print("添加好友")

    def OnPopupTwo(self, event):
        print("查看资料")

    def OnRoomSelected(self, event):
        print('触发选择事件')
        event.Skip()

    def OnEnterRoom(self, event):
        event.Skip()

    def OnRefreshList(self, event):
        event.Skip()

    def OnCreateRoom(self, event):
        event.Skip()

    def OnExit(self, event):
        event.Skip()


# unit TEST
if __name__ == '__main__':
    app = wx.App(None)
    frame = m_frameRoomlist(None)
    frame.Show()
    app.MainLoop()
