# New Air Rifle Event

Trying to always shoot the bullseye is so boring, so we invented a new air rifle event for the game this year! Each player gets `N` bullets, where the first `N-1` bullets should form a [convex hull](https://en.wikipedia.org/wiki/Convex_hull#:~:text=The%20convex%20hull%20may%20be,of%20points%20in%20the%20subset.), with no 3 collinear points. That is, no 3 points in the convex hull should form a line. The **final** bullet should land within `M`mm of the bullseye and either inside the convex hull or on one of its edges. Note that the bullseye does not need to be within the convex hull, so long as the final shot is within it and still close enough to the bullseye. Given a list of contestants and their `N` bullets' coordinates on the target paper, compute the contestant that successfully completes the game.

## Input

The first line of the input will contain 3 integers, `A`, the number of competitors; `N`, the number of bullets each competitor has; and `M`, the distance the last shot needs to be from the bullseye in mm. Each following line will have the competitor's name (no spaces), followed by a sequence of coordinates for the shots on the target paper. Each coordinate is numeric and separated by a comma, like `3,3`, meaning the shot is `3 mm` up and `3 mm` to the right of the bullseye. The bullseye has coordinates `0,0`. If two shots land the same position, the competitor did not complete the challenge.

**Example Input**

```
4 5 5
Alice -8,0 -7,0 -6,0 -5,0 -4,0
Bob 1,1 3,1 2,3 4,4 1,2
Carl -1,1 -2,-2 -1,2 2,-1 0,0
Darcy -1,-1 1,1 -1,1 1,-1 0,0
```

## Constraint
- $1 \leq A \leq 1000$
- $4 \leq N \leq 1000$ (It takes at least 3 points to form a convex hull, plus the last center shot.)
- $1 \leq M \leq 10$
- Competitor names are unique and all alphanumeric with no white space
- All coordinates will be in integers, each less than 1000000.

## Output

The expected output are lines of names that completed the challenge. If no competitor completes the challenge successfully, then do not output anything.

**Example Output**

```
Darcy
```
