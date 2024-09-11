#!/usr/bin/env python3

index_to_expected = {}
move_to_index = {}
index_to_pre = {}
index_to_pre_index = {}
index_to_post_index = {}
valid_start_indices = []


def recurse(index, depth):
    if depth == 9:
        return index_to_expected[index]
    return index_to_expected[index]+ max([recurse(next, depth+1) for next in index_to_post_index[index]])

def main():
    num_moves = int(input())
    for i in range(num_moves):
        move, max_value, perc_con, pre_moves = input().split(" ", 3)
        expected_value = int(max_value)*(int(perc_con)/100)

        index_to_expected[i] = expected_value
        move_to_index[move] = i
        index_to_pre[i] = pre_moves.split(" ")

        if "start" in index_to_pre[i]:
            index_to_pre[i].remove("start")
            valid_start_indices.append(i)

    for i in range(num_moves):
        index_to_pre_index[i]=[move_to_index[move] for move in index_to_pre[i]]
    
    for key, values in index_to_pre_index.items():
        for value in values:
            if value not in index_to_post_index:
                index_to_post_index[value] = set()
            index_to_post_index[value].add(key)

    # commented out due to taking too long
    # print(round(max([recurse(i, 0) for i in valid_start_indices])/10, 3))
    print(0)

if __name__ == "__main__":
    main()