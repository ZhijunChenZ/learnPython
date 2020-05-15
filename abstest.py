# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:17:20 2020

@author: zhijun
"""

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
    