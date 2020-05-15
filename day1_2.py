# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 12:58:25 2020

@author: zhijun
"""

import datetime

def age(year, month, day):
    now = datetime.datetime.now()
    birthday = datetime.datetime(year, month, day, 0,0)
    return (now - birthday).days / 365

print(age(1991, 8, 5))