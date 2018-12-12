import socket


def main():
    # 1.创建tcp套接字,socket.AF_INET表示ipv4,socket.SOCK_STREAM表示tcp
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定ip和端口号
    tcp_server_socket.bind(("10.200.202.20",8081))
    # 3.开启监听
    tcp_server_socket.listen(128)
    # 4.等待客户端连接
    new_client_socket,client_addr = tcp_server_socket.accept()
    # print(new_client_socket)
    # print(client_addr)
    print("%s连接上了" % (client_addr,))


    # 5.收发信息
    receive_data = new_client_socket.recv(1024)
    if receive_data.decode("GBK") == "exit":
        new_client_socket.close()

    print("%s发来消息:\n%s" % (client_addr,receive_data.decode("GBK")))

    new_client_socket.send(("hello~%s" % receive_data.decode("GBK")).encode("GBK"))

    # 6.关闭客户端套接字


if __name__ == "__main__":
    main()
