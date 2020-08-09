#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# -----------------------------------------------
# Git 提交器
# -----------------------------------------------

import os
import sys
import time
import git
import uuid
from src.env.cfg import *

PLANT_PATH = '%s/commit.dat' % CACHE_DIR
KEEP_SIZE = 1024   # 缓存文件大小，单位: byte


class GitCommit :
    '''
    Git 提交器
    '''

    def __init__(self, auto_commit=False):
        """
        初始化
        :param auto_commit: 自动提交变更
        """
        self.systime = self._get_systime()
        self.auto_commit = auto_commit


    def _get_systime(self) :
        """
        :return: 获取当前系统时间
        """
        now = time.localtime(time.time())
        return time.strftime("%Y-%m-%d %H:%M:%S", now)

    
    def _to_cache(self) :
        """
        构造变更文件
        """
        fsize = 0
        if os.path.exists(PLANT_PATH) :
            fsize = os.path.getsize(PLANT_PATH)
        mode = 'a+' if KEEP_SIZE > fsize else 'w+'

        with open(PLANT_PATH, mode) as file :
            file.write('%s\n' % self.systime)

    
    def to_repo(self) :
        """
        提交变更到 Git 仓库
        """
        self._to_cache()
        if self.auto_commit :
            repo = git.Repo(PRJ_DIR)
            repo.git.add(PLANT_PATH)
            repo.git.commit(m='"[%s] %s"' % (self.systime, uuid.uuid1()))
            repo.git.push()

