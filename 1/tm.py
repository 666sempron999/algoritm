# -*- coding: utf-8 -*-

# from datetime import datetime
import time


def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print("{} ({}, {}) {} sec".format(method.__name__, args, kw, te-ts))
        print("--------------------------------------------------------------")
        return result

    return timed


@timeit
def f1():
    time.sleep(2)
    print("f1")


@timeit
def f2(a):
    time.sleep(3)
    print("f2", a)


@timeit
def f3(a, *args, **kw):
    time.sleep(0.5)
    print("f3", args, kw)


def main():
    f1()
    f2(42)
    f3(42, 43, foo=2)


if __name__ == "__main__":
    main()
