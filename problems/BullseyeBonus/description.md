# Bullseye Bonus

After a normal round of archery at Lucid's summer games, each archer gets a chance to earn bonus points in the bullseye bonus round!

All $N$ archers who are competing are placed in a line.
They each start with a (possibly negative) integer number of points, which is determined by how well they did during the previous round.

Whenever an archer at some one-indexed position $x$ hits a bullseye, they get to choose both of the following:
- Another archer, denoted by a one-indexed position $y$
- A contiguous subarray $A$ of archers who are competing in the bonus round. This is defined by two indices $l$ and $r$, which represent the inclusive left and right bounds of the subarray $[l,r]$.

Suppose the average score within the subarray $A$, after being rounded down to the nearest integer, is $k$.
The archer who fired the bullseye (at position $x$) gains $k$ points and the archer at position $y$ loses $k$ points.

As the scorekeeper, it is your job to keep track of the scores and determine a victor at the end of the event.

# Input
- The first line will provide space-separated values for $N$ and $M$, the number of archers and bullseye events in the bonus round.
- The second line will provide a space-separated list of $N$ integer scores, indicating the score of each archer before the bullseye bonus round.
- The next $M$ lines will describe all of the $M$ bullseyes that happen during the bonus round in chronological order. 
```
<number of archers N> <number of bullseyes M>
<score 1> <score 2> ... <score N>
<first bullseye event>
<second bullseye event>
...
<Mth bullseye event>
```

For each bullseye event, the input will be provided as follows:
```
<position of shooting archer x> <position of chosen archer y> <left index of range l> <right index of range r>
```
- $x$ is the one-indexed position of the archer who shot the bullseye, who will gain $k$ points
- $y$ is the one-indexed position of the archer called out by the shooting archer, who will lose $k$ points
- $l$ and $r$ represent the inclusive bounds of the contiguous subarray of archers whose scores are used to calculate $k$, the floor of the average score within the subarray

# Constraints
* The number of archers $N$ is between $5 \leq N \leq 10^5$
* The number of bullseye events $M$ is between $1 \leq M \leq 10^5$
* For any archer $i$, the archer's initial score $S_i$ will be between $-10 \leq S_i \leq 10$

# Output
Output a single number indicating the one-indexed position of the archer with the highest score at the end of the game.
If two or more archers are tied, output the position of the archer who appears first in the line.

# Examples
The first 3 test cases are examples.