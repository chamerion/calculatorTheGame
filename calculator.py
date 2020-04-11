from itertools import product
from functools import reduce
from ops import NonIntegerDivisionError
from buttons import create_button


class SolutionDoesNotExistError(Exception):
    pass


def final_value(start, seq_of_buttons):
    '''Returns result of application of sequence of funcs to starting value.'''
    return reduce(lambda x, f: f(x), seq_of_buttons, start)


def solve(start, goal, moves, buttons_by_sign):
    '''Generator of solutions of the puzzle.'''
    for signs in product(buttons_by_sign, repeat=moves):
        seq_of_buttons = (buttons_by_sign[sign] for sign in signs)
        try:
            out = final_value(start, seq_of_buttons)
        except NonIntegerDivisionError:
            continue
        if goal == out:
            yield signs


class CalculatorTheGame:

    def __init__(self, start, goal, moves):
        self.start = start
        self.goal = goal
        self.moves = moves
        self._buttons = {}
        self._solution = None
    
    def __str__(self):
        s = 'CalculatorTheGame(start={}, goal={}, moves={})\n' \
            .format(self.start, self.goal, self.moves)
        s += '\n'.join(map(str, self._buttons.values()))
        return s

    def add_buttons(self, *signs):
        for sign in signs:
            self._buttons[sign] = create_button(sign)

    def solve(self, find_all=False):
        solutions_gen = solve(self.start, self.goal, self.moves, self._buttons)
        if find_all:
            return set(solutions_gen)
        else:
            try:
                self._solution = next(solutions_gen)
            except StopIteration:
                raise SolutionDoesNotExistError
            return self._solution

    def hint(self, number_of_hints=1):
        if not self._solution:
            self._solution = self.solve()
        return self._solution[:number_of_hints]
