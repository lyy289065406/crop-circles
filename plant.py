#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import random
import time
import git
import uuid


REPO_DIR = os.path.split(os.path.realpath(__file__))[0]     # 仓库目录
GRASSLAND = '%s/grassland.dat' % REPO_DIR  # 种草文件
KEEP_SIZE = 1 * 1024 * 1024   # 种草文件大小，单位: M
PROBABILITY = 100             # 种草概率: 默认每小时种1次，每小时下降 5% ，每天凌晨重置 



def main() :
    if is_bingo() :
        now = get_systime()
        to_plant(now)
        to_github(now)


# 获取当前系统时间
def get_systime() :
    time_obj = time.localtime(time.time())
    return time.strftime("%Y-%m-%d %H:%M:%S", time_obj)


# 种草
def to_plant(systime) :
    fsize = 0
    if os.path.exists(GRASSLAND) :
        fsize = os.path.getsize(GRASSLAND)
    mode = 'a+' if KEEP_SIZE > fsize else 'w+'

    with open(GRASSLAND, mode) as file :
        file.write('%s\n' % systime)


# 是否命中种草概率
def is_bingo() :
    hour = time.localtime().tm_hour
    cur_rate = PROBABILITY - hour * 5   # 每小时下降 5%
    return random.randint(0,100) <= cur_rate


# 提交到 github
def to_github(systime) :
    repo = git.Repo(REPO_DIR)
    repo.git.add(GRASSLAND)
    repo.git.commit(m='"[%s] %s"' % (systime, uuid.uuid1()))
    repo.git.push()



if __name__ == '__main__' :
    main()


