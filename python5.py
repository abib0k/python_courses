import threading
import time

print ('Main thread initialized')


def useless_func():
    print("start sleeping")
    time.sleep(10)
    print("stop sleeping")


thread1 = threading.Thread(target=useless_func())
thread1.start()
print ('Main thread printing')
