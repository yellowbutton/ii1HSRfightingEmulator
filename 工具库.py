def 选取(值,字典列表,标签="身份",列表返回=False):
    if 列表返回:
        return [字典 for 字典 in 字典列表 if 标签 in 字典 and 字典[标签]==值]
    for 字典 in 字典列表:
        if 标签 in 字典 and 字典[标签]==值:
            return 字典
    return None