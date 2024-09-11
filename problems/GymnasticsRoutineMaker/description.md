# TODO: Make more test cases, verify DP solution
# Gymnastics Routine Maker

You are a gymnast who is trying to develop the perfect routine to guarantee the gold this year.

At this competition, you are expected to perform 10 moves, and each move has an integer maximum score value assigned by the judges between 1 and 10.
Your final score will be normalized out of 10, so the maximum final score possible is a 10.

However, the judges will deduct points from the maximum score of a move depending on your execution of that move.
For each move you know you can theroetically perform, you also have an integer percentage_confidence between 1 and 100 of how well you'll excecute it.
Conveniently, your confidence maps well to your expected score when attempting a move. Namely expected_score = max_score*(percentage_confidence/100)
This means fractional final scores are possible.

Additionally , given the nature of gymnastics, not every move you can do can immediately follow another. Instead, you must also consider what move you can perform after any other.

Given a list of moves you can do, their maximum score, the percentage of how confident you are at pulling them off, and what moves you can do the move after, return the maximum expected score you can get.

# Input

The first line of input will contain 2 positive integers, D (the number of dancers) and N (the length threshold for copying). Following will be D lines. Each line will have a dancer's name (all alphabetical, no spaces), and then the sequence of moves in their dance routine. Each move will be alphanumeric, and contain no spaces.

```
<N>
<move> <max_score> <percentage_confidence> <preceeding_move_1> <preceeding_move_2>... <preceeding_move_n>
<move> <max_score> <percentage_confidence> <preceeding_move_1> <preceeding_move_2>... <preceeding_move_n>
... 
```

# Constraints
* 1 <= N <= 1000 ???
* Moves are lowercase alphanumeric with no whitespace
* Moves will be unique
* Max Score will be an integer 1 <= n <= 10
* percentage_confidence will be an integer 1 <= n <= 100
* preceeding_move_# will always correspond to either "start" representing that you can start with that move, or match another move's name anywhere else in the input

# Output

The maximum expected score from all possible gymnastic routines

```
<float>
```

# Example Input 1


```
1
flip 10 65 start flip
```

# Example Solution 1


Only 1 possible valid routine: flip flip flip flip flip flip flip flip flip flip

Flip expected value: 10*(65/100)=6.5 

Routine pre-score: 6.5+6.5+6.5+6.5+6.5+6.5+6.5+6.5+6.5+6.5=65 

Final Score: 65/10=6.5

Output:
```
6.5
```

# Example Input 2


```
2
flip 5 100 start flip betterflip
betterflip 10 70 flip betterflip
```

# Example Solution 2


Best possible valid routine: flip betterflip betterflip betterflip betterflip betterflip betterflip betterflip betterflip betterflip

flip expected value: 5*(100/100)=5

betterflip expected value: 10*(70/100)=7

Routine pre-score: 5+7+7+7+7+7+7+7+7+7=68

Final Score: 68/10=6.8

Output:
```
6.8
```