def 选取(选择字典,字典列表,列表返回=False):
    if 列表返回:
        返回值= []
        for 字典 in 字典列表:
            for 标签,值 in 选择字典.items():
                if 标签 not in 字典 or 字典[标签]!=值:
                    break
            else:
                返回值.append(字典)
        return 返回值
    for 字典 in 字典列表:
            for 标签,值 in 选择字典.items():
                if 标签 not in 字典 or 字典[标签]!=值:
                    break
            else:
                return 字典
    return None

def 表出栈(项,列表):
    返回值=列表[:项]
    del 列表[:项]
    return 返回值