import socket


def main():
    # 1.创建tcp套接字,socket.AF_INET表示ipv4,socket.SOCK_STREAM表示tcp
    tcp_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.连接服务器
    dest_ip=input("请输入您要连接的服务器ip:\n")
    dest_port=int(input("请输入服务器的端口号:\n"))
    dest_addr=(dest_ip,dest_port)
    print(dest_addr)
    tcp_client_socket.connect(dest_addr)

    # 3.发送数据
    send_data=input("请输入要发送的内容:\n")

    tcp_client_socket.send(send_data.encode("GBK"))
    # 4.关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()
