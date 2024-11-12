import heapq

n = int(input())
penguin_data = []

for _ in range(n):
    line = input().strip()
    name, time = line.split(' - ')
    time = int(time)
    penguin_data.append((time, name))
top_three = heapq.nsmallest(3, penguin_data)

print(f"First: {top_three[0][1]}")
print(f"Second: {top_three[1][1]}")
print(f"Third: {top_three[2][1]}")