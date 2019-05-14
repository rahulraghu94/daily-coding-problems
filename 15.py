"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a stream of elements too large to store in memory, pick a random element
from the stream with uniform probability.

"""

import random


def randomize(stream):
    rand_elem = None

    for i in range(0, len(stream)):
        if i == 0:
            rand_elem = stream[i]

        elif random.randint(1, i+1) == 0:
            rand_elem = stream[i]

    return rand_elem


_stream = [random.randint(0, 1000000) for x in range(1000000)]

print(randomize(_stream))


