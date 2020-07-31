#!/usr/bin/env python
# -*- coding: utf-8 -*-


# from src.letter import *
# FIXME
from letter import *


CANVAS_WIDTH = 53
CANVAS_HEIGHT = 7
WHITE = '□'
BLACK = '■'

tables = {
    'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'G': G, 'H': H, 'I': I, 'J': J, 
    'K': K, 'L': L, 'M': M, 'N': N, 'O': O, 'P': P, 'Q': Q, 'R': R, 'S': S, 'T': T, 
    'U': U, 'V': V, 'W': W, 'X': X, 'Y': Y, 'Z': Z, '0': zero, '1': one, '2': two, 
    '3': three, '4': four, '5': five, '6': six, '7': seven, '8': eight, '9': night
}


def init_canvas(row=CANVAS_HEIGHT, col=CANVAS_WIDTH, default=WHITE):
    canvas = [ None ] * row
    for r in range(len(canvas)):  
        canvas[r] = [ default ] * col
    return canvas


def to_index(str):
    index = list(str)
    return index


def fill_canvas(canvas, index):
    offset = 0
    for ch in index :
        obj = tables.get(ch)

        for r in range(0, 7) :
            for c in range(0, 7) :
                if obj[r][c] == 1 :
                    canvas[r][c + offset] = BLACK
        offset += 7




def to_print(canvas) :
    for i in canvas :
        for j in i :
            print(j, end=' ')
        print()




if __name__ == '__main__' :
    canvas = init_canvas()
    index = to_index("789")
    fill_canvas(canvas, index)
    to_print(canvas)

