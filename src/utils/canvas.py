#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# -----------------------------------------------
# LOGO 绘制
# -----------------------------------------------

WHITE = '□'
BLACK = '■'


class LocalCanvas :

    def __init__(self, height, width, backgroup=WHITE, foreground=BLACK) :
        self.height = height
        self.width = width
        self.backgroup = backgroup
        self.foreground = foreground
        self.canvas = self.init_canvas()


    def init_canvas(self) :
        canvas = [ None ] * self.height
        for h in range(self.height):  
            canvas[h] = [ self.backgroup ] * self.width
        return canvas


    def draw_canvas(self, logo_chs, dot_matrix):
        offset = 0
        for ch in logo_chs :
            dm = dot_matrix.get(ch)
            for r in range(0, len(dm)) :
                for c in range(0, len(dm[0])) :
                    if dm[r][c] == 1 :
                        self.canvas[r][c + offset] = self.foreground
            offset += len(dm[0])
    

    def canvas_to_str(self) :
        rows = [ '' ]
        for row in self.canvas :
            rows.append(' '.join(row))
        return '\n'.join(rows)



class GithubCanvas :

    def __init__(self) :
        pass
