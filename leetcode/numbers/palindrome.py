"""
Given an integer, check whether it is a palindrome or not.

555 ---> true
121 ---> true
120 ---> false

"""


def isGivenNumPalindrom(n:int):
    result = 0
    temp = n
    while temp > 0:
        result = result*10 + temp%10
        temp = temp//10
    return  n==result
print(isGivenNumPalindrom(555))
