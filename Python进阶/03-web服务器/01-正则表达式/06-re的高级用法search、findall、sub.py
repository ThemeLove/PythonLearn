import re


def replace_method(temp):
    num = temp.group()
    print("type of temp=", type(temp))
    print("temp", temp)

    print("type of num=", type(num))
    print("num=", num)

    num = int(num) + 11111
    return str(num)


def main():
    # search()方法不同与match：match默认是从头开始匹配，search是匹配第一个满足条件的内容，可以不从头开始匹配
    # 在search()前添^（从开头匹配）其效果等同于match()
    test_str1 = "12345abc@abc$abc"
    ret1 = re.search(r"abc", test_str1)
    print("ret1=", ret1.group())

    # findall()，也是查找内容，返回值时一个列表，返回所有满足条件的内容
    test_str2 = "12345abc@abc$abc"
    ret2 = re.findall(r"abc", test_str2)
    print("ret2=", ret2)

    # 将匹配到的数据进行替换，直接替换
    test_str3 = "12345abc@abc$abc"
    ret3 = re.sub(r"abc", "xyz", test_str3)
    print("ret3=", ret3)

    # 将匹配到的数据进行替换，支持方法
    test_str4 = "12345abc@abc$abc"
    ret4 = re.sub(r"\d+", replace_method, test_str4)
    print("ret4=", ret4)


if __name__ == "__main__":
    main()
