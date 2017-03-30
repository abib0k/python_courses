from urllib2 import urlopen
from time import sleep
import threading

sites_data = []
thread_lst = []


def site_reader(url, sites_data):
    response = urlopen(url)
    sites_data.append(response.read(10))
    sleep(3)


sites_to_poll = ['http://www.banana.by', 'http://www.tut.by']
for site in sites_to_poll:
    t = threading.Thread(target=site_reader, args=(site, sites_data))
    thread_lst.append(t)

for thread in thread_lst:
    thread.start()

for thread in thread_lst:
    thread.join()


print(sites_data)
