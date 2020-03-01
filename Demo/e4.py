import wx


class Mywin(wx.Frame):
    def __init__(self, parent, title):
        super(Mywin, self).__init__(parent, title=title)
        # 创建白板

        panel = wx.Panel(self)
        boxsizer = wx.BoxSizer(wx.VERTICAL)
        panel.SetSizer(boxsizer)
        button1 = wx.Button(panel, wx.ID_ANY, 'aaaaa')
        button2 = wx.Button(panel, wx.ID_ANY, 'bbbbb')
        boxsizer.Add(button1)
        boxsizer.Add(button2)
        panel2 = wx.Panel(self)
        panel2.SetBackgroundColour('#00ff00')
        boxsizer.Add(panel2)

        boxsizer2 = wx.BoxSizer(wx.VERTICAL)
        panel2.SetSizer(boxsizer2)
        button3 = wx.Button(panel2, wx.ID_ANY, 'ccccc')
        button4 = wx.Button(panel2, wx.ID_ANY, 'ddddd')
        boxsizer2.Add(button3)
        boxsizer2.Add(button4)
        self.Centre()
        panel.Fit()
        self.Show()


app = wx.App()
Mywin(None, 'StaticBoxSizer')
app.MainLoop()

