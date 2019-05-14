"""
This problem was asked by Twitter.
Implement an autocomplete system. That is, given a query string s and a set of
all possible query strings, return all strings in the set that have s as a prefix.
For example, given the query string de and the set of strings [dog, deer, deal],
return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to
speed up queries.


An obviously better way to implelet this would be using a Trie Node tree
Stil a TODO
"""

# Using Tries, like a normal human

_words = ['deer', 'dear', 'dame']


class Node(object):
    def __init__(self, val):
        self.val = val
        self._children = {}
        self.end_of_word = False
        self._word = None

    @property
    def word(self):
        return self._word

    @word.setter
    def word(self, val):
        if self.end_of_word:
            self._word = val

    @property
    def children(self):
        return [x.val for x in self._children.values()]

    @children.setter
    def children(self, node):
        self._children[node.val] = node

    def get_child(self, val):
        return self._children.get(val)


def add_word(root, word):
    _cur = root

    for char in word:
        if char in _cur.children:
            _cur = _cur.get_child(char)
        else:
            new_node = Node(char)
            _cur.children = new_node
            _cur = _cur.get_child(char)
    _cur.end_of_word = True
    _cur.word = word


def _form_all_words(root):
    if root.end_of_word:
        print(root.word)

    for char in root.children:
        _node = root.get_child(char)
        _form_all_words(_node)


def find_all_words(root, prefix):
    _cur = root
    for char in prefix:
        _cur = _cur.get_child(char)

    _form_all_words(_cur)


root = Node("*")

add_word(root, "dear")
add_word(root, "deer")
add_word(root, "dame")

add_word(root, "phone")
# Can it handle word overflows??
add_word(root, "phoneded")
# Yes it can :D
add_word(root, "photo")
add_word(root, "phat")

prefix = "ph"

find_all_words(root, prefix)
