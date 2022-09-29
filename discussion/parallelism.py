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
