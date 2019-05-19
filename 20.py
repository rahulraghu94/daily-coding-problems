"""
'''
This problem was asked by Google.
Given two singly linked lists that intersect at some point, find the
intersecting node.
The lists are non-cyclical.

For example, given A = 1 - > 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10,
return the node with value 8.

In this example, assume nodes with the same value are the exact same node
objects. Do this in O(M + N) time (where M and N are the lengths of the lists)
and constant space.
'''
"""

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class List(object):
    def __init__(self):
        self.head = None

    def insert(self, data):
        if self.head is None:
            self.create_head(data)
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = Node(data)

    def create_head(self, data):
        newNod = Node(data)
        if self.head:
            newNod.next = self.head
        self.head = newNod

    def at_index(self, index):
        count = 0

        # if index == 0:
        #     return self.head

        cur = self.head
        while cur.next:
            count += 1
            cur = cur.next

            if count == index:
                break
        return cur

    @property
    def _list(self):
        tamp = self.head
        while tamp is not None:
            print(tamp.data)
            tamp = tamp.next

    @property
    def _len(self):
        count = 0
        cur = self.head
        while cur.next:
            count += 1
            cur = cur.next
        return count


def add_elements(values):
    _list = List()
    for item in values:
        _list.insert(item)
    return _list


a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [6, 7, 8]

A = add_elements(a)
B = add_elements(b)


"""
Find the difference in length of the two linked lists
We will start traversing the smaller list from the head and the larger list 
from the diff-th element.

Find the starting node (called a_cur and b_cur) from which to start the 
traversal
"""
a_length = A._len
b_length = B._len

diff = abs(a_length - b_length)

a_cur = A.head
b_cur = B.head
if a_length > b_length:
    a_cur = A.at_index(diff)
else:
    b_cur = B.at_index(diff)


"""
Once we've found the correct ndoes to start from, we can start the traversals 
and break once we hit a common element.
Additionally, we can maintain a flag and traverse through the rest of the 
list to ensure that the future elements match
"""

while a_cur.next and b_cur.next:
    if a_cur.data == b_cur.data:

        print(a_cur.data)
        break
    a_cur = a_cur.next
    b_cur = b_cur.next