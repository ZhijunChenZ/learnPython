# -*- coding: utf-8 -*-
"""
Created on Fri May 15 13:44:19 2020

@author: zhijun
"""

import math

def quadratic(a, b, c):
    if not isinstance(a, (int, float)) and not isinstance(b, (int, float)) and not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    if a != 0:
        delta = b ** 2 - 4 * a * c
        if delta > 0:
            print('delta =', delta, '\n判别式大于零，方程有两个不相等的实数根')
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return float('%.2f' % x1), float('%.2f' % x2)
        elif delta == 0:
            print('delta =', delta, '\n判别式为零，方程有两个相等的实数根')
            x = -b  / (2 * a)
            return x
        elif delta < 0:
            print('delta =', delta, '\n判别式小于零，方程无实数根')
            return None
    else:
        x = -c / b
        return float('%.2f' % x)
