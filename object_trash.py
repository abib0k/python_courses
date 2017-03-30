class Cat(object):
    pass


cat = Cat()
cat.legs = 4
print(cat.legs)


class Cookoo(object):
    def __init__(self):
        self.life_remain = 100

    def __getattribute__(self, item):
        print("Asked for " + item)


cookoo = Cookoo()
print(cookoo.life_remain)
print(dir(cookoo.life_remain))


