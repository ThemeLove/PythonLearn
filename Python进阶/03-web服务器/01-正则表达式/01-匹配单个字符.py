import re


def main():
    # \d :匹配一个数字，即0-9
    ret1 = re.match("速度与激情\d","速度与激情1")
    print("ret1=",ret1.group())
    # [] :匹配[]中列举的字符，可以用-连接简写：如果[0-36-9] 表示数字0到3，6到9
    ret2 = re.match("速度与激情[123567]","速度与激情2")
    print("ret2=",ret2.group())
    ret3 = re.match("速度与激情[123567]","速度与激情4")
    # print("ret3=",ret3) 报错，因为不能匹配到4
    print("type of ret3=",type(ret3))

    #用-来简写
    re.match("速度与激情[1-46-9]","速度与激情5")
    ret4 = re.match("速度与激情[1-46-9]","速度与激情5")
    print("type of ret4=", type(ret4))

    #匹配数字和字符
    ret5 = re.match("速度与激情[1-9a-zA-Z]","速度与激情c")
    print("ret5=",ret5.group())

    # \w :匹配一个字符 ,包括0-9，a-z,A-Z，其他单个字符，但不包括特殊符号
    ret6 = re.match("速度与激情\w","速度与激情哈")
    print("ret6=",ret6.group())
    ret7 = re.match("速度与激情\w", "速度与激情1")
    print("ret7=", ret7.group())
    ret8 = re.match("速度与激情\w", "速度与激情a")
    print("ret8=", ret8.group())
    ret9 = re.match("速度与激情\w", "速度与激情@") # 特殊符号
    # print("ret9=", ret9.group()) # 报错

    # \s :匹配一个空格,tab
    ret10 = re.match("速度与激情\s\d","速度与激情 1")
    print("ret10=",ret10.group())
    ret11 = re.match("速度与激情\s\d","速度与激情2") #报错，因为没有空格
    # print("ret11=",ret11.group())
    ret12 = re.match("速度与激情\s\d","速度与激情\t1") #\t在程序中就是代表tab键
    print("ret12=",ret12.group())

    # . :匹配任意一个字符，\n除外
    ret13 = re.match("速度与激情.","速度与激情$") # $ 特殊字符也能匹配
    print("ret13=",ret13.group())

    ret14 = re.match("速度与激情.","速度与激情\n") # 报错，因为\n不能匹配
    # print("ret14=",ret14.group())

    # 特别说明 \s \S；\d \D;\w \W 这几组互为相反，即\s匹配不到的，\S一定能匹配到
    ret15 = re.match("速度与激情\W","速度与激情@")
    print("ret15=",ret15.group())


if __name__ == "__main__":
    main()
