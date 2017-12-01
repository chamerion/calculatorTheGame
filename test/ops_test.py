import pytest
from ..ops import NonIntegerDivisionError
from ..ops import (add_cipher, division, square, eat_cipher,
                   replace_ciphers, reverse)


@pytest.mark.parametrize('k, n, out', [(0, 1, 1),
                                       (-2, 3, -23),
                                       (123, 98, 12398)])
def test_add_cipher(k, n, out):
    assert add_cipher(k, n) == out


@pytest.mark.parametrize('k, n, out', [(10, 2, 5),
                                       (-12, 4, -3),
                                       (20, -4, -5),
                                       (0, 1, 0)])
def test_division(k, n, out):
    assert division(k, n) == out


@pytest.mark.parametrize('k, n', [(3, 2),
                                  (-5, 3),
                                  (412, -5),
                                  (1, 2)])
def test_division_NonIntegerDivisionError(k, n):
    with pytest.raises(NonIntegerDivisionError):
        division(k, n)


def test_division_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)


@pytest.mark.parametrize('k, out', [(0, 0),
                                    (3, 9),
                                    (-4, 16)])
def test_square(k, out):
    assert square(k) == out


eat_cipher_to_zero = [(k, 0) for k in range(-9, 10)]
other_eat_cipher_assertions = [(123, 12), (-10, -1)]
@pytest.mark.parametrize('k, out', eat_cipher_to_zero + 
                         other_eat_cipher_assertions)
def test_eat_cipher(k, out):
    assert eat_cipher(k) == out


@pytest.mark.parametrize('k, a, b, out', [(1, 1, 2, 2),
                                          (3456, 45, 0, 306),
                                          (-232323, 323, 7, -2723)])
def test_replace_ciphers(k, a, b, out):
    assert replace_ciphers(k, a, b) == out


def test_replace_ciphers_ValueError():
    with pytest.raises(ValueError):
        replace_ciphers(123, 1, -1)


@pytest.mark.parametrize('k, out', [(1, 1),
                                    (12, 21),
                                    (50, 5),
                                    (-480, -84)])
def test_reverse(k, out):
    assert reverse(k) == out
