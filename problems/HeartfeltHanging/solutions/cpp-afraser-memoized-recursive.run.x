#!/bin/bash
g++ -std=c++17 $(dirname $0)/cpp/afraser-memoized-recursive.cpp -o $(dirname $0)/cpp/afraser-memoized-recursive.bin
$(dirname $0)/cpp/afraser-memoized-recursive.bin
rm $(dirname $0)/cpp/afraser-memoized-recursive.bin