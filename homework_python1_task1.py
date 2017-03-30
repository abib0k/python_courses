def infinite(*args):

    while True:
        for o in args:
            if isinstance(o, int):
                yield o
            else:
                for l in o:
                    yield l


count = 0
for a in infinite(1,12,"Python"):
    print (a)
    count += 1
    if count == 100:
        raise StopIteration
