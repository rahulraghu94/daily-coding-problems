"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a singly linked list and an integer k, remove the kth last element from
the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.


Asking edge cases:
    - Can k = 0 , i.e., can we be asked to remove the head?
    - Is it okay to add arbitrary attributes to the node class?
    -

"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.tail.prev = self.head
            return val
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def traverse(self):
        cur = self.head
        while cur.next:
            print(cur.val)
            cur = cur.next

    def __iter__(self):
        cur = self.head
        count = 0
        while cur.next:
            count += 1
            cur = cur.next
            yield cur.val

    def __getitem__(self, index):
        cur = self.head
        count = 0
        while cur.next:
            if count == index:
                return cur
            count += 1
            cur = cur.next

    def remove(self, index):
        to_remove = self[index]
        to_remove.prev.next = to_remove.next
        return to_remove

    def traditional_remove(self, index):
        cur = self.head
        count = 0
        while cur.next:
            if count == index:
                cur.prev.next = cur.next
                return cur
            count += 1
            cur = cur.next


list_elem = [1, 2, 3, 4, 5, 6, 7, 8, 9]

linked_list = LinkedList()
for item in list_elem:
    linked_list.add(item)

print(list(linked_list))
print("Removed: {}".format(linked_list.remove(4).val))
print(list(linked_list))

