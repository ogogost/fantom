# from multiprocessing import Process,Pipe
# from multiprocessing import Process,Pipe
import server_module as s
import multiprocessing
# import var
import PostgreSQL as PS


def foo():
	count = 10
	while count > 0:
		count = count - 1
		print('1')

def post():
	PS.postgres_version()

def receive_data(conn):  # ДАННЫЕ ПОЛУЧИТЬ
	while True:
		print('[Получить данные] % s' % conn.recv())

def server_start():
	s.start_server()

if __name__ == '__main__':
	# conn_send, conn_recv = multiprocessing.Pipe()  # трубопровод

	# p1 = Process(target=post)
	p1 = multiprocessing.Process(target=foo)
	p1.start()
	# p2 = Process(target=server_start)
	p2 = multiprocessing.Process(target=server_start)
	p2.start()
