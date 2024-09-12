# Fastest Relay Team
As a coach for the swimming relay event, you are trying to put together the fastest team. You are given an $n$ by 4 array where each 4 length array represents the amount of time it takes a swimmer to complete the leg with a given stroke. (i.e. [0][1] would be the time it takes swimmer 0 to complete a leg using stroke 1). Select the best team of four, with each team member swimming a different stroke. Each swimmer can only be used once. Output the fastest possible time for the entire relay (4 swimmers each using different strokes).

# Input
The first line containes the number of swimmers $n$.    
Each of the following $n$ lines represent how fast each swimmer can swim using the 4 different strokes $m$.

```
<n>
<M_1_1> <M_1_2> <M_1_3> <M_1_4>
...
<M_n_1> <M_n_2> <M_n_3> <M_n_4>
```

# Constraints
- $4 \leq n \leq 10^6$
- $1 \leq m \leq 1000$
- $m$ is always an integer
- Each swimmer may only be used for a single leg
- Each swimmer must use a different stroke


# Output
Print an integer that is the fastest possible time - sum of fastest four strokes from the four different selected swimmers.
```
<fastest possible time>
```

# Examples
## Input
```
5
1 2 3 4
2 1 3 4
3 2 2 1
4 3 1 2
5 6 7 8
```
## Output
```
4
```
### Explanation
Select the following swimmers for your relay team:
- [0][0] - Select swimmer 0 for stroke 0 (1)
- [1][1] - Select swimmer 1 for stroke 1 (1)
- [3][2] - Select swimmer 3 for stroke 2 (1)
- [2][3] - Select swimmer 2 for stroke 3 (1)

Sum of all these strokes is $4$
