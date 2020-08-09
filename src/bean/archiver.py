#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# -----------------------------------------------
# 
# -----------------------------------------------

import os
import re
import datetime
import collections
from src.env.cfg import *
from src.utils.tool import *




class Archiver :
    '''
    存档器
    '''

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
        md5 = to_md5(logo)
        return '%s/%s%s' % (CACHE_DIR, SAVE_PREFIX, md5)


    def to_progress(self, canvas) :
        """
        根据画布在内存生成预设进度表
        """
        days = get_next_weekday()       # 以最近的下一个周日为起始点
        for col in range(0, CANVAS_WIDTH) :
            for row in range(0, CANVAS_HEIGHT) :
                point = canvas[row][col]
                after_day = get_after_day(days)
                after_date = date_to_str(after_day)
                commit = (COMMIT_16 if point == BLACK else COMMIT_1)

                dp = DateProgress(after_date, 0, commit)
                self.dps[after_date] = dp
                days += 1


    def update(self, date=datetime.date.today()) :
        """
        在内存更新指定日期的 commit 进度
        :param day: 指定日期，格式形如 20200520
        """
        sdate = date_to_str(date)
        dp = self.dps[sdate]
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
                    dp = DateProgress(*args)
                    self.dps[dp.date] = dp
        self._del()
        return is_exist

    
    def _del(self) :
        """
        删除所有无效的存档文件
        """
        filenames = os.listdir(CACHE_DIR)
        for filename in filenames :
            if filename.startswith(SAVE_PREFIX) and not self.savepath.endswith(filename) :
                os.remove('%s/%s' % (CACHE_DIR, filename))
                    

    def save(self) :
        """
        把内存进度写入文件
        """
        progress = []
        for key, val in self.dps.items() :
            progress.append(val.to_str())

        with open(self.savepath, 'w+') as file :
            file.write('\n'.join(progress))
        



class DateProgress :
    '''
    日期进度
    '''

    def __init__(self, date, cnt=COMMIT_0, commit=COMMIT_1) :
        """
        初始化
        :param date: 日期，格式形如 20200520
        :param cnt: 已提交次数
        :param commit: 需提交次数
        """
        self.date = date
        self.cnt = int(cnt)
        self.commit = int(commit)


    def update(self) :
        if self.cnt < self.commit :
            self.cnt += 1


    def to_str(self) :
        return '%s=%i/%i' % (self.date, self.cnt, self.commit)


    def __repr__(self):
        return self.to_str()

    
    def __str__(self):
        return self.to_str()
    
