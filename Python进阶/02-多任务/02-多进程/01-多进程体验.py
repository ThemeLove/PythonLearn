import multiprocessing
import threading
import time


def test1(sleep_time):
    while True:
        time.sleep(sleep_time)
        print("-----test1-----processName= "+multiprocessing.current_process().name+" ;threadName= "+threading.current_thread().getName())
        # -----test1-----processName= Process-1 ;threadName= MainThread
        # 每个进程里默认都有个主线程


def test2(sleep_time):
    while True:
        time.sleep(sleep_time)
        print("-----test2-----processName=" + multiprocessing.current_process().name+" ;threadName= "+threading.current_thread().getName())
        # -----test2-----processName=Process-2 ;threadName= MainThread
        # 每个进程里默认都有个主线程


def main():
    # 获取cpu核心数
    cpu_count=multiprocessing.cpu_count()
    print("cpu_count="+str(cpu_count))

    # 创建多进程
    process1 = multiprocessing.Process(target=test1, args=(1,))
    process2 = multiprocessing.Process(target=test2, args=(1,))
    # 开启多进程
    process1.start()
    process2.start()
    print("-----main-----processName=" + multiprocessing.current_process().name + " ;threadName= " + threading.current_thread().getName())
    # -----main-----processName=MainProcess ;threadName= MainThread

    process1.join(5) # process1阻塞主进程5秒
    print("5 second later")
    process1.join(5) # process2阻塞主进程5秒
    print("5 second later") # process1 和 process2 一共阻塞主进程10秒，10秒后才能打印该行


if __name__ == "__main__":
    main()
