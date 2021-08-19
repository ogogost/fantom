import socket
from _thread import *
import var as v


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
    while True:
        data = connection.recv(2048)
        reply = "Server Says: " + data.decode('utf-8')
        v.list_of_var.append(data.decode('utf-8'))
        print(v.list_of_var)
        if data.decode('utf-8') == '0':
            break
        connection.sendall(str.encode(reply))
    connection.close()
    print('connection closed')
    print('Waiting for a Connection..')


def start_server():

    ServerSocket = socket.socket()
    ThreadCount = 0
    # host = '127.0.0.1'
    # port = 1233

    try:
        ServerSocket.bind((v.host, v.port))
    except socket.error as e:
        print(str(e))

    print('Waiting for a Connection..')
    ServerSocket.listen(5)


    while True:
        Client, address = ServerSocket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))
        start_new_thread(threaded_client, (Client,))
        ThreadCount += 1
        print('Thread Number: ' + str(ThreadCount))


