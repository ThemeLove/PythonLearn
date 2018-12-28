import threading
import time

'''
1.Python中可以通过继承threading.Thread来定义线程，线程中可以自定义方法来完成自生身逻辑
2.Python类中调用自身方法时要用self调用，比如self.do_something()
3.自定义线程对象只有调用start()方法时，才是真正开启一个线程;调用start()方法后，会自动调用自定义线程中的run方法。
4.my_thread=MyThread()执行时，只是创建了线程对象，并没有真正创建一个线程，只有在调用start()方法时，系统才会开启一个新线程，这一点可以用threading.enumerate()方法来验证
'''


class MyThread(threading.Thread):
    def run(self):
        for i in range(10):
            time.sleep(1)
            self.do_something()
            print(self.format_msg(i))

    def format_msg(self, num):
        return "I'm "+self.name+" @ "+str(num)

    def do_something(self):
        print("I'm doing very important things")


def main():
    my_thread = MyThread()
    my_thread.start()


if __name__ == "__main__":
    main()
