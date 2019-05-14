"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

There exists a staircase with N steps, and you can climb up either 1 or 2
steps at a time. Given N, write a function that returns the number of unique
ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could
climb any number from a set of positive integers X? For example,
if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""


# solution 1 where number of steps possible is just 1 or two

def solution(n):
    if n <= 1:
        return 1

    return solution(n - 1) + solution(n - 2)

print(solution(4))


# Solving the same thing dynamically, cause why not

def solution_dyn(n):
    a, b, = 1, 2

    for i in range(n - 1):
        a, b, = b, a + b

    return a

print(solution_dyn(4))


# solve for if X equals anything

def solution(n, X):
    # restrinc x to be a list

    cache = [0 for x in range(n + 1)]
    cache[0] = 1

    for x in range(n + 1):
        cache[x] = cache[x] + sum(cache[x - i] for i in X if x - i > 0)
        cache[x] += 1 if x in X else 0

    return cache[-1]

print(solution(4, [1, 2]))