import os


# 输出 shell 交互的返回内容
def print_shell(shell_res):
    for line in shell_res.readlines():
        line = line.strip()
        print(line)


# 获取当前需要被 exploit 的文件
def file_name():
    file_dir = "./exploit_file"
    list_file = os.listdir(file_dir)
    # length = len(list_file)
    cnt = 0
    for i in list_file:
        print(str(cnt) + ":" + i)
        cnt = cnt + 1

    choice = int(input("选择要进行操作的文件："))
    chose_file = list_file[choice]
    # print(type(chose_file))
    return chose_file

