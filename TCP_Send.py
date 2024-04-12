import socket
import json


def tcp_send(host, port, data):
    # 创建 socket 对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取本地主机名
    # host = socket.gethostname()
    # port = 9999

    # 连接服务，指定主机和端口
    # client_socket.connect((host, port))

    # 发送的数据
    # data = {'name': 'ChatGPT', 'message': 'Hello, World!'}
    message = json.dumps(data)
    print(f"Sending: {message}")

    # 发送 JSON 字符串
    # client_socket.send(message.encode('utf-8'))

    # 关闭连接
    # client_socket.close()

    
def get_host_ip():
    try:
        # 创建一个 socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 连接到一个不存在的地址，这里使用 Google 的 DNS 服务器地址
        s.connect(("8.8.8.8", 80))
        # 获取本地端点的 IP 地址
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip