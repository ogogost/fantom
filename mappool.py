from multiprocessing import Process
import server_2.py as server

count = 100000

def foo():
	global count
	while count > 0:
		count = count - 1
		print('1')

def doo():
	global count
	while count > 0:
		count = count - 1
		print('0')

def server_2():
	server

if __name__=='__main__':
	p1 = Process(target=foo)
	p1.start()
	p2 = Process(target=server_2())
	p2.start()