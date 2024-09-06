# This solution is meant to be a naive approach that times out in the stress tests

D, N = [int(ea) for ea in input().split(" ")]

routines = []
for d in range(D):
    routines.append(input().split(" "))


# Function from https://www.geeksforgeeks.org/check-whether-an-array-is-subarray-of-another-array/
def isSubArray(A, B):
    n = len(A)
    m = len(B)

    for i in range(n - m + 1):
        for j in range(m):
            if A[i + j] != B[j]:
                break
        else:
            # If the inner loop did not break, all elements of B match the subarray starting at index i
            return True

    return False

copiers = set()
for d in range(D):
    current_routine = routines[d]
    name = current_routine[0]
    seq = []
    for move in current_routine[1:]:
        seq.append(move)
        if len(seq) == N:
            for o in range(D):
                if o == d:
                    continue
                if isSubArray(routines[o], seq):
                    copiers.add(name)
            seq.pop(0)

print(len(copiers))
