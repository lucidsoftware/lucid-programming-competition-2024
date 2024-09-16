# Tug of War

You are coaching a tug of war team for this year's summer games!
Tug of war is a game of strength and strategy. Different positions on the rope can be easier or harder to pull, and some participants are stronger than others. You will be given the pulling power of the participants on your team, a list of positional multipliers for the different positions on the rope, and a target score to beat that represents the pulling power of the opposing team.

For example, one participant may have a pulling power of 10, but if he is lined up in the first position on the rope, and that rope has a positional multiplier of 1.5, that participant would contribute a pulling power of 15 from that position. 

Your team will win the tug of war if all the participants have a combined pulling power greater than that of the opposing team. Additionally, all participants on your team must compete in the game. Your job is to find out how many different ways you can arrange your team, such that your team will win the tug of war. 

# Input

You will be given 3 lines of input. The first line will have an integer, `N`, and a floating point value, `P`. The second line is a space separated list of floating point values, `D`. The third line is a space separated list of floating point values, `M`.
1. An integer `N`, denoting the number of participants on your team, and a floating point value `P`, denoting the total pulling power of the opposing team.
2. A list of length `N` of the pulling power, `D`, of each of the participants on your team
3. A list of length `N` denoting the positional multiplier, `M`, for each position on the rope
```
<N> <P>
<D_0> <D_1> <D_2> ...
<P_0> <P_1> <P_2> ...
```

# Constraints

* 2 <= N <= 9
* 1.0 <= D <= 100.0
* 0.1 <= M <= 10.0
* 1.0 <= P <= 10000.0

# Output

Output the number of ways your team can line up and still beat the other team.
```
<int>
```

# Examples
The first 2 test cases are examples