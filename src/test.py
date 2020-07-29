#!/usr/bin/env python
# -*- coding: utf-8 -*-


# from src.letter import *
# FIXME
from letter import *

WHITE = '□'
BLACK = '■'



def to_print(matrix) :
    for i in matrix :
        for j in i :
            print('%s ' % (WHITE if j == 0 else BLACK), end='')
        print()


if __name__ == '__main__' :
    to_print(a)
