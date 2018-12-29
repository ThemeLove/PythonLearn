import socket


def main():
    # 1.创建tcp套接字,socket.AF_INET表示ipv4,socket.SOCK_STREAM表示tcp
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定ip和端口号
    server_addr = ("10.200.202.22", 8081)
    tcp_server_socket.bind(server_addr)
    # 3.开启监听
    tcp_server_socket.listen(128)
    print("服务器%s已经开启了，等待连接中..." %(server_addr,))
    # 4.循环等待客户端连接
    while True:
        new_client_socket, client_addr = tcp_server_socket.accept()

        print("%s连接上了" % (client_addr,))

        # 5.循环接收连接上的socket信息，如果receive_data为null则说明tcp客户端断开
        while True:
            receive_data = new_client_socket.recv(1024)
            if receive_data and receive_data.decode("GBK") != "exit":  # 如果receive_data不为null,并且receive_data不等于“exit”,就给tcp客户端回消息
                print("%s发来消息:\n%s" % (client_addr, receive_data.decode("GBK")))
                new_client_socket.send(("hello~%s" % receive_data.decode("GBK")).encode("utf-8"))
            else:
                print("%s断开连接了,服务完毕!" % (client_addr,))
                # 服务端在单线程里同时只能为一个tcp连接服务，连接时处于阻塞状态，其他的tcp连接进不来
                # 为一个客户端服务完毕了，这里主动关闭连接，解阻塞
                new_client_socket.close()
                break

    # 6.关闭服务端套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
