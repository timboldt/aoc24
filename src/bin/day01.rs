use std::collections::HashMap;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    let path = Path::new("input/01.txt");
    let file = File::open(path)?;
    let reader = io::BufReader::new(file);

    let mut left_list = Vec::new();
    let mut right_list = Vec::new();

    for line in reader.lines() {
        let line = line?;
        let mut parts = line.split_whitespace();
        if let (Some(left), Some(right)) = (parts.next(), parts.next()) {
            left_list.push(left.parse::<i32>().unwrap());
            right_list.push(right.parse::<i32>().unwrap());
        }
    }

    let total_distance = part1(left_list.clone(), right_list.clone());
    println!("Total distance: {}", total_distance);

    let simularity_score = part2(left_list, right_list);
    println!("Simularity score: {}", simularity_score);

    Ok(())
}

/// Calculate the total distance between each number in the left list and the corresponding number in
/// the right list. The total distance is the sum of the absolute differences between each pair of
/// numbers.
fn part1(mut left_list: Vec<i32>, mut right_list: Vec<i32>) -> i32 {
    left_list.sort();
    right_list.sort();

    let total_distance: i32 = left_list
        .iter()
        .zip(right_list.iter())
        .map(|(left, right)| (left - right).abs())
        .sum();
    total_distance
}

/// Figure out exactly how often each number from the left list appears in the right list. Calculate
/// a total similarity score by adding up each number in the left list after multiplying it by the
/// number of times that number appears in the right list.
fn part2(left_list: Vec<i32>, right_list: Vec<i32>) -> i32 {
    // Count the number of times each number appears in the right list.
    let mut right_count = HashMap::new();
    for &num in &right_list {
        *right_count.entry(num).or_insert(0) += 1;
    }

    // Calculate the similarity score.
    let mut similarity_score = 0;
    for &num in &left_list {
        if let Some(&count) = right_count.get(&num) {
            similarity_score += num * count;
        }
    }

    similarity_score
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part1() {
        let left_list = vec![3, 4, 2, 1, 3, 3];
        let right_list = vec![4, 3, 5, 3, 9, 3];
        assert_eq!(part1(left_list, right_list), 11);
    }

    #[test]
    fn test_part2() {
        let left_list = vec![3, 4, 2, 1, 3, 3];
        let right_list = vec![4, 3, 5, 3, 9, 3];
        assert_eq!(part2(left_list, right_list), 31);
    }
}
