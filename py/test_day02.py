import pytest
import numpy as np
from day02 import is_safe, is_safe_ignoring_one, calculate_part1, calculate_part2

levels = [
    np.array([7, 6, 4, 2, 1]),
    np.array([1, 2, 7, 8, 9]),
    np.array([9, 7, 6, 2, 1]),
    np.array([1, 3, 2, 4, 5]),
    np.array([8, 6, 4, 4, 1]),
    np.array([1, 3, 6, 7, 9]),
]


def test_calculate_part1():
    assert calculate_part1(levels) == 2

def test_calculate_part2():
    assert calculate_part2(levels) == 4

if __name__ == "__main__":
    pytest.main()
