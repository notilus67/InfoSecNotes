#!/usr/bin/env python3
counter = 100       # integer
miles   = 1000.0    # float, 混合计算标准
name    = "runoob"  # string

a = b = c = 1
a, b, c, d= 20, 5.5, True, 4+3j

print(a, b, c, d)
# 20 5.5 True (4+3j)
print(type(a), type(b), type(c), type(d))
# <class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
print(isinstance(a, int))   # True
print(isinstance(a, float)) # False
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

del a, b, c, d # 删除对象引用
# print(a)

print("2//4=", 2 // 4) # 整除 =0
print("2**5=", 2 ** 5) # 乘方 =32

## List
