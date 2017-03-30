from abc import ABCMeta, abstractmethod

class Engine(object):

    #@abstractmethod
    def __init__(self, fuel, max_mileage):
        self.fuel = fuel
        self.max_mileage = max_mileage


class Car(object):
    #__metaclass__ = ABCMeta

    def __init__(self,engine):
        self.engine = engine

    @classmethod
    def get_new_diesel(cls):
        return cls(engine=Engine(fuel="diesel", max_mileage=1000))

    @classmethod
    def get_new_petrol(cls):
        return cls(engine=Engine(fuel="petrol", max_mileage=2000))


c = Car.get_new_diesel()

print(type(Car.get_new_diesel()))

