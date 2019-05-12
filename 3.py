"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string back
into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


node = Node('root', Node('left', Node('left.left')), Node('right'))
# node = Node('root', Node('left'), Node('right'))


def serialize(root, st):
    node = root

    if node is None:
        return

    if node.left is not None:
        st = serialize(node.left, st)
    if node.right is not None:
        st = serialize(node.right, st)

    st = "{}:{}".format(st, node.val)

    return st


def deserialize(str):



print(serialize(node, ''))

