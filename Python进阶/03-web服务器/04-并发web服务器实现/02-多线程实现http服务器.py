import threading
import socket
import logging
import re


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
    client_socket.close()


def main():
    # 创建tcp服务端socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定服务端端口
    tcp_server_socket.bind(("10.200.202.22", 8889))
    print("服务器（10.200.202.22)已开启，等待连接中...")
    # 开启服务端监听
    tcp_server_socket.listen(1024)
    while True:
        # 接收客户端连接
        tcp_client_socket, tcp_client_address = tcp_server_socket.accept()
        # 创建线程
        new_thread = threading.Thread(target=serve_client, args=(tcp_client_socket,))
        # 开启线程
        new_thread.start()

    tcp_server_socket.close()


if __name__ == "__main__":
    main()
