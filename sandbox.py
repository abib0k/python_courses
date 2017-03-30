class A(object):
    def __init__(self, x=0):
        self.__mileage = x

    @property
    def mileage(self):
        return self.__mileage

    @mileage.setter
    def mileage(self, value):
        self.__mileage += value


a = A()
print a.mileage
a.mileage = 2
print a.mileage
a._A__mileage = 7
print a.mileage
a.mileage(1)
