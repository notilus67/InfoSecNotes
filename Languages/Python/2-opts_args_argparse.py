#!/usr/bin/env python3

import argparse

def test_result(year, name, msg):
    print('the year is', year)
    print('the name is', name)
    print('the body is', msg)

# 更多选项: https://docs.python.org/zh-cn/3/library/argparse.html?highlight=argparse#module-argparse
parser = argparse.ArgumentParser(description='Test for argparse:')
parser.add_argument('--year', '-y', help='year 属性，非必要参数，有默认值', default=2020)
parser.add_argument('--name', '-n', help='name 属性，非必要参数')
parser.add_argument('--msg', '-m', help='m 属性，必要参数', required=True)
args = parser.parse_args()

if __name__ == '__main__':
    try:
        test_result(args.year, args.name, args.msg)
    except Exception as e:
        print(e)