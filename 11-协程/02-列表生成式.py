def main():

    """
        这里的list生成方式就是列表生成式（list comprehensions）,可以大大提高对list的操作效率
        语法： [表达式]
        return :list
    """
    list1 = [x**2 for x in range(1, 11) if x % 2 == 0]
    print("list1= ", list1)
    for temp in list1:
        print(temp)

    list2 = [m+n for m in "abc" for n in "123"]
    print("list2= ", list2)

    print(list2)


if __name__ == "__main__":
    main()
