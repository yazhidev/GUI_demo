#!/usr/bin/python
# -*- coding: utf-8 -*-

# newclass.py

import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
                                      size=(600, 700))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        # 测试信息部分内容
        sizer = wx.GridBagSizer(12, 4)
        sb = wx.StaticBox(panel, label=" 测试信息 ")
        boxsizer_ver = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer_hor1 = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
        # boxsizer_hor2 = wx.StaticBoxSizer(sb, wx.HORIZONTAL)
        # boxsizer_hor3 = wx.StaticBoxSizer(sb, wx.HORIZONTAL)

        tx1 = wx.StaticText(panel, label=" 测试APP： ")
        boxsizer_hor1.Add(tx1, flag=wx.TOP, border=10)
        nm1 = wx.TextCtrl(panel)
        boxsizer_hor1.Add(nm1, 0, wx.ALL | wx.LEFT, 5)

        tx2 = wx.StaticText(panel, label=" APP版本： ")
        boxsizer_hor1.Add(tx2, flag=wx.TOP, border=10)
        nm2 = wx.TextCtrl(panel)
        boxsizer_hor1.Add(nm2, 0, wx.ALL | wx.LEFT, 5)

        tx3 = wx.StaticText(panel, label=" 测试账号及密码: ")
        boxsizer_hor1.Add(tx3, flag=wx.TOP, border=10)
        nm3 = wx.TextCtrl(panel)
        boxsizer_hor1.Add(nm3, 3, wx.ALL | wx.LEFT, 5)

        # tx4 = wx.StaticText(panel, label=" 测试手机： ")
        # boxsizer_hor2.Add(tx4, flag=wx.TOP, border=10)
        # nm4 = wx.TextCtrl(panel)
        # boxsizer_hor2.Add(nm4, 0, wx.ALL | wx.LEFT, 5)
        #
        # tx5 = wx.StaticText(panel, label=" 设备名称： ")
        # boxsizer_hor2.Add(tx5, flag=wx.TOP, border=10)
        # nm5 = wx.TextCtrl(panel)
        # boxsizer_hor2.Add(nm5, 0, wx.ALL | wx.LEFT, 5)
        #
        # tx6 = wx.StaticText(panel, label=" 设备ID： ")
        # boxsizer_hor2.Add(tx6, flag=wx.TOP, border=10)
        # nm6 = wx.TextCtrl(panel)
        # boxsizer_hor2.Add(nm6, 0, wx.ALL | wx.LEFT, 5)
        #
        # tx7 = wx.StaticText(panel, label=" PID： ")
        # boxsizer_hor3.Add(tx7, flag=wx.TOP, border=10)
        # nm7 = wx.TextCtrl(panel)
        # boxsizer_hor3.Add(nm7, 0, wx.ALL | wx.LEFT, 5)
        #
        # tx8 = wx.StaticText(panel, label=" UIID： ")
        # boxsizer_hor3.Add(tx8, flag=wx.TOP, border=10)
        # nm8 = wx.TextCtrl(panel)
        # boxsizer_hor3.Add(nm8, 0, wx.ALL | wx.LEFT, 5)

        # tx9 = wx.StaticText(panel, label=" 固件key： ")
        # boxsizer_hor3.Add(tx9, flag=wx.TOP, border=10)
        # nm9 = wx.TextCtrl(panel)
        # boxsizer_hor3.Add(nm9, 0, wx.ALL | wx.LEFT, 5)
        #
        # tx10 = wx.StaticText(panel, label=" 固件版本： ")
        # boxsizer_hor3.Add(tx10, flag=wx.TOP, border=10)
        # nm10 = wx.TextCtrl(panel)
        # boxsizer_hor3.Add(nm10, 0, wx.ALL | wx.LEFT, 5)

        boxsizer_ver.Add(boxsizer_hor1, 0, wx.ALL | wx.CENTER, 5)
        # boxsizer_ver.Add(boxsizer_hor2, 0, wx.ALL | wx.CENTER, 5)
        # boxsizer_ver.Add(boxsizer_hor3, 0, wx.ALL | wx.CENTER, 5)

        sizer.Add(boxsizer_ver, pos=(0, 0), span=(1, 5),
                  flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=5)

        # 缺陷描述部分内容
        # text1 = wx.StaticText(panel, label=" 缺陷描述 ")
        # font = wx.Font(20, wx.DECORATIVE, wx.ITALIC, wx.NORMAL)
        # text1.SetFont(font)
        # sizer.Add(text1, pos=(1, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM,
        #           border=10)
        #
        # line = wx.StaticLine(panel)
        # sizer.Add(line, pos=(2, 0), span=(1, 5),
        #           flag=wx.EXPAND | wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label=" 简要描述： ")
        sizer.Add(text2, pos=(3, 0), flag=wx.LEFT, border=10)
        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(3, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND)

        text3 = wx.StaticText(panel, label=" 前提条件： ")
        sizer.Add(text3, pos=(4, 0), flag=wx.LEFT | wx.TOP, border=10)
        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(4, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)

        text4 = wx.StaticText(panel, label=" 操作步骤： ")
        sizer.Add(text4, pos=(5, 0), flag=wx.TOP | wx.LEFT, border=10)
        tc3 = wx.TextCtrl(panel)
        sizer.Add(tc3, pos=(5, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)
        tc4 = wx.TextCtrl(panel)
        sizer.Add(tc4, pos=(6, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)
        tc5 = wx.TextCtrl(panel)
        sizer.Add(tc5, pos=(7, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)
        tc6 = wx.TextCtrl(panel)
        sizer.Add(tc6, pos=(8, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)

        text5 = wx.StaticText(panel, label=" 测试结果： ")
        sizer.Add(text5, pos=(9, 0), flag=wx.TOP | wx.LEFT, border=10)
        tc7 = wx.TextCtrl(panel)
        sizer.Add(tc7, pos=(9, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)

        text6 = wx.StaticText(panel, label=" 期望结果： ")
        sizer.Add(text6, pos=(10, 0), flag=wx.TOP | wx.LEFT, border=10)
        tc8 = wx.TextCtrl(panel)
        sizer.Add(tc8, pos=(10, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)

        text7 = wx.StaticText(panel, label=" 备注： ")
        sizer.Add(text7, pos=(11, 0), flag=wx.TOP | wx.LEFT, border=10)
        tc9 = wx.TextCtrl(panel)
        sizer.Add(tc9, pos=(11, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)


if __name__ == '__main__':
    app = wx.App()
    Example(None, title=" 缺陷提交小助手 ")
    app.MainLoop()
