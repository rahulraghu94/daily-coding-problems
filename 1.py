"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

arr = [10, 15, 3, 7]
sumation = 17

def find_pair(arr, sum):
    store = set()

    for i in range(0, len(arr)):
        temp_diff = sum - arr[i]

        if (temp_diff >= 0 and temp_diff in store):
            print("Pair = {} and {}".format(arr[i], temp_diff))
        store.add(arr[i])


find_pair(arr, sumation)