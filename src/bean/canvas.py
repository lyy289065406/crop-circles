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


class Canvas :
    '''
    画布
    '''

    def __init__(self, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, backgroup=WHITE, foreground=BLACK) :
        """
        初始化
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


    def _init(self) :
        """
        初始化画布
        :return: 空画布
        """
        canvas = [ None ] * self.height
        for h in range(self.height) :  
            canvas[h] = [ self.backgroup ] * self.width
        return canvas




class LocalCanvas(Canvas) :
    '''
    本地画布
    '''

    def __init__(self, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, backgroup=WHITE, foreground=BLACK) :
        Canvas.__init__(self, height, width, backgroup, foreground)


    def draw(self, logo):
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




class HtmlCanvas(Canvas) :
    '''
    HTML 画布
    '''

    def __init__(self, archiver, height=CANVAS_HEIGHT, width=CANVAS_WIDTH, backgroup=WHITE, foreground=BLACK) :
        """
        初始化
        :param archiver: 存档记录
        """
        Canvas.__init__(self, height, width, backgroup, foreground)
        self.arch = archiver
        self.dps = self.arch.dps.copy()

    
    def _read_tpl(self) :
        """
        :return: HTML 模板
        """
        with open(HTML_TPL, 'r') as file :
            tpl = file.read()
        return tpl
    

    def _to_canvas(self) :
        """
        根据存档记录绘制 HTML 预览画布
        :return: HTML 画布内容
        """
        today = self.arch._get_today_progress()
        for c in range(self.width - 1, -1, -1) :
            for r in range(self.height - 1, -1, -1) :
                key, val = self.dps.popitem()
                if today is not None and today.date == key :
                    color = COLOR_TODAY
                elif val.commit <= COMMIT_1 :
                    color = COLOR_1
                else :
                    color = COLOR_32
                self.canvas[r][c] = '<i style="color:%s" class="tooltip fa fa-square"><span class="tooltiptext">%s:%i/%i</span></i>' % (color, key, val.cnt, val.commit)

        _canvas = []
        for line in self.canvas :
            _canvas.append(' '.join(line))
        return '<br/> '.join(_canvas)
                

    def _to_html(self) :
        """
        构造 Giuhub HTML 页面
        :return: HTML 页面内容
        """
        today = self.arch._get_today_progress()
        tpl = self._read_tpl()
        html = tpl % {
            'logo': self.arch.logo,
            'datetime': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            'commit_cnt': today.cnt,
            'commit_total': today.commit,
            'canvas': self._to_canvas()
        }
        return html

    
    def to_page(self) :
        html = self._to_html()
        with open(HTML_PATH, 'w+') as file :
            file.write(html)




