from itertools import product
from functools import reduce
from buttons import create_button, NonIntegerDivisionError


class SolutionDoesNotExistError:
    pass


def compute(start, seq_of_buttons):
    return reduce(lambda x, f: f(x), seq_of_buttons, start)


class CalculatorTheGame:
    
    def __init__(self, start, goal, moves):
        self.start = start
        self.goal = goal
        self.moves = moves
        self._buttons = {}
        self._solution = None
    
    def add_buttons(self, *signs):
        for sign in signs:
            self._buttons[sign] = create_button(sign)
    
    def solve(self, find_all=False):
        if find_all:
            solutions = set()
        for signs in product(self._buttons, repeat=self.moves):
            btns = (self._buttons[sign] for sign in signs)
            try:
                out = compute(self.start, btns)
            except NonIntegerDivisionError:
                continue
            if self.goal == out:
                self._solution = signs
                if find_all:
                    solutions.add(signs)
                else:
                    return signs
        return solutions
    
    def hint(self, number_of_hints=1):
        if not self._solution:
            self._solution = self.solve()
        return self._solution[:number_of_hints]