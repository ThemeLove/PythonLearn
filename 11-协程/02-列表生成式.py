

def main():

    """
        这里的list生成方式就是列表生成式（list comprehensions）,可以大大提高对list的操作效率
    """
    lista = [x**2 for x in range(1, 11) if x % 2 == 0]
    print("lista= ", lista)
    for temp in lista:
        print(temp)

    listb = [m+n for m in "abc" for n in "123"]
    print("listb= ",listb)

    print(lista)


if __name__ == "__main__":
    main()
