import numpy as np
import sys as sys
from numpy import pi

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


print(np.arange( 10, 30, 5 ))
#array([10, 15, 20, 25])
print(np.arange( 0, 2, 0.3 ) )              # it accepts float arguments
#array([0. , 0.3, 0.6, 0.9, 1.2, 1.5, 1.8])

np.linspace( 0, 2, 9 )                 # 9 numbers from 0 to 2
#array([0.  , 0.25, 0.5 , 0.75, 1.  , 1.25, 1.5 , 1.75, 2.  ])
x = np.linspace( 0, 2*pi, 100 )        # useful to evaluate function at lots of points
f = np.sin(x)



print(a)

b = np.arange(12).reshape(4,3)           # 2d array
print(b)

c = np.arange(24).reshape(2,3,4)         # 3d array
print(c)

print(np.arange(10000))

print(np.arange(10000).reshape(100,100))

np.set_printoptions(threshold=sys.maxsize)

a = np.array( [20,30,40,50] )
b = np.arange( 4 )
print(b)

c = a-b
print(c)

print(b**2)

print(10*np.sin(a))

print(a<35)


A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0],[3,4]] )
print(A * B)                      # elementwise product

print(A @ B  )                     # matrix product

print(A.dot(B)  )                  # another matrix product


rg = np.random.default_rng(1)     # create instance of default random number generator
print(rg)
a = np.ones((2,3), dtype=int)
print(a)
b = rg.random((2,3))
print(b)
a *= 3
print(a)

b += a
print(b)

#a += b                            # b is not automatically converted to integer type

a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
print(b.dtype.name)

c = a+b
print(c)

print(c.dtype.name)

d = np.exp(c*1j)
d

print(d.dtype.name)

b = np.arange(12).reshape(3,4)
b


b.sum(axis=0)                            # sum of each column


b.min(axis=1)                            # min of each row

