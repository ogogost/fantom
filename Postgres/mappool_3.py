from multiprocessing import Process, Queue
import server_module2 as s # модуль для работы по сети
import PostgreSQL as PS # модуль для работы с БД постгрес
from psycopg2 import Error
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
# import var


def receive_data(q):
	PS.connection = None
	PS.cursor = None
	connection = psycopg2.connect(PS.cs)
	connection.autocommit = False
	connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
	cursor = connection.cursor()
	insertion = ("insert into test2 (cash,user_name) values (%s,%s)")
	while True:
		data = q.get()
		try:
			v1 = data.split(',')
			cursor.execute(insertion, v1)
			print('[Полученные данные] % s' % v1)
		except (Exception, Error) as error:
			print("Error", error)

	# connection.commit()
	cursor.close()
	connection.close()


def server_start(que):
	s.start_server(que)


if __name__ == '__main__':
	queue = Queue()
	p1 = Process(target=receive_data, args=((queue),))
	p1.start()
	p2 = Process(target=server_start, args=((queue),))
	p2.start()
