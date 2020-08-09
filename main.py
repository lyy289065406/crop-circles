#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# -----------------------------------------------
# 用一年时间在 Github 画画
# -----------------------------------------------

import sys
from src.bean.archiver import *
from src.bean.canvas import *
from src.env.cfg import *
from src.env.dot_matrix import *
from src.utils import log
from src.utils import tool


def main(help, view, logo) :
    if help :
        log.info(help_info())

    elif view :
        log.info(ch_info())

    else :
        logo = tool.format(logo)
        log.info('LOGO: %s' % logo)

        lc = LocalCanvas(logo)
        log.info('Preview in Canvas: %s' % lc.to_str())

        arch = Archiver(logo)
        if not arch.load() :            # 加载存档文件
            arch.to_progress(lc.canvas) # 生成新的存档文件


        # TODO 提交
        draw_in_github(logo)

        arch.update()
        arch.save()



def help_info():
    return '''
    -h                帮助信息
    -logo <string>    期望绘制的 LOGO 字符画， 要求总宽度 <= 53
                      （其中 A-Z 0-9 宽度为 7 ，标点符号宽度为 3）
    -v                打印支持绘制的字符
'''



def ch_info() :
    """
    :return: 返回支持绘制的字符及其宽度
    """
    infos = [ '' ]
    for key, val in DOT_MATRIX.items() :
        infos.append("character = '%s', width = %i" % (key, len(val[0])))
    return '\n'.join(infos)




def draw_in_github(logo_chs) :
    pass







def get_sys_args(sys_args) :
    help = False
    view = False
    logo = DEFAULT_LOGO

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
        except :
            pass
        idx += 1
    return help, view, logo



if __name__ == '__main__':
    log.init()
    main(*get_sys_args(sys.argv))


