from time import time
from multiprocessing import cpu_count, Pool

def factorize(*number):
    
    result = []
    i = 1
    for num in number:
        factor = []
        for i in range(1, num + 1):
            if num % i == 0:
                factor.append(i)
                i += 1
        result.append(factor)
    return result

def factorize_cpu_bound(*number):
    result = []
    i = 1
    for num in number:

        for i in range(1, num + 1):
            if num % i == 0:
                result.append(i)
                i += 1
    
    return result

if __name__ == "__main__":
    start = time()
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    # print(factorize(128, 255, 99999, 10651060))
    print(time() - start)
    start = time()
    with Pool(cpu_count()) as pool:
        a, b, c, d = pool.map(factorize_cpu_bound, (128, 255, 99999, 10651060))
        # print(pool.map(factorize_cpu_bound, (128, 255, 99999, 10651060)))
    print(time() - start)



    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [
        1,
        2,
        4,
        5,
        7,
        10,
        14,
        20,
        28,
        35,
        70,
        140,
        76079,
        152158,
        304316,
        380395,
        532553,
        760790,
        1065106,
        1521580,
        2130212,
        2662765,
        5325530,
        10651060,
    ]
