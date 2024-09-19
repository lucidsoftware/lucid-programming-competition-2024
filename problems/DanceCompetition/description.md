# Dance Competition

You are helping to judge a dance competition. In this competition, each dancer takes turns going on stage and performing a series of dance moves. There is a strict no-copying policy, and so your job is to determine whether any of the dancers is copying any other dancer too closely.

Two dancers are considered to be copying each other if any run of N moves is identical between their routines. If so, both dancers are disqualified.

For example, consider two dancers named `Alice` and `Bob`, and their respective routines. For this example, N is set to 4, meaning if a run of 4 or more identical moves is found between the routines, the dancers are copying.

- `Alice`: Spin - Flip - Spin - Somersault - Jump - Handstand
- `Bob`: Spin - Somersault - Jump - Handstand - Twist - Handstand

In this case, `Alice` and `Bob` are copying each other, since they have a run of 4 moves in common (Spin - Somersault - Jump - Handstand). If N were set to 5 instead, they would not be copying, since there is no run of 5 identical moves between their routines.

Given a list of dancers and their routines, return the number of dancers that are copying.

# Input

The first line of input will contain 2 positive integers, D (the number of dancers) and N (the length threshold for copying). Following will be D lines. Each line will have a dancer's name (all alphabetical, no spaces), and then the sequence of moves in their dance routine. Each move will be alphanumeric, and contain no spaces.

```
<D> <N>
<dancer name> <move> <move> ...
<dancer name> <move> <move> ...
...
```

# Constraints
* 2 <= D <= 1000
* 1 <= N <= 1000
* Dancer names and moves are alphanumeric with no whitespace
* Dancer names and moves are no longer than 10 characters each
* Dancer names will be unique
* Moves are alphanumeric with no whitespace
* Each dance routine will not exceed 1000 moves

# Output

The expected output is the number of dancers that are copying at least 1 other dancer.

```
<int>
```

# Examples
The first 2 test cases are examples.
