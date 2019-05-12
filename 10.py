"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and
an integer n, and calls f after n milliseconds.


Notes:

    This is a very simplistic sceduler that can take just one job at a time.
    Ideally, you'd want a scheduler that can accept multiple jobs at varying
    times.

    In order to do this, we'll need to maintain an optimal data structure to
    house all these jobs.
    One would think of heaps or priorety queues for the same.

    A PQ with a time stamp would bubble up the tree if it's to be executed
    sooner than other methods.

    The problem at hand now becomes on how we poll this queue in a timely way
    so as to not miss times, etc.

"""

from contextlib import ExitStack
from functools import partial
import time


def _schedule(func, delay):
    time.sleep(delay / 1000)
    func()


def schedule(func, delay):
    with ExitStack() as stack:
        stack.callback(partial(_schedule, func, delay))
        print(
            "Scheduling {} to run after {} milliseconds!"
            "".format(func, delay)
        )


def do_something():
    print("Here I am, doing something!!!")


if __name__ == '__main__':
    schedule(do_something, 10000)
