import socket


def main():
    # 1.创建tcp套接字
    tcp_download_client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 2.连接服务器
    dest_ip=input("请输入要连接的服务器ip:\n")
    dest_port=int(input("请输入要绑定的端口号：\n"))
    dest_addr=(dest_ip,dest_port)
    tcp_download_client_socket.connect(dest_addr)
    # 3.发送数据（告诉服务器要下载的文件名）
    download_file_name=input("请输入要下载的文件名：\n")
    tcp_download_client_socket.send(download_file_name.encode("utf-8"))
    receive_data=tcp_download_client_socket.recv(1024)
    if receive_data :
        with open("new_%s" % download_file_name,"w",encoding="utf-8") as f:
            f.write(receive_data.decode("GBK"))

    # 4.关闭tcp套接字
    tcp_download_client_socket.close()


if __name__ == "__main__":
    main()
