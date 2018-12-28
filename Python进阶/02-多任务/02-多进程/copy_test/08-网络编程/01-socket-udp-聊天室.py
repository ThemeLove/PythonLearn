import socket

'''
发送消息
return True  退出
return False 继续发送
'''


def send_message(udp_socket,dest_addr):

    # 读取用户输入的数据
    send_data = input("请输入要发送的数据(exit-退出;enter键-发送):\n")

    if send_data == "exit":
        return True
    # 发送数据
    udp_socket.sendto(send_data.encode("GBK"),dest_addr)  # 因为这里和window交互,所以这里编码用GBK
    return False


'''
接收消息
return True  退出
return False 继续接收
'''


def receive_message(udp_socket):

    # 指定每次缓存的大小，返回值是一个元祖,第一个元素receive_data是客户端发送过来的数据；第二个元素receive_addr是客户端ip和port
    receive_data,receive_addr=udp_socket.recvfrom(1000)

    if receive_data.decode("GBK") == "exit":
        return True

    print("消息来源于%s:\n%s" %(receive_addr,receive_data.decode("GBK")))  # 因为这里和window交互,所以这里编码用GBK
    return False


def main():
    # 创建socket,socket.AF_INET表示ipv4,socket.SOCK_STREAM表示tcp
    udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 手动绑定端口，如果不手动绑定端口的话，系统会随机分配一个，每次运行程序的时候可能不一样
    udp_socket.bind(("", 8081))  # ip不填默认是本机公网ip，可以用ifconfig查看

    # 开启循环，定义退出规则
    while True:
        # 提示用户选择要进行的操作：1-发送消息；2-接受消息；3-退出程序
        option=input("请选择宁要执行的操作：\n1-发送消息\n2-接收消息\n3-退出程序\n")
        if option == "1":
            print("您选择了 '发送消息'\n")
            # 提示用户输入对方ip
            dest_ip = input("请输入对方ip：\n")
            # 提示用户输入对方端口
            dest_port = int(input("请输入对方端口号：\n"))
            dest_addr = (dest_ip, dest_port)
            while True:
                is_exit=send_message(udp_socket,dest_addr)
                if is_exit:
                    print("退出发送消息\n")
                    break

        elif option == "2":
            print("您选择了 '接收消息,接收等待中...'\n")
            while True:
                is_exit=receive_message(udp_socket)
                if is_exit:
                    print("退出接收消息\n")
                    break

        elif option == "3":
            print("您选择了 '退出程序'\n")
            break
        else :
            print("输入有误，请重新输入")

    # 循环结束，关闭socket
    udp_socket.close()


if __name__ == "__main__":
    main()
