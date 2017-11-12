from itertools import permutations, combinations_with_replacement
from operator import add, sub, mul

class NonIntegerDivision(Exception):
    pass

def division(n, k):
    if n % k == 0:
        return n // k
    else:
        raise NonIntegerDivision

def variations_with_replacement(iterable, r):
    for comb in combinations_with_replacement(iterable, r):
        for perm in permutations(comb):
            yield perm

OPS = {'+': add, '-': sub, '*': mul, '/': division}

def create_button(s):
    if s == '^2':
        def f(x):
            return x * x
    elif s == '+/-':
        def f(x):
            return -x
    elif s == '<<':
        def f(x):
            return int(str(x)[:-1])
    elif s[0] in OPS.keys():
        d, c = s[0], int(s[1:])
        def f(x):
            return OPS[d](x, c)
    elif '=>' in s:
        a, b = s.split('=>')
        def f(x):
            return int(str(x).replace(a, b))
    else:
        c = int(s)
        def f(x):
            return int('{}{}'.format(x, c))
    return f

def compute(x, buttons, funcs):
    for button in buttons:
        try:
            x = funcs[button](x)
        except NonIntegerDivision:
            raise
    return x

class Calculator:
    
    def __init__(self, start, goal, moves):
        self.start = start
        self.goal = goal
        self.moves = moves
        self._buttons = {}
        self._solutions = []
    
    def add_buttons(self, *buttons):
        for button in buttons:
            self._buttons[button] = create_button(button)
    
    def solve(self, all=False):
        for v in variations_with_replacement(self._buttons, self.moves):
            try:
                out = compute(self.start, v, self._buttons)
            except NonIntegerDivision:
                continue
            if self.goal == out:
                if all:
                    self._solutions.append(v)
                else:
                    return v
        return set(self._solutions)