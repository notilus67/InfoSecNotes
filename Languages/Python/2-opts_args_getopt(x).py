#!/usr/bin/env python
# @Date
#python3 2-opts_args.py -i input -o output arg1 arg2

import sys, getopt

def main(argv):
   inputfile = ''
   outputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
      #args是非-或--的参数列表
      for arg in args:
         print('无option参数:', arg)
   except getopt.GetoptError:
      print ('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2) 
      '''
      0 ：成功结束
      1 ：通用错误　　
      2 ：误用Shell命令
      '''
   for opt, arg in opts:
      if opt == '-h':
         print ('usage: test.py -i <inputfile> -o <outputfile> <arg1> <arg2>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print ('输入的文件为:', inputfile)
   print ('输出的文件为:', outputfile)

if __name__ == "__main__":
   #argv[0] 是文件名
   p = 0
   for allArg in sys.argv:
      print ('sys.argv['+str(p)+']:', allArg)
      p = p + 1
   main(sys.argv[1:])