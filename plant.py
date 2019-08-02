#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python 2.7
# pip install GitPython
# https://www.cnblogs.com/baiyangcao/p/gitpython.html


# crontab -> this.py : 
# 1. now(datetime) to grassland 
# 2. git push

import os
import time
import git
import uuid

CUR_DIR = os.path.split(os.path.realpath(__file__))[0]
GRASSLAND = '%s/grassland.dat' % CUR_DIR


def main() :
    now = get_systime()
    to_plant(now)
    to_github(now)


def get_systime() :
    time_obj = time.localtime(time.time())
    return time.strftime("%Y-%m-%d %H:%M:%S", time_obj)


def to_plant(systime) :
    with open(GRASSLAND, 'a+') as file :
        file.write('%s\n' % systime)


def to_github(systime) :
    repo = git.Repo(r'.')
    repo.git.add(GRASSLAND)
    repo.git.commit(m='[%s] %s' % (systime, uuid.uuid1()))
    repo.git.push()


if __name__ == '__main__' :
    main()

