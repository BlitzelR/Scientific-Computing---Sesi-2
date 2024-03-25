# -*- coding: utf-8 -*-
"""2702220100 - Bryan Joy - Numpy.LINALG

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1enmmC_VwcM9hQsQzrlF8CaG_ZD9u4mC2
"""

import numpy as np
A = np.array([[4,3,-5],
              [-2,-4,5],
              [8,8,0]])
y = np.array([2,5,-3])

x = np.linalg.solve(A,y)
print(x)

"""Matrix inversion approach"""

A_inv = np.linalg.inv(A)

x = np.dot(A_inv, y)
print(x)