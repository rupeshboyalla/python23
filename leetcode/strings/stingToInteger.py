"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


"""


def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    isNegative = False
    for char in s:
        if char == '-':
            isNegative = True
            continue
        elif char.isalpha():
            return 0
        elif char.isnumeric():
            result = result * 10 + int(char)
    if isNegative:
        result = 0-result
    return result

# from leetcode

def myAtoi(s):
    def myAtoi(self, s):
        MIN, MAX = -2 ** 31, 2 ** 31 - 1
        n, empty, sign = 0, True, 1  # empty denotes we have not seen any number, sign is -1 or 1
        for c in s:
            if empty:
                if c == ' ':
                    continue  # ignore the leading whitespace
                elif c == '-':
                    sign = -1  # final answer is a negative number
                elif c.isdigit():
                    n = int(c)  # the first digit of number
                elif c != '+':
                    return 0  # the first char is not a digit and not in (' ', '+', '-'), so s is invalid
                empty = False  # the first char is a digit or '+' or '-', valid number starts
            else:
                if c.isdigit():
                    n = n * 10 + int(c)
                    if sign * n > MAX:
                        return MAX
                    elif sign * n < MIN:
                        return MIN
                else:
                    break  # end of valid number
        return sign * n  # sign is 1 or -1 

print(myAtoi("-42"))