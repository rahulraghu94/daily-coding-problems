
"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

class Node(object):
    '''
    Tree Node
    If the tree rooted at this node is a unival tree, then 'is_unival' == True
    '''
    def __init__(self, val=None, left=None, right=None, is_unival=False):
        self.val = val
        self.left = left
        self.right = right
        self.is_unival = is_unival