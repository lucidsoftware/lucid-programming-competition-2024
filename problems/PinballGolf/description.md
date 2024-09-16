# Pinball golf
The last hole in the golf course is very weird. The success of the golfers is completely up to chance!

This location is on a hill - the tee is placed at $(0,0)$, the highest point of the hill, and the hole straight downward, located at $(0, L)$. (Downward in this problem is denoted in the $+Y$ direction.) The golfers are to putt the ball straight downhill. Seems pretty easy, right?

There are $N$ pinball flippers placed across this hill, that hit the ball in a random direction. If the ball hits a pinball flipper, these events happen in order:
- The ball flies into the air, and lands either to the left or the right of the flipper.
- Then, the ball continues to roll down this hill in the $+Y$ direction, until it either hits another flipper, reaches the hole, or gets lost into the deep dark beyond.

For each flipper, the following information is provided to you:
- The location (X and Y coordinate)
- All possible values of horizontal displacement (i.e. all the values in the $+X$ or $-X$ direction in which the flipper can hit the ball). **Each displacement value has an equal chance**.

# Input
First, you're given a single line `N L` with the integer $N$ (number of flippers) and $L$ (the Y-coordinate of the hole. The X coordinate is 0)

Data about each flipper follows. For each flipper, the following lines are given:
- One line with `x y k` where $(x, y)$ is the coordinate of the flipper and $k$ is the number of possible displacement values
- Another line follows with:
    - `d_1 d_2 ... d_k` where $d_i$ is the displacement value $i$ ranging from 1 to $k$. These are given in no particular order, and separated by a space.
    - If $d_i$ is positive, that denotes the right direction, and if it's negative, it denotes left. 
    - **All displacement values have an equal chance** (i.e. the probability that this flipper will hit the ball by $d_i$ is $1/k$, for all $i$).

# Constraints
- $N \leq 10^5$, $1 \leq k \leq 10^3$
- There's no vertical displacement - the flippers hit the ball strictly horizontally.
- There is never a displacement of 0.
- When the ball lands after hitting a flipper, **it's guaranteed that it will not land onto another flipper.**
- The hole will always be below all the flippers.

## Example input
A visualization for this input can be seen [here](https://i.imgur.com/vhJkJyd.png)!
```
8 16
0 3 3
-2 8 -6
-2 5 3
2 -8 -6
0 7 1
3
8 6 2
3 -8
3 8 1
-3
3 9 2
-9 3
-10 12 1
1
-5 13 1
5
```
## Example output
```
0.3333333
```
## Explanation
Here's how to interpret the displacements of flipper 1 and 8:
- If the ball reaches flipper 1, it has a 
    - $1/3$ chance to get hit to $(-6, 3)$, causing it to roll down into the void
    - $1/3$ chance to get hit to $(-2, 3)$, causing it to roll down to flipper 2
    - $1/3$ chance to get hit to $(8, 3)$ causing it to roll down to flipper 4
- If the ball reaches flipper 8, it has a 100% chance to get hit to $(0, 13)$, causing it to roll down the hill and reach the hole!

Here's the probabilities of reaching each flipper, as well as the calculation of the answer.
- 100% chance to reach flipper 1
- $1/3$ chance to reach flipper 2 (can only get here from flipper 1)
- $5/18$ chance to reach flipper 3 (can get here from flippers 2 and 4)
- $1/3$ chance to reach flipper 4 (can only get here from flipper 1)
- $5/18$ chance to reach flipper 5 (can only get here from flipper 3)
- 0 chance to reach flipper 6
- $1/9$ chance to reach flipper 7 (can only get here from flipper 2)
- 0 chance to reach flipper 8
- $1/3$ chance to reach the hole (can get here from flippers 5, 7, and 8). This calculation is: 
    - $P(\text{reaching flipper 5}) * P(\text{flipper 5 hitting it to }x=0) + P(\text{reaching flipper 7}) * P(\text{flipper 7 hitting it to }x=0) + P(\text{reaching flipper 8}) * P(\text{flipper 8 hitting it to }x=0) = 5/18 \cdot 1 + 1/9 \cdot 1/2 + 0 \cdot 1$

# Output
Output a single line with the probability of the ball reaching the hole. Answers will be accepted if they are accurate to within a tolerance of $10^{-6}$.
