import threading
import multiprocessing


def thread_hello():
    other = threading.Thread(target=thread_say_hello, args=())
    other.start()
    thread_say_hello()


def thread_say_hello():
    print('hello from', threading.current_thread().name)


def process_hello():
    other = multiprocessing.Process(target=process_say_hello, args=())
    other.start()
    process_say_hello()


def process_say_hello():
    print('hello from', multiprocessing.current_process().name)


items = []
flag = []


def consume():
    while not flag:
        pass
    print('items is', items)


def produce():
    consumer = threading.Thread(target=consume, args=())
    consumer.start()
    for i in range(10):
        items.append(i)
    flag.append('go')


produce()
