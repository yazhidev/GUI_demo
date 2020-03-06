import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(480, 450))
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        container = wx.BoxSizer(wx.VERTICAL)
        container.Add(self.buildTestInfo(panel), flag=wx.ALL, border=20)
        container.Add(self.buildSteps(panel), flag=wx.LEFT | wx.RIGHT, border=20)
        # 复制内容按钮
        finishBtn = wx.Button(panel, label='完成并复制内容')
        container.Add(finishBtn, flag=wx.ALIGN_RIGHT | wx.RIGHT | wx.TOP, border=20)
        # 内容显示框
        resultLabel = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(440, 100))
        container.Add(resultLabel, flag=wx.ALL, border=20)
        panel.SetSizerAndFit(container)

    # 测试信息
    def buildTestInfo(self, panel):
        testInfo = wx.StaticBox(panel, label="测试信息")
        testInfoSizer = wx.StaticBoxSizer(testInfo, wx.VERTICAL)

        gridBagSizer = wx.GridBagSizer(12, 0)

        line1 = wx.BoxSizer(wx.HORIZONTAL)
        testAppName = wx.StaticText(panel, label="测试APP ")
        testAppInput = wx.TextCtrl(panel)
        versionName = wx.StaticText(panel, label="版本 ")
        versionInput = wx.TextCtrl(panel)
        line1.Add(testAppName, flag=wx.RIGHT, border=10)
        line1.Add(testAppInput, flag=wx.RIGHT, border=30)
        line1.Add(versionName)
        line1.Add(versionInput)
        gridBagSizer.Add(line1, pos=(0, 0), span=(1, 3))

        line2 = wx.BoxSizer(wx.HORIZONTAL)
        accountAndPwd = wx.StaticText(panel, label="测试账号及密码 ")
        area = wx.ComboBox(panel, value='中国', choices=['中国', '美国', "火星"])
        gridBagSizer.Add(area, pos=(1, 3), span=(1, 1))
        # 添加事件处理
        self.Bind(wx.EVT_COMBOBOX, self.on_combobox, area)
        accountAndPwdInpu = wx.TextCtrl(panel, size=(200, 20))
        line2.Add(accountAndPwd, flag=wx.Top, border=3)
        line2.Add(area, flag=wx.LEFT, border=10)
        line2.Add(accountAndPwdInpu, flag=wx.LEFT, border=20)
        gridBagSizer.Add(line2, pos=(1, 0), span=(1, 3))

        testInfoSizer.Add(gridBagSizer, flag=wx.ALL, border=5)
        return testInfoSizer

    # 操作步骤
    def buildSteps(self, panel):
        testInfo = wx.StaticBox(panel, label="操作步骤")
        testInfoSizer = wx.StaticBoxSizer(testInfo, wx.VERTICAL)

        gridBagSizer = wx.GridBagSizer(12, 0)

        line1 = wx.BoxSizer(wx.HORIZONTAL)
        testAppName = wx.StaticText(panel, label="测试APP ")
        testAppInput = wx.TextCtrl(panel)
        versionName = wx.StaticText(panel, label="版本 ")
        versionInput = wx.TextCtrl(panel)
        line1.Add(testAppName, flag=wx.RIGHT, border=10)
        line1.Add(testAppInput, flag=wx.RIGHT, border=30)
        line1.Add(versionName)
        line1.Add(versionInput)
        gridBagSizer.Add(line1, pos=(0, 0), span=(1, 3))

        line2 = wx.BoxSizer(wx.HORIZONTAL)
        accountAndPwd = wx.StaticText(panel, label="测试账号及密码 ")
        area = wx.ComboBox(panel, value='中国', choices=['中国', '美国', "火星"])
        gridBagSizer.Add(area, pos=(1, 3), span=(1, 1))
        # 添加事件处理
        self.Bind(wx.EVT_COMBOBOX, self.on_combobox, area)
        accountAndPwdInpu = wx.TextCtrl(panel, size=(200, 20))
        line2.Add(accountAndPwd, flag=wx.Top, border=3)
        line2.Add(area, flag=wx.LEFT, border=10)
        line2.Add(accountAndPwdInpu, flag=wx.LEFT, border=20)
        gridBagSizer.Add(line2, pos=(1, 0), span=(1, 3))

        testInfoSizer.Add(gridBagSizer, flag=wx.ALL, border=5)
        return testInfoSizer

    def on_combobox(self, event):
        print("选择{0}".format(event.GetString()))


app = wx.App()
Example(None, 'Demo')
app.MainLoop()
