def find_copiers(D, N, dancers):
    subarray_map = {}  # This maps subarrays to the dancers who have them
    copiers = set()

    for dancer_name, moves in dancers.items():
        # Generate all subarrays of length N
        for i in range(len(moves) - N + 1):
            subarray = tuple(moves[i:i + N])
            if subarray in subarray_map:
                # If subarray exists, add both current dancer and the existing dancers to copiers
                subarray_map[subarray].add(dancer_name)
            else:
                # Otherwise, initialize the set of dancers for this subarray
                subarray_map[subarray] = {dancer_name}

    # Find all dancers who share subarrays with others
    for dancer_set in subarray_map.values():
        if len(dancer_set) > 1:  # Only consider subarrays shared by more than one dancer
            copiers.update(dancer_set)

    return len(copiers)


if __name__ == "__main__":
    # Read the first line of input
    D, N = map(int, input().split())

    # Initialize a dictionary to store dancers and their moves
    dancers = {}

    # Read the next D lines containing dancers' routines
    for _ in range(D):
        line = input().split()
        dancer_name = line[0]
        moves = line[1:]
        dancers[dancer_name] = moves

    # Calculate and print the number of copiers
    result = find_copiers(D, N, dancers)
    print(result)
