def solution(A, B, K):
    # write your code in Python 2.7
    x = xrange(A, B)
    y = filter(lambda a: a % K == 0, x)
    return len(y)
