use std::collections::{hash_map::Entry, HashMap, HashSet};

type MoveId = u32;

struct MoveCatalog {
    /*
      Assigns every unique dance move an integer id, as comparing integers is way faster than string compares.
      This doesn't make a difference until the larger test cases.

      On the larger test cases, this technique speeds things up enough that we can just use
      what I think is a naive solution to solve this.
    */
    catalog: HashMap<String, MoveId>,
    unique_counter: MoveId
}

impl MoveCatalog {

    fn new() -> Self {
        MoveCatalog {
            catalog: HashMap::new(),
            unique_counter: 0
        }
    }

    fn to_move_id(&mut self, dance_move: &str) -> MoveId {
        match self.catalog.entry(dance_move.to_string()) {
            Entry::Occupied(move_id_entry) => *move_id_entry.get(),
            Entry::Vacant(move_id_entry) => {
                self.unique_counter += 1;
                *move_id_entry.insert(self.unique_counter)
            }
        }
    }

}

#[derive(Debug)]
struct Dancer {
    name: String,
    moves: Vec<MoveId>,
}

impl Dancer {
    fn new(input_line: String, catalog: &mut MoveCatalog) -> Self {
        let line: Vec<&str> = input_line.split(' ').collect();

        let name = line[0].to_string();
        let moves: Vec<MoveId> = line[1..].iter().map(|dance_move| {
            catalog.to_move_id(dance_move)
        }).collect();

        Dancer {
            name,
            moves
        }
    }

    fn submoves(&self, threshold: usize) -> Vec<Vec<MoveId>> {
        self.moves.windows(threshold).map(|window| {
            window.to_vec()
        }).collect()
    }
}

fn count_copycats(dancers: &Vec<Dancer>, threshold: usize) -> usize {
    let mut submove_owners: HashMap<Vec<MoveId>, &str> = HashMap::new();
    let mut copycats: HashSet<&str> = HashSet::new();

    for dancer in dancers {
        for submoves in dancer.submoves(threshold) {
            match submove_owners.entry(submoves) {
                Entry::Vacant(entry) => {
                    entry.insert(&dancer.name);
                },
                Entry::Occupied(entry) => {
                    let copycat_a = entry.get();
                    let copycat_b = &dancer.name;

                    if copycat_a != copycat_b {
                        copycats.insert(copycat_a);
                        copycats.insert(copycat_b);
                    }
                }
            }
        }
    }

    copycats.len()
}


fn main() {

    let mut dancers = Vec::new();
    let mut catalog = MoveCatalog::new();

    let mut header_buffer: String = String::new();
    std::io::stdin().read_line(&mut header_buffer).unwrap();
    let header: Vec<usize> = header_buffer.trim().split(' ').map(|x| x.parse::<usize>().unwrap()).collect();
    let threshold: usize = header[1];

    for line in std::io::stdin().lines() {
        let dancer = Dancer::new(line.unwrap(), &mut catalog);
        dancers.push(dancer);
    }

    if header[0] != dancers.len() {
        panic!("Oh no, the stated number of dancers is wrong in this test case!");
    }

    println!("{}", count_copycats(&dancers, threshold));
}
