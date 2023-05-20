def cumulative(num):
    if num in [0, 1]:
        return num
    else:
        return num + cumulative(num-1)

print(cumulative(10))