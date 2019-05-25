"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a string of round, curly, and square open and closing brackets,
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.


Solution:

Maintain a stack that can hendle the basics such as adding, popping, checking
if empty etc.

For each character in the sequence, check if the opposite back reference to
that character exists in the stack, in which case we pop it, else, we continue
adding

At the end, if the sequence was right, we will be left with an empty stack.

"""


relation = {
    "{": "}",
    "[": "]",
    "(": ")"
}
back_relation = {
    "}": "{",
    "]": "[",
    ")": "("
}


class Stack(object):
    def __init__(self):
        self._stack = []
        self.top = -1

    def add(self, elem):
        self._stack.append(elem)
        self.top += 1

    def pop(self):
        elem = self._stack[self.top]
        del self._stack[self.top]
        self.top -= 1
        return elem

    def at_top(self):
        if not self._stack:
            return None
        return self._stack[self.top]

    def is_empty(self):
        return True if not self._stack else False


def check_sequence(to_parse):
    stack = Stack()
    for elem in to_parse:
        if elem in relation.keys():
            stack.add(elem)
        else:
            if stack.at_top() == back_relation[elem]:
                stack.pop()

    return stack.is_empty()


print(check_sequence("([])[](({}))"))

