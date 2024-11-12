# Gymnastics Routine Maker

You are a gymnast who is trying to develop the perfect routine to guarantee the gold this year.

At this competition, you are expected to perform exactly 10 moves, and each move has an integer maximum score value assigned by the judges between 1 and 10.
Your final score will be normalized out of 10, so the maximum final score possible is a 10.

However, the judges will deduct points from the maximum score of a move depending on your execution of that move.
For each move you know you can theoretically perform, you also have an integer `percentage_confidence` (between 1 and 100) of how well you'll excecute it.
Conveniently, your confidence maps well to your expected score when attempting a move. Namely `expected_score=max_score * (percentage_confidence/100)`. This means fractional final scores are possible.

Additionally, given the nature of gymnastics, not every move can come after every other move. Instead, you must consider which moves are allowed to follow which other moves.

Given a list of moves you can do, their maximum score, the percentage of how confident you are at pulling them off, and what moves you can do just before this move, return the maximum expected score you can get.

# Input

The first line will contain an integer N (the number of possible moves). Each of the following N lines will contain the name of the move, the max score for that move, your confidence level for that move, and then a list of moves that may precede this move.

```
<N>
<move> <max_score> <percentage_confidence> <preceeding_move_1> <preceeding_move_2>... <preceeding_move_n>
<move> <max_score> <percentage_confidence> <preceeding_move_1> <preceeding_move_2>... <preceeding_move_n>
... 
```

# Constraints
* $1 \leq N \leq 1000$
* Moves are lowercase alphanumeric with no whitespace
* Moves will be unique
* $1 \leq $ `max_score` $\leq 10$
* $1 \leq $ `percentage_confidence` $\leq 100$
* `max_score`, `percentage_confidence` are integers
* `preceeding_move_#` will always correspond to either "start" representing that you can start with that move, or match another move's name anywhere else in the input
* There will always be at least 1 valid routine of length 10
* 
# Output

The maximum expected score from all possible gymnastic routines, precise to 3 decimal places (e.g. 0.50000 => 0.500; 0.333333 => 0.333; 0.55555 => 0.556)

```
<float>
```

# Example Input 1


```
1
flip 10 65 start flip
```

# Example Solution 1


Only 1 possible valid routine: `flip flip flip flip flip flip flip flip flip flip`

Flip expected value: $10*(65/100)=6.5$

Routine pre-score: $6.5+6.5+6.5+6.5+6.5+6.5+6.5+6.5+6.5+6.5=65$ 

Final Score: $65/10=6.5$

Output:
```
6.500
```

# Example Input 2


```
2
flip 5 100 start flip betterflip
betterflip 10 70 flip betterflip
```

# Example Solution 2


Best possible valid routine: `flip betterflip betterflip betterflip betterflip betterflip betterflip betterflip betterflip betterflip`

flip expected value: $5*(100/100)=5$

betterflip expected value: $10*(70/100)=7$

Routine pre-score: $5+7+7+7+7+7+7+7+7+7=68$

Final Score: $68/10=6.8$

Output:
```
6.800
```