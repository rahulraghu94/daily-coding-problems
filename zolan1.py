# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    """
    Simples solution:
    Find the length (L) of the number as a string and return
    10^(L-1) as the solution.
    Handle edge case where N == 1
    """
    return 0 if N==1 else 10 ** (len(str(N)) - 1)

print(solution(9))
