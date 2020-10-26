import pywinauto
from pywinauto.mouse import *
from pywinauto.keyboard import *
import time

# 1.运行记事本程序
app = pywinauto.Application().start('notepad.exe')
url = "D:\Software\Navicat 15 for MySQL\navicat.exe"

"""
可通过窗口标题选择窗口（推荐）
app[类名/标题]
"""

# 1.
# 使用窗口标题来选择窗口
dlg = app["无标题 - 记事本"]
# 打印该窗口所有控件
dlg.print_control_identifiers()
