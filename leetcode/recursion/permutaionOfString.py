def permute(s, answer):
    if len(s) == 0:
        print(answer, end="  ")
        return

    for i in range(len(s)):
        ch = s[i]
        leftSubstr = s[0:i]
        rightSubstr = s[i + 1:]
        rest = leftSubstr + rightSubstr
        permute(rest, answer + ch)
result = ""
permute("abc", result)



