def power(num, powerOfnum):
    # If power is 0 then return 1
    # if condition is true
    # only then it will enter it,
    # otherwise not
    if powerOfnum== 0:
        return 1

    # Recurrence relation
    return num * power(num, powerOfnum - 1)

print(power(2, 3))
