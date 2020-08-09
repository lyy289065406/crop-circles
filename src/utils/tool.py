#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/09 13:14
# -----------------------------------------------
# 辅助工具
# -----------------------------------------------

import calendar
import datetime
from src.env.cfg import *
from src.env.dot_matrix import *


def format(logo, canvas_width=CANVAS_WIDTH, dot_matrix=DOT_MATRIX) :
    """
    格式化 logo 字符串
    :param logo: 期望绘制的 logo 字符串
    :param canvas_width: 用于绘制 logo 的画布宽度
    :param dot_matrix: 点阵字符表
    :return: 合法的 logo （仅包含支持绘制的字符）
    """
    logo_chs = []
    width = 0
    chs = list(logo.upper())
    for ch in chs :
        dm = dot_matrix.get(ch)
        if dm :
            if width + len(dm[0]) >= canvas_width :
                continue
            else :
                logo_chs.append(ch)
                width += len(dm[0])
    return ''.join(logo_chs)



def get_next_weekday(target=calendar.SUNDAY) :
    nextday = datetime.date.today()
    delta = datetime.timedelta(days = 1)

    cnt = 0
    while nextday.weekday() != target:
        nextday += delta
        cnt += 1
    # next = nextday.strftime('%Y%m%d')
    # return nextday
    return cnt


def get_next_day(next=1) :
    today = datetime.date.today()
    delta = datetime.timedelta(days = next)
    nextday = today + delta
    return nextday

