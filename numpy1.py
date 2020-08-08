import numpy as np
a = np.arange(15).reshape(3, 5)
a
#array([[ 0,  1,  2,  3,  4],   [ 5,  6,  7,  8,  9],     [10, 11, 12, 13, 14]])
a.shape
#(3, 5)
a.ndim
#2
a.dtype.name
#'int64'
a.itemsize
#8
a.size
#15
type(a)
#<class 'numpy.ndarray'>
b = np.array([6, 7, 8])
b
#array([6, 7, 8])
type(b)
#<class 'numpy.ndarray'>

a = np.array([2,3,4])
a
#array([2, 3, 4])
a.dtype
#dtype('int64')
b = np.array([1.2, 3.5, 5.1])
b.dtype
#dtype('float64')


np.zeros((3, 4))
np.ones( (2,3,4), dtype=np.int16 )                # dtype can also be specified
np.empty( (2,3) )                                 # uninitialized
