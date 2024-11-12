# Fatigued Four Hundred

The 400m Individual Medley (often abbreviated simply as "400 IM") is one of the most challenging events in the sport of swimming, requiring endurance, strength, and profiency in all four competition strokes in a single race.
In the 400 IM, swimmers must swim 100 meters of each stroke, in this exact order: Butterfly, Backstroke, Breaststroke, Freestyle.
One difficulty of the 400 IM is correctly pacing the race to yield the fastest final time.
If you start the race too fast, you may sink your chances of finishing the race with a competitive time.
On the other hand, if you go too slow at first, you may find yourself so far behind the competition that you cannot catch up!
Another serious challenge of the 400 IM is the progressive fatigue that increasingly impacts the swimmers' ability to swim.
As each swimmer has a unique balance of skills and strengths in each of the four strokes, the ideal race strategy is unique every swimmer.

Help the swimmers at the 2024 Lucid Summer Games out by computing a recommended target pace for each 100m leg of the race that will yield the fastest possible overall time for each swimmer.

**Did you know?** The current world record holder in the 400 IM is Léon Marchand, a computer science major. No doubt swimming is just one of many floating point operations he is an expert in.

### Details

For the purposes of this challenge, you will use a simplified rules-based human performance model.

### Model Variables
The input to your model will be the swimmer's fastest 100m time for each stroke.
This time is the fastest time that the swimmer has ever swum when swimming only 100m of each stroke on its own (not as part of a 400 IM).
_Not accounting for fatigue_, simply adding together the 100m times for each of the four strokes would yield the theoretical fastest 400 IM time possible from that swimmer.
However, this will yield an unrealistically fast time due to the progressive fatigue that happens over the course of the race.

To account for this, your model will assign each leg of the race a recommended _effort-level_.

### Effort Level Penalty
For each leg of the race, in our model a swimmer can choose to swim at any of the following effort levels.
A lower effort level is slower, but causes much less fatigue.
A higher effort level is faster, but causes much more fatigue.

Each effort level is associated with a time penalty for that leg.

```
75% effort => 16% time penalty on that leg (slowest)
80% effort => 12.5% time penalty
85% effort => 8.8% time penalty
90% effort => 5.5% time penalty
95% effort => 2.6% time penalty
100% effort => 0.0% time penalty (fastest)
```

### Progressive Fatigue Penalty

The effort level you choose for each leg of the race impacts the leg itself via the above time penalties.
The effort level of a leg also impacts _all_ legs that follow via the below progressive fatigue penalties.
You must be strategic about choosing an ideal effort level for each 100m leg of the race to avoid having your swimmer becoming overly fatigued.

```
75% effort => 1.5% fatigue penalty on all following legs
80% effort => 2.2% fatigue penalty on all following legs
85% effort => 3.2% fatigue penalty on all following legs
90% effort => 4.5% fatigue penalty on all following legs
95% effort => 6.0% fatigue penalty on all following legs
100% effort => 10% fatigue penalty on all following legs
```

The fatigue penalty applies only to the _following_ legs of the race; it does not apply to the leg itself.
You must correctly account for _all_ applicable penalties that have accumulated when computing the total penalty.
Penalties are cumulative against each other.
For example, as you can see from the table, the progressive fatigue penalty of swimming at $100\%$ exertion level is $10\%$.
If you were to exert $100\%$ effort level on the butterfly, backstroke, and breaststroke legs, a $33.1\%$ fatigue penalty would accumulate for the freestyle leg of the race.

### Order of Strokes
The order of strokes in the Individual Medley is always Butterfly, Backstroke, Breaststroke, Freestyle.

No other order of strokes is allowed.

# Input

The input consists of a single line of input indicating how many swimmers you have, followed by a line of input for each swimmer.
Each swimmer will have four numbers representing that swimmer's fastest ever time (in seconds) swimming 100m of the stroke at $100\%$ effort.
The times are always given in the exact order of Butterfly, Backstroke, Breaststroke, Freestyle.

```
<Number of Swimmers>
<Butterfly 100m time> <Backstroke 100m time> <Breaststroke 100m time> <Freestyle 100m time>
<Butterfly 100m time> <Backstroke 100m time> <Breaststroke 100m time> <Freestyle 100m time>
...
```

The `<time>` inputs are given in number of seconds.
Our input always includes exactly two digits to the right of the decimal, for example: `60.00`, `75.31`, `115.20`.

# Constraints
* The number of swimmers will always be between 1 and 50000
* The input times in seconds will always be between 1.00 and 1000.00

# Output
For each swimmer, you should output the four recommended effort levels for each stroke followed by the predicted fastest possible time they could swim the 400 IM using the predictive model described above.
The effort level must be one of these numbers: `{75, 80, 85, 90, 95, 100}` (You should omit the `%` sign).
The predicted time should be measured in seconds and rounded to the nearest _tenth_ of a second (a single digit to the right of the decimal). You should always include a single digit to the right of the decimal.

```
<Butterfly effort level> <Backstroke effort level> <Breaststroke effort level> <Freestyle effort level> <Predicted time>
<Butterfly effort level> <Backstroke effort level> <Breaststroke effort level> <Freestyle effort level> <Predicted time>
<Butterfly effort level> <Backstroke effort level> <Breaststroke effort level> <Freestyle effort level> <Predicted time>
<Butterfly effort level> <Backstroke effort level> <Breaststroke effort level> <Freestyle effort level> <Predicted time>
...
```

### Hints for formatting the output time
These code snippets are provided as-is with no warranty. Swim at your own risk; no lifeguard on duty.

**Python**
```
"{:.1f}".format(time)
```

**C**
```
printf("%.1f", time);
```

**Rust**
```
print!("{:.1}", time);
```

**Java**
```
System.out.printf("%.1f", time);
```

# Examples
The first 2 test cases are examples.