import socket


"""
    socket.setblocking(False)的作用是：设置当前sokcet为非阻塞，即当调用socket的阻塞api时，不会去等待，会立刻尝试获得结果；
    当没有成功时会报错，编写代码时需要进行异常处理
    比如：socket.accept()会尝试立刻获得一个客户端连接，如果此时没有客户端连接的话会报错；
         socket.recv()会尝试立刻获得一个客户端数据，如果客户端只是连接上，但是没有立刻发送数据，就会报错。
"""


def main():
    # 创建tcp服务器套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定服务起ip和端口，ip为空默认为当前本机ip
    tcp_server_socket.bind(("", 8888))
    print("服务器（10.200.202.22)已开启，等待连接中...")
    # 开启服务器监听
    tcp_server_socket.listen(1024)
    # 设置tcp服务器套接字为非阻塞
    tcp_server_socket.setblocking(False)
    # 创建一个空列表，用于存放接收的客户端连接
    tcp_client_socket_list = list()

    while True:
        try:
            # 接收客户端套接字
            tcp_client_socket, tcp_client_address = tcp_server_socket.accept()
            # 设置客户端套接字为非阻塞，并添加到客户端socket列表中
            tcp_client_socket.setblocking(False)
            # 将接收的连接添加到列表中
            tcp_client_socket_list.append(tcp_client_socket)
        except Exception as e:  # 捕获异常，说明没有客户端连接
            pass
            # print("当前没有客户端的连接...")
            # logging.exception(e)

        for tcp_client_socket in tcp_client_socket_list:
            try:
                client_data = tcp_client_socket.recv(1024)
                if client_data:
                    print("成功获取到客户端数据 data=", client_data.decode("utf-8"))
                    tcp_client_socket.send("hello~client:num =%d".encode("utf-8") % (tcp_client_socket.fileno(),))
                    tcp_client_socket_list.remove(tcp_client_socket)
                else:
                    print("数据为空，客户端关闭了连接")
                    tcp_client_socket_list.remove(tcp_client_socket)
            except Exception as e:  # 捕获到异常，说明该客户端socket连接暂时没有发送数据
                pass
                # logging.exception(e)


if __name__ == "__main__":
    main()
