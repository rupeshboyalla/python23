"""
Given a number N. Count the number of digits in N which evenly divides N.

Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.


always math.log10 gives you number of digits


"""
import math


def evenlyDivides(n:int):
    noOfDigits = int(math.log10(n)) + 1
    if n % noOfDigits == 0:
        return noOfDigits
    else:
        return 0
print(evenlyDivides(24))