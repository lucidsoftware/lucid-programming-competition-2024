# Bullseye Bonus

After a normal round of archery at Lucid's summer games, each archer gets a chance to earn bonus points in the bullseye bonus round!

All $N$ archers who are competing are placed in a line.
They each start with a (possibly negative) integer number of points, which is determined by how well they did during the previous round.

Whenever an archer at some one-indexed position $x$ hits a bullseye, they get to choose both of the following:
- Another archer, denoted by a one-indexed position $y$.
- A range (contiguous subarray) $A$ of archers who are competing in the bonus round. This is defined by two indices $l$ and $r$, which represent the inclusive left and right bounds of the range $[l,r]$.

Suppose the integer floor of the average score within the range $A$ is $k$.
The archer who fired the bullseye (at position $x$) adds $k$ points to their score and the archer at position $y$ subtracts $k$ points from their score.

Note that since archers can have negative scores, $k$ can be negative and therefore the archer at position $x$ may lose points instead of gaining them.

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
- $x$ is the one-indexed position of the archer who shot the bullseye, who will gain $k$ points.
- $y$ is the one-indexed position of the archer called out by the shooting archer, who will lose $k$ points.
- $l$ and $r$ represent the inclusive bounds of the range of archers whose scores are used to calculate $k$, the floor of the average score within the range.

# Constraints
* The number of archers $N$ is between $5 \leq N \leq 10^5$
* The number of bullseye events $M$ is between $1 \leq M \leq 10^5$
* For any archer $i$, the archer's initial score $S_i$ will be between $-10 \leq S_i \leq 10$

# Output
Output a single number indicating the one-indexed position of the archer with the highest score at the end of the game.
If two or more archers are tied, output the position of the archer who appears first in the line.

# Example 1 explanation
Example 1 input:
```
5 1
1 3 5 7 10
1 5 3 5
```
Example 1 output:
```
1
```

In this example, there are $N = 5$ archers and $M = 1$ bullseye events.
The archers initially have scores 1, 3, 5, 7, and 10 respectfully.

Archer 1 gets a bullseye and calls out archer 5, along with the range of archers from 3 to 5.
- The sum of the range is $5 + 7 + 10 = 22$.
- The average of the range is $22 / 3 = 7.3333$.
- The floor of the average of the range is $\lfloor 7.3333 \rfloor = 7$.

Therefore, we add 7 points to archer 1's score and subtract 7 points from archer 5's score.

At the end of the bonus round, here are the scores:
```
8 3 5 7 3
```
Therefore, Archer 1 has won the competition.

# Example 2 explanation
Example 2 input:
```
5 2
8 4 1 7 2
2 5 1 5
5 1 2 4
4 5 3 3
```

Example 2 output:
```
2
```

In this example, there are $N = 5$ archers and $M = 3$ bullseye events.
The archers initially have scores 8, 4, 1, 7, and 2 respectfully.

Archer 2 gets a bullseye and calls out archer 5, along with the range of archers from 1 to 5.
- The sum of the range is $8 + 4 + 1 + 7 + 2 = 22$
- The average of the range is $22 / 5 = 4.2$
- The floor of the average of the range is $\lfloor 4.2\rfloor = 4$

Therefore, we add 4 points to archer 2's score and subtract 4 points from archer 5's score:
```
8 8 1 7 -2
```

Archer 5 gets a bullseye and calls out archer 1, along with the range of archers from 2 to 4.
- The sum of the range is $8 + 1 + 7 = 16$
- The average of the range is $16 / 3 = 5.3333$
- The floor of the average of the range is $\lfloor 5.3333\rfloor = 5$

Therefore, we add 5 points to archer 5's score and subtract 5 points from archer 1's score.
```
3 8 1 7 3
```

Archer 4 gets a bullseye and calls out archer 5, along with the range of archers from 3 to 3.
- The sum of the range is $1$
- The average of the range is $1 / 1 = 1$
- The floor of the average of the range is $\lfloor 1 \rfloor = 1$

Therefore, we add 1 point to archer 4's score and subtract 1 point from archer 5's score.
```
3 8 1 8 2
```

At the end of the bonus round, both archer 2 and archer 4 are tied for the highest score.
Archer 2 is declared the winner because they appear first in the line of archers.

# Examples
The first 3 test cases are examples.