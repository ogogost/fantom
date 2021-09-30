import socket

ClientSocket = socket.socket()
host = '194.87.144.25'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

print((ClientSocket.recv(1024).decode('utf-8')))
ClientSocket.send(str.encode(input('Input name:')))

while True:
    Input = input('Say Something: ')
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))
