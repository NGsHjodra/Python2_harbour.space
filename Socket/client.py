import socket


#HOST = str(input("Enter The server's hostname : "))
#HOST = "93.184.216.34"  # The server's hostname or IP address
#PORT = 80  # The port used by the server

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #ip4 = socket.gethostbyname(HOST)
    HOSTNAME = socket.gethostbyaddr(HOST)
    SString = f"GET / HTTP/1.0\nHost: {HOSTNAME}\n\n"
    #print(SString)
    s.sendall(bytes(SString, 'utf-8'))
    data = s.recv(4096)

print(f"Received {data.decode('UTF-8')}")