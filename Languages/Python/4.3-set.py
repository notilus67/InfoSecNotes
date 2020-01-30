#!/usr/bin/env python3

# 基本功能是进行成员关系测试和删除重复元素。
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if 'Rose' in student :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
 
# 创建空集合用set() {}用于创建新字典(dictionary)
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
 
print(a - b)     # a 和 b 的差集
 
print(a | b)     # a 和 b 的并集
 
print(a & b)     # a 和 b 的交集
 
print(a ^ b)     # a 和 b 中不同时存在的元素