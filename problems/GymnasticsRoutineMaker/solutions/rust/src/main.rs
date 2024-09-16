use core::panic;
use std::{cell::RefCell, collections::{hash_map::Entry, HashMap}, rc::Rc};


struct GraphBuilder {
    adjacent: HashMap<String, Vec<String>>,
    moves: HashMap<String, Rc<RefCell<GraphNode>>>,
}

impl GraphBuilder {
    fn new() -> Self {
        let mut moves = HashMap::new();
        moves.insert("start".to_string(), Rc::new(RefCell::new(GraphNode::new(0))));
        Self {
            adjacent: HashMap::new(),
            moves,
        }
    }

    fn insert(&mut self, name: &str, max_score: u64, confidence: u64, prior_moves: Vec<String>) {
        let node = GraphNode::new(max_score * confidence);
        self.moves.insert(name.to_string(), Rc::new(RefCell::new(node)));

        for prior in prior_moves {
            match self.adjacent.entry(prior.to_string()) {
                Entry::Vacant(entry) => {
                    entry.insert(vec![name.to_string()]);
                },
                Entry::Occupied(mut entry) => {
                    entry.get_mut().push(name.to_string())
                }
            }
        }
    }

    fn collect(&self) -> Rc<RefCell<GraphNode>> {
        for entry in &self.moves {
            let (key, node) = entry;

            for adjacent_name in self.adjacent.get(key).unwrap() {
                let adjacent_node = self.moves.get(adjacent_name).unwrap();
                node.borrow_mut().next.push(adjacent_node.clone());
            }
        }

        self.moves.get("start").unwrap().clone()
    }

}

struct GraphNode {
    expected_value: u64,
    next: Vec<Rc<RefCell<GraphNode>>>,
    cached_max_score: RefCell<HashMap<usize, Option<u64>>>,
}

impl GraphNode {
    fn new(expected_value: u64) -> Self {
        Self {
            expected_value,
            next: Vec::new(),
            cached_max_score: RefCell::new(HashMap::new()),
        }
    }

    fn max_score(&self, remaining_nodes: usize) -> Option<u64> {
        if remaining_nodes == 0 {
            return Some(self.expected_value);
        }

        {
            let cache = self.cached_max_score.borrow();
            let maybe_cached = cache.get(&remaining_nodes);
            if maybe_cached.is_some() {
                return maybe_cached.unwrap().clone();
            }
        }


        let max_children_score = self.next.iter().map(|adjacent_node| {
            adjacent_node.borrow().max_score(remaining_nodes - 1)
        }).max().flatten();

        let mut cache = self.cached_max_score.borrow_mut();
        let max_expected_value = max_children_score.map(|score| score + self.expected_value);
        cache.insert(remaining_nodes, max_expected_value);
        max_expected_value
    }
}


fn stdin_to_start_node() -> Rc<RefCell<GraphNode>> {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).unwrap();
    let num_moves = buffer.trim().parse::<usize>().unwrap();

    let mut graph = GraphBuilder::new();

    for str_line in std::io::stdin().lines() {
        let line: Vec<String> = str_line.unwrap().split(' ').map(|x| x.to_string()).collect();

        let name = &line[0];
        let max_score: u64 = line[1].parse().unwrap();
        let confidence: u64 = line[2].parse().unwrap();
        let moves = line[3..].to_vec();

        graph.insert(name, max_score, confidence, moves);
    }

    if graph.moves.len() - 1 != num_moves {
        panic!("Misleading test case had claims {} moves, but actually has {}", num_moves, graph.moves.len());
    }

    graph.collect()
}


fn main() {
    let start_node = stdin_to_start_node();

    // Questions:
    // Is it always possible to form a valid routine? Do you guarantee it?
    //
    let max_score = start_node.borrow_mut().max_score(10).unwrap();

    println!("{}", max_score as f64 / 1000.0);
}
