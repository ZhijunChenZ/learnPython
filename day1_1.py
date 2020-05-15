# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 13:07:27 2020

@author: zhijun
"""

def f(expr):
    expList = expr.split()
    a, b, c = int(expList[0]), expList[1], int(expList[2])
    if b == '+':
        return a + c
    elif b == '-':
        return a - c
    elif b == '*':
        return a * c
    elif b == '/':
        return a / c
    else:
        return None
    
print(f('10 + 10'))
print(f('10 - 10'))
print(f('10 * 10'))
print(f('10 / 10'))