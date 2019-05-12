import math


def find_perfect_squares(minimum, maximum):
    """
    Return all the perfect squares inclusive of the
    two range ends, assuming A < B, as described in problem
    statement
    :param minimum: lowest end of the range
    :param maximum: highest end of the range
    :return: generator of perfect squares as integers between the limits
    """
    lowest = int(math.ceil(math.sqrt(minimum)))
    highest = int(math.sqrt(maximum))

    if minimum == maximum:
        # Return either min or max given that they are equal
        return [minimum]

    return (n**2 for n in range(lowest, highest + 1))


def find_depth(n):
    """
    :param n: The number to find the max possible depth for
    :return: depth count
    """
    count = 0
    while isinstance(n, int):
        sqrt = math.sqrt(n)
        n = int(sqrt) if sqrt.is_integer() else sqrt
        count += 1 if sqrt.is_integer() else 0
    return count


def solution(A, B):
    count = 0
    for perfect_square in find_perfect_squares(A, B):
        count = max(find_depth(perfect_square), count)
    return count

print(solution(2, 1000000000))
