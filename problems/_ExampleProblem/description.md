# Watering Holes
You are running a park with several watering holes. Your job is to track which dinosaurs are at each watering hole, and report which ones are still there at the end of the day.

Every time a dinosaur moves to a new watering hole or leaves the park, they register their movement with you. Each watering hole is identified by a positive integer.

# Input
The input will consist of a positive integer n, indicating the number of logs. Next will follow n lines. Each line will be 1 of the following 2 formats:

1. `timmytrex 2`, meaning the dinosaur named `timmytrex` moved to watering hole `2`.
2. `timmytrex 0`, meaning the dinosaur named `timmytrex` left the park.

Here is an example input:

```
5
timmytrex 1
allyallosaurus 1
timmytrex 3
allyallosaurus 0
bobbybrontosaurus 3
```

# Constraints

* Each dinosaur has a unique name
* Each dinosaur name consists of only lowercase letters
* Every watering hole will appear in at least 1 log
* There will be at most 1000 watering holes
* There will be at most 10,000 logs

# Output
Your output should be the list of dinosaurs left at each watering hole at the end of the day. The watering holes should be sorted in ascending numerical order. The dinosaurs at each watering hole should be printed as a space separated list in ascending alphabetical order. If no dinosaurs are left at a given watering hole, output `n/a`.

Here is the output for the example given above:

```
1 n/a
3 bobbybrontosaurus timmytrex
```

### Explanation:
- `timmytrex` enters the park and moves to watering hole 1
- `allyallosaurus` enters the park and moves to watering hole 1
- `timmytrex` leaves watering hole 1 and moves to watering hole 3
- `allyallosaurus` leaves the park
- `bobbybrontosaurus` enters the park and moves to watering hole 3

At the end of the day, no dinosaurs are left at watering hole `1`, and 2 dinosaurs are left at watering hole `3`: `bobbybrontosaurus` and `timmytrex`. Note that there is no watering hole with the number 2, since it did not appear in the input.

# Examples
The first 2 test cases are examples.
