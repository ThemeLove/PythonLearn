import socket
import threading

is_exit_send_msg = False


def send_msg(udp_socket, dest_addr):
    global is_exit_send_msg
    while True:
        send_data = input("请输入要发送的内容：\n")
        if send_data == "exit":
            is_exit_send_msg = True
            print("退出发送消息")
            break
        udp_socket.sendto(send_data.encode("GBK"), dest_addr)


def receive_msg(udp_socket):
    global is_exit_send_msg
    while True:
        receive_data, from_addr = udp_socket.recvfrom(1024)
        if receive_data.decode("GBK") == "exit":
            print("退出接收消息")
            break
        print(str(from_addr)+" 发来消息：\n"+receive_data.decode("GBK"))

        if not is_exit_send_msg:
            print("请输入要发送的内容:")


def main():
    # 1.创建udp socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 2.输入要连接的ip和端口
    dest_ip = input("输入要连接的ip:\n")
    dest_port = int(input("输入端口号：\n"))
    dest_addr = (dest_ip, dest_port)
    # 3.创建发送消息线程
    thread_send = threading.Thread(target=send_msg, args=(udp_socket, dest_addr))
    # 4.创建接收消息线程
    thread_receive = threading.Thread(target=receive_msg, args=(udp_socket,))

    # 5.开启发送消息线程
    thread_send.start()
    # 6.开启接收消息线程
    thread_receive.start()


if __name__ == "__main__":
    main()
