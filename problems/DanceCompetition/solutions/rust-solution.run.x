#!/bin/bash
cargo build --release --quiet --manifest-path $(dirname $(realpath $0))/rust/Cargo.toml
$(dirname $(realpath $0))/rust/target/release/rust