#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def reduceNum(n):
    print ('{} = '.format(n),end='')
    if not isinstance(n, int) or n <= 0:
        print ('请输入一个正确的数字 !')
        exit(0)
    elif n==1 :
        print ('{}'.format(n))
    else:  # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n = int(n/index) # n 等于 n/index
                if n == 1: 
                    print (index) 
                else : # index 一定是素数
                    print ('{} *'.format(index),end='')
                break
reduceNum(90)
reduceNum(100)