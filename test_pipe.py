import multiprocessing


def send_data(conn, data):  # Отправка данных
    conn.send(['test1', 'test2', data])


def receive_data(conn):  # ДАННЫЕ ПОЛУЧИТЬ
    print('[Получить данные] % s' % conn.recv())

def main():
    conn_send, conn_recv = multiprocessing.Pipe()  # трубопровод
    # Создайте два дочерних процесса и одновременно передайте объекты двух конвейеров разным функциям обработки процессов
    process_send = multiprocessing.Process(target=send_data, args=(conn_send, "www.baidu.com"))
    process_receive = multiprocessing.Process(target=receive_data, args=(conn_recv,))
    process_send.start()
    process_receive.start()

if __name__ == '__main__':
    main()