import re
import logging


def main():
    """
    ^ :表示以什么开头
    $ :表示以什么结尾
    python中re.match默认只判断开头，没有判断结尾，即mathc方法默认自带了^,没有自带$
    """

    names = ["age", "a1ge", "1age", "a_age", "age_1", "age!", "a#123", "#age", "_______"]
    for name in names:
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if ret:
            print(name, " 符合要求...通过正则匹配的数据是：", ret.group())
        else:
            try:
                print(name, "不符合要求...通过正则匹配的数据是：", ret.group())
            except Exception as e:
                logging.exception(e)


if __name__ == "__main__":
    main()
