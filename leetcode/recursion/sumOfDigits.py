def sumOfDigit(n):
    if n == 0:
        return 0
    return n % 10 + sumOfDigit(int(n / 10))


# Driven code to check above
num = 12345
result = sumOfDigit(num)
print ("Sum of digits in", num, "is", result)