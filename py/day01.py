from collections import Counter


def calculate_total_distance(left_list, right_list):
    left_list.sort()
    right_list.sort()
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    return total_distance


def calculate_similarity_score(left_list, right_list):
    right_counter = Counter(right_list)
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counter[num]
    return similarity_score


if __name__ == "__main__":
    # Read input from file
    left_list = []
    right_list = []
    with open("input/01.txt", "r") as file:
        for line in file:
            left, right = map(int, line.split())
            left_list.append(left)
            right_list.append(right)

    # Calculate total distance
    total_distance = calculate_total_distance(left_list, right_list)
    print(f"Total Distance: {total_distance}")

    # Calculate similarity score
    similarity_score = calculate_similarity_score(left_list, right_list)
    print(f"Similarity Score: {similarity_score}")
