"""
Given a number N. Count the number of digits in N which evenly divides N.

Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.


always math.log10 gives you number of digits


"""
import math


# def evenlyDivides(n:int):
#     noOfDigits = int(math.log10(n)) + 1
#     if n % noOfDigits == 0:
#         return noOfDigits
#     else:
#         return 0
# print(evenlyDivides(24))

def countDigits(n:int):
    count = 0
    while n > 0:
        n = n//10
        count +=1
    return count

print(countDigits(12345678))
