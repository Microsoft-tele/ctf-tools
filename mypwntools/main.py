# main for mypwntools
import os
from checksec import *
from util import *


def menu():
    print("0:exit")
    print("1:gcc")
    print("2:clang")
    print("3:checksec")
    return int(input("选择要进行的操作："))


if __name__ == '__main__':
    filename = file_name()
    print("要操作的文件：" + filename)
    choice_menu = menu()
    if choice_menu == 0:
        exit(0)
    elif choice_menu == 3:
        checksec("./exploit_file/" + filename)
        menu()

