"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


"""

class ValidParentheses:

    def isValid(self, s:str):
        stack = []
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] != '(':
                    return False
            elif char == '}':
                if stack and stack[-1] != '{':
                    return False
            elif char == ']':
                print(stack)
                print(stack[-1] != '[')

                if stack and stack[-1] != '[':
                    return False
            else:
                return False
        return len(stack) == 0

    # this is the best solution works for all cases

    def isValidLeetcode(self, s):
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0


obj = ValidParentheses()
print(obj.isValid("]"))

