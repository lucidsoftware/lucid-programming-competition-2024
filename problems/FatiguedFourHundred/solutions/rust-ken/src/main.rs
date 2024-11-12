use std::{f64::INFINITY, fmt::Debug, sync::LazyLock};

struct EffortLevel {
    level: u16,
    time_penalty: f64,
    progressive_penalty: f64,
}

static EFFORT_LEVELS: LazyLock<Vec<EffortLevel>> = LazyLock::new(|| {
    let mut levels = Vec::new();
    for level in (75..=100).step_by(5) {
        levels.push(EffortLevel::new(level));
    }
    levels
});

impl Debug for EffortLevel {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        f.write_str(&self.level.to_string())
    }
}

impl EffortLevel {
    fn new(level: u16) -> Self {
        let time_penalty: f64 = match level {
            75 => 1.160,
            80 => 1.125,
            85 => 1.088,
            90 => 1.055,
            95 => 1.026,
            100 => 1.00,
            _ => panic!(),
        };

        let progressive_penalty: f64 = match level {
            75 => 1.015,
            80 => 1.022,
            85 => 1.032,
            90 => 1.045,
            95 => 1.060,
            100 => 1.10,
            _ => panic!(),
        };

        Self {
            level,
            time_penalty,
            progressive_penalty,
        }
    }

    fn permute_all_effort_levels() -> Vec<Vec<&'static EffortLevel>> {
        Self::recursive_generate_all_efforts(3)
    }

    fn recursive_generate_all_efforts(n: usize) -> Vec<Vec<&'static EffortLevel>> {
        if n == 0 {
            let max_effort = EFFORT_LEVELS.last().unwrap();
            return vec![vec![max_effort]];
        }

        let sub_permutations = Self::recursive_generate_all_efforts(n - 1);

        let mut result = Vec::new();
        for perm in sub_permutations {
            for level in EFFORT_LEVELS.iter() {
                let mut permutation = Vec::new();
                permutation.push(level);
                permutation.extend(perm.clone());
                result.push(permutation);
            }
        }
        result
    }
}

struct Swimmer {
    times: Vec<f64>,
}

impl Swimmer {
    fn new(times: Vec<f64>) -> Self {
        Self { times }
    }

    fn compute_total_time(&self, levels: &Vec<&EffortLevel>) -> f64 {
        let mut progressive_fatigue: f64 = 1.0;
        let mut total_time: f64 = 0.0;

        for (time, effort) in self.times.iter().zip(levels.iter()) {
            total_time += time * effort.time_penalty * progressive_fatigue;
            progressive_fatigue *= effort.progressive_penalty;
        }

        total_time
    }

    fn find_optimal_time(
        &self,
        effort_permutations: &Vec<Vec<&EffortLevel>>,
    ) -> (Vec<String>, f64) {
        let mut fastest_time: f64 = INFINITY;
        let mut winning_effort_levels: &Vec<&EffortLevel> = effort_permutations.first().unwrap();

        for effort_permutation in effort_permutations.iter() {
            let time = self.compute_total_time(effort_permutation);
            if time < fastest_time {
                fastest_time = time;
                winning_effort_levels = effort_permutation;
            }
        }

        (
            winning_effort_levels
                .iter()
                .map(|effort| effort.level.to_string())
                .collect(),
            fastest_time,
        )
    }
}

fn main() {
    let possible_effort_permutations = EffortLevel::permute_all_effort_levels();

    let mut buffer = String::new();
    let stdin = std::io::stdin();
    stdin.read_line(&mut buffer).unwrap();

    stdin.lines().for_each(|line| {
        let line = line.unwrap();
        let times: Vec<f64> = line
            .split(' ')
            .map(|time| time.parse::<f64>().unwrap())
            .collect();

        let (optimal_effort_levels, best_time) =
            Swimmer::new(times).find_optimal_time(&possible_effort_permutations);
        println!("{} {:.1}", optimal_effort_levels.join(" "), best_time);
    });
}
