import re


def main():

    """
    * : 匹配前1个字符0次或多次，即可有可无
    + : 匹配前1个字符1次或多次，即至少1次
    ? : 匹配前1个字符出现1次或者0次，即要么1次，要么没有；住re.match(r"\d?","123") 可以匹配到“1”，后面的“23”匹配不到
    {m}: 匹配前1个字符出现m次，中间不能断开
    {m,n} : 匹配前1个字符出现m到n次
    """
    ret1 = re.match(r"速度与激情\d*", "速度与激情")  # * 匹配0次
    print("ret1=", ret1.group())
    ret2 = re.match(r"速度与激情\d*", "速度与激情123")  # *匹配多次
    print("ret2=", ret2.group())

    ret3 = re.match(r"速度与激情\d+", "速度与激情")  # + 至少1次，这里ret3 为None
    print("type of ret3=", type(ret3))
    ret4 = re.match(r"速度与激情\d+", "速度与激情4325")
    print("ret4=", ret4.group())

    ret5 = re.match(r"速度与激情\d?", "速度与激情")  # ? 匹配0次
    print("ret5=", ret5.group())
    ret6 = re.match(r"速度与激情\d?", "速度与激情7")  # ? 匹配1次
    print("ret6=", ret6.group())
    ret7 = re.match(r"速度与激情\d?", "速度与激情789哈")  # ? 匹配多次失败，ret7 为 “速度与激情7”
    print("type or ret7=", type(ret7))
    print("ret7=", ret7.group())

    ret8 = re.match(r"0564-\d{7}", "0564-7739123")  # {m} 匹配m次，必须为m次
    print("ret8=", ret8.group())
    ret9 = re.match(r"0564-\d{7}", "0564-123")  # {m} 少于7位，ret9为None
    print("type of ret9=", type(ret9))

    ret10 = re.match(r"\d{2,4}-\d{7}", "01-1234567")  # {m,n} 匹配m到n次都可以
    print("ret10=", ret10)
    ret11 = re.match(r"\d{2,4}-\d{7}", "12345-1234567")  # {m.n} 匹配失败，在m~n范围之外，ret11 为 None
    print("type or ret11=", type(ret11))

    # 特别的一下输出为 “我”，可以说明“.” 不能匹配到\n换行符，如需匹配需要添加正则的修饰符re.S
    ret12 = re.match(r".*", """我
    爱
    python
    """)
    print("ret12=", ret12.group())

    ret13 = re.match(r".*", """我
    爱
    python
    """, re.S)
    print("ret13=", ret13.group())


if __name__ == "__main__":
    main()
