
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 13:43:36 2025
@author: hyytijuh & Copilot
Examples of propper vectors in Python
"""

# Setup 
# If NumPy / pandas are not installed in your environment:
# pip install numpy pandas

#  NumPy: Proper vectors with shapes and math

import numpy as np

# 1D array: shape (3,)
v = np.array([1, 2, 3])
print("v:", v, "shape:", v.shape)  # (3,)

# Explicit ROW vector: shape (1, 3)
row = np.array([[1, 2, 3]])
print("row:", row, "shape:", row.shape)

# Explicit COLUMN vector: shape (3, 1)
col = np.array([[1],
                [2],
                [3]])
print

# Transpose

v = np.array([1, 2, 3])     # shape (3,)
row = v.reshape(1, -1)      # (1, 3) → row vector
col = v.reshape(-1, 1)      # (3, 1) → column vector

print("row shape:", row.shape)   # (1, 3)
print("col shape:", col.shape)   # (3, 1)

# Transpose:
print("row.T shape:", row.T.shape)  # (3, 1)
print("col.T shape:", col.T.shape)  # (1, 3)

# Note: Transposing a 1D array does nothing to shape:
print("v.T shape:", v.T.shape)      # still (

# Concise constructors

# Row vector directly:
row2 = np.atleast_2d([10, 20, 30])       # (1, 3)

# Column vector directly:
col2 = np.atleast_2d([10, 20, 30]).T     #

# Arithmetic & broadcasting (mini manual)

# Elementwise operations
v = np.array([1, 2, 3])
print(v + 5)         # [6 7 8]
print(v * 2)         # [2 4 6]

# Broadcasting with row/column
row = np.array([[1, 2, 3]])     # (1, 3)
col = np.array([[10], [20], [30]])  # (3, 1)

# Produces a 3x3 matrix by broadcasting: (3,1) + (1,3) -> (3,3)
M = col + row
print("M:\n", M)
# M =
# [[11 12 13# [[11 12 13]
#  [21 22 23]

# Dot products & matrix multiplication

# Dot product (vector • vector)
a = np.array([1, 2, 3])   # (3,)
b = np.array([4, 5, 6])   # (3,)
dot1 = np.dot(a, b)       # 1*4 + 2*5 + 3*6 = 32
print("dot1:", dot1)

# Using explicit row/column shapes:
row = a.reshape(1, -1)    # (1,3)
col = b.reshape(-1, 1)    # (3,1)

# Matrix multiply: (1,3) @ (3,1) -> (1,1)
dot2 = row @ col
print("dot2:", dot2)      # [[32]]

# Outer product: (3,1) @ (1,3) -> (3,3)
outer = a.reshape(-1, 1) @ b.reshape(1, -1)
print("outer:\n", outer)
# [[ 4  5  6]
#  [ #  [ 8 10 12]

# Horizontal vs vertical stacking

x = np.array([1, 2, 3])       # (3,)
y = np.array([4, 5, 6])       # (3,)

# Stack as rows -> 2x3
H = np.vstack([x, y])
print("H:\n", H, "shape:", H.shape)

# Stack as columns -> 3x2
V = np.column_stack([x, y])
print("V:\n", V, "shape:", V.shape)

# Or ensure shapes explicitly:
row_x = x.reshape(1, -1)              # (1,3)
row_y = y.reshape(1, -1)              # (1,3)
H2 = np.concatenate([row_x, row_y], axis=0)
print("H2:\n", H2)

col_x = x.reshape(-1, 1)              # (3,1)
col_y = y.reshape(-1, 1)              # (3,1)
V2 = np.concatenate([col_x, col_y], axis=1)
print("V2:\n", V2)

# pandas Series/DataFrame (brief)

import pandas as pd

# Series: 1D labeled vector
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
print("Series:\n", s)

# Row-like (1 row, 3 columns) DataFrame
df_row = pd.DataFrame([[1, 2, 3]], columns=["x", "y", "z"])
print("df_row shape:", df_row.shape)   # (1,3)

# Column-like (3 rows, 1 column) DataFrame
df_col = pd.DataFrame({"x": [1, 2, 3]})
print("df_col shape:", df_col.shape)   # (3,1)

# Convert to NumPy when you need math:
row_np = df_row.to_numpy()   # (row_np = df_row.to_numpy()   # (1,3)

# Common pitfalls & quick checks

import numpy as np

v = np.array([1, 2, 3])

# Pitfall: v.T is STILL (3,) and looks unchanged.
print("v.T shape:", v.T.shape)  # (3,)

# Always check shape when you need row/column behavior:
row = v.reshape(1, -1)  # (1,3)
col = v.reshape(-1, 1)  # (3,1)

# Another pitfall: Mixing Python lists with NumPy arrays in arithmetic
# is okay if the list auto-converts, but be mindful:
print(np.array([1,2,3]) + [4,5,6])  # [5 7 9]  (list is coer