import socket
from _thread import *
import var as v

import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

dn = "postgres"
du = "postgres"
dp = "defender32"
dh = "127.0.0.1"
dbp = "5433"
dt = "table1"

cs = "dbname=%s user=%s password=%s host=%s port=%s" % (dn, du, dp, dh, dbp)


def threaded_client(connection, que_1, que_2):
    connection.send(str.encode('Welcome to the Server! Please, say your name:'))
    name = (connection.recv(2048)).decode('utf-8')
    check_user_name(name)

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
        print(client)
        print(address)
        start_new_thread(threaded_client, ((client), (que_1), (que_2)))
        thread_count += 1
        print('Thread Number: ' + str(thread_count))

def check_user_name(name):
    # connection = None
    # cursor = None
    try:
        connection = psycopg2.connect(cs)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute("SELECT * from test2 where user_name='%s'" % (name))
        print('Your name is:', cursor.fetchone()[2])

    except (Exception, Error) as error:
        print("Error", error)
