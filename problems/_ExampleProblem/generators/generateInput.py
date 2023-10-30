import random

# all_names = ["rickyraptor", "timmytrex", "allyallosaurus", "pennypterodactyl", "igoriguanodon", "spencerspinosaurus"]

N = 10000
numHoles = 999

import string
import random

lengthOfName = 21

names = []
for i in range(numHoles):
    names.append(''.join(random.choices(string.ascii_lowercase +
                             string.digits, k=lengthOfName)))

print(N)

for n in range(N):
    print(f'{names[random.randint(0, len(names) - 1)]} {random.randint(1, numHoles + 1)}')
