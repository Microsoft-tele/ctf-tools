# 自动执行 checksec 检测程序保护
import os
from util import *


def checksec(file_name):
    checksec_res = os.popen("checksec " + file_name)
    print_shell(checksec_res)
