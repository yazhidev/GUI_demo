import os
import sys
import time
import re


# 把执行命令和休眠等待封装成一个方法
def perform(command, seconds=0.5):
    os.system(command)
    time.sleep(seconds)


# 封装触摸事件
def click(coordinate, seconds=0.5):
    perform("adb shell input tap {}".format(coordinate), seconds)


# 执行按返回键
def back():
    perform("adb shell input keyevent 4")


#截图并传输到电脑
def screen_shot(flag):
    print("进入面板，准备截图")
    name = "/sdcard/screen-{}-{}.png".format(get_time(), flag)
    command = "adb shell screencap -p " + name
    os.system(command)
    time.sleep(1.5)
    command = "adb pull " + name + " " + sys.path[0]
    print("截图完毕，传输到电脑上，保存路径：", sys.path[0])
    os.system(command)
    time.sleep(1.5)


# 获取当前时间，用于命名
def get_time():
    now = time.time()
    timeArray = time.localtime(now)
    return time.strftime("%Y-%m-%d_%H:%M:%S", timeArray)


# 判断目前所在的页面名称是否是 activity_name
def is_top_activity(activity_name):
    dumpsys = os.popen("adb shell dumpsys activity activities")
    info = dumpsys.readlines()  # 读取命令行的输出到一个list
    result = False
    for line in info:  # 按行遍历
        line = line.strip()
        dumpsys = re.match("mResumedActivity.*", line)
        if dumpsys:
            str = dumpsys.group(0)
            if str.__contains__(activity_name):
                return True
    return result


# 检查当前页面是否是 activity_name
def check_activity_(activity_name):
    while True:
        if is_top_activity(activity_name):
            # 即使进入页面也会有 loading 的时间，所以等2秒
            time.sleep(2)
            return
        time.sleep(1)


def test_case():
    # 点击 office
    click("536 813")
    # 如果没进入面板，就一直等待
    check_activity_("TYRCTSmartPanelActivity")
    # 截图，并传输到电脑上
    screen_shot(num)
    back()
    # 进入我的
    click("915 2246")
    # 进入设置，有个网络请求，所以等久一点，等4秒
    click("330 1183", 4)
    # 清除缓存
    click("934 769")
    back()
    click("125 2250")


num = 1
while True:
    print("第{}轮".format(num))
    test_case()
    num = num + 1