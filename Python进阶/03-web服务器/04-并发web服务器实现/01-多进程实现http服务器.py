import multiprocessing
import socket
import re
import logging


def serve_client(client_socket):
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
    if client_param:
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
    else:  # 成功获取到用户的参数
        client_socket.send(response_header_fail.encode("utf-8"))
        client_socket.send("error----->params error".encode("utf-8"))
        pass
    # 关闭socket
    client_socket.close()  # 在子进程也关闭socket连接


def main():
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定服务端ip和端口
    tcp_server_socket.bind(("10.200.202.22", 8887))
    print("服务器（10.200.202.22)已开启，等待连接中...")
    # 开启监听
    tcp_server_socket.listen(1024)

    while True:
        # 接收客户端连接
        tcp_client_socket, tcp_client_address = tcp_server_socket.accept()
        # 创建一个进程
        p = multiprocessing.Process(target=serve_client, args=(tcp_client_socket, ))
        # 开启进程
        p.start()
        # 在主进程关闭客户端连接才有用，因为在主进程持有的才是客户端socket连接的直接引用，子进程只是主进程的拷贝
        tcp_client_socket.close()
    # 关闭服务端连接
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
