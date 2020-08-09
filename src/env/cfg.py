#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# @File   : log.py
# -----------------------------------------------

import os

PRJ_DIR = os.path.dirname(os.path.abspath(__file__)).replace(r'/src/env', '').replace(r'\src\env', '')
CACHE_DIR = '%s/cache' % PRJ_DIR
SAVE_PREFIX = 'save_'
CHARSET = 'utf-8'


# canvas
WHITE = '□'         # 画布背景色
BLACK = '■'         # 画布前景色
CANVAS_WIDTH = 53   # 画布宽度
CANVAS_HEIGHT = 7   # 画布高度
DEFAULT_LOGO = 'EXP - GIT'


# commit
COMMIT_0 = 0        # 提交 0 次： 白色
COMMIT_1 = 1        # 提交 [1, 16) 次： 浅绿色
COMMIT_16 = 16      # 提交 [16, 32) 次： 翠绿
COMMIT_32 = 32      # 提交 [32, 64) 次： 深绿
COMMIT_64 = 64      # 提交 [64, +∞) 次： 墨绿
