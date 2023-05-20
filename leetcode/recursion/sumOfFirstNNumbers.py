
# 2 ways we can do this problem 1. Using parameterized and using functional

# parameterized way

def sumOfNNumbers(n, sum):
    if n < 1:
        print(sum)
        return
    sum = sum + n
    n -= 1
    sumOfNNumbers(n, sum)


sumOfNNumbers(100, 0)


# functional

def sumOfNNumberFunctional(n):
    if n == 0:
        return 0
    return n + sumOfNNumberFunctional(n-1)
print(sumOfNNumberFunctional(3))