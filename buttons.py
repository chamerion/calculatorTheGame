#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:12:54 2017

@author: tomek
"""

import re
from operator import add, sub, mul, neg


class NonIntegerDivisionError(Exception):
    pass


class ItIsNotaButtonError(Exception):
    pass


class Button:

    def __init__(self, *parameters, op):
        self.parameters = tuple(int(p) for p in parameters) if parameters else ()
        self.op = op
        self.as_string = None

    def __call__(self, *args):
        return self.op(*args, *self.parameters)

    def __str__(self):
        return 'Button({})'.format(self.as_string)

    def __repr__(self):
        if not self.parameters:
            return 'Button({})'.format(self.op.__name__)
        else:
            spar = ', '.join(str(p) for p in self.parameters)
            return 'Button({}, {})'.format(spar, self.op.__name__)


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
    s = str(k)
    return int(s[::-1])


EMPTY_STR = ''


func_by_sign = {EMPTY_STR: add_cipher, '+': add, '-': sub,
                '*': mul, '/': division,
                '^2': square, '+/-': neg,
                '<<': eat_cipher, '=>': replace_ciphers,
                'reverse': reverse}

regexs = (r'^(?P<sign>)(?P<n>\d+)$',
          r'^(?P<sign>\+)(?P<n>\d+)$',
          r'^(?P<sign>-)(?P<n>\d+)$',
          r'^(?P<sign>\*)(?P<n>-?\d+)$',
          r'^(?P<sign>/)(?P<n>-?\d+)$',
          r'^(?P<sign>\^2)$',
          r'^(?P<sign>\+/-)$',
          r'^(?P<sign><<)$',
          r'^(?P<n1>\d+)(?P<sign>=>)(?P<n2>\d+)$',
          r'^(?P<sign>reverse)$')

compiled_regexs = tuple(re.compile(r) for r in regexs)


def create_button(s):
    s = s.strip()
    for r in compiled_regexs:
        match = r.match(s)
        if match:
            d = match.groupdict()
            sign = d.pop('sign')
            parameters = (v for k, v in sorted(d.items()))
            button = Button(*parameters, op=func_by_sign[sign])
            button.as_string = s
            return button
    raise ItIsNotaButtonError
