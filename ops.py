#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:07:04 2017

@author: tomek
"""

import re
from operator import add, sub, mul, neg


class NonIntegerDivisionError(Exception):
    pass


def add_cipher(k, n):
    return int('{}{}'.format(k, n))


def division(k, n):
    if k % n == 0:
        return k // n
    else:
        raise NonIntegerDivisionError


def square(k):
    return k * k


def eat_cipher(k):
    if -10 < k < 10:
        return 0
    else:
        return int(str(k)[:-1])


def replace_ciphers(k, a, b):
    return int(str(k).replace(str(a), str(b)))


def reverse(k):
    if k < 0:
        s = str(k)[1:]
    else:
        s = str(k)
    return int(s[::-1])


EMPTY_STR = ''


FUNC_BY_SIGN = {EMPTY_STR: add_cipher, '+': add, '-': sub,
                '*': mul, '/': division,
                '^2': square, '+/-': neg,
                '<<': eat_cipher, '=>': replace_ciphers,
                'reverse': reverse}

REGEXS = (r'^(?P<sign>)(?P<n>\d+)$',
          r'^(?P<sign>\+)(?P<n>\d+)$',
          r'^(?P<sign>-)(?P<n>\d+)$',
          r'^(?P<sign>\*)(?P<n>-?\d+)$',
          r'^(?P<sign>/)(?P<n>-?\d+)$',
          r'^(?P<sign>\^2)$',
          r'^(?P<sign>\+/-)$',
          r'^(?P<sign><<)$',
          r'^(?P<n1>\d+)(?P<sign>=>)(?P<n2>\d+)$',
          r'^(?P<sign>reverse)$')

COMPILED_REGEXS = tuple(re.compile(r) for r in REGEXS)
