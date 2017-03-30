import threading
from time import sleep


class Car(threading.Thread):
    def __init__(self, name, daemonize=False):
        super(Car, self).__init__()
        self.name = name
        self.setDaemon(daemonize)

    def drive(self):
        print("Car {} started".format(self.name))
        sleep(3)
        print("Car {} finished".format(self.name))

    def run(self):
        self.drive()


cars = [Car(_) for _ in range(5)]
for car in cars:
    car.start()
