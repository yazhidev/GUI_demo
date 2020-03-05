import wx

import wx


# ########################################################################
# class MyPanel(wx.Panel):
#     """"""
#
#     # ----------------------------------------------------------------------
#     def __init__(self, parent):
#         """Constructor"""
#         wx.Panel.__init__(self, parent)
#         self.number_of_buttons = 0
#         self.frame = parent
#
#         self.mainSizer = wx.BoxSizer(wx.VERTICAL)
#         controlSizer = wx.BoxSizer(wx.HORIZONTAL)
#         self.widgetSizer = wx.BoxSizer(wx.VERTICAL)
#
#         self.addButton = wx.Button(self, label="Add")
#         self.addButton.Bind(wx.EVT_BUTTON, self.onAddWidget)
#         controlSizer.Add(self.addButton, 0, wx.CENTER | wx.ALL, 5)
#
#         self.removeButton = wx.Button(self, label="Remove")
#         self.removeButton.Bind(wx.EVT_BUTTON, self.onRemoveWidget)
#         controlSizer.Add(self.removeButton, 0, wx.CENTER | wx.ALL, 5)
#
#         self.mainSizer.Add(controlSizer, 0, wx.CENTER)
#         self.mainSizer.Add(self.widgetSizer, 0, wx.CENTER | wx.ALL, 10)
#
#         self.SetSizer(self.mainSizer)
#
#     # ----------------------------------------------------------------------
#     def onAddWidget(self, event):
#         """"""
#         self.number_of_buttons += 1
#         label = "Button %s" % self.number_of_buttons
#         name = "button%s" % self.number_of_buttons
#         new_button = wx.Button(self, label=label, name=name)
#         self.widgetSizer.Add(new_button, 0, wx.ALL, 5)
#         self.frame.fSizer.Layout()
#         self.frame.Fit()
#
#     # ----------------------------------------------------------------------
#     def onRemoveWidget(self, event):
#         """"""
#         if self.widgetSizer.GetChildren():
#             self.widgetSizer.Hide(self.number_of_buttons - 1)
#             self.widgetSizer.Remove(self.number_of_buttons - 1)
#             self.number_of_buttons -= 1
#             self.frame.fSizer.Layout()
#             self.frame.Fit()
#
#
# ########################################################################
# class MyFrame(wx.Frame):
#     """"""
#
#     # ----------------------------------------------------------------------
#     def __init__(self):
#         """Constructor"""
#         wx.Frame.__init__(self, parent=None, title="Add / Remove Buttons")
#         self.fSizer = wx.BoxSizer(wx.VERTICAL)
#         panel = MyPanel(self)
#         self.fSizer.Add(panel, 1, wx.EXPAND)
#         self.SetSizer(self.fSizer)
#         self.Fit()
#         self.Show()
#
#
# # ----------------------------------------------------------------------
# if __name__ == "__main__":
#     app = wx.App(False)
#     frame = MyFrame()
#     app.MainLoop()

#
class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title,
                                      size=(450, 400))

        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)

        sizer = wx.GridBagSizer(5, 5)

        text1 = wx.StaticText(panel, label="Java Class ")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM,
                  border=15)

        image = wx.Image('icon.png')
        image.Rescale(30, 30)
        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap(image))
        sizer.Add(icon, pos=(0, 4), flag=wx.TOP | wx.RIGHT | wx.ALIGN_RIGHT,
                  border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5),
                  flag=wx.EXPAND | wx.BOTTOM, border=30)

        text2 = wx.StaticText(panel, label=" Name ")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)

        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND)

        text3 = wx.StaticText(panel, label="Package")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT | wx.TOP, border=10)

        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)

        button1 = wx.Button(panel, label="Browse...")
        sizer.Add(button1, pos=(3, 4), flag=wx.TOP | wx.RIGHT, border=5)

        text4 = wx.StaticText(panel, label="Extends")
        sizer.Add(text4, pos=(4, 0), flag=wx.TOP | wx.LEFT, border=10)

        list1 = ['Python', 'Java', "C++"]
        combo = wx.ComboBox(panel, -1, value='Java', choices=list1)
        # 添加事件处理
        self.Bind(wx.EVT_COMBOBOX, self.on_combobox, combo)

        # combo = wx.ComboBox(panel)
        sizer.Add(combo, pos=(4, 1), span=(1, 3),
                  flag=wx.TOP | wx.EXPAND, border=5)

        button2 = wx.Button(panel, label="Browse...")
        sizer.Add(button2, pos=(4, 4), flag=wx.TOP | wx.RIGHT, border=5)

        sb = wx.StaticBox(panel, label="Optional Attributes")

        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer.Add(wx.CheckBox(panel, label="Public"),
                     flag=wx.LEFT | wx.TOP, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Generate Default Constructor"),
                     flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Generate Main Method"),
                     flag=wx.LEFT | wx.BOTTOM, border=5)
        sizer.Add(boxsizer, pos=(5, 0), span=(1, 5),
                  flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=10)

        button3 = wx.Button(panel, label='Help')
        sizer.Add(button3, pos=(7, 0), flag=wx.LEFT, border=10)

        button4 = wx.Button(panel, label="Ok")
        sizer.Add(button4, pos=(7, 3))

        button5 = wx.Button(panel, label="Cancel")
        sizer.Add(button5, pos=(7, 4), span=(1, 1),
                  flag=wx.BOTTOM | wx.RIGHT, border=5)

        sizer.AddGrowableCol(2)

        panel.SetSizer(sizer)

    def on_combobox(self, event):
        # wx.ProgressDialog("title", "message", maximum=5).ShowModal()
        print("选择{0}".format(event.GetString()))

if __name__ == '__main__':
    app = wx.App()
    Example(None, title="Creates")
    app.MainLoop()

# class MyForm(wx.Frame):
#
#     def __init__(self):
#         # wx.Frame.__init__(self, None, wx.ID_ANY, title='My Form', style=wx.DEFAULT_FRAME_STYLE ^(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
#         wx.Frame.__init__(self, None, wx.ID_ANY, title='My Form')
#
#         # Add a panel so it looks correct on all platforms
#         self.panel = wx.Panel(self, wx.ID_ANY)
#         hbox = wx.BoxSizer(wx.HORIZONTAL)
#
#         fgs = wx.FlexGridSizer(3, 2, 0, 0)
#         self.flexItem("设备名称", fgs)
#         self.flexItem("设备ID", fgs)
#         # title = wx.StaticText(self.panel, label="Title")
#         # author = wx.StaticText(self.panel, label="Author")
#         # review = wx.StaticText(self.panel, label="Review")
#         #
#         # tc1 = wx.TextCtrl(self.panel)
#         # tc2 = wx.TextCtrl(self.panel)
#         # tc3 = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
#
#
#         # fgs.AddMany([(title), (tc1, 1, wx.EXPAND), (author),
#         #              (tc2, 1, wx.EXPAND), (review, 1, wx.EXPAND), (tc3, 1, wx.EXPAND)])
#
#         # fgs.AddGrowableRow(2, 1)
#         fgs.AddGrowableCol(0, 1)
#         fgs.AddGrowableCol(1, 1)
#
#
#
#         hbox.Add(fgs, proportion=1, flag=wx.ALL | wx.EXPAND, border=15)
#         # panel.SetSizer(hbox)
#         self.panel.SetSizer(hbox)
#         hbox.Fit(self)
#
#     def flexItem(self, title, flexGrid):
#         titleLable = wx.StaticText(self.panel, label=title)
#         tc1 = wx.TextCtrl(self.panel)
#         box = wx.BoxSizer(wx.HORIZONTAL)
#         box.Add(titleLable, flag=wx.ALL, border=5)
#         box.Add(tc1, proportion=1, flag=wx.ALL | wx.EXPAND, border=5)
#         flexGrid.Add(box, 1, wx.EXPAND)
#
#     def onOK(self, event):
#         # Do something
#         print("ok")
#
#     def onCancel(self, event):
#         self.closeProgram()
#
#     def closeProgram(self):
#         self.Close()
#
# if __name__ == '__main__':
#     app = wx.PySimpleApp()
#     frame = MyForm().Show()
#     app.MainLoop()