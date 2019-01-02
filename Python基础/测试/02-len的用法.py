def main():
    str1 = "我们aaaa"
    print("str1 的 len=",len(str1))

    b_str1 = str1.encode("utf-8")
    print("b_str1=", b_str1)
    print("type of b_str1=", type(b_str1))
    print("b_str1 的 len=", len(b_str1))

    rf1 =open("images/banner.jpg", "rb")
    print("rf1= ", rf1.read())
    print("type of rf1=", type(rf1.read(1024)))



if __name__ == "__main__":
    main()
