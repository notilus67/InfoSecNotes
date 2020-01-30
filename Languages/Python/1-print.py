#!/usr/bin/env python
 
str1='Runoob'
 
print(str1)                 # 输出字符串
print(str1[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str1[0])              # 输出字符串第一个字符
print(str1[2:5])            # 输出从第三个开始到第五个的字符
print(str1[2:])             # 输出从第三个开始后的所有字符
print(str1 * 2)             # 输出字符串两次
print(str1 + '你好')        # 连接字符串
 
print('------------------------------')
 
print('hello\nrunoob')      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

import sys;x='runoob';sys.stdout.write(x+'\n')
input("\n\nPress Enter & Exit")

# 不换行输出
print( 'a', end="" )
print( 'b', end=" " )
print("c")

print ('参数个数为:', len(sys.argv), '个参数。')
print ('参数列表:', str(sys.argv))