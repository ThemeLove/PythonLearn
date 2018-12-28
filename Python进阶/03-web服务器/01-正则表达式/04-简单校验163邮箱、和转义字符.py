import re


def main():
    """
    转义字符：正则表达式中如果需要将有特殊意义的符号（比如 . ? +）原样输出可以用 \ 来进行转义
    """
    email = input("请输入一个邮箱地址")
    print(email)
    print()
    ret = re.match(r"^[a-zA-Z0-9]{4,12}@163\.com$", email)
    print(ret.group())
    while not ret:
        print(email, "不符合163邮箱规则")
        email = input("请输入一个邮箱地址")
        print()
        ret = re.match(r"^[a-zA-Z0-9]{4,12}@163\.com$", email)
    print(email, "该邮箱符合163邮箱规则")


if __name__ == "__main__":
    main()
