import multiprocessing,time

def put_worker(queue): #Queue Producer
    for item in range(50): # Производство 50 раз данные
        time.sleep(1)
        print("[% s] Данные производителя, item =% s" %(multiprocessing.current_process().name,item))
        queue.put("item = %s" % item)

def get_worker(queue):#Queue Consumer
        while True:
            try:
                print("[% s] Данные о потреблении:% s" % (multiprocessing.current_process().name,
                                   queue.get(block=True,timeout=2)))
            except:
                pass
def main():#Основная функция
    queue = multiprocessing.Queue()# Создать очередь задержки процесса
    pool = multiprocessing.Pool(4)
    producer_process = multiprocessing.Process(target=put_worker,name='«Продюсерский процесс»',args=(queue,))
    consumer_process = multiprocessing.Process(target=get_worker,name='«Потребительский процесс»',args=(queue,))
    producer_process.start()
    consumer_process.start()
    producer_process.join()
    consumer_process.join()

if __name__ == '__main__':
    main()