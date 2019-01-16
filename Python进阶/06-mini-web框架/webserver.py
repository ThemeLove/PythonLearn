import socket
import multiprocessing
import re
import logging
import sys


class WSGIServer:
    def __init__(self, port, application, static_path):
        # 创建tcp server socket对象
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.application = application
        self.static_path = static_path
        self.response_header = ""

    def run(self):
        # 绑定端口
        self.server_socket.bind(("", self.port))
        # 开启监听
        self.server_socket.listen(1024)
        print("服务端已开启(port:%s)" % self.port)
        # 循环接受客户端连接
        while True:
            client_socket, client_addr = self.server_socket.accept()
            print("客户端已连接(ip：%s,port:%s)" % (client_addr[0], client_addr[1]))
            p = multiprocessing.Process(target=self.server_client, args=(client_socket,))
            p.start()
            client_socket.close()
        self.server_socket.close()

    def set_response_header(self, status, response_header_params):
        response_header = ""
        if status == "200":
            status_line = "HTTP/1.1 %s OK\r\n" % status
        elif status == "404":
            status_line = "HTTP/1.1 %s Fail\r\n" % status
        else:
            status_line = "HTTP/1.1 %s Fail\r\n" % status
        response_header += status_line
        for temp in response_header_params:
            response_header += "%s:%s\r\n" % (temp[0], temp[1])
        self.response_header = response_header

    def server_client(self, client_socket):
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
        if not client_param.endswith(".py"):  # 说明请求的时静态资源
            if client_param:
                if client_param == "/":
                    client_param = "/index.html"
                response_path = self.static_path + client_param
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
        else:  # 动态返回的结果
            client_params = dict()
            client_params["path"] = client_param

            body = self.application(client_params, self.set_response_header)

            print("response_header", self.response_header)
            response = "%s\r\n\r\n%s" % (self.response_header, body)
            client_socket.send(response.encode("utf-8"))

        # 关闭socket
        client_socket.close()  # 在子进程也关闭socket连接


def main():
    args = sys.argv
    if len(args) == 3:
        try:
            port = int(args[1])
            frame_app_name = args[2]
        except Exception as e:
            print("端口输入错误！")
            return

        ret = re.match("([^:]+):(.*)", frame_app_name)
        if ret:
            frame_name = ret.group(1)
            app_name = ret.group(2)
        else:
            print("参数输入错误")
            return
    else:
        print("请传入正确的参数个数")
        return

    with open("./webserver.conf") as f:
        server_conf = f.read()
    conf_dict = eval(server_conf)
    print("conf_dict", conf_dict)
    static_path = conf_dict["static_path"]
    dynamic_path = conf_dict["dynamic_path"]

    sys.path.append(dynamic_path)

    # 动态导入
    frame = __import__(frame_name)
    frame_application = getattr(frame, app_name)

    server = WSGIServer(port, frame_application, static_path)
    server.run()


if __name__ == "__main__":
    main()
