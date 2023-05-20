



def gcd(x , y):
    if y == 0:
        return x
    divisor = x % y
    return gcd(y, divisor)

print(gcd(46, 12))