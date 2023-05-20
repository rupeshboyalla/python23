def recussion():
    count = 0
    recPrint(count)

def recPrint(count: int):
    if count == 3:
        return
    else:
        count += 1
        print(count, end=" ")
        recPrint(count)


recussion()

"""
solve these problems in recursion

1. Print Name 5 times
2. print linearly from 1 to N
3. print from N to 1
4. print linearly from 1 to N (by using backtracking)
5. Print from N to 1 (By using backtracking)

"""

# 1. print name 5 times


def printName(start, numOfTimes):
    if start > numOfTimes:
        return
    else:
        print("rupesh")
        printName(start, numOfTimes)
printName(1, 20)


#2. print linearly from 1 to N

def printNumbers(start, end):
    if start > end:
        return
    else:
        print(start)
        start +=1
        printNumbers(start, end)

printNumbers(1, 100)

#3. print linearly from N to 1

def printNumbersNto1(start, end):
    if start >= end:
        return
    else:
        start += 1
        printNumbers(start, end)
        print(start)

printNumbers(1, 100)

#4. print linearly from 1 to N (by using backtracking)

