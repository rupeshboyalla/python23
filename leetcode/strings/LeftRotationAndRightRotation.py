"""
Given a string of size n, write functions to perform the following operations on a string-

Left (Or anticlockwise) rotate the given string by d elements (where d <= n)

Right (Or clockwise) rotate the given string by d elements (where d <= n).
Examples:

Input : s = "GeeksforGeeks"
        d = 2
Output : Left Rotation  : "eksforGeeksGe"
         Right Rotation : "ksGeeksforGee"


Input : s = "qwertyu"
        d = 2
Output : Left rotation : "ertyuqw"
         Right rotation : "yuqwert"

"""

def leftRotate(str1, n):
    length = len(str1)-1
    start = 0
    while n >= 0:
        str1[start], str1[length] = str1[length], str1[start]
        n -=1
        start += 1
        length -= 1
    return str1
print(leftRotate("GeeksforGeeks", 2))