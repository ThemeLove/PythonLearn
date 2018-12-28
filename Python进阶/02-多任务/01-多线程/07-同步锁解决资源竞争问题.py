import threading

lock=threading.Lock()
test_num = 0


def test1(num):
    global test_num
    for i in range(num):
        lock.acquire()
        test_num += 1
        lock.release()
    print("-----test1_num= "+str(test_num))


def test2(num):
    global test_num
    for i in range(num):
        lock.acquire()
        test_num += 1
        lock.release()
    print("-----test2_num= "+str(test_num))


'''
1.lock=threading.Lock()方法可以获取到同步锁对象
2.lock.require()和lock.release()之间的代码就是上锁的代码
3.程序执行时谁先抢到锁就先执行，同时将同步锁锁起来，其他线程要执行需要等待该同步锁的释放，
这样技能保证一个同步锁锁起来的代码可以执行完毕，就相当于原子操作，就保证了多线程操作同一全局变量时线程安全问题。
4.同一个lock可以给多处代码上锁，但是同一时间只能执行一处，其他线程都处于等待状态
'''


def main():
    thread1 = threading.Thread(target=test1, args=(1000000,))
    thread2 = threading.Thread(target=test2, args=(1000000,))

    thread1.start()

    thread2.start()


if __name__ == "__main__":
    main()
