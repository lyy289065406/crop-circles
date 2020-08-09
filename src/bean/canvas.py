#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# -----------------------------------------------
# LOGO 绘制器
# -----------------------------------------------


import time
from src.bean.archiver import *
from src.env.cfg import *
from src.env.dot_matrix import *


class LocalCanvas :
    '''
    本地画布
    '''

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




class HtmlCanvas :
    '''
    HTML 画布
    '''

    def __init__(self, archiver) :
        self.arch = archiver

    
    def _read_tpl(self) :
        with open(HTML_TPL, 'r') as file :
            tpl = file.read()
        return tpl
    

    def _to_canvas(self) :
        canvas = []
        cnt = 0
        today = self.arch._get_today_progress()
        for key, val in self.arch.dps.items() :
            if today is not None and today.date == key :
                color = '#FF0000'
            elif val.commit <= COMMIT_1 :
                color = '#9be9a8'
            else :
                color = '#216e39'

            canvas.append('<i style="color:%s" class="fa fa-square"></i>' % color)
            cnt += 1
            if cnt == CANVAS_WIDTH :
                cnt = 0
                canvas.append('<br/>')

        return ' '.join(canvas)
                

    def _to_html(self) :
        today = self.arch._get_today_progress()
        tpl = self._read_tpl()
        html = tpl % {
            'datetime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'logo': self.arch.logo,
            'last_commit_date': today.date,
            'commit_cnt': today.cnt,
            'commit_total': today.commit,
            'canvas': self._to_canvas()
        }
        return html

    
    def to_page(self) :
        html = self._to_html()
        with open(HTML_PATH, 'w+') as file :
            file.write(html)

#  <br/> <i class="fa fa-square-o"></i> <i class="fa fa-square-o"></i> <i class="fa fa-square-o"></i>
#  <br/> <i style="color:red" class="fa fa-square-o"></i> <i class="fa fa-square"></i> <i class="fa fa-square-o"></i>
