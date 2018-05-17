#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-03-05 16:21:57
# @Author  : JohnAlex (843765942@qq.com)
# @Link    : http://taolvezh.cn/
# @Version : $Id$

import wx

#---------------------------------------------------------------------------
# Create and set a help provider.  Normally you would do this in
# the app's OnInit as it must be done before any SetHelpText calls.
provider = wx.SimpleHelpProvider()
wx.HelpProvider.Set(provider)

#---------------------------------------------------------------------------


class TestDialog(wx.Dialog):

    def __init__(
            self, parent, id, title, size=wx.DefaultSize, pos=wx.DefaultPosition,
            style=wx.DEFAULT_DIALOG_STYLE, name='dialog'
    ):

        # Instead of calling wx.Dialog.__init__ we precreate the dialog
        # so we can set an extra style that must be set before
        # creation, and then we create the GUI object using the Create
        # method.
        wx.Dialog.__init__(self)
        self.SetExtraStyle(wx.DIALOG_EX_CONTEXTHELP)
        self.Create(parent, id, title, pos, size, style, name)

        # Now continue with the normal construction of the dialog
        # contents
        sizer = wx.BoxSizer(wx.VERTICAL)

        # label = wx.StaticText(self, -1, "This is a wx.Dialog")
        # label.SetHelpText("This is the help text for the label")
        # sizer.Add(label, 0, wx.ALIGN_CENTRE | wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "房间名称:")
        #label.SetHelpText("This is the help text for the label")
        box.Add(label, 0, wx.ALIGN_CENTRE | wx.ALL, 5)

        text = wx.TextCtrl(self, -1, "", size=(80, -1))
        # text.SetHelpText("Here's some help text for field #1")
        box.Add(text, 1, wx.ALIGN_CENTRE | wx.ALL, 5)

        sizer.Add(box, 0, wx.GROW | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        box = wx.BoxSizer(wx.HORIZONTAL)

        label = wx.StaticText(self, -1, "房间简介:")
        #label.SetHelpText("This is the help text for the label")
        box.Add(label, 0, wx.ALIGN_CENTRE | wx.ALL, 5)

        text = wx.TextCtrl(self, -1, "", size=(80, -1))
        # text.SetHelpText("Here's some help text for field #2")
        box.Add(text, 1, wx.ALIGN_CENTRE | wx.ALL, 5)

        sizer.Add(box, 0, wx.GROW | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        line = wx.StaticLine(self, -1, size=(20, -1), style=wx.LI_HORIZONTAL)
        sizer.Add(line, 0, wx.GROW | wx.ALIGN_CENTER_VERTICAL |
                  wx.RIGHT | wx.TOP, 5)

        btnsizer = wx.StdDialogButtonSizer()

        if wx.Platform != "__WXMSW__":
            btn = wx.ContextHelpButton(self)
            btnsizer.AddButton(btn)

        self.m_btnOK = wx.Button(self, wx.ID_OK, '确定')
        #btn.SetHelpText("The OK button completes the dialog")
        # btn.SetDefault()
        btnsizer.AddButton(self.m_btnOK)

        btn = wx.Button(self, wx.ID_CANCEL, '取消')
        #btn.SetHelpText("The Cancel button cancels the dialog. (Cool, huh?)")
        btnsizer.AddButton(btn)
        btnsizer.Realize()

        sizer.Add(btnsizer, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.SetSizer(sizer)
        sizer.Fit(self)

        self.m_btnOK.Bind(wx.EVT_BUTTON, self.on_OKbutton_click)

    def on_OKbutton_click(self, event):
        print('OK')
        pass


app = wx.App(None)
dlg = TestDialog(None, -1, "创建房间", size=(350, 200),
                 style=wx.DEFAULT_DIALOG_STYLE,
                 )
dlg.CenterOnScreen()
dlg.Show()
app.MainLoop()


# # this does not return until the dialog is closed.
# val = dlg.ShowModal()
