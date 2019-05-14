"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be
smaller than or equal to N.
You should be as efficient with time and space as possible.

"""

from uuid import uuid4


class Queue(object):
    def __init__(self, length):
        self.queue_length = length
        self.queue = [None for x in range(self.queue_length)]
        self.index = 0

    def record(self, record):
        self.index = (self.index + 1) % self.queue_length

        self.queue[self.index] = record

    def get_last(self, index):
        return self.queue[index]


record_list = [uuid4() for x in range(20)]
queue = Queue(10)

for x in record_list:
    queue.record(x)

print(queue.get_last(3))
