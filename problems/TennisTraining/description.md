# Tennis Training

You are preparing for an upcoming tennis competition. You need access to a training facility by purchasing memberships.
The days you want to train yourself is given as an integer array `days`. The costs of different levels of membership is
given as an integer array `costs`.

The membership is sold in the following three different ways:

- a 1-day membership is sold for `costs[0]` dollars
- a 7-day membership is sold for `costs[1]` dollars
- a 30-day membership is sold for `costs[2]` dollars

The membership allow that many days of consecutive training. For example, you if purchase a 7-day membership on day 2,
then you can train for 7 days: 2, 3, 4, 5, 6, 7 and 8

Return the minimum number of dollars you need to practice every day in `days`

# Input

The input format consists of a two integer arrays, `days` and `costs`

# Constraints

- $1 \leq $ `days.length` $\leq 365$
- $1 \leq $ `days[i]` $\leq 365$
- `days` is in strictly increasing order.
- `costs.length` $=3$
- $1 \leq $ `costs[i]` $\leq 1000$

# Output

An integer representing the minimum number of dollars you need spend on purchasing memeber

# Examples
The first 2 test cases are examples
