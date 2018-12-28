import re


def main():

    """
    分组的作用：
    1.当正则表达式比较长时，分组写法可读性较强
    2.分组可以起别名，可以通过数组和别名来引用
    3.group(分组名)方法中可以传入分组名来获取指定分组名匹配的内容，注意分组名要存在；
      不传值表示获取所有匹配内容
    """

    #  | 匹配左右任意一个表达式
    ret1 = re.match(r"[a-zA-Z0-9]{4,12}@(163|126)\.com$", "12345@163.com")
    print("ret1=", ret1.group())
    print("ret1's group(1)=", ret1.group(1))
    ret2 = re.match(r"[a-zA-Z0-9]{4,12}@(163|126)\.com$", "12345@126.com")
    print("ret2=", ret2.group())
    print("ret2's group(1)=", ret2.group(1))

    # 一个分组
    html_str1 = "<h1>我来演示正则表达式分组</h1>"
    ret3 = re.match(r"<(\w*)>.*</(\1)>", html_str1)
    print("ret3=", ret3.group())

    # 二个分组
    html_str2 = "<body><h1>我来演示正则表达式分组</h1></body>"
    ret4 = re.match(r"<(\w*)><(\w*)>.*</(\2)></(\1)>", html_str2)
    print("ret4=", ret4.group())
    print("ret4's group(1)=", ret4.group(1))
    print("ret4's group(2)=", ret4.group(2))

    # 给分组起别名
    html_str3 = "<header><h1>我来演示正则表达式分组</h1></header>"
    ret5 = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", html_str3)
    print("ret5=", ret5.group())
    print("ret5's group(1)=", ret5.group(1))
    print("ret5's group(2)=", ret5.group(2))
    print("ret5's name1=", ret5.group("name1"))
    print("ret5's name2=", ret5.group("name2"))

    # 匹配失败，因为html_str4不满足分组1前后内容必须一样
    html_str4 = "<body><h1>我来演示正则表达式分组</h1></header>"
    ret6 = re.match(r"<(?P<name1>\w*)><(?P<name2>\w*)>.*</(?P=name2)></(?P=name1)>", html_str4)
    print("type or ret6=", type(ret6))
    # print("ret6=", ret5.group())
    # print("ret6's group(1)=", ret6.group(1))
    # print("ret6's group(2)=", ret6.group(2))


if __name__ == "__main__":
    main()
