#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# @File   : main.py
# -----------------------------------------------
# 用一年时间在 Github 画画
# -----------------------------------------------

import sys
import os
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
        infos.append(f"character = '{key}', width = {len(val[0])}")
    return '\n'.join(infos)



def draw(logo, auto_commit) :
    """
    在 Github 绘画
    :param logo: 合法的 logo 字符串
    :param auto_commit: 自动提交到 Github
    """
    logo = tool.format(logo)
    log.info(f'LOGO: {logo}')

    lc = LocalCanvas()
    lc.draw(logo)
    log.info(f'Preview in Canvas: {lc.to_str()}')

    arch = Archiver(logo)
    if not arch.load() :
        arch.to_progress(lc.canvas)

    if arch.check_today() :
        log.info('Update Progress')
        real_commits = tool.count_today_commits(
            os.environ.get('GIT_USER'),
            os.environ.get('_GITHUB_TOKEN')
        )
        count = arch.complete_today(real_commits)
        log.info(f'Already committed: {real_commits}, need: {count}')

        hc = HtmlCanvas(arch)
        hc.to_page()
        arch.save()
        arch.check_finish()

        if auto_commit :
            git_commit(count)              # 一次 push 完成 N 个 commit
    else :
        log.info('Today Finish')

        



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



