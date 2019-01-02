import socket
import re
import logging


def serve_client(client_socket, client_socket_list):
    client_data = client_socket.recv(1024).decode("utf-8")
    print("\r\n\r\n\r\nstart>>>>>>>>>>>>>>>>>>>>")
    print("client_data=", client_data)

    # 对客户端参数进行处理，获取用户浏览器输入的参数
    client_param = ""
    if client_data:
        client_data_list = client_data.splitlines()
        if client_data_list and client_data_list[0]:
            print("list[1]=", client_data_list[0])
            client_param = re.search(r"/[^ ]*", client_data_list[0]).group()

    # 根据是否成功获取到客户端参数，费别处理
    response_header_ok = "HTTP/1.1 200 OK\r\n\r\n"  # 注意header 和 body之间时通过一个空行来区分的
    response_header_fail = "HTTP/1.1 404 FAIL\r\n\r\n"
    if client_param:  # 成功获取到用户的参数
        if client_param == "/":
            client_param = "/index.html"
        response_path = "./html_test"+client_param
        print("response_path=", response_path)
        try:
            rf = open(response_path, "rb")
            client_socket.send(response_header_ok.encode("utf-8"))
            client_socket.send(rf.read())
            rf.close()
        except IOError as e:
            client_socket.send(response_header_fail.encode("utf-8"))
            client_socket.send("error----->file not found".encode("utf-8"))
            logging.exception(e)
    else:  # 获取用户的参数失败
        print("连接关闭了")
        client_socket.send(response_header_fail.encode("utf-8"))
        client_socket.send("error----->params error".encode("utf-8"))
        pass
    # 处理完毕关闭socket，并将其从列表中移除
    client_socket.close()
    client_socket_list.remove(client_socket)


"""
    socket.setblocking(False)的作用是：设置当前sokcet为非阻塞，即当调用socket的阻塞api时，不会去等待，会立刻尝试获得结果；
    当没有成功时会报错，编写代码时需要进行异常处理
    比如：socket.accept()会尝试立刻获得一个客户端连接，如果此时没有客户端连接的话会报错；
         socket.recv()会尝试立刻获得一个客户端数据，如果客户端只是连接上，但是没有立刻发送数据，就会报错。
"""


def main():
    # 创建tcp服务器套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定服务起ip和端口
    tcp_server_socket.bind(("10.200.202.22", 8892))
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
        except Exception as e:
            pass
            # print("当前没有客户端的连接...")
            # logging.exception(e)

        for tcp_client_socket in tcp_client_socket_list:
            try:
                serve_client(tcp_client_socket, tcp_client_socket_list)
            except Exception as e:
                pass
                # logging.exception(e)


if __name__ == "__main__":
    main()
