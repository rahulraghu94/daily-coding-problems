"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Given an integer k and a string s, find the length of the longest substring
that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct
characters is "bcb".
"""

string = "abcbcbcbcbca"
k = 2
max_count = 0


def if_uniq(str, k):
    if len(set(str)) > k:
        return False, 0
    else:
        return True, len(str)


for i in range(0, len(string)):
    for j in range(i, len(string)):
        is_uniq, length = if_uniq(string[i:j], k)
        max_count = max(max_count, length)


print(max_count)

