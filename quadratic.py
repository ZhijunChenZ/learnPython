# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:44:19 2020

@author: zhijun
"""

import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    if a != 0:
        delta = b ** 2 - 4 * a * c
        return (-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)
    else:
        pass
