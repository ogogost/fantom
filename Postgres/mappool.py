from multiprocessing import Process
import server_module as s
import var
import PostgreSQL as PS


def foo():
	count = 10
	while count > 0:
		count = count - 1
		print('1')

def post():
	PS.postgres_version()

def server_start():
	s.start_server()

if __name__ == '__main__':
	p1 = Process(target=post)
	p1.start()
	p2 = Process(target=server_start)
	p2.start()
