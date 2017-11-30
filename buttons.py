#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:12:54 2017

@author: tomek
"""
from ops import COMPILED_REGEXS, FUNC_BY_SIGN


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


def create_button(s):
    s = s.strip()
    for r in COMPILED_REGEXS:
        match = r.match(s)
        if match:
            d = match.groupdict()
            sign = d.pop('sign')
            parameters = (v for k, v in sorted(d.items()))
            button = Button(*parameters, op=FUNC_BY_SIGN[sign])
            button.as_string = s
            return button
    raise ItIsNotaButtonError
