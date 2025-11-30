#copy numpy as np 
import numpy as np
a = np.array([1,2,3,4])
b = a.copy()
a[0] = 100
print (a)
print(b)

#view (shallow copy)
import numpy as np
a = np.array([1,2,3,4])
b = a.view()
a[0] = 100
print (a)
print(b)

import numpy as np
a = np.array([1, 2, 3])
b = a.copy()

a[0] = 99
print(b)   # no change
