#!/usr/bin/env python
# coding:utf-8

import numpy as np


print '--------------------------------------------------------------------------------'
a1 = np.array(range(10))
print type(a1)
print a1
print a1.dtype
print a1.shape
# <type 'numpy.ndarray'>
# [0 1 2 3 4 5 6 7 8 9]
# int64
# (10,)
print '--------------------------------------------------------------------------------'
a2 = np.array([range(10), range(10)])
print type(a2)
print a2
print a2.dtype
print a2.shape
# <type 'numpy.ndarray'>
# [[0 1 2 3 4 5 6 7 8 9]
#  [0 1 2 3 4 5 6 7 8 9]]
# int64
# (2, 10)
print '--------------------------------------------------------------------------------'
"""
可以通过修改数组的shape属性，在保持数组元素个数不变的情况下，改变数组每个轴的长度。
(并不是对数组进行转置，而只是改变每个轴的大小，数组元素在内存中的位置并没有改变)
"""
a2.shape = 5, 4
print a2
print a2.dtype
print a2.shape
# [[0 1 2 3]
#  [4 5 6 7]
#  [8 9 0 1]
#  [2 3 4 5]
#  [6 7 8 9]]
# int64
# (5, 4)
"""
当某个轴的元素为-1时，将根据数组元素的个数自动计算此轴的长度。
"""
a2.shape = 4, -1
print a2
print a2.dtype
print a2.shape
# [[0 1 2 3 4]
#  [5 6 7 8 9]
#  [0 1 2 3 4]
#  [5 6 7 8 9]]
# int64
# (4, 5)
print '--------------------------------------------------------------------------------'
"""
使用数组的reshape方法，可以创建一个改变了尺寸的新数组，原数组的shape保持不变。
"""
a3 = a2.reshape((20, 1))
print a3
print a2
"""
原数组和新数组，其实共享数据存储内存区域，因此修改其中任意一个数组的元素都会同时修改另外一个数组的内容。
"""
a3[0] = 100
print a3
print a2
print '--------------------------------------------------------------------------------'
print '--------------------------------------------------------------------------------'

