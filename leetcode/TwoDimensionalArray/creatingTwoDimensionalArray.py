import numpy as np
import numpy as numpy

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
print(twoDArray)

# inserting an element in a two dimensional array we can't insert a single element in an array we have to either insert either row or column
# two ways we can insert in a two dimensional array adding row or adding column

# adding column

newTwoArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=1) # axis field 0 for row and 1 for column
print(newTwoArray)

# adding row

newTwoArray = np.insert(twoDArray, 0, [[1, 2, 3, 4]], axis=0)
print(newTwoArray)

# adding in a 2nd row
newTwoArray = np.insert(twoDArray, 1, [[1, 2, 3, 4]], axis=0)
print(newTwoArray)

#append will add row at the end

newTwoArray = np.append(twoDArray, [[1, 2, 3, 4]], axis=0)
print(newTwoArray)

# access an element in a twodimensional array

def accessElements(array, rowIndex, columIndex):
