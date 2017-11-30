import pytest
from ..ops import add_cipher, division, NonIntegerDivisionError


@pytest.mark.parametrize('k, n, out', [
                                       (0, 1, 1),
                                       (-2, 3, -23),
                                       (123, 98, 12398)
                                       ])
def test_add_cipher(k, n, out):
    assert add_cipher(k, n) == out


@pytest.mark.parametrize('k, n, out', [
                                       (10, 2, 5),
                                       (-12, 4, -3),
                                       (20, -4, -5),
                                       (0, 1, 0)])
def test_division(k, n, out):
    assert division(k, n) == out


@pytest.mark.parametrize('k, n', [
                                  (3, 2),
                                  (-5, 3),
                                  (412, -5),
                                  (1, 2)
                                  ])
def test_division_NonIntegerDivisionError(k, n):
    with pytest.raises(NonIntegerDivisionError):
        division(k, n)


def test_division_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        division(1, 0)