# -*- coding: utf-8 -*-

# from datetime import datetime
import time


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        # print("{} ({}, {}) {} sec".format(method.__name__, args, kw, te-ts))
        print("Exec time of {}".format(method.__name__))
        print("{} sec".format(te - ts))
        print("--------------------------------------------------------------")
        return result

    return timed


@timeit
def binary_search(sList, item):
    low = 0
    high = len(sList) - 1
    while low < high:
        mid = low + high
        guess = sList[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


@timeit
def line_search(sList, item):
    index = 0
    listLen = len(sList)

    while sList[index] != item:
        index += 1
        if index == listLen:
            return None

    return index


@timeit
def range_list_creation(numbers):
    return list(range(1, numbers))


def main():
    a = range_list_creation(1000000000)
    first = (binary_search(a, 99999999))
    second = (line_search(a, 99999999))


if __name__ == "__main__":
    main()
