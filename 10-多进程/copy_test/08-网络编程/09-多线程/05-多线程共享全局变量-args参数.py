import threading
import time


test_list = [10, 20]


def test1(temp):
    temp.append(30)
    print("-----test1-----"+str(test_list))


def test2(temp):
    print("-----test2-----"+str(temp))


def main():
    # target=指明了将要运行的函数，args必须是一个元祖，表示传递给函数的参数
    thread1 = threading.Thread(target=test1, args=(test_list,))
    thread2 = threading.Thread(target=test2, args=(test_list,))

    thread1.start()
    time.sleep(2)
    thread2.start()


if __name__ == "__main__":
    main()
