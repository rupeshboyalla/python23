"""




"""

# without recussion

def fib(n: int) -> int:
    num1, num2, result = 1, 0, 0
    if n <= 1:
        return n
    for i in range(n):
        result = num1 + num2
        num1 = num2
        num2 = result
    return result

# using recussion

def fib(N: int) -> int:
    if N <= 1:
        return N
    return fib(N - 1) + fib(N - 2)