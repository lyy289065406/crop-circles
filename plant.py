#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import git
import uuid

REPO_DIR = os.path.split(os.path.realpath(__file__))[0]
GRASSLAND = '%s/grassland.dat' % REPO_DIR
KEEP_SIZE = 1 * 1024 * 1024     # unit: M


def main() :
    now = get_systime()
    to_plant(now)
    to_github(now)


def get_systime() :
    time_obj = time.localtime(time.time())
    return time.strftime("%Y-%m-%d %H:%M:%S", time_obj)


def to_plant(systime) :
    fsize = 0
    if os.path.exists(GRASSLAND) :
        fsize = os.path.getsize(GRASSLAND)
    mode = 'a+' if KEEP_SIZE > fsize else 'w+'

    with open(GRASSLAND, mode) as file :
        file.write('%s\n' % systime)


def to_github(systime) :
    repo = git.Repo(REPO_DIR)
    repo.git.add(GRASSLAND)
    repo.git.commit(m='[%s] %s' % (systime, uuid.uuid1()))
    repo.git.push()


if __name__ == '__main__' :
    main()

