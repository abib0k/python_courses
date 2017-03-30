class Animal(object):
    def __init__(self):
        self.body = True
    def breathe(self):
        print("I am {} and I breathe". format(self.__class__.__name__))

class Mammals(Animal):
    def __init__(self, legs=4):
        self.legs = legs

class Fish(Animal):
    def __init__(self, legs=0):
        self.legs = legs

class Dog(Mammals):
    def __init__(self):
        self.tail = True

class Penguin(Mammals, Fish):
    def __init__(self):
        self.tail =True

class Cat(Animal, Penguin):
    def __init__(self):
        self.tail = True
        super(Cat, self).__init__()
        Penguin.__init__(self)

barky = Penguin()
print(type(barky).mro())
#barky.breathe()
#Mammals().breathe()
print(Penguin.mro())
cl = type("Cat", (object,), {name: "TOMAS"})
cat = cl()
print(barky.__dict__)


