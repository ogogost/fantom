import socket

client = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

client.connect(
    ("127.0.0.1", 2000)
)

while True:
    data = client.recv(2048)
    print(data.decode("utf-8"))

    client.send(input("Input:").encode('utf-8'))