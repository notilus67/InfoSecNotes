#!/usr/bin/env python3

import click

@click.command()
@click.option('--name','-n',help='name 参数，非必须，有默认值')
@click.option('--year','-y',help='year 参数',type=int,default=2020,)
@click.option('--msg','-m',help='msg 参数',required=True)

def test_result(year, name, msg):
    print('the year is', year)
    print('the name is', name)
    print('the body is', msg)

if __name__ == '__main__':
    try:
        test_result()
    except Exception as e:
        print(e)