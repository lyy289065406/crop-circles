#!/usr/bin/env python
# -*- coding: utf-8 -*-


# from src.letter import *
# FIXME
from letter import *


CANVAS_WIDTH = 53
CANVAS_HEIGHT = 7
WHITE = '□'
BLACK = '■'


def init_canvas(row=CANVAS_HEIGHT, col=CANVAS_WIDTH, default=WHITE):
    canvas = [ None ] * row
    for r in range(len(canvas)):  
        canvas[r] = [ default ] * col
    return canvas


def to_index(str):
    index = list(str)

def to_matrix(index):
    pass


def to_print(canvas) :
    for i in canvas :
        for j in i :
            print(j, end=' ')
        print()




if __name__ == '__main__' :
    canvas = init_canvas()
    to_print(canvas)

