#array.shape python
import numpy as np
arr = np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)#output((2, 4))

#create an array with dimension using ndmin using a vector with value 1,2,3,4 and verify that dimension has value 4
import numpy as np
arr = np.array([1,2,3,4],ndmin=5)
print(arr.shape) #output [(1, 1, 1, 1, 4)]
