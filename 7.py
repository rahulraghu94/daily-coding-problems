"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not
allowed.

"""

"""
1119

1 1 1 9
11 1 9
1 11 9
1 1 19
11 19
"""


def decode(code):
    if len(code) <= 1:
        return 1

    if len(code) >= 2:
        if 1 <= int(''.join(code[0:2])) <= 26:
            return (
                decode(code[1:]) + decode(code[2:])
              )
    return decode(code[1:])


if __name__ == '__main__':
    code = '1119'
    print(decode(list(code)))
