#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : EXP
# @Time   : 2020/08/01 13:14
# -----------------------------------------------
# 
# -----------------------------------------------

import calendar
import datetime


def get_next_weekday(target=calendar.SUNDAY) :
    nextday = datetime.date.today()
    delta = datetime.timedelta(days = 1)
    while nextday.weekday() != target:
        nextday += delta
    # next = nextday.strftime('%Y%m%d')
    return nextday


def get_next_day(today=datetime.date.today()) :
    delta = datetime.timedelta(days = 1)
    nextday = today + delta
    return nextday


class DayProgress :

    def __init__(self, day='20200101', commit=1) :
        self.day = day
        self.cnt = 0
        self.commit = commit

    
