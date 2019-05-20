"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement locking in a binary tree. A binary tree node can be locked or
unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

- is_locked, which returns whether the node is locked

- lock, which attempts to lock the node. If it cannot be locked, then it should
return false. Otherwise, it should lock it and return true.

- unlock, which unlocks the node. If it cannot be unlocked, then it should return
false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would
like. You may assume the class is used in a single-threaded program, so there
is no need for actual locks or mutexes. Each method should run in O(h), where h
is the height of the tree.
"""


class Node(object):
    def __init__(self, val, locked=False):
        self.val = val
        self.right = None
        self.left = None
        self._lock = locked
        self._operable = True

    def _check_lock(self, root):
        """
        :param root: root of the tree/subtree to traverse from
        :return: True if all it's children are unlocked, else False
        """

        def _inorder_lockable(node):
            if node._lock:
                self._operable = False
                return

            if node.right:
                _inorder_lockable(node.right)
            if node.left:
                _inorder_lockable(node.left)

        _inorder_lockable(root.right)
        _inorder_lockable(root.left)
        return self._operable

    def _locked(self):
        return self._lock

    def unlock(self):
        if self._check_lock(root) and root._lock == True:
            root._lock = False
            return True
        return False

    def lock(self):
        if self._check_lock(root) and root._lock == False:
            root._lock = True
            return True
        return False


def create_tree():
    root = Node(0, False)
    root.left = (
        Node(1, False)
    )
    root.right = (
        Node(2, True)
    )

    return root


if __name__ == '__main__':
    root = create_tree()

    print(root._locked())
    print(root.lock())
    print(root.unlock())