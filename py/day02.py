import numpy as np

def is_safe(level):
    level = np.array(level)
    diffs = np.diff(level)
    signs = np.sign(diffs)

    # Check if all differences have the same sign
    if not np.all(signs == signs[0]):
        return 0

    # Check if all differences are within 1-3
    abs_diffs = np.abs(diffs)
    if np.any((abs_diffs < 1) | (abs_diffs > 3)):
        return 0

    return 1

def is_safe_ignoring_one(level):
    for i in range(len(level)):
        modified_level = np.delete(level, i)
        if is_safe(modified_level):
            return 1
    return 0

def calculate_part1(levels):
    return np.sum([is_safe(level) for level in levels])

def calculate_part2(levels):
    return np.sum([is_safe_ignoring_one(level) for level in levels])

if __name__ == "__main__":
    with open("input/02.txt", "r") as file:
        lines = file.readlines()
        levels = [np.array(list(map(int, line.split()))) for line in lines]

    print(f"Part 1: {calculate_part1(levels)}")
    print(f"Part 2: {calculate_part2(levels)}")
