import wx
import const
import pyperclip


class Example(wx.Frame):
    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(1000, 665),
                                      style=wx.DEFAULT_FRAME_STYLE ^ wx.RESIZE_BORDER ^ wx.MAXIMIZE_BOX)
        self.InitUI()
        self.Centre()
        self.Show()

    def InitUI(self):
        panel = wx.Panel(self)
        # 一个垂直容器，一个水平容器
        container_hor = wx.BoxSizer(wx.HORIZONTAL)
        container_ver = wx.BoxSizer(wx.VERTICAL)
        # 测试信息部分
        container_ver.Add(self.buildTestInfo(panel), flag=wx.ALL | wx.EXPAND, border=10)
        clear_info_btn = wx.Button(panel, label='清空所有测试信息')
        self.Bind(wx.EVT_BUTTON, self.on_clear_infos, clear_info_btn)
        container_ver.Add(clear_info_btn, flag=wx.ALIGN_RIGHT | wx.RIGHT, border=15)
        # 操作步骤部分
        container_ver.Add(self.buildSteps(panel), flag=wx.LEFT | wx.RIGHT | wx.EXPAND, border=10)
        # 复制内容按钮
        finish_btn = wx.Button(panel, label='清空所有操作步骤')
        self.Bind(wx.EVT_BUTTON, self.on_clear_actions, finish_btn)
        container_ver.Add(finish_btn, flag=wx.ALIGN_RIGHT | wx.RIGHT | wx.TOP, border=15)
        # 内容显示框
        result_container = wx.BoxSizer(wx.VERTICAL)
        result_label = wx.TextCtrl(panel, style=wx.TE_MULTILINE | wx.TE_READONLY, size=(450, 550))
        self.save2dic(const.KEY_RESULT, result_label)
        result_container.Add(result_label)
        copy_btn = wx.Button(panel, label='复制到剪贴板')
        self.Bind(wx.EVT_BUTTON, self.copy_result, copy_btn)
        result_container.Add(copy_btn, flag=wx.ALIGN_RIGHT | wx.TOP, border=20)
        container_hor.Add(container_ver, flag=wx.ALL, border=10)
        container_hor.Add(result_container, flag=wx.TOP | wx.RIGHT, border=35)
        panel.SetSizerAndFit(container_hor)

    # 测试信息
    def buildTestInfo(self, panel):
        test_info = wx.StaticBox(panel, label="测试信息：")
        test_info_sizer = wx.StaticBoxSizer(test_info, wx.VERTICAL)

        # 在 test_info的布局中插入横向间隔为 5 的 GridBagSizer 布局
        grid_bag_sizer = wx.GridBagSizer(5, 0)

        # 在 GridBagSizer 中逐行增加内容，每行的内容放在一个横向的 BoxSizer 中
        line1 = wx.BoxSizer(wx.HORIZONTAL)
        test_app_name = wx.StaticText(panel, label="测试APP: ")
        test_app_input = wx.TextCtrl(panel)
        self.save2dic(const.KEY_NAME, test_app_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, test_app_input)
        version_name = wx.StaticText(panel, label="版本: ")
        version_input = wx.TextCtrl(panel)
        self.save2dic(const.KEY_VERSION, version_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, version_input)
        line1.Add(test_app_name, flag=wx.RIGHT, border=10)
        line1.Add(test_app_input, flag=wx.RIGHT, border=10)
        line1.Add(version_name)
        line1.Add(version_input)
        grid_bag_sizer.Add(line1, pos=(0, 0), span=(1, 3))

        line2 = wx.BoxSizer(wx.HORIZONTAL)
        account_and_pwd = wx.StaticText(panel, label="测试账号及密码: ")
        area = wx.ComboBox(panel, value='中国', choices=["中国", "美国", "欧洲", "印度"])
        grid_bag_sizer.Add(area, pos=(1, 3), span=(1, 1))
        # 添加事件处理
        self.save2dic(const.KEY_AREA, area)
        self.Bind(wx.EVT_COMBOBOX, self.on_combobox, area)
        account_and_pwd_input = wx.TextCtrl(panel, size=(150, 20))
        self.save2dic(const.KEY_ACCOUNT, account_and_pwd_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, account_and_pwd_input)
        line2.Add(account_and_pwd, flag=wx.Top, border=3)
        line2.Add(area, flag=wx.LEFT, border=10)
        line2.Add(account_and_pwd_input, flag=wx.LEFT, border=10)
        grid_bag_sizer.Add(line2, pos=(1, 0), span=(1, 3))

        line3 = wx.BoxSizer(wx.HORIZONTAL)
        test_mobile = wx.StaticText(panel, label="测试手机型号及版本: ")
        test_mobile_input1 = wx.TextCtrl(panel, size=(130, 20))
        test_mobile_input2 = wx.TextCtrl(panel, size=(130, 20))
        self.save2dic(const.KEY_MOBILE1, test_mobile_input1)
        self.Bind(wx.EVT_TEXT, self.on_text_input, test_mobile_input1)
        self.save2dic(const.KEY_MOBILE2, test_mobile_input2)
        self.Bind(wx.EVT_TEXT, self.on_text_input, test_mobile_input2)
        line3.Add(test_mobile, flag=wx.RIGHT, border=10)
        line3.Add(test_mobile_input1, flag=wx.RIGHT, border=10)
        line3.Add(test_mobile_input2)
        grid_bag_sizer.Add(line3, pos=(2, 0), span=(1, 3))

        line4 = wx.BoxSizer(wx.HORIZONTAL)
        device_name = wx.StaticText(panel, label="设备名称: ")
        device_name_input = wx.TextCtrl(panel)
        self.save2dic(const.KEY_DEVICE, device_name_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, device_name_input)
        device_id = wx.StaticText(panel, label="设备ID: ")
        device_id_input = wx.TextCtrl(panel)
        self.save2dic(const.KEY_DEVICE_ID, device_id_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, device_id_input)
        line4.Add(device_name, flag=wx.RIGHT, border=10)
        line4.Add(device_name_input, flag=wx.RIGHT, border=10)
        line4.Add(device_id)
        line4.Add(device_id_input)
        grid_bag_sizer.Add(line4, pos=(3, 0), span=(1, 3))

        line5 = wx.BoxSizer(wx.HORIZONTAL)
        pid_name = wx.StaticText(panel, label="PID: ")
        pid_name_input = wx.TextCtrl(panel)
        self.save2dic(const.KEY_PID, pid_name_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, pid_name_input)
        uiid_name = wx.StaticText(panel, label="UIID: ")
        uiid_name_input = wx.TextCtrl(panel)
        self.save2dic(const.KEY_UIID, uiid_name_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, uiid_name_input)
        line5.Add(pid_name, flag=wx.RIGHT, border=10)
        line5.Add(pid_name_input, flag=wx.RIGHT, border=30)
        line5.Add(uiid_name)
        line5.Add(uiid_name_input)
        grid_bag_sizer.Add(line5, pos=(4, 0), span=(1, 3))

        line6 = wx.BoxSizer(wx.HORIZONTAL)
        firmware_key = wx.StaticText(panel, label="固件 Key: ")
        firmware_key_input = wx.TextCtrl(panel)
        self.save2dic(const.KEY_FIRMWARE_KEY, firmware_key_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, firmware_key_input)
        firmware_version = wx.StaticText(panel, label="固件版本: ")
        firmware_version_input = wx.TextCtrl(panel)
        self.save2dic(const.KEY_FIRMWARE_VERSION, firmware_version_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, firmware_version_input)
        line6.Add(firmware_key, flag=wx.RIGHT, border=10)
        line6.Add(firmware_key_input, flag=wx.RIGHT, border=30)
        line6.Add(firmware_version)
        line6.Add(firmware_version_input)
        grid_bag_sizer.Add(line6, pos=(5, 0), span=(1, 3))

        test_info_sizer.Add(grid_bag_sizer, flag=wx.ALL, border=5)
        return test_info_sizer

    # 操作步骤
    def buildSteps(self, panel):
        operation_step = wx.StaticBox(panel, label="操作步骤: ")
        operation_step_sizer = wx.StaticBoxSizer(operation_step, wx.VERTICAL)

        grid_bag_sizer1 = wx.GridBagSizer(5, 0)

        precondition = wx.StaticText(panel, label="前提条件： ")
        precondition_input = wx.TextCtrl(panel, size=(400, 20))
        self.save2dic(const.KEY_PRECONDITION, precondition_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, precondition_input)
        grid_bag_sizer1.Add(precondition, pos=(0, 0), span=(1, 1))
        grid_bag_sizer1.Add(precondition_input, pos=(0, 1), span=(1, 10), flag=wx.RIGHT, border=10)

        precondition = wx.StaticText(panel, label="操作步骤： ")
        num1 = wx.StaticText(panel, label="(1) ")
        precondition_input1 = wx.TextCtrl(panel, size=(374, 20))
        self.save2dic(const.KEY_ACTION1, precondition_input1)
        self.Bind(wx.EVT_TEXT, self.on_text_input, precondition_input1)
        grid_bag_sizer1.Add(precondition, pos=(1, 0), span=(1, 1))
        grid_bag_sizer1.Add(num1, pos=(1, 1), span=(1, 1))
        grid_bag_sizer1.Add(precondition_input1, pos=(1, 2), span=(1, 10))

        num2 = wx.StaticText(panel, label="(2) ")
        precondition_input2 = wx.TextCtrl(panel, size=(374, 20))
        self.save2dic(const.KEY_ACTION2, precondition_input2)
        self.Bind(wx.EVT_TEXT, self.on_text_input, precondition_input2)
        grid_bag_sizer1.Add(num2, pos=(2, 1), span=(1, 1))
        grid_bag_sizer1.Add(precondition_input2, pos=(2, 2), span=(1, 10))

        num3 = wx.StaticText(panel, label="(3) ")
        precondition_input3 = wx.TextCtrl(panel, size=(374, 20))
        self.save2dic(const.KEY_ACTION3, precondition_input3)
        self.Bind(wx.EVT_TEXT, self.on_text_input, precondition_input3)
        grid_bag_sizer1.Add(num3, pos=(3, 1), span=(1, 1))
        grid_bag_sizer1.Add(precondition_input3, pos=(3, 2), span=(1, 10))

        num4 = wx.StaticText(panel, label="(4) ")
        precondition_input4 = wx.TextCtrl(panel, size=(374, 20))
        self.save2dic(const.KEY_ACTION4, precondition_input4)
        self.Bind(wx.EVT_TEXT, self.on_text_input, precondition_input4)
        grid_bag_sizer1.Add(num4, pos=(4, 1), span=(1, 1))
        grid_bag_sizer1.Add(precondition_input4, pos=(4, 2), span=(1, 10))

        num5 = wx.StaticText(panel, label="(5) ")
        precondition_input5 = wx.TextCtrl(panel, size=(374, 20))
        self.save2dic(const.KEY_ACTION5, precondition_input5)
        self.Bind(wx.EVT_TEXT, self.on_text_input, precondition_input5)
        grid_bag_sizer1.Add(num5, pos=(5, 1), span=(1, 1))
        grid_bag_sizer1.Add(precondition_input5, pos=(5, 2), span=(1, 10))

        actual_result = wx.StaticText(panel, label="实际结果： ")
        actual_result_input = wx.TextCtrl(panel, size=(400, 40))
        self.save2dic(const.KEY_ACTUAL_RESULT, actual_result_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, actual_result_input)
        grid_bag_sizer1.Add(actual_result, pos=(6, 0), span=(1, 1))
        grid_bag_sizer1.Add(actual_result_input, pos=(6, 1), span=(2, 10))

        expect_result = wx.StaticText(panel, label="期望结果： ")
        expect_result_input = wx.TextCtrl(panel, size=(400, 40))
        self.save2dic(const.KEY_EXPECT_RESULT, expect_result_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, expect_result_input)
        grid_bag_sizer1.Add(expect_result, pos=(8, 0), span=(1, 1))
        grid_bag_sizer1.Add(expect_result_input, pos=(8, 1), span=(2, 10))

        remark = wx.StaticText(panel, label="备注： ")
        remark_input = wx.TextCtrl(panel, size=(400, 40))
        self.save2dic(const.KEY_REMARK, remark_input)
        self.Bind(wx.EVT_TEXT, self.on_text_input, remark_input)
        grid_bag_sizer1.Add(remark, pos=(10, 0), span=(1, 1))
        grid_bag_sizer1.Add(remark_input, pos=(10, 1), span=(2, 10))

        operation_step_sizer.Add(grid_bag_sizer1, flag=wx.ALL, border=5)
        return operation_step_sizer

    def on_combobox(self, event):
        print("选择{0}".format(event.GetString()))
        self.show_result()

    def on_clear_infos(self, event):
        infos_key = [const.KEY_NAME, const.KEY_VERSION, const.KEY_AREA, const.KEY_ACCOUNT, const.KEY_DEVICE_ID,
                     const.KEY_DEVICE, const.KEY_MOBILE2, const.KEY_MOBILE1, const.KEY_UIID, const.KEY_PID,
                     const.KEY_FIRMWARE_KEY, const.KEY_FIRMWARE_VERSION]
        for item in infos_key:
            self.dic[item].SetValue('')

    def copy_result(self, event):
        result = self.dic[const.KEY_RESULT].GetValue()
        # print(result)
        pyperclip.copy(result)

    def on_clear_actions(self, event):
        actions_key = [const.KEY_PRECONDITION, const.KEY_ACTION1, const.KEY_ACTION2, const.KEY_ACTION3,
                       const.KEY_ACTION4, const.KEY_ACTION5, const.KEY_REMARK, const.KEY_EXPECT_RESULT,
                       const.KEY_ACTUAL_RESULT]
        for item in actions_key:
            self.dic[item].SetValue('')

    def on_text_input(self, event):
        self.show_result()

    dic = {}

    def save2dic(self, key, value):
        self.dic[key] = value

    def get_info(self, key):
        return self.dic[key].GetValue()

    def show_result(self):
        result_list = []
        result_list.append("【测试信息】\n")
        self.add_info(result_list, "测试App :{}", const.KEY_NAME)
        self.add_info(result_list, " ({})", const.KEY_VERSION)
        self.add_info(result_list, "\n地区 :{}", const.KEY_AREA)
        self.add_info(result_list, "\n测试账号及密码 :{}", const.KEY_ACCOUNT)
        self.add_info(result_list, "\n测试手机型号及版本 :{}", const.KEY_MOBILE1)
        self.add_info(result_list, "\n测试手机型号及版本 :{}", const.KEY_MOBILE2)
        self.add_info(result_list, "\n设备名称 :{}", const.KEY_DEVICE)
        self.add_info(result_list, "\n设备ID :{}", const.KEY_DEVICE_ID)
        self.add_info(result_list, "\nPID :{}", const.KEY_PID)
        self.add_info(result_list, "\nUIID :{}", const.KEY_UIID)
        self.add_info(result_list, "\n固件key :{}", const.KEY_FIRMWARE_KEY)
        self.add_info(result_list, "\n固件版本 :{}", const.KEY_FIRMWARE_VERSION)
        self.add_info(result_list, "\n\n【前提条件】\n{}", const.KEY_PRECONDITION)
        self.add_info(result_list, "\n\n【操作步骤】\n（1）:{}", const.KEY_ACTION1)
        self.add_info(result_list, "\n（2）:{}", const.KEY_ACTION2)
        self.add_info(result_list, "\n（3）:{}", const.KEY_ACTION3)
        self.add_info(result_list, "\n（4）:{}", const.KEY_ACTION4)
        self.add_info(result_list, "\n（5）:{}", const.KEY_ACTION5)
        self.add_info(result_list, "\n\n【实际结果】\n{}", const.KEY_ACTUAL_RESULT)
        self.add_info(result_list, "\n\n【期望结果】\n{}", const.KEY_EXPECT_RESULT)
        self.add_info(result_list, "\n\n【备注】\n{}", const.KEY_REMARK)
        self.dic[const.KEY_RESULT].SetValue(''.join(result_list))

    def add_info(self, array, format_str, key):
        if len(self.get_info(key).strip()) > 0:
            array.append(format_str.format(self.get_info(key).strip()))


app = wx.App()
Example(None, 'Demo')
app.MainLoop()
