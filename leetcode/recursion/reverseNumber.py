


# def reverse(n, r):
#     if n==0:
#         return r
#     else:
#         return reverse(n//10, r*10 + n%10)
#
# # Read number
# number = int(input("Enter number: "))
#
# # Function call
# reversed_number = reverse(number,0)
#
# # Display output
# print("Reverse of %d is %d" %(number, reversed_number))


def reverseNum(num, result):

    if num == 0:
        return result
    else:
        result = result*10 + num%10
        return reverseNum(num//10, result)

print(reverseNum(123, 0))