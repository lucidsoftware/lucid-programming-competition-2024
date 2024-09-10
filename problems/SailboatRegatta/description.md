# Sailboat Regatta

The Lucid Summer Games wouldn't be complete without a sailboat race, and you're the captain!
Unfortunately, the weather isn't ideal for regular sailing...the wind is too chaotic.
You'll need to be a skilled navigator to get through the finish line with the best time.

You are given a 2-d matrix of the wind's x-y velocity over a rectangle of river between the start and finish line.
Boats move in discrete time steps to discrete x,y coordinates on the river.
Positive x represents rightward motion, and positive y represents moving down the length of the river toward the finish line.
A boat can begin at any x-coordinate on the starting line (y=0) and will have an initial velocity of `x_delta=0, y_delta=1` before the starting line.

During each time step, two events happen:

1. First, the boat's velocity changes by the velocity of the wind on the boat's current square (if the sails are raised).
2. Then, the boat's position changes by its new velocity.

However, a boat can lower/raise their sails during a time step before the wind pushes your boat.
When the sail is lowered, the velocity of the wind does not affect the velocity of the boat and the boat's velocity remains the same.
Once a sail is lowered/raised, it cannot be lowered or raised again until `k` (provided as input) time steps have passed.
For example, if `k=1` and you lower your sails, on the next time step the sails must remain lowered, then on then following time step, you can raise them again.

If at any point your boat goes off the course too far to the left or right, you'll be disqualified from the race. This includes before the starting line and after the finish line as well.
The sailboat starts just before the course starting line, and on the first time step it will land on the first row. Assume no winds before the starting line.
The race is completed when the sailboat goes _past_ the last row.

Find the minimum number of time steps to finish the regatta.

# Input

The input format consists of three space-separated positive integers to indicate the width of the course (`w`) and the length of the course (`l`) and the number of time steps between changing the sail status (`k`).
Following the course dimensions, there will be `l` lines representing a cross-section of the wind velocity at that y-coordinate.
There will be `w` x-y velocities in that cross section. The input will be given in the following format:

```
<width of course> <length of course> <sail raise/lower cooldown>
(<wind's x_delta at (0,0)>, <wind's y_delta at this (0,0)>), ..., (<wind's x_delta at (w,0)>, <wind's y_delta at this (w,0)>)
...
(<wind's x_delta at (0,l)>, <wind's y_delta at this (0,l)>), ..., (<wind's x_delta at (w,l)>, <wind's y_delta at this (w,l)>)

```

# Constraints

- The width of the course will always be between 1 and 100 (inclusive)
- The length of the course will always 5 and 100 (inclusive)

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

On the first tick, your boat crosses the starting line with velocity (0,1) and your best option is to lower the sails immediately to avoid the headwinds.
On the second tick, your boat still has velocity x=0 y=1 and the boat crosses the finish line.
The expected output is `2`.

Here's another example:

```
2 3 1
1,0 0,0
1,0 0,1
0,-1 0,-1
```

On the first tick, your boat crosses the starting line with velocity (0,1) and your best option is to start with the boat entering the square with wind velocity of (0,0).
On the second tick, your boat still has the velocity of (0,1) and you proceed into the next lower square.
On the third tick, your sail remains up, your boat's velocity becomes (0,2), and you skip over the headwinds and over the finish line.
The expected output is `3`.
