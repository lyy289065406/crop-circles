#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pip install GitPython
# https://www.cnblogs.com/baiyangcao/p/gitpython.html


# crontab -> this.py : 
# 1. now(datetime) to grassland 
# 2. git push


import time
import git



def main() :
    plant()
    to_github()


def plant() :
    time_obj = time.localtime(time.time())
    now = time.strftime("%Y-%m-%d %H:%M:%S", time_obj)
    with open('./grassland.dat', 'a+') as file :
        file.write('%s\n' % now)

def to_github() :
    repo = git.Repo(r'.')
    repo.git.commit(m='this is a test')
    repo.git.push()


if __name__ == '__main__' :
    main()

