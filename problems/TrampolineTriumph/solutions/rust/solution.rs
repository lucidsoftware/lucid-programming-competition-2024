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

fn get_score(milestone: &[f64], factor: f64) -> f64 {
    let local_maxima = get_local_maxima(milestone[0], milestone[1], factor);
    let local_maxima_value = get_position(local_maxima, factor);
    if local_maxima_value >= milestone[2] {
        local_maxima_value
    } else {
        0.0
    }
}

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let players_count: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let factors: Vec<f64> = lines.next().unwrap().unwrap()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    let milestones_count: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let mut milestones: Vec<Vec<f64>> = Vec::with_capacity(milestones_count);
    for _ in 0..milestones_count {
        let milestone: Vec<f64> = lines.next().unwrap().unwrap()
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();
        milestones.push(milestone);
    }

    let mut scores = vec![0.0; players_count];
    for milestone in &milestones {
        for i in 0..players_count {
            scores[i] += get_score(&milestone, factors[i]);
        }
    }

    let mut sorted_scores: Vec<(usize, f64)> = (0..players_count)
        .map(|i| (i + 1, scores[i]))
        .collect();

    sorted_scores.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());

    for (player_index, score) in sorted_scores {
        println!("{}", player_index);
        println!("{:.6}", score);
    }
}
