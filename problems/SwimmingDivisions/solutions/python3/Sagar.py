def find_parent(parents, x):
    while parents[x] != x:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x

def union(parents, sizes, x, y):
    x = find_parent(parents, x)
    y = find_parent(parents, y)
    if x == y:
        return
    if sizes[x] < sizes[y]:
        x, y = y, x
    parents[y] = x
    sizes[x] += sizes[y]
    sizes[y] = 0

def main():
    competitors_count = int(input())
    competitor_names = []
    competitor_indexes = dict()
    for i in range(competitors_count):
        name = input()
        competitor_names.append(name)
        competitor_indexes[name] = i

    parents = [i for i in range(competitors_count)]
    sizes = [1 for i in range(competitors_count)]
    winners = [-1 for i in range(competitors_count)]

    while True:
        line = input()
        if line == "END":
            break
        query_type = line.split()[0]
        if query_type == "COMPETITION":
            current_competitors_count = int(line.split()[1])
            current_competitor_names = [input() for i in range(current_competitors_count)]
            current_competitor_indexes = [competitor_indexes[name] for name in current_competitor_names]
            winner = current_competitor_indexes[0]
            for competitor in current_competitor_indexes[1:]:
                union(parents, sizes, winner, competitor)
            winners[find_parent(parents, winner)] = winner

        elif query_type == "REQUEST":
            competitor_name = line.split()[1]
            competitor_index = competitor_indexes[competitor_name]
            winner = winners[find_parent(parents, competitor_index)]
            print(competitor_names[winner])
        else:
            print("Invalid query type")
            break

if __name__ == "__main__":
    main()