def infinite(*args):

    while True:
        for o in args:
            if isinstance(o, int):
                yield o
            else:
                for l in o:
                    yield l


def limiter(*args):
    count = 0
    while True:
        for gen in args:
            for l in gen:
                print l
                if l == "X" or count == 10:
                    raise StopIteration
                else:
                    count += 1
                    yield l


g1 = infinite(1, "X", 'Python')
g2 = g1
count = 1
for a in limiter(g1):
    print(a)

