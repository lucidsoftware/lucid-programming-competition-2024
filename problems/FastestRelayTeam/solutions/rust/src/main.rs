use std::collections::{BTreeMap, BinaryHeap, HashSet};

type TimeSeconds = u16; //Problem guarantees no greater than 1000
type SwimmerId = u32; // Problem guarantees less than 1,000,000

struct Swimmer {
    times: [TimeSeconds; 4],
}

impl Swimmer {
    fn new(times: [TimeSeconds; 4]) -> Self {
        Swimmer { times }
    }
}

struct Swimmers {
    speedy_swimmers: [Vec<(TimeSeconds, SwimmerId)>; 4],
}

impl Swimmers {
    fn new(swimmers: Vec<Swimmer>) -> Self {
        let mut speedy_swimmers = [
            BTreeMap::new(),
            BTreeMap::new(),
            BTreeMap::new(),
            BTreeMap::new(),
        ];

        // Keep only the top 4 contenders in every category
        for (swimmer_id, swimmer) in swimmers.iter().enumerate() {
            for (i, time) in swimmer.times.iter().enumerate() {
                speedy_swimmers[i].insert((*time as TimeSeconds, swimmer_id), swimmer_id as SwimmerId);

                if speedy_swimmers[i].len() > 4 {
                    speedy_swimmers[i].pop_last().unwrap();
                }
            }
        }

        let speedy_swimmers_array = speedy_swimmers.map(|stroke_swimmers| {
            stroke_swimmers
                .iter()
                .map(|((swimmer_time,_), swimmer_id)| (*swimmer_time, *swimmer_id))
                .collect()
        });

        Self {
            speedy_swimmers: speedy_swimmers_array,
        }
    }

    fn fastest_relay(&self) -> TimeSeconds {
        let mut fastest_time = TimeSeconds::MAX;

        for backstroker in 0..4 {
            for breaststroker in 0..4 {
                for butterflyer in 0..4 {
                    for freestyler in 0..4 {
                        // Remember these indexes are not SwimmerIds, they are just indexes into the fastest swimmers array, which then lead to the id.
                        fastest_time = fastest_time.min(self.time_trial_relay(
                            backstroker,
                            breaststroker,
                            butterflyer,
                            freestyler,
                        ));
                    }
                }
            }
        }

        fastest_time
    }

    // Returns MAX_INT if someone in the proposal is going twice
    fn time_trial_relay(
        &self,
        backstroker: usize,
        breaststroker: usize,
        butterflyer: usize,
        freestyler: usize,
    ) -> TimeSeconds {
        let (bk_time, bk_id) = self.speedy_swimmers[0][backstroker];
        let (br_time, br_id) = self.speedy_swimmers[1][breaststroker];
        let (fl_time, fl_id) = self.speedy_swimmers[2][butterflyer];
        let (fr_time, fr_id) = self.speedy_swimmers[3][freestyler];

        let unique_ids = HashSet::from([bk_id, br_id, fl_id, fr_id]);
        if unique_ids.len() != 4 {
            TimeSeconds::MAX
        } else {
            bk_time + br_time + fl_time + fr_time
        }
    }
}

fn main() {
    let mut buffer = String::new();
    let stdin = std::io::stdin();
    stdin.read_line(&mut buffer).unwrap();

    let _reported_number_of_swimmers: u64 = buffer.trim().parse().unwrap();
    let mut swimmers = Vec::new();

    stdin.lines().for_each(|line| {
        let line = line.unwrap();
        let times: Vec<u16> = line
            .split(' ')
            .map(|time| time.parse::<u16>().unwrap())
            .collect();

        let swimmer = Swimmer::new([times[0], times[1], times[2], times[3]]);
        swimmers.push(swimmer);
    });

    let swimmers = Swimmers::new(swimmers);
    let fastest_time = swimmers.fastest_relay();

    println!("{fastest_time}");
}
