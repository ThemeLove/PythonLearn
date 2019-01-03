import socket
import re

response_header_ok = """HTTP/1.1 200 OK

"""
response_header_failed = """HTTP/1.1 404 Failed

"""


def handle_client_socket(client_socket):
    client_data = client_socket.recv(1024)
    print("client_data=", client_data.decode("utf-8"))
    # 处理客户端发送过来的数据
    client_str = client_data.decode("utf-8")
    client_data_list = re.split(r"\r\n", client_str)
    print("client_data_list=", client_data_list)
    # 获取list的第一个元素
    ret = re.match(r"[^/]+(/[^ ]*)", client_data_list[0])  # 用正则匹配客户端参数

    if ret:   # 成功获取客户端参数
        client_request_params = ret.group(1)
        print("client_request_params=", client_request_params)
        if client_request_params == "/":
            client_request_params = "/index.html"
        response_path = "./html_test"+client_request_params
        print("response_path=", response_path)
        try:
            rf = open(response_path, "rb")
            client_socket.send(response_header_ok.encode("utf-8"))
            client_socket.send(rf.read())
            rf.close()
        except IOError as e:  # 没有成功打开数据
            client_socket.send(response_header_failed.encode("utf-8"))
            client_socket.send("未知错误".encode("utf-8"))

    else:   # 没有获取到客户端数据
        client_socket.send(response_header_failed.encode("utf-8"))
        client_socket.send("未知错误".encode("utf-8"))
    # 关闭客户端socket连接
    client_socket.close()


def main():
    # 创建tcp套接字socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定端口
    tcp_server_ip = input("请输入要绑定的ip:\n")
    tcp_server_port = input("请输入要绑定的端口：\n")
    # tcp_server_socket.bind((tcp_server_ip, int(tcp_server_port)))
    tcp_server_socket.bind(("10.200.202.22", 8888))
    # 监听连接
    tcp_server_socket.listen(1024)
    while True:
        # 接收客户端连接
        tcp_client_socket, client_address = tcp_server_socket.accept()
        handle_client_socket(tcp_client_socket)
    # 关闭服务端socket
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
