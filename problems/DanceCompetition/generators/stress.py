import string
import random

NUM_DANCERS = 1000
NUM_MOVES = 500
MATCH_THRESHOLD = 50
NUM_COPIED_ROUTINES = 5
LENGTH_MOVE = 10
CHANCE_COPIED = .15

def get_random_string(l):
    return ''.join(random.choices(string.ascii_letters, k=l))

routines = []
for d in range(NUM_DANCERS):
    routine = [d]
    for n in range(NUM_MOVES):
        routine.append(get_random_string(LENGTH_MOVE))
    routines.append(routine)

copied_routines = []
for i in range(NUM_COPIED_ROUTINES):
    copied_routine = [get_random_string(LENGTH_MOVE) for _ in range(MATCH_THRESHOLD)]
    for d in range(NUM_DANCERS):
        if random.random() < CHANCE_COPIED:
            print("inserting copy")
            insert_point = random.randint(2, NUM_MOVES - 1)
            new_routine = routines[d][:insert_point] + copied_routine + routines[d][insert_point:]
            routines[d] = new_routine

size_constrained_routines = []
for routine in routines:
    new_routine = routine
    if len(routine) > NUM_MOVES + 1:
        new_routine = routine[:NUM_MOVES + 1]
    size_constrained_routines.append(new_routine)


with open("test.in", 'w') as f:
    print(NUM_DANCERS, MATCH_THRESHOLD, file=f)
    for routine in size_constrained_routines:
        print(*routine, file=f)
