#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# -----------------------------------------------
# 用一年时间在 Github 画画
# -----------------------------------------------

import sys
from src.cfg.dot_matrix import *
from src.utils import log
from src.utils import canvas


CANVAS_WIDTH = 53
CANVAS_HEIGHT = 7



def main(help, view, logo, start_time) :
    if help :
        log.info(help_info())

    elif view :
        show()

    else :
        logo_chs = to_chs(logo)
        draw_in_local(logo_chs)
        draw_in_github(logo_chs, start_time)



def help_info():
    return '''
    -h                帮助信息
    -logo <string>    期望绘制的 LOGO 字符画， 要求总宽度 <= 53
                      （其中 A-Z 0-9 宽度为 7 ，标点符号宽度为 3）
    -st               开始绘制的日期，格式为： yyyy-MM-dd
    -v                打印支持绘制的字符
'''



def show() :
    for key, val in DICTS.items() :
        log.info("character = '%s', width = %i" % (key, len(val[0])))



def to_chs(logo) :
    logo_chs = []
    width = 0
    chs = list(logo.upper())
    for ch in chs :
        dm = DOT_MATRIX.get(ch)
        if dm :
            if width + len(dm[0]) >= CANVAS_WIDTH :
                continue
            else :
                logo_chs.append(ch)
                width += len(dm[0])
    return logo_chs



def draw_in_local(logo_chs) :
    log.info('LOGO: %s' % ''.join(logo_chs))
    lc = canvas.LocalCanvas(CANVAS_HEIGHT, CANVAS_WIDTH)
    lc.draw_canvas(logo_chs, DOT_MATRIX)
    log.info('Show in Local:')
    log.info(lc.canvas_to_str())



def draw_in_github(logo_chs, start_time) :
    pass







def get_sys_args(sys_args) :
    help = False
    view = False
    logo = 'EXP-REPO'
    start_time = '1990-01-01'

    idx = 1
    size = len(sys_args)
    while idx < size :
        try :
            if sys_args[idx] == '-h' :
                help = True

            elif sys_args[idx] == '-v' :
                view = True

            elif sys_args[idx] == '-logo' :
                idx += 1
                logo = sys_args[idx]

            elif sys_args[idx] == '-st' :
                idx += 1
                logo = sys_args[idx]
        except :
            pass
        idx += 1
    return help, view, logo, start_time



if __name__ == '__main__':
    log.init()
    main(*get_sys_args(sys.argv))

    print(get_next_weekday(calendar.MONDAY))


