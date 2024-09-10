# New Air Rifle Event

Trying to always shoot the bullseye is so boring, so we invented a new air rifle event for the game this year! Each player gets `N` bullets, where `N-1` bullets should form a [convex hull](https://en.wikipedia.org/wiki/Convex_hull#:~:text=The%20convex%20hull%20may%20be,of%20points%20in%20the%20subset.), and the **final** bullet should land within `M`mm of the bullseye and inside the convex hull. Given a list of contestants and their `N` bullets' coordinate on the target paper, compute the contestant that successfully completes the game.

## Input

The first line of the input will contain 3 integers, `A`, the number of competitors; `N`, the number of bullets each competitor has; and `M`, the distance the last shot needs to be from the bullseye in mm. Each following line will have the competitor's name (no spaces), followed by a sequence of coordinates for the shots on the target paper. Each coordinate is numeric and separated by a comma, like `3,3`, meaning the shot is `3 mm` up and `3 mm` to the right of the bullseye. The bullseye has coordinates `0,0`. If two shots land the same position, the competitor did not complete the challange, because the

**Example Input**

```
3 5 3
Alice 2,3 1,1 0,-1 -2,3 -1,0
Bob -1,-2 0,2 3,-3 1,0 -2,1
Charlie 0,0 1,1 -1,-1 2,-2 -3,3
```

## Constraint

- 1 <= A <= 1000
- 4 <= N <= 1000 (It takes at least 3 points to form a convex hull and we still need the last center shot.)
- Competitor names are unique and all alphanumeric with no white space
- All coordinates will be in integers.

## Output

The expected output are lines of names that completed the challange. If no competitor completes the challange successfully, then do no output anything.

**Example Output**

```
Jimmy
Jenny
James
Jessica
```
