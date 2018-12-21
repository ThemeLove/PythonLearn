from collections import Iterable
from collections import Iterator


class School:
    def __init__(self):
        self.teachers = list() # 创建一个空列表
        self.index = 0

    def append(self,teacher):
        self.teachers.append(teacher)

    """
        1.Python中如果一个对象是可迭代的,该对象中必须有__iter__方法 
        2.当对一个可迭代对象用for .. in 迭代的时候，python会去调用该迭代对象的__iter__方法返回值对象中的__next__方法
           本例中返回self（即该对象本身），所以School对象被迭代的时候会去调用对象本身的__next__方法
    """

    def __iter__(self):
        return self

    """
        Python中，
    
    """

    def __next__(self):
        # next里的代码通常需要try...catch，来捕获从迭代器里取不到数据的情况；
        # 并且可以raise一个StopIteration异常，这样外部调用的代码Python就会停止迭代
        try:
            ret = self.teachers[self.index]
            self.index += 1
            return ret
        except Exception as e:
            raise StopIteration()


def main():
    lista = range(10)
    for i in lista:
        print(i)

    school = School()
    school.append("王老师")
    school.append("韩老师")
    school.append("廖老师")

#     判断一个对象是否时可迭代的，isinstance可一判断一个对象是否时某种数据类型，Iterable 表示可迭代的
    str = "abc"
    tuplea = ("a","b","c","d")
    dict = {"name": "张三", "age": 18, "gender": "male"}
    print(isinstance(str, Iterable)) # True
    print(isinstance(lista, Iterable)) #T rue
    print(isinstance(tuplea, Iterable)) # True
    print(isinstance(dict,Iterable))
    print(isinstance(1,Iterable))  # False

    print(isinstance(school, Iterable))

    # 判断一个对象是不是一个迭代器 isinstance(obj, Iterator)

    print(isinstance(school, Iterator))
    # 调用iter(obj) 就相当于调用可迭代对象（obj）的__iter__方法
    print(iter(school))
    # 调用next(obj) 就相当于调用一次可迭代对象（obj）的__next__方法,即对可迭代对象迭代一次
    print(next(school))

    # 可以看出，list、tuple、dict、字符串都是 可迭代的对象
    for temp in school:
        print(temp)


if __name__ == "__main__":
    main()
