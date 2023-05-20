def isPalindrom(str):
    if len(str) == 0:
        return True
    if str[0] != str[len(str)-1]:
        return False

    return isPalindrom(str[1:-1])
print(isPalindrom("madam"))


# better readability code

def isPalindromeRec(givenStr, start, end):
    # If there is only one character
    if start == end:
        return True
    # If first and last
    # characters do not match
    while not givenStr[start].isalnum():
        start += 1
    while not givenStr[end].isalnum():
        end -= 1
    if givenStr[start] != givenStr[end]:
        return False
    # If there are more than
    # two characters, check if
    # middle substring is also
    # palindrome or not.
    if start < end + 1:
        return isPalindromeRec(givenStr, start + 1, end - 1)

    return True
givenStr = "A man, a plan, a canal: Panama"
givenStr = givenStr.lower()
givenStr = givenStr.strip()
print(isPalindromeRec(givenStr, 0, len(givenStr) - 1))
