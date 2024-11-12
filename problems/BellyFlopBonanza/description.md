# Belly Flop Bonanza
The next event in the Summer Games is the Bellyflop Bonanza. In this event, athletes compete to splash water as far away as possible from the origin (edge of the diving board) by performing belly flops (dives where they hit the water flat on their stomach to create large splashes).

# Input
If there are $n$ athletes competing, there will be $n + 1$ lines of input. The first line states $n$. The remaining lines describe, one athlete per line, the splash caused by each athlete's belly flop. These lines will be in the format `name; (x, y); diameter;` giving the athlete's `name`, the `(x, y)` position of the center of the splash, and the `diameter` of the splash. For example, the line `Alice; (0.300000, -0.400000); 0.800000` indicates that Alice's belly flop caused a splash located $0.3$ m away from the origin along one axis, $-0.4$ m in the other, and had a diameter of $0.8$ m.

Here is an example input:

```
5
Alice; (0.300000, -0.400000); 0.800000
Bob; (-1.100000, 1.100000); 0.500000
Carol; (0.800000, 1.200000); 1.900000
David; (0.500000, -1.200000); 1.900000
Eve; (-1.700000, -1.100000); 0.200000
```

In this example, Alice splashed water $0.9$ m away from the origin as her splash is centered $d = \sqrt{(\Delta x)^2+(\Delta y)^2} = \sqrt{(0.3)^2+(-0.4)^2} = 0.5$ m away from the origin and splashed water $0.4$ m (half of the $0.8$ m diameter) further than that.

# Constraints
* $3 \leq n \leq 25,000$
* Each athlete has a unique name.
* There are no ties in the top three places.
* Splashes are perfectly circular.

# Output
Your output should be the names of the the 1st (that is, the athlete that splashed water furthest way from the origin), 2nd, and 3rd place athletes; one per line.

# Examples
The first 2 test cases are examples.
