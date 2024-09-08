use std::{
    fs::File,
    io::{LineWriter, Write},
};

use rand::{thread_rng, Rng};

fn generate_random_time() -> String {
    let seconds = thread_rng().gen_range(1..1000);
    let hundredths = thread_rng().gen_range(0..100);

    format!("{}.{:02}", seconds, hundredths)
}

fn generate_swimmer_times() -> String {
    let cases: Vec<String> = (0..4).into_iter().map(|_| generate_random_time()).collect();
    cases.join(" ")
}

fn write_out_test_case(test_case: u32, num_swimmers_override: Option<u32>) {
    let test_input_file = File::create(format!("../tests/{:02}.in", test_case)).unwrap();
    let mut writer = LineWriter::new(test_input_file);

    let num_swimmers = num_swimmers_override.unwrap_or(2_u32.pow(test_case));

    writeln!(writer, "{}", num_swimmers).unwrap();
    for _ in 0..num_swimmers {
        writeln!(writer, "{}", generate_swimmer_times()).unwrap();
    }

    writer.flush().unwrap();
}

fn main() {
    // for test_case in 2..16 {
    //     write_out_test_case(test_case, None);
    // }
    for test_case in 16..24 {
        write_out_test_case(test_case, Some(17500))
    }
}
