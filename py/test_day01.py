from day01 import calculate_total_distance, calculate_similarity_score


def test_calculate_total_distance():
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]
    assert calculate_total_distance(left_list, right_list) == 11


def test_calculate_similarity_score():
    left_list = [3, 4, 2, 1, 3, 3]
    right_list = [4, 3, 5, 3, 9, 3]
    assert calculate_similarity_score(left_list, right_list) == 31
