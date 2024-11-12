# Athlete Area Allocation

Your team is responsible for marking spots on the field where athletes can warm up for their events. Unfortunately, your clumsy assistant put down flags randomly across the field, and now you have to quickly make sure none of them are too close to each other before the athletes arrive. Luckily, you know how to write a program that will do it for you.

Given a list of length $n$ of $X, Y$ coordinates for each flag on the field, output the distance between the two closest flags.

# Input

The first line of input will contain a positive integer $n$, denoting the number of flags on the field. The following $n$ lines will contain two space separated integers, $X$ and $Y$, denoting the coordinates of the flag.

```
<n>
<X_0> <Y_0>
<X_1> <Y_1>
<X_2> <Y_2>
...
<X_(n - 1)> <Y_(n - 1)>
```

# Constraints

* $2 \leq n \leq 10000$
* $0 \leq X \leq 100000$
* $0 \leq Y \leq 100000$
* All numbers are positive integers
* No two flags will have the same location

# Output

Output the distance between the two closest flags rounded to 3 decimal places.

```
<distance>
```