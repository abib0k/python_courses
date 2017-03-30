import multiprocessing
import threading
from time import sleep

e = multiprocessing.Event()

print('main thread initalized')


def consumer():
    while True:
        e.wait()
        #cur_proc = multiprocessing.current_process()
        print('Cookie was tasty ... (: waiting for more')
        e.clear()


def producer():
    while True:
        sleep(3)
        print("One cookie is ready")
        e.set()


t1 = multiprocessing.Process(target=consumer)
t2 = multiprocessing.Process(target=producer)
t1.start()
t2.start()
