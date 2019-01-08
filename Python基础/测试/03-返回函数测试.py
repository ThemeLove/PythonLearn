
num = 0


def counter():
    a = [0]

    def count():
        a[0] = a[0] + 1
        return a[0]
    return count


def counter1():
    def count1():
        global num
        num = num+1
        return num
    return count1


def main():
    a = counter()
    print("a1=", a())
    print("a2=", a())
    print("a3=", a())
    print("a4=", a())

    b = counter1()
    print("b1=", b())
    print("b2=", b())
    print("b3=", b())
    print("b4=", b())






if __name__ == "__main__":
    main()
