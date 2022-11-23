import numpy as np
x = np.array(1)
print(x.ndim) # 0

x = np.array([1, 2, 3])
print(x.ndim) # 1

x = np.array([[1, 2, 3],
              [4, 5, 6]])
print(x.ndim) # 2