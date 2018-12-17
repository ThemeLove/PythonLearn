import multiprocessing
import threading
import time


def test1():
    while True:
        time.sleep(1)
        print("-----test1-----processName= "+multiprocessing.current_process().name+" ;threadName= "+threading.current_thread().getName())
        # -----test1-----processName= Process-1 ;threadName= MainThread
        # 每个进程里默认都有个主线程


def test2():
    while True:
        time.sleep(1)
        print("-----test2-----processName=" + multiprocessing.current_process().name+" ;threadName= "+threading.current_thread().getName())
        # -----test2-----processName=Process-2 ;threadName= MainThread
        # 每个进程里默认都有个主线程


def main():
    # 获取cpu核心数
    cpu_count=multiprocessing.cpu_count()
    print("cpu_count="+str(cpu_count))

    # 创建多进程
    process1 = multiprocessing.Process(target=test1)
    process2 = multiprocessing.Process(target=test2)
    # 开启多进程
    process1.start()
    process2.start()
    print("-----main-----processName=" + multiprocessing.current_process().name + " ;threadName= " + threading.current_thread().getName())
    # -----main-----processName=MainProcess ;threadName= MainThread


if __name__ == "__main__":
    main()
