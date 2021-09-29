#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# @File   : main.py
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


def main(help, view, auto_commit, logo) :
    if help :
        log.info(help_info())

    elif view :
        log.info(ch_info())

    else :
        draw(logo, auto_commit)
        


def help_info():
    return '''
    -h                帮助信息
    -logo <string>    期望绘制的 LOGO 字符画， 要求总宽度 <= 53
                      （其中 A-Z 0-9 宽度为 7 ，标点符号宽度为 3）
    -v                打印支持绘制的字符
    -ac               自动提交变更到 Github
'''



def ch_info() :
    """
    :return: 返回支持绘制的字符及其宽度
    """
    infos = [ '' ]
    for key, val in DOT_MATRIX.items() :
        infos.append("character = '%s', width = %i" % (key, len(val[0])))
    return '\n'.join(infos)



def draw(logo, auto_commit) :
    """
    在 Github 绘画
    :param logo: 合法的 logo 字符串
    :param auto_commit: 自动提交到 Github
    """
    # 格式化 logo
    logo = tool.format(logo)
    log.info('LOGO: %s' % logo)

    # 预览画布
    lc = LocalCanvas()
    lc.draw(logo)
    log.info('Preview in Canvas: %s' % lc.to_str())

    # 获取画布绘制进度
    arch = Archiver(logo)
    if not arch.load() :            # 加载存档文件
        arch.to_progress(lc.canvas) # 生成新的存档文件

    # 更新今天的进度
    if arch.check_today() :
        log.info('Update Progress')
        arch.update_today()
        arch.check_finish()         # 检查是否全部绘制完成

        # 生成进度展示页面
        hc = HtmlCanvas(arch)
        hc.to_page()
    else :
        log.info('Today Finish')

    arch.save()

    # 提交变更以进行累积性绘画      
    if auto_commit :
        git_commit()



def get_sys_args(sys_args) :
    """
    获取脚本入参
    :param sys_args: 脚本参数列表
    """
    help = False
    view = False
    auto_commit = False
    logo = DEFAULT_LOGO

    idx = 1
    size = len(sys_args)
    while idx < size :
        try :
            if sys_args[idx] == '-h' :
                help = True

            elif sys_args[idx] == '-v' :
                view = True

            elif sys_args[idx] == '-ac' :
                auto_commit = True

            elif sys_args[idx] == '-logo' :
                idx += 1
                logo = sys_args[idx]
        except :
            pass
        idx += 1
    return help, view, auto_commit, logo



if __name__ == '__main__':
    log.init()
    main(*get_sys_args(sys.argv))



