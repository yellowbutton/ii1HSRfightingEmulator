
def 交互选择(可选列表,整个游戏):
    for 选项 in 可选列表:
        print(选项)
    return 可选列表[int(input("请选择:"))][0]["激活器标签"]