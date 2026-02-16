import numpy as np

import math

a = np.array([[1, 3], [2, -1]])
b = np.array([[2, 0, -4], [3, -2, 6]])

dotproduct = np.dot(a, b)
# dotproduct1 = np.dot(b, a)
print(a @ b)

print(dotproduct)
# print(dotproduct1)
c = ([[2, 3, -1], [4, -2, 5]])
d = ([[2, -1, 0, 6], [1, 3, -5, 1], [4, 1, -2, 2]])

dotproduct2 = np.dot(c, d)
print(dotproduct2)

#checking are these inverse of each other or not
e = ([[1, 0, 2], [2, -1, 3], [4, 1, 8]])
f = ([[-11, 2, 2], [-4, 0, 1], [6, -1, -1]])
dotproduct3 = np.dot(e, f)
print(dotproduct3)
