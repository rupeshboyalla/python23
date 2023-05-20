from array import *

# 1. create an array and traverse

myArray = array('i', [1,2,3,4,5]) # i is integer

for i in myArray:
    print(i)

# 2. access individal elements through index

print(myArray[0])

# 3 . append any value in an array using append() method

# by using append method we can add an element at the end of an array

myArray.append(9)

print(myArray)

#4 insert value in an array uising insert() method

myArray.insert(0, 11)
print(myArray)

#5. extend python array using extend() method

myArray1 = [10, 11, 12, 13]
myArray.extend(myArray1)
print(myArray)
#6. add items