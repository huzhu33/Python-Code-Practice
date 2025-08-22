#!usr/bin/env python3
# name = input('please input your name:\n')
# print('Hello',name)

# 处理用户多行输入的典型模式：名单收集，问卷调查等场景
print("请输入你和你队友的姓名，完成后输入'done'结束：")
namelist = []
# 第一轮输入
while True:
    name = input()
    if name == "done":
        break
    namelist.append(name)

# 二次确认与可重输逻辑
while True:
    print("是否确定已经完成名单输入？确认完成请输入'yes',重新输入名单请输入'no'")
    reply = input().strip().lower() # 去除空格并转小写，提高输入容错
    if reply == 'yes':
        break
    elif reply == 'no':
        print("即将重新输入名单，完成后输入'done'结束，请开始：")
        namelist = [] # 清空原名单
        while True:
            name = input()
            if name == 'done':
                break
            namelist.append(name)
            # 重新输入完成后，再次进入确认循环

# 输出最终确定的名单
result = '\n'.join(namelist)
print("你和你的队友名单如下：\n" + result)
