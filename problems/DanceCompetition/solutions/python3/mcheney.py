from collections import defaultdict

D, N = [int(ea) for ea in input().split(" ")]
if D > 500 or N > 50: # QA check of tests
    exit(1)

seen_seqs = defaultdict(set)
for d in range(D):
    line = input().split(" ")
    name = line[0]
    seq = []
    if len(line[1:]) > 500: # QA check of tests
        exit(1)
    for move in line[1:]:
        seq.append(move)
        if len(seq) == N:
            seen_seqs[tuple(seq)].add(name)
            seq.pop(0)

# for key, values in seen_seqs.items():
#     if (len(values) > 1):
#         print(key, seen_seqs[key])

dancersThatCopied = set([name for dancers in seen_seqs.values() for name in dancers if len(dancers) > 1])
print(len(dancersThatCopied))
