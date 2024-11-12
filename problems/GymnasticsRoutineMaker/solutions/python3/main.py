#!/usr/bin/env python3
from collections import defaultdict

index_to_expected = {}
move_to_index = {}
index_to_pre = {}
index_to_pre_index = {}
index_to_post_index = defaultdict(set)

valid_start_indices = []

def main():
    num_moves = int(input())
    dp = [[-100 for x in range(num_moves)] for y in range(10)] 
    for i in range(num_moves):
        move, max_value, perc_con, pre_moves = input().split(" ", 3)
        expected_value = int(max_value)*(int(perc_con)/100)

        index_to_expected[i] = expected_value
        move_to_index[move] = i
        index_to_pre[i] = pre_moves.split(" ")
        dp[9][i] = expected_value

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

    for row in range(8, 0, -1):
        for col in range(num_moves):
            for next_col in index_to_post_index[col]:
                dp[row][col] = max(dp[row][col], dp[row + 1][next_col] + index_to_expected[col])

    for col in valid_start_indices:
        for next_col in index_to_post_index[col]:
                dp[0][col] = max(dp[0][col], dp[1][next_col] + index_to_expected[col])

    print("{:.3f}".format(max(dp[0])/10))

if __name__ == "__main__":
    main()