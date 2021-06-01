import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def client_udp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        data = 'Hello, world'.encode()
        s.sendto(data, (HOST, PORT))
        data, _ = s.recvfrom(1024)
        print('Received', data.decode())


if __name__ == '__main__':
    client_udp()
