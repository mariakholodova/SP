import socket

HOST = '127.0.0.1'
PORT = 65432


def server_tcp():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print('wait data...')
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024).decode()
            print('Received ', data)
            data = data.upper()
            conn.sendall(data.encode())

if __name__ == '__main__':
    server_tcp()
