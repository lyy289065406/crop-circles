#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# -----------------------------------------------
# LOGO 绘制
# -----------------------------------------------


from src.bean.archiver import *
from src.env.cfg import *
from src.env.dot_matrix import *


class LocalCanvas :

    def __init__(self, logo, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, backgroup=WHITE, foreground=BLACK) :
        """
        初始化
        :param logo: 期望绘制的 logo 字符串
        :param height: 画布高度
        :param width: 画布宽度
        :param backgroup: 画布背景色
        :param foreground: 画布前景色
        """
        self.height = height
        self.width = width
        self.backgroup = backgroup
        self.foreground = foreground
        self.canvas = self._init()
        self._draw(logo)


    def _init(self) :
        """
        初始化画布
        :return: 空画布
        """
        canvas = [ None ] * self.height
        for h in range(self.height):  
            canvas[h] = [ self.backgroup ] * self.width
        return canvas


    def _draw(self, logo):
        """
        绘制 logo 到画布
        :param logo: 期望绘制的 logo 字符串
        """
        logo_chs = list(logo)
        print(logo_chs)
        offset = 0
        for ch in logo_chs :
            dm = DOT_MATRIX.get(ch)
            for r in range(0, len(dm)) :
                for c in range(0, len(dm[0])) :
                    if dm[r][c] == 1 :
                        self.canvas[r][c + offset] = self.foreground
            offset += len(dm[0])


    def to_str(self) :
        rows = [ '' ]
        for row in self.canvas :
            rows.append(' '.join(row))
        return '\n'.join(rows)


    def __repr__(self):
        return self.to_str()

    
    def __str__(self):
        return self.to_str()




class GithubCanvas :

    def __init__(self) :
        pass
