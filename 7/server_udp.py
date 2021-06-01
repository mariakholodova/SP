import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432  # The port used by the server


def server_udp():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('wait data...')
        data, addr = s.recvfrom(1024)
        data = data.decode()
        print('Connected by', addr)
        print('Received ', data)
        data = data.upper()
        s.sendto(data.encode(), addr)


if __name__ == '__main__':
    server_udp()
