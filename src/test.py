#!/usr/bin/env python
# -*- coding: utf-8 -*-

WHITE = '□'
BLACK = '■'

A = [
    [ 0, 0, 0, 0, 0, 0, 0 ] , 
    [ 0, 0, 1, 1, 1, 0, 0 ] , 
    [ 0, 1, 0, 0, 0, 1, 0 ] , 
    [ 0, 1, 0, 0, 0, 1, 0 ] , 
    [ 0, 1, 1, 1, 1, 1, 0 ] , 
    [ 0, 1, 0, 0, 0, 1, 0 ] , 
    [ 0, 0, 0, 0, 0, 0, 0 ]
]


def to_print(matrix) :
    for i in A :
        for j in i :
            print('%s ' % (WHITE if j == 0 else BLACK), end='')
        print()


if __name__ == '__main__' :
    to_print(A)
