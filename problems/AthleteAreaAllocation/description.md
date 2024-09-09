# Athlete Area Allocation

Your team is responsible for marking spots on the field where athletes can warm up for their events. Unfortunately, your clumsy assistant put down flags randomly across the field, and now you have to quickly make sure none of them are too close to each other before the athletes arrive. Luckily, you know how to write a program that will do it for you.

Given a list of length `n` of X and Y coordinates for each flag on the field, output the distance between the two closest flags.

# Input

The first line of input will contain a positive integer `n`, the number of flags on the field. The following `n` lines will contain the positive integer coordinates of each flag given in an `X Y` format, one flag per line.

```
<n>
<X and Y of flag 0>
<X and Y of flag 1>
<X and Y of flag 2>
...
<X and Y of flag n - 1>
```

# Constraints

* 2 <= `n` <= 4000 ??
* 0 <= `X` <= 100000 ??
* 0 <= `Y` <= 100000 ??
* All numbers are positive integers
* No two flags will have the same location

# Output

Output the distance between the two closest flags rounded to 3 decimal places. ??

```
<distance>
```