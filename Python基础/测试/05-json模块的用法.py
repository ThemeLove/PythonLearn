import json


def main():
    dicta = dict()
    dicta['a'] = "aa"
    dicta['b'] = "bb"
    dicta['c'] = "cc"
    # 将dict转化为json字符串
    json_dict = json.dumps(dicta)
    print("json_dict="+json_dict)

    #  将json字符串写入文件
    with open("./files/test.json","w") as f:
        json.dump(json_dict, f)

    # 将json字符串转化为dict
    dict_b = json.loads(json_dict)
    print("type of dict_b=" + str(type(dict_b)))

    # 从文件中读取json字符串
    with open("./files/test.json", "r") as f:
        dict_c = json.load(f)
        print("type of dict_c=" + str(type(dict_c)))

    stu1 = Student("zhangsan", 23)

    # 将自定义对象转化为json字符串，lambda obj:obj.__dict__ 将任意obj转化为dict,json.dumps再将dict转化为json字符串
    stu_str = json.dumps(stu1, default=lambda obj: obj.__dict__)
    print("stu_str="+stu_str)

    # 将json字符串，转化为自定义对象,需要传入关键字参数object_hook指明转化方式
    stu2 = json.loads(stu_str, object_hook=dict2student)
    print("type of stu2=" + str(type(stu2)))


def dict2student(d):
    return Student(d["name"], d["age"])


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    main()
