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


def findSmaller(arr):
    smaller = arr[0]
    smallerIndex = 0
    for i in range(1, len(arr)):
        if arr[i] < smaller:
            smaller = arr[i]
            smallerIndex = i

    return smallerIndex


@timeit
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smaller = findSmaller(arr)
        newArr.append(arr.pop(smaller))

    return newArr


@timeit
def random_range_list_creation(numbers):
    return random.sample(range(numbers), numbers)


def main():
    a = random_range_list_creation(20000)
    # print(a)
    sortA = selectionSort(a)
    # print("---------------------------------------------")
    # print(sortA)


if __name__ == "__main__":
    main()
