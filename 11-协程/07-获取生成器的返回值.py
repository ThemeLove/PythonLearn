def generator(num):
    count = 0
    while count < num:
        yield count
        count += 1
    return "i'm the result of generator"


def main():
    gen10 = generator(10)
    for temp in gen10:
        print("gen1----->", temp)

    # 再获取一次就会有异常产生，这里手动捕获
    try:
        next(gen10)
    except StopIteration as e:
        print("e.value= %s" % e.value)


if __name__ == "__main__":
    main()
