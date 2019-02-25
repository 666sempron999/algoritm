# -*- coding: utf-8 -*-

import time
import random


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        # print("{} ({}, {}) {} sec".format(method.__name__, args, kw, te-ts))
        print("Exec time of '{}' is".format(method.__name__))
        print("{} sec".format(te - ts))
        print("--------------------------------------------------------------")
        return result

    return timed


@timeit
def random_range_list_creation(numbers):
    return random.sample(range(numbers), numbers)


def r_sum(data):
    if len(data) == 0:
        return 0
    else:
        return data[0] + r_sum(data[1:])


def r_count(data):
    if len(data) == 0:
        return 0
    else:
        return 1 + r_count(data[1:])


def r_find_max(data):
    if len(data) == 0:
        return 0
    else:
        m = r_find_max(data[1:])
        if m > data[0]:
            return m
        else:
            return data[0]


def r_binary_search(ary, elem):
    def recurse(first, last):
        mid = (first + last) // 2 
        if first > last:
            return None
        elif (ary[mid] < elem):
            return recurse(mid + 1, last)
        elif (ary[mid] > elem):
            return recurse(first, mid - 1)
        else:
            return mid 

    return recurse(0, len(ary)-1)


def main():
    a = random_range_list_creation(10)
    so = a[::]
    so.sort()
    print(a)
    summ = r_sum(a)
    print(summ)
    cnt = r_count(a)
    print(cnt)
    mx = r_find_max(a)
    print(mx)

    print(so)
    iof = r_binary_search(so, 8)
    print(r_binary_search(so, 10))


if __name__ == "__main__":
    main()
