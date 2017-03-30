"""
BOO

"""
__all__ = ['modules_func', 'modules_name']


def modules_func():
    print()


modules_name = "A"


def say_bye(self):
    print("Say bye" + self.name)


class Cat():
    def __init__(self, name):
        self.name = name
        print(id(self))

    def say_hi(self):
        print("Hi, my name is" + self.name)


tom = Cat(name="Thomas")
print(dir(tom))
Cat.say_by = say_bye
tom.say_by()
tom.say_hi()
