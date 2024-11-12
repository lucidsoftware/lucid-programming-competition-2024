# Penguin Slide

Welcome to the Summer Games. 
After a very dramatic finish, a rogue penguin knocked over the intern that was carrying the Penguin Slide results. 
This caused them to fall onto the ground and get mixed up. 
It is your job to sort the results and announce the winner of the event!

# Input
Input will be given as follows:
- $N$ (number of penguins)
- Followed by a list that of penguin names and their times: `<Penguin Name> - <Time>`

Input Constraints:

- $3 < N < 1000$
- Time is positive integer
- All times for a given input will be unique, there are no ties
- Penguin names can have a space  and will all be unique

Example 1:
```
5
Penguin 1 - 30
Penguin 2 - 40
Penguin 3 - 20
Penguin 4 - 15
Penguin 5 - 45
```

Example 2:
```
5
Pink - 15
Slider - 21
Macaroni - 45
Flippers - 24
Tux - 38
```


# Output
Output the top three penguin names in the following format:
```
First: <Name>
Second: <Name>
Third: <Name>
```

Example 1:
```
First: Penguin 4
Second: Penguin 3
Third: Penguin 1
```

Example 2:
```
First: Pink
Second: Slider
Third: Flippers
```

# Examples
The first 2 test cases are examples.