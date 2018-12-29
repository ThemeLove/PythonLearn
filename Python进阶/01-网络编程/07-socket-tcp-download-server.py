import socket


def main():
    # 1.创建tcp套接字
    tcp_download_server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.绑定ip和端口
    server_ip=input("请输入服务器要绑定的ip:\n")
    server_port=int(input("请输入服务器要绑定的端口：\n"))
    server_addr=(server_ip,server_port)
    tcp_download_server_socket.bind(server_addr)
    # 3.开启监听状态
    tcp_download_server_socket.listen(128)  # listen 的参数表示同时能接收处理的套接字数

    # 4. accept 等待客户端连接
    print("服务器已开启等待连接...")
    while True:
        work_socket,client_addr=tcp_download_server_socket.accept()
        print("%s连接上了"%(client_addr,))
        while True:
            # 5.接收和发送数据
            receive_data=work_socket.recv(1024)
            print("%s发来数据:\n%s"%(client_addr,receive_data.decode("GBK")))
            if receive_data:
                file_content=None
                try:
                    f = open(receive_data.decode("GBK"), "r")
                    file_content = f.read(1024)
                except Exception as e:
                    print(e)
                if file_content:
                    # 将数据发送给客户端
                    work_socket.send(file_content.encode("GBK"))
            else:
                print("%s断开连接了\n等待其他连接...." %(client_addr,))
                work_socket.close()
                break

    tcp_download_server_socket.close()


if __name__ == "__main__":
    main()
