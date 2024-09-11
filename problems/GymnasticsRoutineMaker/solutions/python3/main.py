#!/usr/bin/env python3

index_to_expected = {}
move_to_index = {}
index_to_pre = {}
index_to_look_next = {}
valid_start_indices = []

def main():
    num_moves = int(input())
    dp = [[-1 for x in range(num_moves)] for y in range(10)] 
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
        index_to_look_next[i]=[move_to_index[move] for move in index_to_pre[i]]

    for row in range(8, 0, -1):
        for col in range(num_moves):
            dp[row][col] = max([index_to_expected[col] + dp[row+1][index] for index in index_to_look_next[col]])

    for i in valid_start_indices:
        dp[0][i] = index_to_expected[i]+ max([dp[1][id] for id in index_to_look_next[i]])

    print(round(max(dp[0])/10, 3))

if __name__ == "__main__":
    main()