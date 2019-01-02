import socket
import re
import logging


def serve_client(client_socket, client_socket_list):
    client_data = ""
    try:
        client_data = client_socket.recv(1024).decode("utf-8")
    except Exception as e:  # socket尝试立刻接收数据失败
        return

    print("\r\n\r\n\r\nstart>>>>>>>>>>>>>>>>>>>>")
    print("client_data=", client_data)

    # 对客户端参数进行处理，获取用户浏览器输入的参数
    client_param = ""
    if client_data:
        client_data_list = client_data.splitlines()
        if client_data_list and client_data_list[0]:
            print("list[0]=", client_data_list[0])
            ret = re.search(r"/[^ ]*", client_data_list[0])
            if ret:
                client_param = ret.group()
            # 根据是否成功获取到客户端参数，费别处理
        response_header_ok = "HTTP/1.1 200 OK\r\n"  # 注意header 和 body之间时通过一个空行来区分的
        response_header_ok += "Content-Type:charset=utf-8\r\n"
        response_header_fail = "HTTP/1.1 404 FAIL\r\n"
        response_header_fail += "Content-Type:charset=utf-8\r\n"
        response_body = ""
        if client_param:  # 成功获取到用户的参数
            if client_param == "/":
                client_param = "/index.html"
            response_path = "./html_test" + client_param
            print("response_path=", response_path)
            try:
                rf = open(response_path, "rb")
                response_body = rf.read()
                # 拼接Content-Length请求头，请求头用于告诉浏览器请求体的内容的长度，让浏览器识别本次返回结束，不再等待
                # 注意header 和 body之间时通过一个空行来区分的
                response_header_ok += "Content-Length:%d\r\n\r\n" % (len(response_body),)
                client_socket.send(response_header_ok.encode("utf-8"))
                client_socket.send(response_body)
                rf.close()
            except IOError as e:
                response_body = "error----->没有相关资源"
                response_header_fail += "Content-Length:%d\r\n\r\n" % (len(response_body.encode("utf-8")),)
                client_socket.send(response_header_fail.encode("utf-8"))
                client_socket.send(response_body.encode("utf-8"))
                logging.exception(e)
        else:  # 获取用户的参数失败
            response_body = "error----->params error"
            response_header_fail += "Content-Length:%d\r\n\r\n" % (len(response_body.encode("utf-8")),)
            client_socket.send(response_header_fail.encode("utf-8"))
            client_socket.send(response_body.encode("utf-8"))
    else:  # 如果接收的数据为空，则说明客户端关闭了连接
        # 处理完毕关闭socket，并将其从列表中移除
        client_socket.close()
        client_socket_list.remove(client_socket)


def main():
    # 创建tcp服务端socket
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定服务器socket的ip和端口号，ip传空表示绑定本地
    tcp_server_socket.bind(("", 8111))
    print("服务器（10.200.202.22)已开启，等待连接中...")
    # 开启监听
    tcp_server_socket.listen(1024)
    # 设置为tcp服务端socket为非阻塞
    tcp_server_socket.setblocking(False)
    # 创建存放客户端连接的list
    tcp_client_socket_list = list()
    while True:
        try:
            # 接收客户端套接字
            tcp_client_socket, tcp_client_address = tcp_server_socket.accept()
            # 设置客户端套接字为非阻塞，并添加到客户端socket列表中
            tcp_client_socket.setblocking(False)
            # 将接收的连接添加到列表中
            tcp_client_socket_list.append(tcp_client_socket)
        except Exception as e:  # 服务端socket尝试立即获取客户端连接失败
            pass
            # print("当前没有客户端的连接...")
            # logging.exception(e)

        for tcp_client_socket in tcp_client_socket_list:
            serve_client(tcp_client_socket, tcp_client_socket_list)


if __name__ == "__main__":
    main()
