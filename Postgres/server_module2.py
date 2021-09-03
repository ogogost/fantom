import socket
from _thread import *
import var as v


def threaded_client(connection, que_1, que_2):
    connection.send(str.encode('Welcome to the Server'))
    while True:
        data = connection.recv(2048)
        if data.decode('utf-8') == '0':
            break
        que_1.put(data.decode('utf-8'))
        que_2.put(data.decode('utf-8'))
        reply = "Server Says: " + data.decode('utf-8')
        # v.list_of_var.append(data.decode('utf-8'))
        # print(v.list_of_var)
        connection.sendall(str.encode(reply))
    connection.close()
    print('connection closed')
    print('Waiting for a Connection..')


def start_server(que_1, que_2):

    server_socket = socket.socket()
    thread_count = 0

    try:
        server_socket.bind((v.host, v.port))
    except socket.error as e:
        print(str(e))

    print('Waiting for a Connection..')
    server_socket.listen(5)

    while True:
        client, address = server_socket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, ((client),(que_1),(que_2)))
        thread_count += 1
        print('Thread Number: ' + str(thread_count))
