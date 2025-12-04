#iteratiing means going through element one by one .
#As we deal with multi-dimension array in numpy , we can do this using basic for loop of python
#if we iterate on a 1 d array it will go through each element one by one
import numpy as np
arr = np.array([1,2,3,])
for x in arr:
    print(x)
#outout
#1
#2
#3
#iteratiing 2 d array
import numpy as np
arr = np.array([[1,2,3,],[4,5,6,]])
for  x in arr:
    print(x)
#[1 2 3]
#[4 5 6]

#iterating 3 d array
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    print(x)
    #output
    #[[1 2 3]
 #[4 5 6]]
#[[ 7  8  9]
 #[10 11 12]]   

 #iterate down to the scaler
import numpy as np
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

#iterate through the following 3-d array np.nditer
import numpy as np
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr):
    print(x)