#!/bin/bash
g++ -std=c++17 $(dirname $0)/cpp/afraser-brute-force-recursive.cpp -o $(dirname $0)/cpp/afraser-brute-force-recursive.bin
$(dirname $0)/cpp/afraser-brute-force-recursive.bin
rm $(dirname $0)/cpp/afraser-brute-force-recursive.bin