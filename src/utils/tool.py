#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/09 13:14
# @File   : tool.py
# -----------------------------------------------
# 辅助工具
# -----------------------------------------------

import git
import uuid
import calendar
import datetime
import time
import hashlib
import subprocess

from ..env.cfg import *
from ..env.dot_matrix import *



def format(logo, canvas_width=CANVAS_WIDTH, dot_matrix=DOT_MATRIX) :
    """
    格式化 logo 字符串
    :param logo: 期望绘制的 logo 字符串
    :param canvas_width: 用于绘制 logo 的画布宽度
    :param dot_matrix: 点阵字符表
    :return: 合法的 logo （仅包含支持绘制的字符）
    """
    logo_chs = []
    width = 0
    chs = list(logo.upper())
    for ch in chs :
        dm = dot_matrix.get(ch)
        if dm :
            if width + len(dm[0]) >= canvas_width :
                continue
            else :
                logo_chs.append(ch)
                width += len(dm[0])
    return ''.join(logo_chs)


def to_md5(string) :
    """
    :param string: 目标字符串
    :return: MD5
    """
    hl = hashlib.md5()
    hl.update(string.encode(encoding=CHARSET))
    return hl.hexdigest()


def get_next_weekday(target_weekday=calendar.SUNDAY) :
    """
    :param target_weekday: 目标的周几（周日、周一、周二、......）
    :return: 从今天到下一个周几之间的天数
    """
    days = 0
    nextday = datetime.date.today()
    delta = datetime.timedelta(days = 1)
    while nextday.weekday() != target_weekday:
        nextday += delta
        days += 1
    return days



def get_after_day(after_days=0) :
    """
    :param after_days: N 天后
    :return: N 天后的日期
    """
    today = datetime.date.today()
    delta = datetime.timedelta(days = after_days)
    afterday = today + delta
    return afterday



def date_to_str(date) :
    """
    :param date: 日期
    :return: 格式化日期
    """
    return date.strftime('%Y%m%d')



def str_to_date(str) :
    """
    :param str: 格式化日期
    :return: 日期
    """
    return datetime.datetime.strptime(str, '%Y%m%d')



def get_systime() :
    """
    :return: 获取当前系统时间
    """
    now = time.localtime(time.time())
    return time.strftime("%Y-%m-%d %H:%M:%S", now)


def git_commit(count=1) :
    """
    一次性提交多个 commit（主 commit 含存档文件，其余为空 commit）
    :param count: 需要产生的 commit 次数（>= 1）
    """
    repo = git.Repo(PRJ_DIR)
    repo.git.add('.')
    # 除了主 commit 之外的额外空 commit，仅用于在 GitHub 贡献图表上累积颜色深度
    for _ in range(count - 1):
        repo.git.commit(m=f'"[bot] {uuid.uuid1()}"', allow_empty=True)
    repo.git.commit(m=f'"[{get_systime()}] {uuid.uuid1()}"')
    repo.git.push()


def count_today_commits(username=None, token=None) :
    """
    通过 GitHub Search API 统计该用户今天在全站所有仓库的 commit 总数
    （需要 PAT 才有跨仓库搜索权限）。失败时回退到仅统计本仓库。
    :param username: GitHub 用户名
    :param token: Personal Access Token（非 Actions 自带的 GITHUB_TOKEN）
    """
    today = datetime.date.today().strftime('%Y-%m-%d')
    if username and token :
        try:
            result = subprocess.run([
                'gh', 'api',
                '-H', 'Accept: application/vnd.github+json',
                '-H', f'Authorization: token {token}',
                f'search/commits?q=author:{username}+author-date:{today}&per_page=1',
                '--jq', '.total_count'
            ], capture_output=True, text=True, timeout=15)
            if result.returncode == 0 and result.stdout.strip().isdigit():
                return int(result.stdout.strip())
        except:
            pass
    repo = git.Repo(PRJ_DIR)
    try:
        log = repo.git.log(f'--since={today}T00:00:00Z', '--oneline')
        return len(log.strip().split('\n')) if log.strip() else 0
    except:
        return 0

