# test case generation
for i in $(seq 1 3); do python tests-generator/main.py > "tests/${i}.in" 2> "tests-generator/${i}.log"; done
# run solution to generate output
for i in $(seq 1 3); do cat "tests/${i}.in" | python solutions/python3/solution.py > "tests/${i}.out" ; done

for i in $(seq 4 6); do python tests-generator/main.py > "tests/${i}.in" 2> "tests-generator/${i}.log"; done
for i in $(seq 4 6); do cat "tests/${i}.in" | python solutions/python3/solution.py > "tests/${i}.out" ; done

for i in $(seq 7 9); do python tests-generator/main.py > "tests/${i}.in" 2> "tests-generator/${i}.log"; done
for i in $(seq 7 9); do cat "tests/${i}.in" | python solutions/python3/solution.py > "tests/${i}.out" ; done

for i in $(seq 10 12); do python tests-generator/main.py > "tests/${i}.in" 2> "tests-generator/${i}.log"; done
for i in $(seq 10 12); do cat "tests/${i}.in" | python solutions/python3/solution.py > "tests/${i}.out" ; done
