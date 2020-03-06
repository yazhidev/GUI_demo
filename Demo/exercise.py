import wx


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(0, 0)
        panel2 = wx.Panel(self)

        # pos=(0, 0)：放在1行1列，不设置span，默认span=(1,1)占一行一列的大小
        text = wx.StaticText(panel, label="Name:")
        sizer.Add(text, pos=(0, 0), flag=wx.ALL, border=5)

        sb = wx.StaticBox(panel, label="Optional Attributes")
        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)

        panel.SetSizerAndFit(sizer)


app = wx.App()
Example(None, 'Demo')
app.MainLoop()
