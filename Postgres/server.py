import socket
from Postgres import PostgreSQL as PS

server = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM,
)

server.bind(
    ("127.0.0.1", 2000)  # localhost
)

server.listen(5)
print("Server is listen")

while True:
    user_socket, address = server.accept()
    print(f"User {user_socket} connected!")

    user_socket.send("You connected\n"
                     "1.postgres_version\n"
                     "2.create_database\n"
                     "3.create_table".encode("utf-8"))

    data = user_socket.recv(2048)

    print(data.decode("utf-8"))

    data2 = user_socket.recv(2048)

    if data.decode("utf-8") == "1":
        PS.postgres_version()
    if data.decode("utf-8") == "2":
        PS.create_database()
    if data.decode("utf-8") == "3":
        PS.create_table()
