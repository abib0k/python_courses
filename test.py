
def func(x, y=None):
    y = y or {}
    y[x] = x
    print(y)
    return y

name = "Vasya"
def func_(x = name):
    print(x)
    return x

def not_found(x = name):
    print("Word () cannot be ran", format(x))
    return x
d = {"page": func}

wordlist = ['list', 'page', 'chapter']

for word in wordlist:
    d.get(word, not_found)

l = ["F", 4, {}]
list(filter(lambda x: isinstance(x, int), l)
list(map(0))