# from multiprocessing import Process,Pipe
# from multiprocessing import Process,Pipe
import server_module as s
# import multiprocessing
from multiprocessing import Process, Queue

import var as v
# import PostgreSQL as PS


def receive_data(q):  # ДАННЫЕ ПОЛУЧИТЬ
	data = q.get()
	while True:
		print('[Полученные данные] % s' % data)

def server_start():
	s.start_server()

if __name__ == '__main__':
	q = Queue()
	# p1 = Process(target=post)
	p1 = Process(target=receive_data, args=(q,))
	p1.start()
	# p2 = Process(target=server_start)
	# p2 = multiprocessing.Process(target=server_start)
	# p2.start()
	while True:
		server_start()
		dann_ = v.list_of_var
		q.put(dann_)
