import threading
from time import sleep

print('main thread initalized')


def printer(*args, **kwargs):
    print('Thread started')


t1 = threading.Thread(target=printer, args=(1,), kwargs={'2': 3})
t1.start()
t2 = threading.Thread(target=printer, args=(2,), kwargs={'4': 5})
t2.start()

