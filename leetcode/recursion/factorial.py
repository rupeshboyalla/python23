def factorial(num:int) -> int:
    if num <= 1:
        return 1
    return num * factorial(num-1)

# without recussion

def noRecFactorial(num: int) -> int:
    result = 1
    if num <= 1:
        return result
    for i in range(num):
        result = result * i
    return result


