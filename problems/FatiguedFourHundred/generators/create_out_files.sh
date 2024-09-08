#!/bin/bash
set -e
cd ../solutions/rust-ken

for input_file in ../../tests/*.in; do
    output_file="$(basename $input_file .in).out"
    echo $output_file
    cargo run --release < $input_file > ../../tests/$output_file
done
