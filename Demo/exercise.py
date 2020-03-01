import wx


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title)
        # 创建白板

        panel = wx.Panel(self)
        # 创建垂直与水平box盒子
        vbox = wx.BoxSizer(wx.VERTICAL)
        nmbox1 = wx.BoxSizer(wx.HORIZONTAL)
        nmbox2 = wx.BoxSizer(wx.HORIZONTAL)

        # 创建一个wx.StaticBox对象。
        # 声明一个wx.StaticBoxSizer与创建的wx.StaticBox对象作为其参数。
        nm = wx.StaticBox(panel, -1, 'Name:')
        nmSizer = wx.StaticBoxSizer(nm, wx.VERTICAL)

        # 构建静态文本框与输入框
        tx1 = wx.StaticText(panel, -1, " 测试APP： ")
        nm1 = wx.TextCtrl(panel, -1, style=wx.ALIGN_LEFT)
        tx2 = wx.StaticText(panel, -1, " 版本： ")
        nm2 = wx.TextCtrl(panel, -1, style=wx.ALIGN_LEFT)
        tx3 = wx.StaticText(panel, 0, " 测试账号及密码： ")
        nm3 = wx.TextCtrl(panel, 0, style=wx.ALIGN_LEFT)
        tx4 = wx.StaticText(panel, -1, " 测试手机： ")
        nm4 = wx.TextCtrl(panel, -1, style=wx.ALIGN_LEFT)
        # 在水平盒子里添加进上面四个
        nmbox1.Add(tx1, 0, wx.ALL | wx.CENTER, 5)
        nmbox1.Add(nm1, 0, wx.ALL | wx.CENTER, 5)
        nmbox1.Add(tx2, 0, wx.ALL | wx.CENTER, 5)
        nmbox1.Add(nm2, 0, wx.ALL | wx.CENTER, 5)
        nmbox2.Add(tx3, 0, wx.ALL | wx.CENTER, 5)
        nmbox2.Add(nm3, 0, wx.ALL | wx.CENTER, 5)
        nmbox2.Add(tx4, 0, wx.ALL | wx.CENTER, 5)
        nmbox2.Add(nm4, 0, wx.ALL | wx.CENTER, 5)
        # 在StaticBoxSizer添加进水平盒子
        nmSizer.Add(nmbox1, 0, wx.ALL | wx.CENTER, 10)
        nmSizer.Add(nmbox2, 0, wx.ALL | wx.CENTER, 10)

        # 在垂直盒子里添加StaticBoxSizer盒子
        vbox.Add(nmSizer, 0, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(vbox)
        self.Centre()
        panel.Fit()
        self.Show()
        # 关系：
        # 垂直box盒子添加StaticBoxSizer盒子
        # StaticBoxSizer盒子添加水平盒子


app = wx.App()
Mywin(None, 'StaticBoxSizer')
app.MainLoop()
