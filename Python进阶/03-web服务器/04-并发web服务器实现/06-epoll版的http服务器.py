import select
import re
import socket
import logging


def serve_client(fd, epl, client_socket_dict):
    client_data = ""
    client_socket = None
    try:
        client_socket = client_socket_dict[fd]
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
                client_param = "/index_origin.html"
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
                response_body = r"<meta charset='UTF-8'>error----->没有相关资源"
                response_header_fail += "Content-Length:%d\r\n\r\n" % (len(response_body.encode("utf-8")),)
                client_socket.send(response_header_fail.encode("utf-8"))
                client_socket.send(response_body.encode("utf-8"))
                logging.exception(e)
        else:  # 获取用户的参数失败
            response_body = "error----->params error"
            response_header_fail += "Content-Length:%d\r\n\r\n" % (len(response_body.encode("utf-8")),)
            client_socket.send(response_header_fail.encode("utf-8"))
            client_socket.send(response_body.encode("utf-8"))
    else:  # 如果接收的数据为空，则说明客户端关闭了连接，服务端这时可以关闭该连接
        # 处理完毕关闭socket，并将其从列表中移除
        print("客户端断开连接...")
        client_socket.close()
        epl.unregister(fd)
        del client_socket_dict[fd]


def main():
    # 创建tcp服务端套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定服务器ip和端口号
    tcp_server_socket.bind(("", 8888))
    print("服务器（10.200.202.22)已开启，等待连接中...")
    # 开启监听
    tcp_server_socket.listen(1024)
    # 创建一个epoll对象
    epl = select.epoll()
    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)
    # 创建一个存放客户端套接字的和索引（fd）的字典
    fd_event_dict = dict()
    while True:
        fd_event_list = epl.poll()  # 默认会阻塞，直到os检测到数据到来，通过事件通知方式告知这个程序，此时才会解堵塞
        for fd, event in fd_event_list:
            if fd == tcp_server_socket.fileno():
                tcp_client_socket, tcp_client_address = tcp_server_socket.accept()
                epl.register(tcp_client_socket.fileno(), select.EPOLLIN)
                fd_event_dict[tcp_client_socket.fileno()] = tcp_client_socket
            elif event == select.EPOLLIN:
                # 判断已经连接的客户端是否有数据发送过来
                serve_client(fd, epl, fd_event_dict)


if __name__ == "__main__":
    main()
