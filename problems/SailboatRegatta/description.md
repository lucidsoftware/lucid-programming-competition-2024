# Sailboat Regatta

The Lucid Summer Games wouldn't be complete without a sailboat race, and you're the captain!
Unfortunately, the weather isn't ideal for regular sailing...the wind is too chaotic.
You'll need to be a skilled navigator to get through the finish line with the best time.

You are given a 2-D matrix of the wind's $x, y$ velocity over a rectangle of river between the start and finish line.
Boats move in discrete time steps to discrete $x, y$ coordinates on the river.
The direction $+X$ represents rightward motion, and $+Y$ represents moving down the length of the river toward the finish line.
A boat can begin at any $x$-coordinate on the starting line ($y=0$) and will have an initial velocity of `x_delta = 0, y_delta = 1` before the starting line.

During each time step, two events happen:

1. First, the boat's velocity changes by the velocity of the wind on the boat's current square (if the sails are raised).
2. Then, the boat's position changes by its new velocity.

However, in between each time step, a boat can lower/raise their sails. This is known as **toggling the sail**.
When the sail is lowered, the velocity of the wind does not affect the velocity of the boat and the boat's velocity remains the same.

Once a sail is toggled, there is a cooldown - it cannot be toggled again until **at least** `k` (provided as input) time steps have passed.
For example, if `k = 2` and you lower your sails at `t = 7`, it must remain lowered for at least 2 time steps, and can be raised again at or after `t = 9`.
If `k = 1`, the sail can be toggled in between each time step.

If at any point your boat goes off the course too far to the left or right, you'll be disqualified from the race. This includes before the starting line and after the finish line as well.
The sailboat starts just before the course starting line, and on the first time step it will land on the first row. Assume no winds before the starting line.
The race is completed when the sailboat goes past the last row.

Find the minimum number of time steps to finish the regatta.

# Input

The input format consists of three space-separated positive integers to indicate the width of the course (`w`) and the length of the course (`l`) and the number of time steps between changing the sail status (`k`).
Following the course dimensions, there will be `l` lines representing a cross-section of the wind velocity at that y-coordinate.
There will be `w` $x,y$ velocities in that cross section. The input will be given in the following format:

```
<width of course> <length of course> <sail raise/lower cooldown>
(<wind's x_delta at (1,1)>,<wind's y_delta at this (1,1)>), ..., (<wind's x_delta at (w,1)>,<wind's y_delta at this (w,1)>)
...
(<wind's x_delta at (1,l)>,<wind's y_delta at this (1,l)>), ..., (<wind's x_delta at (w,l)>,<wind's y_delta at this (w,l)>)
```

# Constraints

- The width of the course will always be between 1 and 1000 (inclusive)
- The length of the course will always be between 1 and 1000 (inclusive)
- The sail cooldown will always be between 1 and 100 (inclusive)

# Output

The expected output is the minimum number of time steps to finish the regatta:

```
<time steps>
```

# Examples

Here's an simple example with headwinds.

```
1 1 1
0,-1
```

On the first tick, your boat crosses the starting line with velocity $(0,1)$. Here's the best path to take:

- Enter the course at $x = 1$ (only choice)
- Velocity of $(0, 1)$ pushes you to square $(1, 1)$ which has a wind vector of $(0, -1)$. Lower your sails immediately upon entering this square to avoid the headwinds.
- Velocity of $(0, 1)$ pushes you to square $(1, 2)$ which is across the finish line!

It takes 2 time ticks to cross the finish line, so the expected output is `2`.

Here's another example:

```
2 3 1
1,0 0,0
1,0 0,1
0,-1 0,-1
```

Here's the optimal path across the finish line:

- Enter the course at $x = 2$
- Velocity of $(0,1)$ pushes you to the square $(2,1)$ which has a wind vector of $(0,0)$. Velocity doesn't change.
- Velocity of $(0,1)$ pushes you to square $(2, 2)$ which has a wind vector of $(0,1)$. Keep your sails up, and your velocity is now $(0, 2)$.
- Velocity of $(0, 2)$ pushes you to square $(2, 4)$ which is across the finish line!

It takes 3 time ticks to cross the finish line so the output is

```
3
```
