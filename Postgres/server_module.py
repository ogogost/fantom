import socket
from _thread import *
import var as v
from multiprocessing import Queue


def threaded_client(connection):
    connection.send(str.encode('Welcome to the Server'))
    while True:
        q = Queue()
        data = connection.recv(2048)
        if data.decode('utf-8') == '0':
            break
        q.put(data.decode('utf-8'))
        reply = "Server Says: " + data.decode('utf-8')
        v.list_of_var.append(data.decode('utf-8'))
        print(v.list_of_var)
        connection.sendall(str.encode(reply))
    connection.close()
    print('connection closed')
    print('Waiting for a Connection..')


def start_server():

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
        start_new_thread(threaded_client, (client,))
        thread_count += 1
        print('Thread Number: ' + str(thread_count))
