import multiprocessing

global_data = []

def filler(data):
    data.append(1)

p1 = multiprocessing.Process(target=filler, args=(global_data,))