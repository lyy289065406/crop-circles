#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# -----------------------------------------------
# 
# -----------------------------------------------

import os
import re
import hashlib
import datetime
import collections
from src.env.cfg import *
from src.utils.tool import *




class Archiver :

    def __init__(self, logo) :
        """
        初始化
        :param logo: 合法的 logo 字符串
        """
        self.logo = logo
        self.savepath = self._to_savepath(logo)
        self.dps = collections.OrderedDict()


    def _to_savepath(self, logo) :
        """
        生成存档文件路径
        :param logo: 合法的 logo 字符串
        """
        hl = hashlib.md5()
        hl.update(logo.encode(encoding=CHARSET))
        md5 = hl.hexdigest()
        return '%s/cache/save_%s' % (PRJ_DIR, md5)


    # FIXME
    def to_progress(self, canvas) :
        """
        根据画布在内存生成预设进度表
        """
        next = get_next_weekday()
        for col in range(0, CANVAS_WIDTH) :
            for row in range(0, CANVAS_HEIGHT) :
                point = canvas[row][col]
                nextday = get_next_day(next).strftime('%Y%m%d')
                commit = COMMIT_16 if point == BLACK else COMMIT_1
                dp = DayProgress(nextday, 0, commit)
                self.dps[nextday] = dp
                next += 1


    # FIXME
    def update(self, day=datetime.date.today()) :
        """
        在内存更新指定日期的 commit 进度
        :param day: 指定日期，格式形如 20200520
        """
        dp = self.dps[day.strftime('%Y%m%d')]
        if dp is not None :
            dp.update()


    def load(self) :
        """
        加载进度
        :return: 存档文件是否存在
        """
        is_exist = False
        if os.path.exists(self.savepath) :
            is_exist = True
            with open(self.savepath, 'r') as file :
                lines = file.readlines()
                for line in lines :
                    args = re.split('=|/', line)
                    dp = DayProgress(*args)
                    self.dps[dp.day] = dp
        self._del()
        return is_exist

    
    def _del(self) :
        """
        删除所有无效的存档文件
        """




    def save(self) :
        """
        把内存进度写入文件
        """
        progress = []
        for key, val in self.dps.items() :
            progress.append(val.to_str())

        with open(self.savepath, 'w+') as file :
            file.write('\n'.join(progress))
        
        




class DayProgress :


    def __init__(self, day, cnt=COMMIT_0, commit=COMMIT_1) :
        self.day = day
        self.cnt = int(cnt)
        self.commit = int(commit)


    def update(self) :
        if self.cnt < self.commit :
            self.cnt += 1


    def to_str(self) :
        return '%s=%i/%i' % (self.day, self.cnt, self.commit)


    def __repr__(self):
        return self.to_str()

    
    def __str__(self):
        return self.to_str()
    
