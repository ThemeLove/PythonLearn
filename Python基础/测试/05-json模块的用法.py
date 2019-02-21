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


if __name__ == "__main__":
    main()
