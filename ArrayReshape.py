#Reshaping Array
#Reshaping means changing the shape of an array.The shape of an array is the number of element in each dimension . by reshaping we can add remove dimension or change number of element in each dimension.
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)
#output[[ 1  2  3]
      #[ 4  5  6]
      #[ 7  8  9]
       #[10 11 12]]

#convert the following 1- d array with 12 element into 3 d array
#the outermost dimension will have 2 array that contains 3 array , each with 2 element 
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)
print(newarr)
#output[[[ 1  2]
#  [ 3  4]
 # [ 5  6]]

 #[[ 7  8]
  #[ 9 10]
  #[11 12]]]
