import socket

HOST = "127.0.0.1"
PORT = 8080

# https://realpython.com/python-sockets/

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Accepted connection from {addr}")
        data: bytes = conn.recv(4096)
        if data:
            print(f"Received: {data.decode('utf-8')}")
            conn.sendall(bytearray("HTTP/1.1 200 OK\nContent-Length: 24\nContent-Type: text/plain; charset=utf-8\n\nHello from our server!\n\n", "utf-8"))

    conn.close()

    s.shutdown(socket.SHUT_RDWR)
    s.close()