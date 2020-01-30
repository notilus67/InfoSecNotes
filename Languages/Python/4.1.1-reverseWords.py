#!/usr/bin/env python3

def reverseSentence(input):
    inputWords = list(input)    # str不用split就能一个一个字符转换为list
    inputWords = inputWords[-1::-1]
    output = ''.join(inputWords)
    return output

def reverseWords(input):
    inputWords = input.split(' ')
    inputWords = inputWords[-1::-1]
    output = ' '.join(inputWords)
    return output

if __name__ == "__main__":
    input = 'I like runoob'
    print(reverseWords(input))
    print(reverseSentence(input))