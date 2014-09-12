import timeit
strlist = ['it is a long str' for n in range(10000)]
def joinstr():
    return ''.join(strlist)
    
def plusstr():
    result = ''
    for i in strlist:
        result = result + i
    return i

if __name__ == "__main__":
    jointimer = timeit.Timer('joinstr()','from __main__ import joinstr')
    print jointimer.timeit(number = 100)
    plustimer = timeit.Timer('plusstr()','from __main__ import plusstr')
    print plustimer.timeit(number = 100)