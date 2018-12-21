def yanghui_triangle(num):
    count = 1
    ret_list = list()
    list1 = [1]
    list2 = [1, 1]
    while count <= num:
        if count == 1:
            ret_list = list1
        elif count == 2:
            ret_list = list2
        else:
            temp_ret_list = ret_list
            # 给temp_ret_list的首尾添加两个0元素
            temp_ret_list.insert(0, 0)
            temp_ret_list.append(0)
            print("aaaaaaaaaa")
            print(temp_ret_list)
            temp_list = list()
            for temp in temp_ret_list:
                # 获取temp的索引
                index = temp_ret_list.index(temp)
                # 判断边界
                if index < len(temp_ret_list):
                   temp_list.append(temp + temp_ret_list[index+1])
            ret_list = temp_list

        yield ret_list
        count += 1


def main():
    yang0 = yanghui_triangle(0)
    yang1 = yanghui_triangle(1)
    yang2 = yanghui_triangle(2)
    yang3 = yanghui_triangle(3)
    yang10 = yanghui_triangle(10)

    print("type yang0= ", type(yang0))

    print(yang0)
    print(yang1)
    print(yang2)
    print(yang3)
    print(yang10)
    #
    # for temp in yang0:
    #     print(temp)
    # print("---------------\n\n\n")
    #
    # for temp in yang1:
    #     print(temp)
    # print("---------------\n\n\n")
    #
    # for temp in yang2:
    #     print(temp)
    # print("---------------\n\n\n")

    for temp in yang3:
        print(temp)
    print("---------------\n\n\n")

    # for temp in yang10:
    #     print(temp)
    # print("---------------\n\n\n")


if __name__ == "__main__":
    main()
