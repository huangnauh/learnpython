import multiprocessing

def broken():
    vals = [1,2,3]

    def test(x):
        return x

    pool = multiprocessing.Pool()
    output = pool.map(test, vals)
    print(output)


	
if __name__ == '__main__':
    vals = [1,2,3]

    def test(x):
        return x

    pool = multiprocessing.Pool()
    output = pool.map(test, vals)
    print(output)