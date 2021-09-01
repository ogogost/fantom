from multiprocessing import Process, Queue

def do_thing(q):
    data = q.get()  # Get data queued by the parent process
    print(data)

if __name__ == '__main__':
    q = Queue()
    p = Process(target=do_thing, args=(q,))
    p.start()
    while True:
        data = get_data_from_server()
        q.put(data)  # Queue data for a child server