"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character. For example, the string "AAAABBBCCDAA" would be encoded as
"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
"""


str_encode = "AAAABBBCCDAA"
str_decode = "4A3B2C1D2A"


def encode(str):
    solution = ""
    prev = 0
    for x in range(0, len(str)):
        if x == (len(str) - 1):
            solution += "{}{}".format(x + 1 - prev, str[x])
            return solution
        elif str[x+1] != str[x]:
            solution += "{}{}".format(x + 1 - prev, str[x])
            prev = x + 1
    return solution


def decode(str):
    solution = ""

    for x in range(0, len(str)):
        if str[x].isdigit():
            solution += str[x + 1] * int(str[x])
            x += 2

    return solution


print("Encoding: {} -----> {}".format(str_encode, encode(str_encode)))
print("Decoding: {} -----> {}".format(str_decode, decode(str_decode)))