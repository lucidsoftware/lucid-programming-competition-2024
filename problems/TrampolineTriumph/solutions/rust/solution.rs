use std::io::{self, BufRead};

fn get_position(x: f64, factor: f64) -> f64 {
    (6.0 - 2.0 * factor * (x / 2.0).sin()
        - 2.0 * factor * (x / 5.0).sin()
        - 2.0 * factor * (x / 7.0).sin()) * (0.9 + (1.0 + (x * factor / 3.0).sin()) / 20.0)
}

fn get_local_maxima(mut l: f64, mut r: f64, factor: f64) -> f64 {
    while r - l > 1e-9 {
        let m1 = l + (r - l) / 3.0;
        let m2 = r - (r - l) / 3.0;
        if get_position(m1, factor) > get_position(m2, factor) {
            r = m2;
        } else {
            l = m1;
        }
    }
    l
}

fn get_jump_distance(milestone: &[f64], factor: f64) -> f64 {
    let local_maxima = get_local_maxima(milestone[0], milestone[1], factor);
    get_position(local_maxima, factor)
}

fn get_scores(milestones: &[Vec<f64>], factors: &[f64]) -> Vec<i32> {
    let players_count = factors.len();
    let mut scores = vec![0; players_count];
    for milestone in milestones {
        let mut max_jump_distance = None;
        let mut winner = None;
        for (i, &factor) in factors.iter().enumerate() {
            let jump_distance = get_jump_distance(milestone, factor);
            if max_jump_distance.is_none() || jump_distance > max_jump_distance.unwrap() {
                max_jump_distance = Some(jump_distance);
                winner = Some(i);
            } else if jump_distance == max_jump_distance.unwrap() {
                println!("Error: multiple winners");
            }
        }
        if let Some(winner) = winner {
            scores[winner] += 1;
        }
    }
    scores
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let _players_count: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let factors: Vec<f64> = lines.next().unwrap().unwrap()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    let milestones_count: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let mut milestones = Vec::new();
    for _ in 0..milestones_count {
        let milestone: Vec<f64> = lines.next().unwrap().unwrap()
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        milestones.push(milestone);
    }

    let scores = get_scores(&milestones, &factors);
    let mut sorted_scores: Vec<(usize, i32)> = scores.into_iter().enumerate().collect();
    sorted_scores.sort_by(|a, b| b.1.cmp(&a.1).then_with(|| a.0.cmp(&b.0)));

    for (i, score) in sorted_scores {
        println!("{} {}", i + 1, score);
    }
}
